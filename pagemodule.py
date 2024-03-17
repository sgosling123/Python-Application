from datetime import datetime
from authentication import accounts

###### Says that a class called Page exists and sets default values for it ######
class Page:
    def __init__(self, title, keywords, text, created_by, date_created=None, date_edited=None, edited_by=None, times_viewed=0):
        self.title = title
        self.keywords = keywords
        self.text = text
        self.date_created = date_created if date_created is not None else datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.created_by = created_by
        self.date_edited = date_edited
        self.edited_by = edited_by
        self.times_viewed = times_viewed

###### Required to interact with the Page class ###### 
class PageManager:
    def __init__(self):
        self.pages = {}

###### Function to add a page (not directly accessible by users, used for testing purposes) ######
    def add_page(self, title, keywords, text, date_created=None, created_by=None, date_edited=None, edited_by=None, times_viewed=0):
        self.pages[title] = Page(title, keywords, text, date_created, created_by, date_edited, edited_by, times_viewed)
        
###### Function to add a page (user accessible) ###### 
    def add_page_user(self, title=None, keywords=None, text=None, username=None):
        print('\n')
        print("\x1B[1m" "| CREATE NEW PAGE |""\x1B[0m", '\n'*2)
        
        title = input("Enter the title of the page or type exit to quit: ")
        if title.lower() == 'exit': ### Exit
            print('\n', "...", '\n')
            return
        
        keywords = input("Enter keywords for the page separated by commas: ")
        if keywords.lower() == 'exit': ### Exit
            print('\n', "...", '\n')
            return
        
        ### Commas used to separate keywords  
        keywords = [kw.strip() for kw in keywords.split(',')]
        
        text = input("Enter the text for the page: ")
        if text.lower() == 'exit': ### Exit
            print('\n', "...", '\n')
            return
        
        ### Ask user to confirm before committing the new page
        confirm = input("Do you want to add this page? (y/n): ").lower()
        if confirm == 'y':
            created_by = accounts.session_username(username) ### Sets the Created by field to logged in username
            date_created = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.pages[title] = Page(title, keywords, text, created_by, date_created)
            print("\nPage successfully added.")
        else:
            print("New page cancelled.")
        
###### Function to edit a page ######
    def edit_page(self):
        print('\n')
        print("\x1B[1m" "| EDIT PAGE |""\x1B[0m", '\n'*2)
        
        self.list_pages() ### List all pages
        pagename = input("Enter the name of the page you want to edit or type exit to quit: ")
        
        if pagename.lower() == 'exit': ### Exit
            print('\n', "...", '\n')
            return
      
        if pagename not in self.pages:
            print(f"'{pagename}' does not exist.")
            return

        print("\n")
        print(f"\x1B[1mEditing page {pagename}\x1B[0m\n")
        
        new_title = input("Enter the new title (press Enter to keep the current title): ")
        if new_title.lower() == 'exit': ### Exit
            print('\n', "...", '\n')
            return
        
        new_keywords = input("Enter the new keywords separated by commas (press Enter to keep the current keywords): ")
        if new_keywords.lower() == 'exit': ### Exit
           print('\n', "...", '\n')
           return
        
        new_text = input("Enter the new text (press Enter to keep the current text): ")
        if new_text.lower() == 'exit': ### Exit
            print('\n', "...", '\n')
            return
      
        ### Update page attributes if new values are provided
        if new_title:
            self.pages[pagename].title = new_title
        if new_keywords:
            self.pages[pagename].keywords = [kw.strip() for kw in new_keywords.split(',')]
        if new_text:
            self.pages[pagename].text = new_text
        
        print(f"\n '{pagename}' has been updated successfully.")
      
###### Function to delete a page ######
    def delete_page(self):
        print('\n')
        print("\x1B[1m" "| DELETE PAGE |""\x1B[0m", '\n'*2)
        
        self.list_pages() ### List all pages
        page_to_delete = input("Enter the title of the page you want to delete or type exit to quit: ")
        
        if page_to_delete.lower() == 'exit': ### Exit
                print('\n', "...", '\n')
                return
        elif page_to_delete in self.pages:
            ### Asks user to confirm to delete
            confirm = input(f"Are you sure you want to delete '{page_to_delete}'? (y/n): ")
            if confirm.lower() == 'y':
                del self.pages[page_to_delete]
                print(f"'{page_to_delete}' has been deleted.")
            else:
                print(f"'{page_to_delete}' was not deleted.")
        else:
            print(f"'{page_to_delete}' does not exist.")
      
###### Function to list all pages ######
    def list_pages(self):
        print("\x1B[1m""Existing pages:""\x1B[0m")
        for title, page in self.pages.items():
            print(f"{title}")
        print('\n')
            
###### Function to go to a specific page ######
    def goto_page(self):
        print('\n')
        print("\x1B[1m""| GO TO PAGE |""\x1B[0m", '\n'*2)
        self.list_pages() ### List all pages
        while True:
            pagename = input("Enter page name or type exit to quit: ")
            if pagename.lower() == 'exit': ### Exit
                print('\n', "...", '\n')
                break ### Get out of the loop
              
            page = self.pages.get(pagename)
            if page:
                print(f"Title: {page.title}")
                print(f"Keywords: {page.keywords}")
                print(f"Text: {page.text}")
                print(f"Date Created: {page.date_created}")
                print(f"Created By: {page.created_by}")
                print(f"Date Edited: {page.date_edited}")
                print(f"Edited By: {page.edited_by}")
                print(f"Times Viewed: {page.times_viewed}")
                print('\n')
                
            else:
                print("Page not found.")
                
