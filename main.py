import chatgptdisc_bot
import store_responses

if __name__ == '__main__':
    db = store_responses.MessageDataBase()
    chatgptdisc_bot.run_discord_bot()
