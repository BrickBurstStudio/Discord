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

DB_URL = "https://92eb51de178a.ngrok.io"
WEBSITE = "https://revivalexploit.com"

ROLES = {
    "boost"                     : 842627158031859714,
    "blacklisted"               : 842482029618397297,
    "pro"                       : 842480457526280213,
    "owner"                     : 842480279842586684,
    "mod"                       : 842480476118581260,
    # "premium_plus_and_premium"  : 830658549180923944,
    # "premium_plus"              : 821563791627386881,
    # "premium"                   : 754874982999261244,
    # "standard"                  : 820752869141512192,
    # "basic"                     : 754874930667192442,
    # "trial"                     : 821563230249025606,
}

LOGS = 842491915521490986