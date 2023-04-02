## Jonathan Vazquez
## chatgptdisc_bot.py
##
## Desc: main code to set up bot


import discord
import responses

import api_control

import re

import os
from dotenv import load_dotenv



async def work_on_message(message, user_message, username, userid, ctrl, is_private):
    try:
        response = responses.parse(userid, user_message, ctrl)

        ## Bot was called for so respond appropriately
        if ( response != None):
            await message.author.send(response) if is_private else await message.channel.send(response)
            print('Gave user: '+username+' their pscyh eval')
        ## Bot was not called so just go save message
        ## Only save relatively long messages because most of the time its either @'s or 2 word messages
        elif( len(user_message) > 16):
            ctrl.db.add_message(userid, str(convertMentionIDs(message)))

    except Exception as e:
        print(e)

## Desc: Use to get rid of disord's formatting for mentions i.e. <@1234567890>
## convertMentionIDS(message, client)
## message: The message to go through and replace all the id mentions with the actual username
## return:  The message with the id's replaced with the names of the users
def convertMentionIDs(message):
    mentions = message.mentions

    new_msg = str(message.content)

    for mention in mentions:
        regex = "<@!?"+str(mention.id)+">"
        id = re.search( regex, new_msg )

        new_msg = new_msg.replace(id.group(), mention.name)

    return new_msg


def run_discord_bot():
    load_dotenv()
    TOKEN = str(os.getenv('DISCORDPSYCHEVAL'))

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    my_ctrl = api_control.API_Control()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        ## Do not have bot work on it's own messages or other bots in server
        if message.author == client.user or message.author.bot:
            return

        try:
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            userid = str(message.author.id)
        except Exception as e:
            print("Something went wrong, probably wasn't a message but a picture. Error: " + str(e))
            return

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await work_on_message(message, user_message, username, userid, my_ctrl, is_private=True)
        else:
            await work_on_message(message, user_message, username, userid, my_ctrl, is_private=False)

    client.run(TOKEN)
