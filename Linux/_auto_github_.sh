#!/bin/bash


python3 auto_github.py $1
cd <YOUR_PATH>/$1
git init
echo "---> Remoting your repo"
git remote add origin https://github.com/<USERNAME HERE(REMOVE QUOTES ALSO)>/$1.git
touch README.md
git add .
echo "---> Commiting"
git commit -m "Initial Commit"
git push -u origin master
code .