###### Function to search pages by their keywords ######
    def search_by_keyword(self):
        print('\n')
        print("\x1B[1m""| SEARCH BY KEYWORD |""\x1B[0m", '\n'*2)
        while True:
            keyword = input("Enter a keyword to search for or type exit to quit: ")
            if keyword.lower() == 'exit': ### Exit
                print('\n', "...", '\n')
                return None
            
            matching_pages = []
            for title, page in self.pages.items():
                if keyword in page.keywords:
                    matching_pages.append(title)
            if matching_pages:
                print(f"Pages matching keyword '{keyword}':")
                for title in matching_pages:
                    print(title)
                return matching_pages  ### If there is matching pages, return them
            else:
                print(f"No pages found matching '{keyword}' keyword.")
                search_again = input("Do you want to search again? (y/n): ")
                if search_again.lower() != 'y':
                    break ### breaks the loop as the user said no
                  
##########################################################
### Pages are now saved to notepad in the root directory
### The Page Title starts with Title:
### The Page Keywords start with Keywords:
### The Page Text with Text: and continues until the ^ get-out character is found

####### This saves all pages to the notepad repository ######
    def save_to_notepad(self, filename="pages.txt"):
        try:
            with open(filename, 'w') as file:
                for title, page in self.pages.items():
                    file.write(f"Title: {page.title}\n")
                    file.write(f"Keywords: {', '.join(page.keywords)}\n")
                    file.write(f"Date created: {page.date_created}\n")
                    file.write(f"Created by: {page.created_by}\n")
                    file.write(f"Date edited: {page.date_edited}\n")
                    file.write(f"Edited by: {page.edited_by}\n")
                    file.write(f"Times viewed: {page.times_viewed}\n")
                    file.write("Text:\n")
                    file.write(page.text + '\n^\n')  ### Use ^ as the end marker for text
            print("Successfully saved to pages.txt")
        except Exception as e:
            print(f"Error occurred while saving pages: {e}")  ### Tries to tell us what the exception error is
        
####### Silent save - same as above, but no messages ######
    def save_silent_to_notepad(self, filename="pages.txt"):
        try:
            with open(filename, 'w') as file:
                for title, page in self.pages.items():
                    file.write(f"Title: {page.title}\n")  ### Page title
                    file.write(f"Keywords: {', '.join(page.keywords)}\n")  ### Keywords
                    file.write(f"Date created: {page.date_created}\n")  ### Date created
                    file.write(f"Created by: {page.created_by}\n")  ### Created by
                    file.write(f"Date edited: {page.date_edited}\n")  ### Date edited
                    file.write(f"Edited by: {page.edited_by}\n")  ### Edited by
                    file.write(f"Times viewed: {page.times_viewed}\n")  ### Times viewed
                    file.write("Text:\n")  ### Text
                    file.write(page.text + '\n^\n')  ### Use ^ as the end marker for text
        except Exception as e:
            print(f"Error occurred while saving pages: {e}")  ### Tries to tell us what the exception error is
            
####### This loads all pages from the notepad repository ######
    def load_from_notepad(self, filename):
        try:
            with open(filename, 'r') as file:
                title = None
                keywords = None
                text = []
                date_created = None
                created_by = None
                date_edited = None
                edited_by = None
                times_viewed = 0
                record_valid = True  ### Bool to indicate record validity
                
                for line in file: ### Start of loop to load the data
                    line = line.strip() ### For removing whitespaces
                    if not line: ### continue if line is empty
                        continue
                    if line.startswith("Title:"):
                        title = line.replace("Title:", "").strip()
                    elif line.startswith("Keywords:"):
                        keywords = line.replace("Keywords:", "").strip().split(',')
                    elif line.startswith("Date created:"):
                        date_created = line.replace("Date created:", "").strip()
                    elif line.startswith("Created by:"):
                        created_by = line.replace("Created by:", "").strip()
                    elif line.startswith("Date edited:"):
                        date_edited = line.replace("Date edited:", "").strip()
                    elif line.startswith("Edited by:"):
                        edited_by = line.replace("Edited by:", "").strip()
                    elif line.startswith("Times viewed:"):
                        times_viewed = int(line.replace("Times viewed:", "").strip())
                    elif line.startswith("Text:"):
                        text.append(line.replace("Text:", "").strip())
                    elif line == '^':
                        if not (title and keywords and text):
                            record_valid = False  ### Sets to false if any fields are missing
                        if record_valid:
                            self.add_page(title, keywords, '\n'.join(text), date_created, created_by, date_edited, edited_by, times_viewed)  # Adds the page
                        ### Reset variables and record_valid for the next record
                        title = None
                        keywords = None
                        text = []
                        date_created = None
                        created_by = None
                        date_edited = None
                        edited_by = None
                        times_viewed = 0
                        record_valid = True
                    else:
                        text.append(line)
                ### Check if the last record is val/id after reaching end
                if not (title and keywords and text):
                    record_valid = False
                if not record_valid:
                    print("Failed to load a record.")
        except FileNotFoundError: ### Tells us it cannot find the file
            print("pages.txt not found.")
        except Exception as e:
            print(f"Unable to load pages.txt: {e}") ### Tries to tell us what the exception error is
