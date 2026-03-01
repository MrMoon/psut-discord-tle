import random
from discord.ext import commands

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # The command name is "where"
    @commands.command(name='where')
    async def where_command(self, ctx, *args):
        # Join the extra words together and make them lowercase to avoid case-sensitivity issues
        phrase = " ".join(args).lower()
        
        # Check if they typed exactly "is the prizes" after ";where"
        if phrase == "is the prizes":
            # Generate a random number between 50 and 70
            random_years = random.randint(50, 70)
            
            # Send the response back to the channel
            await ctx.send(f"You will get your prize in {random_years} years")

# Standard function to load the cog into the bot
def setup(bot):
    bot.add_cog(CustomCommands(bot))
