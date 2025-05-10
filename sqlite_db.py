from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Create SQLite engine
engine = create_engine('sqlite:///students.db', echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
