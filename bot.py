import discord
from discord.ext import commands

# ------------------ إعداد البوت ------------------
intents = discord.Intents.default()  # التحكم بما يستطيع البوت رؤيته
intents.message_content = True       # ضروري لقراءة الرسائل
bot = commands.Bot(command_prefix="!", intents=intents)

# ------------------ حدث جاهزية البوت ------------------
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

# -----------------رد البوت-------------------------
@bot.event
async def on_message(message):
    if message.author ==bot.user:
        return
    
    if message.content == "سلام":
        await message.channel.send("وعليكم السلام")

#----------------كوماندز---------------------------
bot.command()
async def ping(ctx):
    await ctx.send("Pong!")



# ------------------ تشغيل البوت ------------------
bot.run("MTQ1MjY4MDQxNzk4Njc0NDM2Mg.GxQzdw.VtT5M0iNk-vQVRpvKBoKde64333T0aOMpjzKys")
