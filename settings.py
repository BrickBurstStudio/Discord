import os
import bot_token

# The prefix that will be used to parse commands.
COMMAND_PREFIX = "e!"

# The bot token. Keep this secret!
BOT_TOKEN = bot_token.BOT_TOKEN

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = f"DM me {COMMAND_PREFIX}help"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DB_URL = "https://099e06aa8985.ngrok.io"
WEBSITE = "https://revivalexploit.com"

ROLES = {
    "pro":838286161029365792,
}