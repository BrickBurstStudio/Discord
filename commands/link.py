from commands.base_command import BaseCommand
import utils
import settings
import requests as req

class Link(BaseCommand):
    def __init__(self):
        description = "Links your discord account to your revival pro account"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        channel = message.channel

        def check(m):
            return m.author.id == message.author.id and m.channel == channel
        
        msg = "Please make sure to delete this information after linking your account\nPlease enter your username:\n"
        await channel.send(msg)
        log = msg

        username = await client.wait_for("message", check=check, timeout=600.0)
        username = username.content
        log += f"<@!{message.author.id}>: {username}\n"

        msg = "Please enter your password:\n"
        await channel.send(msg)
        log += msg

        password = await client.wait_for("message", check=check, timeout=600.0)
        password = password.content
        log += f"*you really thought you can see their passwords lol*\n"
        

        data = {
            "username": username.lower(),
            "password": password,
        }

        response = req.post(f"{settings.DB_URL}/users/login", data)
        if response.status_code != 200:
            msg = f"Oops it looks like the password for **{username}** is incorrect. If you are the owner of this account and forgot your password visit {settings.WEBSITE}/forgot"
            await message.channel.send(msg)
            log += msg
            
        elif response.status_code != 400:
            data = {
                "sessionID": response.json()["sessionID"],
                "newDiscord": message.author.id
            }
            res = req.patch("https://099e06aa8985.ngrok.io/users/link", data=data)
            if res.status_code == 200:
                msg = f"You have successfully linked your discord account to **{username}**. If you have any questions are concerns, please open a support ticket"
                await message.channel.send(msg)
                log += msg
            elif res.status_code == 500:
                msg = "Oops it looks like your account was not linked. This is most likely because revival servers are currently down. If you do not think this is the problem and think it might be a diffrent problem please open up a support ticket."
                await message.channel.send(msg)
                log += msg
        else:
            msg = "Oops it looks like your account was not linked. This is most likely because revival servers are currently down. If you do not think this is the problem and think it might be a diffrent problem please open up a support ticket."
            await message.channel.send(msg)
            log += msg
            
        await utils.log(client, log)
        

