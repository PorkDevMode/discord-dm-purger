import discord
import asyncio  # Use asyncio.sleep instead of time.sleep

TOKEN = input('Enter your discord token: ')  
RECIPIENT_USER_ID = input('Enter the user ID: ') 

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        user = await self.fetch_user(RECIPIENT_USER_ID)
        if user:
            dm_channel = await user.create_dm()
            async for message in dm_channel.history(limit=100000):
                if message.author == self.user and message.type == discord.MessageType.default:
                    try:
                        await message.delete()
                        print(f'Deleted message: {message.content}')
                        await asyncio.sleep(0.2)
                    except discord.Forbidden:
                        print("Lacked permissions to delete a message.")
                    except discord.HTTPException as e:
                        print(f"Failed to delete message: {e}")
            print("Completed deleting messages.")
        else:
            print("User not found.")

        await self.close()

client = MyClient()
client.run(TOKEN)