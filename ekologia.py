import discord
from datetime import date, datetime
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

events = {
    "Dzień bez opakowań foliowych": date(2025, 1, 23),
    "Światowy Dzień Recyklingu": date(2026, 3, 18),
    "Światowy Dzień Ziemi": date(2026, 4, 22),
    "Dzień Bez Śmiecenia": date(2025, 5, 11),
    "Światowy Dzień Ochrony Środowiska": date(2025, 6, 5),
    "Międzynarodowy Dzień Czystego Powietrza": date(2025, 8, 7)
}

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def your_date(ctx,):
    await ctx.send(f"Twoja aktualna data: {date.today().ctime()}")

@bot.command()
async def event(ctx):
    today = date.today()
    response = "Nadchodzące wydarzenia:\n"

    for nazwa, data_wydarzenia in events.items():
        dni_do = (data_wydarzenia - today).days  

        if dni_do > 0:
            response += f"- {nazwa}: za {dni_do} dni ({data_wydarzenia.strftime('%d.%m.%Y')})\n"
        elif dni_do == 0:
            response += f"- {nazwa}: to dzisiaj! ({data_wydarzenia.strftime('%d.%m.%Y')})\n"
        else:
            response += f"- {nazwa}: to już było ({data_wydarzenia.strftime('%d.%m.%Y')})\n"

    await ctx.send(response)
    
bot.run("MTM1NzM5MDg2MTEyMTYxNzk1MA.GqSMdM.-E9iXQg93WgGtg_ibGNSdIkqbTE-jkgLnMd9_Y")

