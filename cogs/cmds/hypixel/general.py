import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.cache = self.bot.get_cog("Cache")

    @commands.command(name="watchdog", aliases=["watchdogstats", "bans"])
    async def watchdog(self, ctx):
        wd40 = await self.cache.get_watchdog_stats()

        embed = discord.Embed(color=self.bot.cc)

        auto = f"Total Bans: `{wd40.get('watchdog_total')}`\n" \
               f"Today: `{wd40.get('watchdog_rollingDaily')}`\n" \
               f"Last Minute: `{wd40.get('watchdog_lastMinute')}`\n"

        staff = f"Total Bans: `{wd40.get('staff_total')}`\n" \
                f"Today: `{wd40.get('staff_rollingDaily')}`\n"

        embed.add_field(name="Watchdog", value=auto)
        embed.add_field(name="Staff", value=staff)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
