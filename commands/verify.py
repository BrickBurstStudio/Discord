from commands.base_command import BaseCommand
import utils
import roblopy
import settings
import requests

class Verify(BaseCommand):
    def __init__(self):
        description = "Checks if *<roblox_username>* have bought any of the revival roblox t-shirts and will give you the role accordingly"
        params = ["roblox_username"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        print("Hello, World!")
        # username = params[0]
        # user_id = message.author.id

        # req = {
        #     "userId": user_id,
        #     "password": settings.KEY,
        # }
        # response = requests.post(f"{settings.DB_URL}/search/roblox", data=req)

        # if str(response) == "<Response [200]>":
        #     try:
        #         roblox_username = response.json()['robloxUsername']
        #     except:
        #         pass

        # req = {
        #     "username": username,
        #     "password": settings.KEY,
        # }


        # response = requests.post(f"{settings.DB_URL}/search/discord", data=req)
        
        
        # if str(response) == "<Response [200]>":
        #     if len(response.json()["discordUsernames"]) > 0 and (roblox_username != username):
        #         msg = f"{params[0]} has already been used to verify. If you think this is a mistake please contact one of the admins."
        #     else:
        #         try:
        #             response = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
        #             print(response.text)
        #             user_idr = response.json()["Id"]
        #             print(user_id)
                    
        #             if response.status_code == 200:
        #                 if roblopy.Assets.user_has_asset(user_idr, 6536081029):
        #                     msg = "You have now been given revival pro role please check your roles in the server. If you have not received your roles please create a support ticket."
        #                     await client.guilds[0].get_member(user_id).add_roles(
        #                         client.guilds[0].get_role(settings.ROLES["pro"])
        #                     )
        #             else:
        #                 msg = "There has been an internal server error with roblox please wait until roblox is back up and functional then try again. To check the status of roblox please visit https://downdetector.com/status/roblox/"
        #         except:
        #             msg = "The username you are currently trying to verify does not exist. Please make sure captilaztion and spelling is correct. It is case sensitive"
        # else:
        #     msg = "Oops it looks like your account was not unable to be verified. This is most likely because revival servers are currently down. If you do not think this is the problem and think it might be a diffrent problem please open up a support ticket."

        # await message.channel.send(msg)
        # await utils.log(client, msg)