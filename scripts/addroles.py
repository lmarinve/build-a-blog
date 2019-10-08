#!/home/ubuntu/.local/share/virtualenvs/build-a-blog-755dbNp1/bin/python
from app import db
from app.models import Role
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.commit()
