from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

# Creating a DB Instance
engine = create_engine("sqlite:///blog2.db")


Base = declarative_base()
#Creating the Tables

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    profile = relationship("Profile", back_populates="user")
    posts= relationship("Post", back_populates="user")
    
class Profile(Base):
    
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True)
    genre = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="profile")
    
class Post(Base):
    
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user =  relationship("User", back_populates="posts")
  

if __name__ == '__main__':  
      
# Creating a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    test_user = User(name="Test User")
    test_profile = Profile(genre="Test Genre", user=test_user)
    test_post = Post(title="Test Post", content="Test Content", user=test_user)
    session.add_all([test_user, test_profile, test_post])
    session.commit()