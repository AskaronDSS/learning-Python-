from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Define the base class for declarative models
Base = declarative_base()

# 2. Define a model class (maps to a 'users' table)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"

# 3. Create a database engine (in-memory SQLite database for this example)
# The `echo=True` argument enables logging of all generated SQL statements
engine = create_engine('sqlite:///:memory:', echo=True)


Base.metadata.create_all(engine)

# 5. Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# 6. Perform CRUD operations

# --- CREATE (Insert data) ---
# Create new user objects
user1 = User(name='spongebob', fullname='Spongebob Squarepants', nickname='sponge')
user2 = User(name='patrick', fullname='Patrick Star', nickname='pat')
session.add(user1)
session.add(user2)

# Commit the changes to the database
session.commit()


users_query = select(User).filter(User.id == 2)
pat_user = session.execute(users_query).fetchone()
print(pat_user)
# for user in users:
#     print(user)
