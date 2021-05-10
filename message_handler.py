from commands.base_command import BaseCommand

from commands import *
import utils

import settings

# Register all available commands
COMMAND_HANDLERS = {c.__name__.lower(): c() for c in BaseCommand.__subclasses__()}

###############################################################################


async def handle_command(command, args, message, bot_client):
    if command not in COMMAND_HANDLERS:
        return

    print(f"{message.author}: {settings.COMMAND_PREFIX}{command} " + " ".join(args))
    msg = f"<@!{message.author.id}>: {settings.COMMAND_PREFIX}{command} " + " ".join(
        args
    )

    revival = bot_client.guilds[0]
    await revival.get_channel(822568003056828437).send(msg)

    def return_user_role(n):
        return n.id
    user_roles_id = list(map(return_user_role, revival.get_member(message.author.id).roles))
    cmd_obj = COMMAND_HANDLERS[command]

    if cmd_obj.params and len(args) < len(cmd_obj.params):
        msg = message.author.mention + " Insufficient parameters!"
        await message.channel.send(msg)
        # await utils.log(bot_client, msg)
    else:
        await cmd_obj.handle(args, message, bot_client)