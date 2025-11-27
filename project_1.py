from time import time
import telebot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
import requests as req

state_storage = StateMemoryStorage()
bot = telebot.TeleBot('8453313366:AAEJfHiadReT3jLZL9r0k8pLxVeVn15v9ww',state_storage=state_storage)

code_grn = 980
code_doll = 840
code_evro = 978
user_data = {}
cached_data = []
last_updated = 0
CACHE_TTL = 30

class ConvertState(StatesGroup):
    waiting_for_amount = State()

def connect_mono():
    global cached_data, last_updated
    now = time()
    if now - last_updated > CACHE_TTL:
        response = req.get('https://api.monobank.ua/bank/currency')
        if response.status_code == 200:
            cached_data = response.json()
            last_updated = now
        else:
            cached_data = []
    return cached_data

def get_rate(data, code_a, code_b):
    for x in data:
        if x.get('currencyCodeA') == code_a and x.get('currencyCodeB') == code_b:
            return x.get('rateBuy'), x.get('rateSell')
    return None, None

def save_operation_to_file(chat_id, operation_text):
    file_path = 'operations.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    new_record = f'[{chat_id}] {operation_text}\n'
    lines.append(new_record)

    if len(lines) > 10:
        lines = lines[-10:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def get_main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Обмен валют', 'Посмотреть курс валют')
    return keyboard

@bot.message_handler(commands=['start'])
def handle_command(message):
    keyboard = get_main_keyboard()
    name = message.from_user.first_name
    bot.reply_to(message, f'Привет, {name}!\nВыберите, чем я могу помочь.')
    bot.send_message(message.chat.id, 'Нажмите на кнопку:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Обмен валют')
def show_convert_val(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'awaiting_amount': True}
    bot.send_message(chat_id, "Введите сумму и исходную валюту (например: `100 USD`):", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == 'Посмотреть курс валют')
def show_rate(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('$', callback_data='btn1')
    button2 = telebot.types.InlineKeyboardButton('€', callback_data='btn2')
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    data = connect_mono()

    if call.data == 'btn1':
        rate_buy, rate_sell = get_rate(data, code_doll, code_grn)
        if rate_buy and rate_sell:
            bot.send_message(chat_id, f'💵 Курс доллара:\nПокупка — {rate_buy}\nПродажа — {rate_sell}')
        else:
            bot.send_message(chat_id, 'Не удалось получить курс доллара.')
        return

    elif call.data == 'btn2':
        rate_buy, rate_sell = get_rate(data, code_evro, code_grn)
        if rate_buy and rate_sell:
            bot.send_message(chat_id, f'💶 Курс евро:\nПокупка — {rate_buy}\nПродажа — {rate_sell}')
        else:
            bot.send_message(chat_id, 'Не удалось получить курс евро.')
        return

    if user_data.get(chat_id, {}).get('awaiting_target_currency'):
        amount = user_data[chat_id]['amount']
        from_curr = user_data[chat_id]['from_currency']
        to_curr = call.data.split('_')[1].upper()

        code_map = {'USD': code_doll, 'EUR': code_evro, 'UAH': code_grn}

        try:
            if from_curr == to_curr:
                result = amount
            else:
                if from_curr != 'UAH':
                    rate_from, _ = get_rate(data, code_map[from_curr], code_grn)
                    if rate_from is None:
                        raise ValueError("Ошибка получения курса.")
                    amount_uah = amount * rate_from
                else:
                    amount_uah = amount

                if to_curr != 'UAH':
                    _, rate_to = get_rate(data, code_map[to_curr], code_grn)
                    if rate_to is None:
                        raise ValueError("Ошибка получения курса.")
                    result = amount_uah / rate_to
                else:
                    result = amount_uah

            result = round(result, 2)
            text = f'{amount} {from_curr} = {result} {to_curr}'
            bot.send_message(chat_id, text)
            save_operation_to_file(chat_id, text)

            keyboard = get_main_keyboard()
            bot.send_message(chat_id, "Хотите сделать ещё одну операцию? Выберите вариант из меню", reply_markup=keyboard)

        except Exception as e:
            bot.send_message(chat_id, f'Ошибка при конвертации: {e}')

        user_data[chat_id]['awaiting_target_currency'] = False

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('awaiting_amount', False))
def handle_currency_input(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('💵 USD', callback_data='to_usd')
    button2 = telebot.types.InlineKeyboardButton('💶 EUR', callback_data='to_eur')
    button3 = telebot.types.InlineKeyboardButton('🇺🇦 UAH', callback_data='to_uah')
    keyboard.add(button1, button2, button3)

    text = message.text.strip().upper()
    try:
        amount_str, from_currency = text.split()
        amount = float(amount_str.replace(',', '.'))
        if from_currency not in ['USD', 'EUR', 'UAH']:
            raise ValueError("Неподдерживаемая валюта.")
    except:
        bot.send_message(chat_id, "Пожалуйста, введите сумму и валюту в формате, например: `100 USD`", parse_mode='Markdown')
        return

    user_data[chat_id] = {
        'amount': amount,
        'from_currency': from_currency,
        'awaiting_target_currency': True
    }

    bot.send_message(chat_id, "Теперь выберите целевую валюту:", reply_markup=keyboard)
    user_data[chat_id]['awaiting_amount'] = True



bot.polling()
