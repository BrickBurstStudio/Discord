from events.base_event import BaseEvent
from utils import get_channel
import requests as req
import discord

# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class CheckVersion(BaseEvent):
    def __init__(self):
        interval_minutes = 10  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        with open("version.txt", "r") as f:
            version = f.read()
            res = req.get("https://clientsettings.roblox.com/v1/client-version/WindowsPlayer")
            latest_version = res.json()["clientVersionUpload"]
            if version == latest_version:
                pass
            else:
                channel = get_channel(client, "〖📌〗announcement")
                msg = client.guilds[0].default_role
                await channel.send(msg)
                embedVar = discord.Embed(title="**New Roblox Version Detected**", color=0x10b1fe, description="This means that revival and all other exploits will be temporally patched as we need to update our custom api. This shouldn't take long to update")
                embedVar.add_field(name="Old Version", value=f"`{version}`", inline=True)
                embedVar.add_field(name="New Version", value=f"`{latest_version}`", inline=True)
                await channel.send(embed=embedVar)
                with open("version.txt", "w") as j:
                    j.write(latest_version)

                print(version)
                print(latest_version)


