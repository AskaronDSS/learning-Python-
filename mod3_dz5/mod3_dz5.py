import unittest
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///mod3_dz5/mod3_dz5.db', echo=True)

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<Users(username='{self.username}', email='{self.email}')>"

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register(self):
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        sess = Session()
        new_user = Users(username= self.username, password= self.password, email= self.email)
        sess.add(new_user)
        sess.commit()

    def login(self, username, password):
        Session = sessionmaker(bind=engine)
        sess = Session()
        exc = select(Users).where(Users.username == username, Users.password == password)
        res = sess.execute(exc).scalars().all()
        if res:
            return 'Welcome'
        else:
            return 'You not pass!!!'
    

# while True:
#     try:
#         select_user = input(f'Select options:\n1 -> Register\n2 -> Login\n3 -> Exit\n')
#         if select_user == '1':
#             username = input('Enter username: ')
#             password = input('Enter password: ')
#             email = input('Enter email: ')
#             user = User(username, password, email)
#             user.register()
#             print('I remembered you!')
#     except:
#         raise TypeError('Select 1, 2 or 3')
#     if select_user == '2':
#         username = input('Enter username: ')
#         password = input('Enter password: ')
#         user = User(username, password, None)
#         print(user.login(username, password))
#     if select_user == '3':
#         break

class MyUnitTest(unittest.TestCase):
    
    def test_register_and_login(self):
        #Создаем нового пользователя и регистрируем его
        user = User('test_user', 'test_pass', 'test_email')
        user.register()
        #Тест на правильный логин и пароль
        login_result = user.login('test_user', 'test_pass')
        self.assertEqual(login_result, 'Welcome')
        #Тест на неправильный логин и пароль
        login_result_fail = user.login('test_user', 'wrong_pass')
        self.assertEqual(login_result_fail, 'You not pass!!!')
   

if __name__ == '__main__':
    unittest.main()
    