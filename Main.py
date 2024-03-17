from authentication import accounts
from pagemodule import PageManager

###### Options Menu - Asks the user to pick an option based on their role ######
def optionsMenu(account_role, page_manager):
    while True:
        print("Please type the corresponding number and press enter to select from the below options.", '\n')
        
        if account_role == 'user': ### Lists user options
            print("\x1B[4m""As a " f"{account_role} you can:""\x1B[0m", '\n')
            print("\x1B[1m""1 ""\x1B[0m" "Go to page")
            print("\x1B[1m""2 ""\x1B[0m" "Search by keyword")
            print("\x1B[1m""3 ""\x1B[0m" "Edit page", '\n')
            print("\x1B[1m""10 ""\x1B[0m" "Save changes to pages.txt", '\n')
            print("\x1B[1m""0 ""\x1B[0m" "Exit", '\n')
            
        elif account_role == 'superuser': ### Lists superuser options
            print("\x1B[4m""As a " f"{account_role} you can:""\x1B[0m", '\n')
            print("\x1B[1m""1 ""\x1B[0m" "Go to page")
            print("\x1B[1m""2 ""\x1B[0m" "Search by keyword")
            print("\x1B[1m""3 ""\x1B[0m" "Edit page")
            print("\x1B[1m""4 ""\x1B[0m" "Create new page")
            print("\x1B[1m""5 ""\x1B[0m" "Delete page")
            print("\x1B[1m""6 ""\x1B[0m" "Create new standard user")
            print("\x1B[1m""7 ""\x1B[0m" "Reset standard user password", '\n')
            print("\x1B[1m""10 ""\x1B[0m" "Save changes to pages.txt", '\n')
            print("\x1B[1m""0 ""\x1B[0m" "Exit", '\n')
            
        elif account_role == 'administrator': ### Lists administrator options
            print("\x1B[4m""As a " f"{account_role} you can:""\x1B[0m", '\n')
            print("\x1B[1m""1 ""\x1B[0m" "Go to page")
            print("\x1B[1m""2 ""\x1B[0m" "Search by keyword")
            print("\x1B[1m""3 ""\x1B[0m" "Edit page")
            print("\x1B[1m""4 ""\x1B[0m" "Create new page")
            print("\x1B[1m""5 ""\x1B[0m" "Delete page")
            print("\x1B[1m""6 ""\x1B[0m" "Create new user")
            print("\x1B[1m""7 ""\x1B[0m" "Reset user password")
            print("\x1B[1m""8 ""\x1B[0m" "Delete user")
            print("\x1B[1m""9 ""\x1B[0m" "Change user role", '\n')
            print("\x1B[1m""10 ""\x1B[0m" "Save changes to pages.txt", '\n')
            print("\x1B[1m""0 ""\x1B[0m" "Exit", '\n')
            
###### These are the user choices for the menu ######
        
        choice = int(input("Enter your choice:"'\n')) ### Asks for user choice
        print("\x1B[1m" + "-" * 50 + "\x1B[0m") ### Puts 50 dashes
        
        ### Exit application ###
        if choice == 0:
          return None, None
          
        ### Go to page ###
        if choice == 1:
            page_manager.load_from_notepad(filename="pages.txt")
            page_manager.goto_page()
            print('\n')
            continue
            
        ### Search by keyword ###
        if choice == 2:
            page_manager.load_from_notepad(filename="pages.txt")
            page_manager.search_by_keyword()
            print('\n')
            continue
            
        ### Edit page ###
        if choice == 3:
            page_manager.load_from_notepad(filename="pages.txt")
            page_manager.edit_page()
            print('\n')
            continue
            
        ### Create new page | Users not allowed to ###
        if choice == 4 and account_role != 'user':
            page_manager.load_from_notepad(filename="pages.txt")
            page_manager.add_page_user()
            print('\n')
            continue
            
        elif choice == 4:
            print("Invalid choice. Please try again.")
            continue
        
        ### Delete page | Users not allowed to ###
        if choice == 5 and account_role != 'user':
            page_manager.load_from_notepad(filename="pages.txt")
            page_manager.delete_page()
            print('\n')
            continue
          
        elif choice == 5:
            print("Invalid choice. Please try again.")
            continue
            
        ### Create user | Admins only ###
        if choice == 6 and account_role == 'administrator':
            accounts.create_any_user()
            print('\n')
            continue
          
        ### Create standard user | Superuser only ###
        elif choice == 6 and account_role == 'superuser':
            accounts.create_standard_user()
            print('\n')
            continue
            
        elif choice == 6:
            print("Invalid choice. Please try again.")
            continue
          
        ### Reset password | Admins only ###
        if choice == 7 and account_role == 'administrator':
            accounts.reset_any_password()
            print('\n')
            continue
          
        ### Reset standard user password | Superuser only ###
        elif choice == 7 and account_role == 'superuser':
            accounts.reset_standard_password()
            print('\n')
            continue
            
        elif choice == 7:
            print("Invalid choice. Please try again.")
            continue
          
        ### Delete user | Admins only ###
        if choice == 8 and account_role == 'administrator':
            accounts.delete_user()
            print('\n')
            continue
          
        elif choice == 8:
            print("Invalid choice. Please try again.")
            continue
            
        ### Change user role | Admins only ###
        if choice == 9 and account_role == 'administrator':
            accounts.change_user_role()
            print('\n')
            continue
          
        elif choice == 9:
            print("Invalid choice. Please try again.")
            continue
          
        ### Save all changes to notepad
        if choice == 10:
            page_manager.save_to_notepad()
            continue
            
        ### Wrong choice ###
        else:
            print("Invalid choice. Please try again.")
            continue
            
###### Main application ######
def main():
    
    login_success, username, account_role = accounts.login() ### Calls the login function to authenticate the user, and returns their username and role.
    if login_success:
      print(f"Welcome, {username}!")
    
      page_manager = PageManager() ### Calls the pageManager function into the main application
    
      ###### These pages only exist for testing purposes; these should replaced with an external text document ######
      #page_manager.add_page("Blue screening", ["blue", "screening", "screen", "BSOD"], "If the computer blue screens:""\n""1. Check the event log for errors""\n""2. Reseat or replace the RAM""\n""3. Open Command prompt and run SFC /scannow""\n""4. Reimage the computer""\n")
      #page_manager.add_page("Account locked", ["account", "locked", "locking", "user", "credentials"], "If the user account is locked:""\n""1. Open Active Directory and unlock user account""\n""2. On the machine which locked them out, open credential manager and delete old credentials""\n")
      #page_manager.add_page("Website inaccessible", ["website", "internet", "webpage", "network"], "If a website is inaccessible:""\n""1. Try to access it on a non-domain device, such as mobile phone to work out if it's their issue or ours""\n""If the issue in on our side""\n""1. Try clearing the cache""\n""2. Try turning the proxy off""\n""3. Use the ping command to see if the traffic is reaching the destination""\n""4. Use the tracert command to see which network route it is taking.""\n")
      ######
    
      page_manager.load_from_notepad(filename="pages.txt") ### Loads up the "pages.txt" where all the page data is kept
    
      optionsMenu(account_role, page_manager) ### Calls the optionsMenu function and shares the user role with it
    
    else: 
        return

if __name__ == "__main__":
    main()
