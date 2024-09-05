import discord
from discord.ext import commands
import aa

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f"Selam {ctx.author}. Ben {bot.user}")

@bot.command()
async def image(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"resimlerali/{dosya.filename}")
            await ctx.send ("işte resmin geldi:")
            sınıf,score = aa.kerasmodel(f"resimlerali/{dosya.filename}")
            if sınıf == "1980\n":
                await ctx.send("ilkel bilgisayar dönemi")
            elif sınıf == "1990\n":
                await ctx.send("internet,web ve windows 95 dönemi")
            elif sınıf == "2000\n":
                await ctx.send("sosyal medya dönemi")
            else:
                await ctx.send("HATA! error code: 954")           
    else:
        await ctx.send ("resmin gelmedi")


bot.run("")