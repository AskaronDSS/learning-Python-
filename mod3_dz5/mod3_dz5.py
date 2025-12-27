from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker

def get_engine():
    return create_engine('sqlite:///mod3_dz5/mod3_dz5.db', echo=True)

Base = declarative_base()

def get_session():
    sess = sessionmaker(bind=get_engine())
    sess = sess()
    return sess


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<Users(username='{self.username}', email='{self.email}')>"

class User:
    def __init__(self, user_name, password, email):
        self.username = user_name
        self.password = password
        self.email = email

    def register(self):
        Base.metadata.create_all(get_engine())
        sess = get_session()
        new_user = Users(username= self.username, password= self.password, email= self.email)
        sess.add(new_user)
        sess.commit()

    def login(self, user_name, password):
        sess = get_session()
        exc = select(Users).where(Users.username == user_name, Users.password == password)
        res = sess.execute(exc).scalars().all()
        if res:
            return '-----Welcome-----'
        else:
            return '-----You not pass!!!-----'
    
# def decor_check_input(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except TypeError:
#             print('Select 1, 2 or 3')
#         except ValueError:
#             print('Select 1, 2 or 3')
#     return wrapper

# @decor_check_input
# def input_user(hint: str)-> str:
#     a = input(f'Enter {hint}')
#     return a


while True:
    select_user = input('Select:\n1 - register\n2 - login\n3 - exit\n')
    if select_user == '1':
        username = input('Enter username: ')
        password = input('Enter password: ')
        email = input('Enter email: ')
        person = User(username, password, email)
        person.register()
        print('-----I remembered you!-----')

    if select_user == '2':
        username = input('Enter username: ')
        password = input('Enter password: ')
        user = User(username, password, None)
        print(user.login(username, password))
    if select_user == '3':
        print('-----See you later-----')
        break


# def test_conn():
#     assert get_engine().connect()
# def test_register_login():
#     person = User('test_name', 'test_pass', 'test_email')
#     person.register()
#     assert person.login('test_name', 'test_pass') == '-----Welcome-----'
#