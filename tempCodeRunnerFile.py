from app.discord_bot.discord_api import client, discord_token
from keep_alive import keep_alive

if __name__ == '__main__':
    keep_alive()
    client.run(discord_token)