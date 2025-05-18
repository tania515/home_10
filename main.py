from user import User
from userManager import UserManager

manager = UserManager()

user_1 = User("Nike", "nike@gmail.com", 45)
print(user_1) 

manager.add_user(user_1)
manager.print_users()
manager.find_user("Nike")
manager.remove_user("Nike")
manager.print_users()