import discord
import leerLaBiblia
import config
from discord.ext import commands
import PaginatorExpress


bot= commands.Bot(command_prefix='+',intents=discord.Intents.all()) 
    
@bot.event    
async def on_ready():
    print(f'Logged on as me!')
 
@bot.command()
async def ayuda(ctx):
    embedDeAyuda=discord.Embed(title='Lista de comandos:')
    embedDeAyuda.set_author(name='+ayuda')
    embedDeAyuda.set_footer(text='Palabra de dios')
    embedDeAyuda.add_field(name="+amen expresion", value="Busca la expresion en la biblia, te dice si existe, cantidad de veces que se repite y en que libros.",inline=False)
    embedDeAyuda.add_field(name="+superAmen", value='Busca la expresion en la biblia, te dice si existe, la cantidad de veces que se repite y te devuelve cada versiculo con el formato "Libro capitulo:versiculo" en el que aparece la palabra',inline=False)
    await ctx.reply(embed=embedDeAyuda)
     
 
@bot.command()
async def amen(ctx,*args):
    message = ' '.join(args)
    existe, cantidad, librosDonde = leerLaBiblia.existePalabraEnCapitulos(message)
    if existe:
        nombreDeLibros = leerLaBiblia.conseguirNombreDeLibros(librosDonde)
        await ctx.message.reply(f"La expresion \"{message}\" se encuentra {cantidad} de veces en la biblia.\nAparece en los libros {nombreDeLibros}")
    else:
        await ctx.message.reply(f'La expresion \"{message}\" no se encuentra en la biblia')
        
        
@bot.command()
async def moriteBotDeMierda(ctx):
    if ctx.author.name == 'juanmateo':
        await ctx.message.reply('Bueno 😔😔😔😔 adios....')
        await bot.close()   
    else:
        await ctx.message.reply('No me decis que hacer JUICIO FINAL')
 
@bot.command()
async def superAmen(ctx,*args):
    message = ' '.join(args)
    existe, cantidad, versiculosDonde = leerLaBiblia.existePalabraEnCapitulosAvanzado(message)
    if existe:
        embeds=[]
        contadorEmbed=0
        maxContadorEmbed=20
        versiculosAcumulados=''

        for versiculo in versiculosDonde:
            if contadorEmbed==maxContadorEmbed:
                contadorEmbed=0
                embedCreado=discord.Embed(title=message,description=versiculosAcumulados)
                embedCreado.set_author(name=f'La expresion \"{message}\" se encuentra {cantidad} de veces en la biblia.')
                embedCreado.set_footer(text=f'Pedido por {ctx.author.nick}')
                embeds.append(embedCreado)
                versiculosAcumulados=''
            versiculosAcumulados= versiculosAcumulados+versiculo+f'\n'
            contadorEmbed+=1
        if contadorEmbed!=0:
            embedCreado=discord.Embed(title=message,description=versiculosAcumulados)
            embedCreado.set_author(name=f'La expresion \"{message}\" se encuentra {cantidad} de veces en la biblia.')
            embedCreado.set_footer(text=f'Pedido por {ctx.author.nick}')
            embeds.append(embedCreado)
        await PaginatorExpress.Simple().start(ctx, pages= embeds)
    else:
        await message.reply(f'La expresion \"{message}\" no se encuentra en la biblia')
 
 
 
 
    
bot.run(config.token)

