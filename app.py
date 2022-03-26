from github import Github 
import os

# Store your github token in this variable
token = os.environ.get("GITTOKEN")



class GithuAutomationApp():

    def __init__(self, token):
        self.user = Github(token)
        
        
    def list_repos(self):
        for repo in self.user.get_user().get_repos():
            print("Repo name:" + " " + str(repo.name))
            print("Repo language: " + " " + str(repo.language))
            print("Last modified: " + " " + str(repo.last_modified) + "\n")

    
    # This function will add the repository in github and clone that empty repository.
    def add_repo(self):
        repo_name = str(input("Repo name to create: ")).lower()
        
        self.user.get_user().create_repo(name=repo_name, private=False)
        
        print("Repo added.")
        print("Cloning...")
        
        try:
            os.system(f"bash .clone.sh {repo_name}") 
            print("Cloned repo into 'PyProject' folder.")

            repository = self.user.get_user().get_repo(repo_name)
            working_repository = repository
            print(working_repository.name)
            


        except:
            print("Repo not found to clone.")




    # This will remove the repository from github
    def remove_repo(self):

        for repo in self.user.get_user().get_repos():
            print(repo.name)
        
        try:
            
            repo = str(input("Repo name to remove: ")).lower()
            confirm = str(input("Are you confirm you want to remove the repo [y/n]: "))

            if confirm == "y":
                self.user.get_user().get_repo(repo).delete()
                print("Repo has deleted.")
                os.system(f"sudo rm -r ../{repo}")
            else:
                print("Repo not found.")
            
            if confirm == "n":
                print("Process abord.")

        
        except:
        
            print("Sorry, repo not found.")




command = ''

# This function will run the commmand that you enter.
def main():

    running = True
    
    print("Type help for display the help menu.")
    
    while running:
        command = str(input("command: ")).lower()
    
        if command == "list repos":
            app = GithuAutomationApp(token)
            app.list_repos()
    
        
        if command == "create repo":
            app = GithuAutomationApp(token)
            app.add_repo()
    
        
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
                        
                        create repo - This will create a repo at github and clone into your folder.
    
                        remove repo - This will remove the repo from github.
    
                        list repos - This will list all repository from your github.
    
    
    
                    """)

if __name__ == "__main__":
    main() # Initiate the programe



