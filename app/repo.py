# from . import Users
#
#
# def create_user(email, username, password_hash):
#     """Creates a user in database, if validation from Check_existing_users passes"""
#
#     data = dict(
#         email=email,
#         username=username,
#         password_hash=password_hash)
#
#     if check_existing_users(username, email):
#         user = Users(data)
#         user.save()
#         return user
#
#
# def check_existing_users(username: str, email: str) -> bool:
#     """ Returns True if Email or username doesn't exist in the database"""
#
#     if User.collection.find_one({"username": username}) is not None:
#         print(f"{username} already exists in database")
#         return False
#
#     if User.collection.find_one({"email": email}) is not None:
#         print(f"{email} already exists in database")
#         return False
#     return True
