from github import Github 
import os


token = os.environ.get("GITTOKEN")



class GithuAutomationApp():

    def __init__(self, token):
        self.user = Github(token)
        
        
    def list_repos(self):
        for repo in self.user.get_user().get_repos():
            print("Repo name:" + " " + str(repo.name))
            print("Repo language: " + " " + str(repo.language))
            print("Last modified: " + " " + str(repo.last_modified) + "\n")


    def add_repo(self):
        repo_name = str(input("Repo name to create: ")).lower()
        
        self.user.get_user().create_repo(name=repo_name, private=False)
        print("Repo added.")


    
    def remove_repo(self):

        for repo in self.user.get_user().get_repos():
            print(repo.name)
        
        try:
            
            repo = str(input("Repo name to remove: ")).lower()
            confirm = str(input("Are you confirm you want to remove the repo [y/n]: "))

            if confirm == "y":
                self.user.get_user().get_repo(repo).delete()
                print("Repo has deleted.")
            
            if confirm == "n":
                print("Process abord.")

        
        except:
        
            print("Sorry, repo not found.")



running = True

command = ''

def main():

    print("Type help for display the help menu.")
    
    while running:
        command = str(input("command: ")).lower()
    
        if command == "list repos":
            app = GithuAutomationApp(token)
            app.list_repos()
    
        
        if command == "create repo":
            app = GithuAutomationApp(token)
            app.add_repo()
            app.list_repos()
    
        
        if command == "remove repo":
            app = GithuAutomationApp(token)
            app.remove_repo()
    
    
        if command == "exit":
            running = False
    
        
        if command == "clear":
            os.system("clear")
    
        if command == "help":
            print("""
                    HELP MENU:
                        
                        create repo - This will create a repo at github.
    
                        remove repo - This will remove the repo from github.
    
                        list repos - This will list all repository from your github.
    
    
    
                    """)

if __name__ == "__main__":
    main()



