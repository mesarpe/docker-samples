from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    String,
    Date,
    DateTime,
    Time,
    ForeignKey,
    Boolean,
    )

class Description(Base):
    __tablename__ = 'descriptions'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(500))

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    salt = Column(String(32))
    password =  = Column(String(32))
