'''

Decorators = "Add behavior."
"Before running this method, check login."
"After running this method, log the result."

'''
class User:
    def login_required(func):
        def wrapper(self):  # Notice 'self'
            print("Checking login...")
            func(self)
        return wrapper
    @login_required
    def view_profile(self):
        print("Welcome to your profile!")

    @login_required
    def settings(self):
        print("Opening settings...")


user = User()

user.view_profile()
user.settings()