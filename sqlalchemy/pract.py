from sqlalchemy import Column, Integer, String, create_engine, select, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    user = relationship("User", backref="pro_file", uselist=False)

    def __repr__(self):
        return f"<Profile(username='{self.username}', email='{self.email}')>"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'), unique=True)
    name = Column(String)
    profile = relationship("Profile", backref="users", uselist=False)

    def __repr__(self):
        return f"<User(name='{self.name}')>"
    

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sess = Session()


new_prof = Profile(username='Sergey', email='dssergey94@gmail.com')
new_prof2 = Profile(username='Alice', email='123123@asd')

new_user = User(name='Eve', profile=new_prof2)
new_user2 = User(name='Sergeevich', profile=new_prof)


# sess.add(new_prof)
# sess.add(new_prof2)
# sess.add(new_user)
# sess.add(new_user2)

# sess.commit()

exc = select(Profile).join(User).where(User.name == 'Sergeevich')

res = sess.execute(exc).scalars().all()
print(res)
print(res[0].user)
