import sys
import os
from github import Github

path = "YOUR PATH"
username = "YOUR GITHUB USERNAME"
password = "YOUR GITHUB PASSWORD"

def create():
    proj_name = str(sys.argv[1])
    os.makedirs(path + "/" + proj_name)
    print("-----Folder Created-----")
    print("----Initializing Github Login-----")
    user = Github(username, password).get_user()
    print("------Creating Repo-----")
    repo = user.create_repo(proj_name)
    print("Succesfully created repository {}".format(proj_name))
    

if __name__ == "__main__":
    create()