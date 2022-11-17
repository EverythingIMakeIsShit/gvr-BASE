import traceback
import discord
from discord.ext import commands
import music
import multiprocessing


print(" ██╗ ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗██████╗ ██╗   ██╗████████╗██╗  ██╗███╗   ███╗██╗ ")
print("██╔╝██╔════╝ ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║████╗ ████║╚██╗")
print("██║ ██║  ███╗██████╔╝█████╗  ███████║   ██║   ██║   ██║███████║██║     ██║   ██║█████╗  ██████╔╝ ╚████╔╝    ██║   ███████║██╔████╔██║ ██║")
print("██║ ██║   ██║██╔══██╗██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝     ██║   ██╔══██║██║╚██╔╝██║ ██║")
print("╚██╗╚██████╔╝██║  ██║███████╗██║  ██║   ██║    ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗██║  ██║   ██║      ██║   ██║  ██║██║ ╚═╝ ██║██╔╝")
print(" ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝ ")
print("                                                                                                                                         ")
print("Made by NatSel#6142")
input("Press enter to start the bot...")
print("currently running: ", multiprocessing.current_process)
print("Running...")

cogs = [music]

# def startup():
#     consolecommands = input("Enter debug commands here: ")
#     if consolecommands == "call_stacks":
#         for line in traceback.format_stack():
#             print(line.strip())
#         else:
#             print("Invalid command")
#             return

client = commands.Bot(command_prefix='`', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTE5MDA5NDQzMTY4MDE0NDA3.YbPkPQ.ilqAYEtG0pKBRZI2QbEflVqkTqs")

# startup();