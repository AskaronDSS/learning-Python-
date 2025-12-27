import mysql.connector
from mysql.connector import Error

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
                """INSERT INTO users (username, password, email) VALUES (%s, %s, %s)""",
                (self.username, self.password, self.email)
            )

            db.commit()
            print(" ---------- Регистрация прошла успешно ----------")

        except Error as e:
            if "Duplicate entry" in str(e):
                print(" Такой логин или емейл уже зарегистрирован!")
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
            """SELECT id FROM users WHERE username=%s AND password=%s""",
            (username, password)
        )

        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            print("---------- Приветствую ----------")
            return user[0]  # user_id
        else:
            print("---------- Ты не пройдешь!! ----------")
            return None


class Site:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_site(self):
        site_name = input("Название сайта: ")
        login_type = input("Тип входа (google / apple / facebook / другой вариант): ").lower()

        if login_type in ["google", "apple", "facebook"]:
            site_login = None
            site_password = None
        else:
            site_login = input("Логин: ")
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
        print("Все ок! Запомнил")

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
            print("У вас пусто")
            return

        print("\nВаши сайты:")
        for ind_site, site in enumerate(sites):
            print(f"""
                -------- Запись № {ind_site} --------
                Сайт: {site[0+1]}
                Тип входа: {site[3]}
                Логин: {site[1]}
                Пароль: {site[2]}
                """)


def main():
    while True:
        choice = input("1 - Регистрация\n2 - Вход\n3 - Выход\nВыберите пункт меню: ")

        if choice == "1":
            print("-------- Вы выбрали РЕГИСТРАЦИЮ --------")
            username = input("Логин: ")
            password = input("Пароль: ")
            email = input("Email: ")

            user = User(username, password, email)
            user.register()

        elif choice == "2":
            print("-------- Вы выбрали ВХОД --------")
            username = input("Логин: ")
            password = input("Пароль: ")

            user_id = User.login(username, password)

            if user_id:
                site_manager = Site(user_id)

                while True:
                    sub = input("1 - Добавить сайт\n2 - Показать сайты\n3 - Выйти с аккаунта\nШо надо? : ")

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