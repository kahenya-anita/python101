#Class Atrr and methods
# Atrr are shared across the instance of a class
# Method alows us to perform an action on an instance of a class and gives us flexibility

class User:
    
    active_users = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        User.active_users += 1
        
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    
student1 = User("John", 20, "Male")
student2 = User("Jane", 21, "Female")
print(User.display_active_users())
        
    
    