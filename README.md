# ChatGptGivesYouAPsychEval

# Local Installation
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
OPENAI="openai-key"
DISCORDPSYCHEVAL="discord-bot-key"
DBHOST = "database-host"
DBNAME = "database-name"
DBUSER = "database-username"
DBPASS = "database-password-for-user"
```