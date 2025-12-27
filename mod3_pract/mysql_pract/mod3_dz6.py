import mysql.connector
from mysql.connector import Error

# ---------- ПОДКЛЮЧЕНИЕ ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="db123123",
        database="db_mod3"
    )

class User:
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def register(self):
        try:
            db = get_connection()
            cursor = db.cursor()

            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                (self.username, self.password, self.email)
            )

            db.commit()
            print(" ---------- Регистрация прошла успешно ----------!")

        except Error as e:
            if "Duplicate entry" in str(e):
                print(" Такой логин или емейл уже зарегестрирован!")
            else:
                print(" Ошибка:", e)

        finally:
            cursor.close()
            db.close()

    @staticmethod
    def login(username, password):
        db = get_connection()
        cursor = db.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            print("✅ Успішний вхід!")
            return user[0]  # user_id
        else:
            print("❌ Неправильні дані!")
            return None


class Site:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_site(self):
        site_name = input("Назва сайту: ")
        login_type = input("Тип входу (google / apple / facebook / інше): ").lower()

        if login_type in ["google", "apple", "facebook"]:
            site_login = None
            site_password = None
        else:
            site_login = input("Логін: ")
            site_password = input("Пароль: ")

        db = get_connection()
        cursor = db.cursor()

        cursor.execute(
            """INSERT INTO sites (user_id, site_name, site_login, site_password, login_type)
               VALUES (%s, %s, %s, %s, %s)""",
            (self.user_id, site_name, site_login, site_password, login_type)
        )

        db.commit()
        cursor.close()
        db.close()
        print("✅ Дані про сайт збережені!")

    def show_sites(self):
        db = get_connection()
        cursor = db.cursor()

        cursor.execute(
            "SELECT site_name, site_login, site_password, login_type FROM sites WHERE user_id=%s",
            (self.user_id,)
        )

        sites = cursor.fetchall()
        cursor.close()
        db.close()

        if not sites:
            print("ℹ️ Немає збережених сайтів")
            return

        print("\n📌 Ваші сайти:")
        for site in sites:
            print(f"""
Сайт: {site[0]}
Тип входу: {site[3]}
Логін: {site[1]}
Пароль: {site[2]}
-------------------------
""")


def main():
    while True:
        print("""
        
        """)
        choice = input("1 - Регистрация\n2 - Вход\n3 - Выход\nВыберите пунк меню: ")

        if choice == "1":
            print("-------- Вы выбрали РЕГИСТРАЦИЮ --------")
            username = input("Логин: ")
            password = input("Пароль: ")
            email = input("Email: ")

            user = User(username, password, email)
            user.register()

        elif choice == "2":
            print("-------- Вы выбрали ВХОД --------")
            username = input("Логін: ")
            password = input("Пароль: ")

            user_id = User.login(username, password)

            if user_id:
                site_manager = Site(user_id)

                while True:
                    print("""
                    1 - Добавить сайт
                    2 - Показать сайты
                    3 - Выйти с аккаунта
                    """)
                    sub = input("Что надо? : ")

                    if sub == "1":
                        site_manager.add_site()
                    elif sub == "2":
                        site_manager.show_sites()
                    elif sub == "3":
                        break

        elif choice == "3":
            print(" -------- ВЫХОД --------")
            break

        else:
            print("Выберите (1 / 2 / 3)")


if __name__ == "__main__":
    main()