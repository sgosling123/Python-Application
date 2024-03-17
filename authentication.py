class accounts:
    session_username = None  ### Store the username for global/public access to it instead of being private
  
    USERS = {
        'user': {'password': '123', 'account_role': 'user'},
        'superuser': {'password': '123', 'account_role': 'superuser'},
        'admin': {'password': '123', 'account_role': 'administrator'},
        'test': {'password': '123', 'account_role': 'user'},
    }
    
###### This asks for username and password, then checks against the USERS dictionary above ######
    @staticmethod
    def login(): 
        while True:
            username = input("Enter your username or type exit: ")
            if username.lower() == 'exit':
                return False, None
              
            password = input("Enter your password or type exit: ")
            if password.lower() == 'exit':
                return False, None
              
            user = accounts.USERS.get(username)
            if user and user['password'] == password:
                print("Login successful.")
                accounts.session_username(username) ### Sets session username
                return True, username, user['account_role']
            else:
                print("Invalid username or password.")
                
    @staticmethod
    def session_username(username):
        accounts.username = username  # Set the username in the class attribute
                
###### Function for a superuser to reset a standard user password ######
    @staticmethod
    def reset_standard_password():
        print('\n')
        print("\x1B[1m" "| RESET PASSWORD (SUPERUSER) |""\x1B[0m", '\n'*2)
        accounts.list_users() ### Lists the already existing users
        while True:
            username_for_superuser_reset = input("Enter the username of the user whose password you want to reset or type exit: ")
            if username_for_superuser_reset.lower() == 'exit':
                return
              
            if username_for_superuser_reset in accounts.USERS and accounts.USERS[username_for_superuser_reset]['account_role'] == 'administrator':
                print("You are not allowed to reset the password for this user.")
                continue
              
            new_password = input(f"Enter the new password for {username_for_superuser_reset}: ")
            accounts.USERS[username_for_superuser_reset]['password'] = new_password
            print(f"Password for {username_for_superuser_reset} has been reset.")
            return
          
###### Function for an admin to reset a password ######
    @staticmethod
    def reset_any_password():
        print('\n')
        print("\x1B[1m" "| RESET PASSWORD (ADMINISTRATOR) |""\x1B[0m", '\n'*2)
        accounts.list_users() ### Lists the already existing users
        while True:
            username_for_reset = input("Enter the username of the user whose password you want to reset or type exit: ")
            if username_for_reset.lower() == 'exit':
                return
              
            if username_for_reset not in accounts.USERS['username']:
                print("You are not allowed to reset the password for this user.")
                continue
              
            new_password = input(f"Enter the new password for {username_for_superuser_reset}: ")
            accounts.USERS[username_for_superuser_reset]['password'] = new_password
            print(f"Password for {username_for_superuser_reset} has been reset.")
            return
          
###### Function for a superuser to create a standard user ######
    @staticmethod
    def create_standard_user():
        print('\n')
        print("\x1B[1m" "| CREATE USER (SUPERUSER) |""\x1B[0m", '\n'*2)
        accounts.list_users() ### Lists the already existing users
        while True:
            new_username = input("Enter the username for the new user or type exit: ")
            if new_username.lower() == 'exit':
                return
              
            if new_username in accounts.USERS:
                print("Username already exists. Please choose a different username.")
                continue
              
            new_password = input(f"Enter the password for {new_username}: ")
            user_role = 'user'  # Superusers only allowed to create standard users
              
            accounts.USERS[new_username] = {'password': new_password, 'account_role': user_role}
            print(f"{new_username} with {user_role} role created successfully.")
            return
          
###### Function for an admin to create a user of any role ######
    @staticmethod
    def create_any_user():
        print('\n')
        print("\x1B[1m" "| CREATE USER (ADMINISTRATOR) |""\x1B[0m", '\n'*2)
        accounts.list_users() ### Lists the already existing users
        while True:
            new_username = input("Enter the username for the new user or type exit: ")
            if new_username.lower() == 'exit':
                return
              
            if new_username in accounts.USERS:
                print("Username already exists. Please choose a different username.")
                continue
              
            new_password = input(f"Enter the password for {new_username}: ")
            user_role = input(f"Enter the role for {new_username} (user/superuser/administrator): ")
            if user_role.lower() not in ['user', 'superuser', 'administrator']:
                print("Invalid user role. Please choose from user, superuser, or administrator.")
                continue
              
            accounts.USERS[new_username] = {'password': new_password, 'account_role': user_role}
            print(f"{new_username} with {user_role} role created successfully.")
            return
          
###### Function for an admin to delete a user ######
    @staticmethod
    def delete_user():
        print('\n')
        print("\x1B[1m" "| DELETE USER (ADMINISTRATOR) |""\x1B[0m", '\n'*2)
        accounts.list_users() ### Lists the already existing users
        while True:
            username_to_delete = input("Enter the username of the user you want to delete or type exit: ")
            if username_to_delete.lower() == 'exit':
                return
              
            if username_to_delete not in accounts.USERS:
                print("Username does not exist. Please enter a valid username.")
                continue
               
            del accounts.USERS[username_to_delete]
            print(f"{username_to_delete} has been deleted.")
            return
          
###### Function for an admin to change a user role ######
    @staticmethod
    def change_user_role():
        print('\n')
        print("\x1B[1m" "| CHANGE USER ROLE (ADMINISTRATOR) |""\x1B[0m", '\n'*2)
        accounts.list_users() ### Lists the already existing users
        while True:
            username_role_to_change = input("Enter the username of the user whose role you want to change or type exit: ")
            if username_role_to_change.lower() == 'exit':
              return
              
            if username_role_to_change not in accounts.USERS:
              print("Username does not exist. Please enter a valid username.")
              continue
              
            new_role = input(f"Enter the new role for {username_role_to_change} (user/superuser/administrator): ")
            
            if new_role.lower() not in ['user', 'superuser', 'administrator']:
              print("Invalid user role. Please choose from user, superuser, or administrator.")
              continue
          
            accounts.USERS[username_role_to_change]['account_role'] = new_role
            print(f"{username_role_to_change} has been changed to {new_role} role.")
            return
          
###### Function to list all users ######
    @staticmethod
    def list_users():
        print("\x1B[1m""List of Users:""\x1B[0m", '\n')
        for username, details in accounts.USERS.items():
            print("\x1B[1m""Username:""\x1B[0m", f"{username},", "\x1B[1m""Role:""\x1B[0m", details['account_role'])
        print('\n')