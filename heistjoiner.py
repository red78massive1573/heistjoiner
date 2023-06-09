from discord.ext import commands
import time


class HeistJoiner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild and self.bot.state:
            for embed in message.embeds:
                embed = embed.to_dict()
                try:
                    if (
                        "is starting a bank robbery" in embed["title"]
                        and self.bot.config_dict["heistjoiner"]["state"]
                    ):
                        await self.bot.click(message, 0, 0)
                        time.sleep(90) # I use blocking method to pause all process on other cogs and main file
                except KeyError:
                    pass

async def setup(bot):
    await bot.add_cog(HeistJoiner(bot))
