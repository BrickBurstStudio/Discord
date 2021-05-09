from commands.base_command import BaseCommand
import utils
import settings
import requests
from bot_token import KEY


class Delete(BaseCommand):
    def __init__(self):
        description = "**MODS ONLY** Deletes the script on the hub by name"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        def return_user_role(n):
            return n.id
        user_roles_id = list(map(return_user_role, client.guilds[0].get_member(message.author.id).roles))

        if settings.ROLES["mod"] in user_roles_id:
            channel = message.channel

            def check(m):
                return m.author.id == message.author.id and m.channel == channel

            msg = "Hello, Please enter the name of the script you want to delete\n"
            await message.channel.send(msg)
            log = msg

            name = await client.wait_for("message", check=check, timeout=600.0)
            log += f"<@!{message.author.id}>: {name.content}\n"
            name = name.content

            req = {
                "key": KEY,
                "name": name, 
            }

            response = requests.delete(f"{settings.DB_URL}/hub", data=req)
            print (response.text)
            if response.status_code == 200:
                msg = f"**{name}** has been successfully deleted"
            elif response.text == "Key not Found":
                msg =f"**{name}** does not seem to exist"
            else:
                msg = "There has been an internal server error this means that the revival severs are currently not functional"
        else:
            msg = "This command is only allowed to be used by moderators and staff members. If you are a staff member and think this is a mistake message one of the admins."

        await message.channel.send(msg)
        await utils.log(client, msg)
