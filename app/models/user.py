from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# base de datos de usuarios ejemplo

users_db = {
    1: User(1, 'admin', 'admin'),
    2: User(2, 'user', 'user'),
    3: User(3, 'user2', 'user2'),
    4: User(4, 'user3', 'user3'),
}