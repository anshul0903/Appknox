from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "sqlite:///./appknox.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()  #Used to create models, model is type of data which will go into db, schemas are used to carry the type of infor from user to the api, orm functionality is used to performing the operation, putting the data into db, api functionality is used to create method for the api to create data

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
