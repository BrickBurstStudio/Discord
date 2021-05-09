from commands.base_command import BaseCommand
import utils
import requests
from time import sleep
import settings
from bot_token import KEY

class Add(BaseCommand):
    def __init__(self):
        description = ("This will add a script to the script hub on the website")
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):

        channel = message.channel

        def check(m):
            return m.author.id == message.author.id and m.channel == channel

        msg = "Hello, Please enter the name of the script\n"
        await channel.send(msg)
        log = msg

        name = await client.wait_for("message", check=check, timeout=600.0)
        log += f"<@!{message.author.id}>: {name.content}\n"

        msg = "Please enter the code for the script\n" # , If you have to put a roblox username, then put in HazimosKeySomething as the roblox username\n"
        await channel.send(msg)
        log += msg

        code = await client.wait_for("message", check=check, timeout=600.0)
        log += f"<@!{message.author.id}>: {code.content}\n"

        json_code = {
            "name": name.content,
            "value": code.content,
            "key": KEY
        }

        # json_msg = f"<@&821781075364675584>\n<@!{message.author.id}> just submitted a request\nname: {json_code['name']}\ncode: {json_code['value']}\n------------------------------------------------------------------------"
        json_msg = f"<@!{message.author.id}> just submitted a request\nname: {json_code['name']}\ncode: {json_code['value']}\n------------------------------------------------------------------------"

        msg = "Thank you for submiting a script to the script hub. Your submission will be revied. You will receive a notification if you have been accepted or denied"
        await message.channel.send(msg)
        log += msg
        await utils.log(client, log)

        msg = await client.guilds[0].get_channel(823448966275530802).send(json_msg)
        await msg.add_reaction(utils.get_emoji(":white_check_mark:"))
        await msg.add_reaction(utils.get_emoji(":no_entry_sign:"))

        def check(reaction, user):
            return user.bot == False

        reaction = await client.wait_for("reaction_add", check=check)
        if reaction[0].emoji == "✅":
            response = requests.put(f"{settings.DB_URL}/hub", data=json_code)
            
            if response.status_code == 200:
                msg = "Congratulations your script has been accepted to be apart of the script hub. Give up to 24 hours to be update on the website"    
            elif response.status_code == 400:
                msg = f"Looks like your script is already inside the hub. If you would like to sumbit another script type {settings.COMMAND_PREFIX}add"
            else:
                msg = "There has been an internal server error this means that the revival severs are currently not functional"

            await channel.send(msg)

        elif reaction[0].emoji == "🚫":
            await channel.send(
                "I'm sorry to tell you that your script that you submitted has been denied. This is most likely because you didn't give a proper Name, description or code"
            )
        else:
            await channel.send(
                f"The staff thought your submission was so bad they reacted with {reaction[0].emoji}"
            )

