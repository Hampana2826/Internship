def login(login_page):
    def wrapper(user,password):
        if user=="admin" and password=="1234":
            print("login successfull")
            login_page(user,password)
        else:
            print("login failed")
    return wrapper




@login
def login_page(user,password):
    print("welcome to the dasboard")
login_page("admin","1234")