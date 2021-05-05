from commands.base_command import BaseCommand
import utils
import settings

class Site(BaseCommand):
    def __init__(self):
        description = "Displays our website"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):

        msg = settings.WEBSITE

        await message.channel.send(msg)
        await utils.log(client, msg)
        
