import sys

import settings
import discord
import message_handler
import settings
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from events.base_event import BaseEvent
from events import *
from multiprocessing import Process

import requests

# Set to remember if the bot is already running, since on_ready may be called
# more than once on reconnects
this = sys.modules[__name__]
this.running = False

# Scheduler that will be used to manage events
sched = AsyncIOScheduler()

###############################################################################

def main():
    # Initialize the client
    print("Starting up...")
    intents = discord.Intents.default()
    intents.members = True
    client = discord.Client(intents=intents)

    # Define event handlers for the client
    # on_ready may be called multiple times in the event of a reconnect,
    # hence the running flag
    @client.event
    async def on_ready():
        if this.running:
            return

        this.running = True

        # Set the playing status
        if settings.NOW_PLAYING:
            print("Setting NP game", flush=True)
            await client.change_presence(
                activity=discord.Game(name=settings.NOW_PLAYING)
            )
        print("Logged in!", flush=True)

        # Load all events
        print("Loading events...", flush=True)
        n_ev = 0
        for ev in BaseEvent.__subclasses__():
            event = ev()
            sched.add_job(
                event.run, "interval", (client,), minutes=event.interval_minutes
            )
            n_ev += 1
        sched.start()
        print(f"{n_ev} events loaded", flush=True)


    # The message handler for both new message and edits
    async def common_handle_message(message):
        if message.author.bot == True:
            return
            
        text = message.content

        if text.startswith(settings.COMMAND_PREFIX) and text != settings.COMMAND_PREFIX:
            if text.startswith(settings.COMMAND_PREFIX) == False:
                await message.channel.send(
                    "If you need help with any of my commands type r!help"
                )
                return
            if str(message.channel.type) != "private":
                await message.channel.send("Please use my commands privately in my dms. This is required for security")
                return

            cmd_split = text[len(settings.COMMAND_PREFIX) :].split()
            try:
                await message_handler.handle_command(
                    cmd_split[0].lower(), cmd_split[1:], message, client
                )
            except:
                print("Error while handling message", flush=True)
                raise

    async def file_upload(message):
        text = message.content
        print(text)

    @client.event
    async def on_message(message):
        await common_handle_message(message)
        await file_upload(message)


    @client.event
    async def on_message_edit(before, after):
        await common_handle_message(after)

    @client.event
    async def on_member_update(before, after):
            def return_user_role(n):
                return n.id

            user_roles_id_before = list(map(return_user_role, before.roles))
            user_roles_id_after = list(map(return_user_role, after.roles))
            
            if not(settings.ROLES["pro"] in user_roles_id_before) and (settings.ROLES["pro"] in user_roles_id_after):
                await after.send(f"Thank you for purchasing Revival Pro. The next step to setting up your account is by creating your account by typing `{settings.COMMAND_PREFIX}create`. If you have any questions please open up a support ticket and staff will be happy to help you.")

    # Finally, set the bot running
    client.run(settings.BOT_TOKEN)


###############################################################################

if __name__ == "__main__":
    main()