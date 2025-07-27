import discord
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
token = os.getenv("BOT_TOKEN")
client = discord.Client(intents=intents)
welcome_channel = 1398247329861074975
@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hello"):
        await message.channel.send("hi how are you")
    elif message.content.startswith("!ping"):
        await message.channel.send(f"pong! { round(client.latency * 1000)} ms")
    elif message.content.startswith("!help?"):
        help_embed = discord.Embed(
            title = "bot help", description = "Here are all the commands you can use!",
        color = 0xbf5708
        )
        #-------------------------------USER INFO---------------------------
    if message.content.startswith("!userinfo"):
        user_info = message.author
        user_embed = discord.Embed(
            title = f"user info for {user_info.name}{user_info.id}",
            description = f"here is the info for {user_info.mention}",
            color = 0xbf5708
            
        )
        user_embed.add_field(name = "name", value = user_info.name, inline = True)
        user_embed.add_field(name = "id", value = user_info.id, inline = True)
        user_embed.add_field(name = "created at", value = user_info.created_at, inline = True)
        user_embed.add_field(name = "joined at", value = user_info.joined_at, inline = True)
        user_embed.set_thumbnail(url = user_info.display_avatar.url)
        user_embed.set_footer(text = f"requested  by {message.author.name}")
        await message.channel.send(embed = user_embed)
#----------------------------------

@client.event
async def on_member_join(member,message):
    w_channel = client.get_channel(welcome_channel)
    if w_channel is not None:
        await w_channel.send(f"welcome {member.mention} to the server")
    w_user_embed = discord.embed(
        title = f"welcome {member.mention} joined the server",
        description = f"we are happy to have you here {member.mention}",
        color = 0xbf507
        )
    w_user_embed.set_thumbnail(url = member.display_avatar.url)
    await message.channel.send(embed = w_user_embed)

client.run(token)
