 #function to login a user
def Login_user():
    username = input("Login: ")
    password = input("Password: ")
    #check if the username exists and the password matches
    if username in User_credentials and User_credentials[username] == password:
        print("Welcome, Back")
    else:
         print("Invalid username or password. Please try again.")


User_credentials = {}

# funtion to register a new user
def Register_user():
        username  = input("Enter your username: ")
        if username in User_credentials:
            print("Username already exists. Please choose a different username.")
        else:
            password = input("Enter your password:")
            User_credentials[username] = password
            print("Registration Successfull")
            Login_user()
                
    #function to login a user
def Login_user():
    username = input("Login: ")
    password = input("Password: ")
    #check if the username exists and the password matches
    if username in User_credentials and User_credentials[username] == password:
        print("Welcome, Back")
    else:
         print("Invalid username or password. Please try again.")

def Basic_Athentication():
    while True:
        print("""***Basic Authentication System***""" "\n\n")
        print("""1.Register)
        2.Login
        3.Exit""")

        option = input("Enter your option:")

        if option == "1":
            Register_user() 
        elif option == "2":
            Login_user()
        elif option == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.") 
Basic_Athentication()








