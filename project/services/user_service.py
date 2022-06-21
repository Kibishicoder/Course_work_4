from project.dao.user import UserDAO
from project.utils import get_hash_by_password, compare_passwords
from project.exceptions import UserNotFound

class UserService:

    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_user_by_id(self, uid):
        user = self.user_dao.get_user_by_id(uid)
        if not user:
            raise UserNotFound
        return user

    def update_partial(self, user_d):
        user = self.get_user_by_id(user_d["id"])
        if "name" in user_d:
            user.name = user_d.get("name")
        if "surname" in user_d:
            user.surname = user_d.get("surname")
        if "favourite_genre" in user_d:
            user.favorite_genre = user_d.get("favourite_genre")
        self.user_dao.update(user)

    def update_password(self, user_d):
        user = self.get_user_by_id(user_d["id"])
        new_password = get_hash_by_password(user_d.get("new_password"))
        old_password_from_db = user.password
        if not compare_passwords(old_password_from_db, get_hash_by_password(user_d.get("old_password"))):
            raise Exception
        user.password = new_password
        self.user_dao.update(user)







