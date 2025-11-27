import requests

url = 'http://127.0.0.1:1420/start'

def score(q) -> int:
    if q['level'] == 'Легкий':
        return 1000
    elif q['level'] == 'Средний':
        return 5000
    else:
        return 15000

def start(number_quest=1, user_score=0):
    response = requests.get(url)
    questions = response.json()

    for x in questions:
        if x['id'] == number_quest:
            print(f"Вопрос №{x['id']}\n{x['quest']}")
            for variant in x['vars']:
                print(variant)

            user_answer = input(f"Если Вы ответите на этот вопрос, Вы заработаете {score(x)} грн\n"
                                f"Вы выбираете букву? -> ").strip().lower()

            post_url = f"{url}/{number_quest}"
            post_response = requests.post(post_url, json={'answer': user_answer})

            updated_question = post_response.json()

            if updated_question.get('done'):
                print(f"И это правильный ответ!\n"
                      f"Вы заработали {score(x)} грн\n")
                user_score += score(x)
                number_quest += 1
            else:
                print(f"\nЭто не правильный ответ.\n"
                      f"Правильный ответ: {x['answer']}\n"
                      f"Ваш заработок: {user_score} грн")
                break
    else:
        print(f"Вы выиграли!!!\n"
              f"Ваш выигрыш составляет {user_score} грн")

if __name__ == '__main__':
    start()