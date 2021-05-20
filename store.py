password_manager_dict = {}


def get_user_info(user_id):
    return password_manager_dict[user_id]


def store_password(user_id, key, value):
    password_manager_dict[user_id] = {}

# TODO: Create class to work with store with CRUD methods
# class UserStore:
#     def __init__(self, user_id):
#         self.store = password_manager_dict[user_id]
#
#     def __get_user_info_by_store(self):
#         user_store = password_manager_dict[self.user_id]
#
#     def save_password(self, key, value):
#         pass
