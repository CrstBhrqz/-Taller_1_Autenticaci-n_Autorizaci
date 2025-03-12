from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, es_admin):
        self.id = id
        self.username = username
        self.password = password
        self.es_admin = es_admin

# base de datos de usuarios ejemplo

users_db = {
  "zeus": User(1, 'admin', 'admin', True),
    "hera": User(2, 'user', 'user', False),
    "poseidon": User(3, 'user2', 'user2', False),
    "apollo": User(4, 'user3', 'user3', False),
}