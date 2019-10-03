#!/home/ubuntu/.local/share/virtualenvs/build-a-blog-755dbNp1/bin/python
from datetime import datetime
from sqlalchemy import *

db2 = create_engine('ibm_db_sa://db2inst1:db2inst1@handymia.com:50000/handymia')

metadata = MetaData()

roles = Table('roles', metadata,
 Column('id', Integer(), primary_key=True),
 Column('role_name', String(20), nullable = False, unique = True, index = True),
 user = relationship('User')
 )

users = Table('users', metadata, 
 Column('id', Integer, primary_key = True),
 Column('user_name', String(20), nullable = False, unique = True, index = True),
 Column('first_name', String(10), nullable = False),
 Column('last_name', String(10), nullable = False),
 Column('email_address', String(30), key='email'),
 Column('password', String(12), nullable = False),
 Column('confirm', String(12), nullable = False),
 Column('created_on', DateTime(), default=datetime.now),
 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now),
 Column('role_id', Integer, ForeignKey('roles.id')))

metadata.create_all(db2)

users_table = Table('users', metadata, autoload=True, autoload_with=db2)

print(users_table)
