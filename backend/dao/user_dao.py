from datetime import datetime

from pymongo import MongoClient
from models.user_model import User, UserInDB


class UserDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.host, username=self.user, password=self.password)
        self.db = self.client[self.database]

    def disconnect(self):
        if self.client is not None:
            self.client.close()

    def create_user(self, user: User):
        users = self.db.users
        user_dict = user.dict()
        users.insert_one(user_dict)

    def get_user_by_username(self, username: str) -> UserInDB | None:
        users = self.db.users
        user_data = users.find_one({"username": username})
        if user_data is None:
            return None
        return UserInDB(**user_data)

    def get_last_user_id(self) -> int:
        users = self.db.users
        last_user = users.find().sort("id", -1).limit(1)
        if last_user is None:
            return 0
        return last_user[0]["id"]

    def blacklist_token(self, token: str):
        blacklist = self.db.blacklist
        blacklist.insert_one({"token": token, "blacklisted_on": datetime.now()})

    def is_token_blacklisted(self, token: str) -> bool:
        blacklist = self.db.blacklist
        blacklisted_token = blacklist.find_one({"token": token})
        return blacklisted_token is not None
