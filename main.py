import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_guild_join(guild):
    await guild.leave()

client.run("TokenHere")