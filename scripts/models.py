from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from handymia import app

#db = SQLAlchemy(app)
engine = create_engine(app)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'schema': 'db2inst1'}
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'db2inst1'}
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, index=True)
    first_name = Column(String(10), nullable=False)
    last_name = Column(String(10), nullable=False)
    password = Column(String(12), nullable=False)
    confirm = Column(String(12), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship(Role, backref='children')

    def __repr__(self):
        return '<User %r>' % self.user_name

