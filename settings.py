import os
import bot_token

# The prefix that will be used to parse commands.
COMMAND_PREFIX = "!"

# The bot token. Keep this secret!
BOT_TOKEN = bot_token.BOT_TOKEN

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = f"DM me {COMMAND_PREFIX}help"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DB_URL = "https://92eb51de178a.ngrok.io"
# DB_URL = "http://localhost:6969"
WEBSITE = "https://revivalexploit.com"

ROLES = {
    "boost"                     : 842627158031859714,
    "blacklisted"               : 842482029618397297,
    "pro"                       : 842480457526280213,
    "owner"                     : 842480279842586684,
    "mod"                       : 842480476118581260,
}

LOGS = 842491915521490986