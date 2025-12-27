from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base
engine = create_engine('sqlite:///my_database.db', echo=True)

Base = declarative_base()
conn = engine.connect()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}')>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Alice', age=30)
new_user2 = User(name='Sergey', age=31)
session.add(new_user)
session.add(new_user2)

session.commit()


stmt = select(User).order_by(User.age)
resul = session.execute(stmt).fetchall()
print(resul)

