from commands.base_command import BaseCommand
import requests
import utils
import settings

class Create(BaseCommand):
    def __init__(self):
        description = "Creates your own Revival Pro account if you have purchased it."
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        with open("users.txt", "r") as f:
            if not(str(message.author.id) in set(f.read().splitlines())):
                def return_user_role(n):
                    return n.id
                user_roles_id = list(map(return_user_role, client.guilds[0].get_member(message.author.id).roles))

                if settings.ROLES["pro"] in user_roles_id:
                    channel = message.channel

                    def check(m):
                        return m.author.id == message.author.id and m.channel == channel
                    
                    msg = "Please make sure to delete this information after creating an account\nPlease enter a username: *(this is going to be used for your Revival Pro account)*\n"
                    await channel.send(msg)
                    log = msg

                    username = await client.wait_for("message", check=check, timeout=600.0)
                    username = username.content
                    log += f"<@!{message.author.id}>: {username}\n"

                    msg = "Please enter a password: *(this is going to be used for your Revival Pro account)*\n"
                    await channel.send(msg)
                    log += msg

                    password = await client.wait_for("message", check=check, timeout=600.0)
                    password = password.content
                    log += f"*you really thought you can see their passwords lol*\n"

                    msg = "Please enter an email address: *(this is going to be used for when reseting your password)*\n"
                    await channel.send(msg)
                    log += msg
                    
                    import re
                
                    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                    
                    def check2(email):
                    
                        # pass the regular expression
                        # and the string in search() method
                        if(re.search(regex, email)):
                            return True
                    
                        else:
                            return False

                    email = await client.wait_for("message", check=check, timeout=600.0)
                    email2 = email.content
                    while not(check2(email2)):
                        msg = "Please enter a valid email address \n"
                        await channel.send(msg)
                        email = await client.wait_for("message", check=check, timeout=600.0)
                        email2 = email.content
                

                    log += f"<@!{message.author.id}>: {email2}\n"

                    data = {
                        "discord": message.author.id,
                        "username": username.lower(),
                        "password": password,
                        "email":    email2,
                    }

                    response = requests.put(f"{settings.DB_URL}/users", data)
                    if response.status_code == 200:
                        msg = f"Thank you for creating a Revival Pro account. Please login by visiting {settings.WEBSITE}/login If you have any questions or messed up any of your login information, please open a support ticket and staff will help you"
                        await message.channel.send(msg)
                        log += msg
                        with open("users.txt", "a") as a:
                            a.write(f"{message.author.id}\n")
                        
                    elif response.status_code == 400:
                        msg = f"Oops it looks like the username you have chosen is already taken. Type {settings.COMMAND_PREFIX}create if you would like to choose a diffrent username"
                        await message.channel.send(msg)
                        log += msg
                    else:
                        msg = "Oops it looks like your account was not created. This is most likely because revival servers are currently down. If you do not think this is the problem and think it might be a diffrent problem please open up a support ticket."
                        await message.channel.send(msg)
                        log += msg

                else:
                    msg = "It looks like you didn't purchase Revival Pro. If you would like to purchase Revival Pro type *donate* in #bot-commands. If you think this is a mistake please make a support ticket and staff will help you."
                    await message.channel.send(msg)
                    await message.channel.send(response.text)
                    log = msg
            else:
                msg = f"It looks like you already have created a Revival Pro account. If you think this is a mistake please make a support ticket and staff will help you. If you would like to change your password visit {settings.WEBSITE}/forgot."
                await message.channel.send(msg)
                log = msg
            print(response.text)
        await utils.log(client, log)

        
