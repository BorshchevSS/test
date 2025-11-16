import hashlib
import uuid

class User:
    def __init__(self, username, email, password_hash=None, user_id=None):
        self.id = str(user_id) if user_id else str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password_hash = password_hash

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)

    def to_dict(self): #сериализация
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash
        }

    @classmethod
    def to_object(cls, data):
        return cls(
            username=data['username'],
            email=data['email'],
            password_hash=data['password_hash'],
            user_id=data['id']
        )

