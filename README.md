# ChatGptGivesYouAPsychEval
# How it works
The bot uses 3 apis, discord.py/mysqlconnector/openai, which it uses all all of these to give you a psych eval from a user. There is a database on AWS that has a format of  
| UserID | oldest | msg1 | msg2 | msg3 | msg4 | msg5 |  
Messages are only updated left to right starting from msg1. Each message can be a length of 400 characters(an essay). The bot will keep get all messages send in the server and add messages to the database if they are relatively long. Specifically if they are longer than 16 characters, this can be changed if you want shorter messages or longer. If the 'gpt peval' command is used then the bot will get all the messages of the calling user from the database and then call all the openai for a response using their chat completion feature.

# Local Installation
## Python
If you do not have python installed then you can download it off their website.  
https://www.python.org/downloads/
## Git Clone
Once you have forked the repo then you can clone it through various methods.
### HTTPS
I would recommend VSCode which is fairly simple or you can use your own IDE. If not the git command is...
```
git clone url
```
### SSH
If you have ssh keys set up then this will work as well
```
git clone git@github.com:user/forkrepo.git
```
## Install PIP
Praise all mighty pip and making everything easy to install. PIP installation changes from system to system(mainly OS) so figure it out.

## Discord API
```
pip install discord.py
```

## Openai API
```
pip install openai
```

## dotenv
```
pip install python-dotenv
```

## mysql connector
```
pip install mysql-connector-python
```
## API Keys
At this point you will need to make a .env within the parent directory. The format for this .env file is...
```
OPENAI = "openai-key"
DISCORDPSYCHEVAL = "discord-bot-key"
DBHOST = "database-host"
DBNAME = "database-name"
DBUSER = "database-username"
DBPASS = "database-password-for-user"
```
**DO NOT** make this .env file part of your repository. Make a .gitignore file and include this file in there.

## GitIgnore
If you do not know how to make a .gitignore file just make a file named **.gitignore** in the parent directory. 
Then in that file just add whatever files you do not want to be pushed to your respository. For example...
```
.env
secretfile.txt
othersecret.py
```
Will make it so *.env*, *secretfile.txt*, and *othersecret.py* will be ignored by your version control sys.

## Running program
If you are in an IDE then this will be easy and just run the main file.
### Running on a LINUX system
There are 2 bash scripts to just run main.py. **run.sh** and **back_run.sh**.  
You first will need to give these files permissions. In your terminal within the parent directory run these cmds...
```
chmod +x main.py
chmod +x run.sh
chmod +x back_run.sh
```
The differences between run.sh and back_run.sh is that back_run.sh will continue to run after closing the window in the background. It does this with the screen 
command and to close it you can look on this site for instructions. https://dev.to/akhileshthite/how-to-keep-ec2-instance-running-after-ssh-is-terminated-45k8

# Installation on an AWS EC2 Server using Amzon LINUX