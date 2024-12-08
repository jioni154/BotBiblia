import discord
import leerLaBiblia
import config

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    async def on_message(self, message):
        if message.author == client.user:
            return
        elif message.content.startswith('+amen'):
            message.content = message.content.replace('+amen','')
            message.content = message.content.strip()
            existe, cantidad = leerLaBiblia.existePalabraEnCapitulos(message.content)
            if existe:
                await message.reply(f"La expresion \"{message.content}\" se encuentra {cantidad} de veces en la biblia")
            else:
                await message.reply(f'La expresion \"{message.content}\" no se encuentra en la biblia')
            
        
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('token')



