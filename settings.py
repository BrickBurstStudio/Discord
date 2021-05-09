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
    "boost"                     : 709793510181830688,
    "blacklisted"               : 770700918110027776,
    "owner"                     : 709188117181104239,
    "mod"                       : 821781075364675584,
    "premium_plus_and_premium"  : 830658549180923944,
    "premium_plus"              : 821563791627386881,
    "premium"                   : 754874982999261244,
    "standard"                  : 820752869141512192,
    "basic"                     : 754874930667192442,
    "trial"                     : 821563230249025606,
    "pro"                       : 838286161029365792,
}