import discord
import responses


async def save_message(message, user_message, is_private):
    try:
        response = responses.get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

## TODO actually make message be stored within sql database
##async def store_message(user, message):


def run_discord_bot():
    TOKEN = 'MTA1MDQ1MzMwOTU5MDM0MzcwMQ.G6uZ8F.g5VkgToCCJ9xWA3KNgAx0iIIVFG0XSRTMCmA_g'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await save_message(message, user_message, is_private=True)
        else:
            await save_message(message, user_message, is_private=False)

    client.run(TOKEN)
