import discord
import asyncio

intents = discord.Intents.default()
intents.reactions = True

client = discord.Client(intents=intents)
reacted_users = set()

@client.event
async def on_ready():
    guild_id = replacewithserverid
    channel_id = replacewithchannelid
    message_id = replacewiththemessagethathasthereactions

    guild = client.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    if channel:
        try:
            message = await channel.fetch_message(message_id)
            for reaction in message.reactions:
                async for user in reaction.users():
                    if user not in reacted_users:
                        reacted_users.add(user)
                        try:
                            await user.send(f"message1 {user.mention}, message2")
                        except discord.Forbidden:
                            print(f"Cannot send a message to user {user.name}#{user.discriminator}")
                            continue
        except discord.NotFound:
            print("Message not found. Please check the message ID.")
    else:
        print("Channel not found. Please check the channel ID.")

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == replacewithmessageid    :
        user = await client.fetch_user(payload.user_id)
        if user not in reacted_users:
            reacted_users.add(user)
            try:
                await user.send(f"this too {user.mention}, ignore this")
            except discord.Forbidden:
                print(f"Cannot send a message to user {user.name}#{user.discriminator}")

client.run('replacewithbottoken')
