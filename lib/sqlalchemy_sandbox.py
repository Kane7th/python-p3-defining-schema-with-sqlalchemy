#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    # This creates an SQLite database named 'students.db' in the current directory.
    engine = create_engine('sqlite:///students.db') 
    # This will create the database and the table if they do not exist.
    Base.metadata.create_all(engine) 

