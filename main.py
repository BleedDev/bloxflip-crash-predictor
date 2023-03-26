import discord
from discord.ext import commands
import numpy as np
import statistics
import cloudscraper

bot = commands.Bot(command_prefix="?", intents=discord.Intents.default())

s = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

def crashPoint(num):
    info = s.get('https://rest-bf.blox.land/games/crash').json()['history'][num]['crashPoint']
    return info

@bot.tree.command(name='crash', description='Predict The Crash Gamemode On Bloxflip Accurate')
async def crash(interaction):
    one = crashPoint(0)
    two = crashPoint(1)
    three = crashPoint(2)
    four = crashPoint(3)
    five = crashPoint(4)
    #six = crashPoint(5)
    #seven = crashPoint(6)
    #eight = crashPoint(7)
    #nine = crashPoint(8)
    #ten = crashPoint(9)
    if "{:.2f}".format(one + two + three) < "3.50":
        risk = "(Unstable Prediction)"
    else:
        risk = ""
    pst10 = [one, two, three, four, five]
    average = sum(pst10) / len(pst10)
    std_dev = statistics.stdev(pst10)
    average_c = np.mean(average)
    std_dev_c = np.std(std_dev)
    prediction = (2 / (average_c - std_dev_c) / 2)
    prediction = prediction + 1
    risky = (1 / (average_c - std_dev_c) / 4)
    risky = risky + prediction
    prediction = "{:.2f}".format(prediction)
    risky = "{:.2f}".format(risky)
    em = discord.Embed(color=15844367)
    em.add_field(name="` ⭐ ` Prediction", value=f"> {prediction}x {risk}", inline=False)
    em.add_field(name="` ⭐ ` Last Games", value=f"> {one}x, {two}x, {three}x", inline=False)
    em.add_field(name="` ⭐ ` Risky Bet", value=f"> {risky}x", inline=False)
    em.add_field(name="` ⭐ ` Credits", value="bleed#5555", inline=False)
    await interaction.response.send_message(embed=em)

bot.run("yourtoken")
