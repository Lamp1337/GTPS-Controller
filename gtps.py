# GTPS Controller by Lamp & Helped by numex, iFanpS
import os, time, threading, json
try:
    from discord.ext import commands
    import discord
    from pathlib import Path
except:
    os.system('pip install discord json')

client = commands.Bot(command_prefix="$", help_command=None)
permission_role_name = "permbot" # YOU MUST HAVE ROLE NAMED "permbot", IF U DONT HAVE THE ROLE.. YOU CANT USE THE COMMANDS
home = Path.home()
path = str(home)

os.system('cls & title GTPS Controller by Lamp#1442')
@client.event
async def on_ready():
    print("=============================
    print("GTPS CONTROLLER BOT IS ONLINE")
    print("=============================")
    await client.change_presence(activity=discord.Game(name=f"GTPS Controller by Lamp#1442"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.qualified_name == 'delplayer':
            await ctx.send("**Usage $delplayer <player>**")
        if ctx.command.qualified_name == 'delworld':
            await ctx.send("**Usage $delworld <world>**")
        if ctx.command.qualified_name == 'banip':
            await ctx.send("**Usage $banip <username> <ip> <reason>**")
        if ctx.command.qualified_name == 'info':
            await ctx.send("**Usage $info <username>**")
        if ctx.command.qualified_name == 'changepass':
            await ctx.send("**Usage $changepass <username> <new password>**")
        if ctx.command.qualified_name == 'checkbanip':
            await ctx.send("**Usage $checkbanip <ip>**")
        if ctx.command.qualified_name == 'gtstart':
            await ctx.send("**Usage $gtstart <enetname>**")
        if ctx.command.qualified_name == 'gtstop':
            await ctx.send("**Usage $gtstop <enetname>**")
        if ctx.command.qualified_name == 'givegems':
            await ctx.send("**Usage $givegems <username> <amount>**")

@client.command()
@commands.has_role(permission_role_name)
async def gtstart(ctx, enet):
    try:
        print(f"[LOGS] {ctx.author.display_name} Used $gtstart {enet}")
        if enet not in path:
            embed=discord.Embed(
                title=f"Error, {enet} Not Found"
            )
            await ctx.send(embed=embed)
        else:
            os.system(f"start {enet}")
            embed=discord.Embed(
                title=f"Enet Started, Server is UP"
            )
            await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title="Error, Cant start enet"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def gtstop(ctx, enet):
    try:
        print(f"[LOGS] {ctx.author.display_name} Used $gtstop {enet}")
        if enet not in path:
            embed=discord.Embed(
                title=f"Error, {enet} Not Found"
            )
            await ctx.send(embed=embed)
        else:
            os.system(f'taskkill /f /im "{enet}.exe"')
            embed=discord.Embed(
                title=f"Enet Closed, Server is Down"
            )
            await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title="Error, Cant close enet"
        )
        await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Commands List",
        description="```\n$help (show this command)\n$checkbanip (check if player got ip ban or no)\n$info (check player info, ip, gmail, etc)\n$givegems (give user gems)\n$delplayer (delete player file)\n$delworld (delete world file)\n$stats (check server stats)\n$unbanip (unban ip banned)\n$changepass (change user password)\n$gtup (auto open enet)\n$gtstop (auto close enet)```"
    )
    await ctx.send(embed=embed)

    print(f"[LOGS] {ctx.author.display_name} Used $help")

@client.command()
async def checkbanip(ctx, ip):
    try:
        print(f"[LOGS] {ctx.author.display_name} Used $checkbanip {ip}")
        f = open(f'./save/ipbans/ip/{ip}.txt', 'r')
        f.read()
        f.close()
        embed=discord.Embed(
            title=f"{ip} is Banned"
        )
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title=f"{ip} is not banned"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def givegems(ctx, name, amount):
    print(f"[LOGS] {ctx.author.display_name} used $givegems {name} {amount}")
    try:
        f = open(f"./save/gemdb/_{name}.txt", "w")
        f.write(f"{amount}")
        f.close()
        embed=discord.Embed(
            title=f"Successfuly give {amount} gems to {name}",
            description=f"Please Told {name} to Relog"
        )
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title=f"Error, Cant give gems to {name}"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def changepass(ctx, name, newpass):
    print(f"[LOGS] {ctx.author.display_name} Changed {name} Password to -> {newpass}")
    try:
        with open(f"./save/players/_{name}.json", "r+") as cps:
            dat = json.load(cps)
            
            dat["password"] = f"{newpass}"
        
        with open(f"./save/players/_{name}.json", "w") as cps:
            json.dump(dat, cps)
            embed=discord.Embed(
                title=f"Successfuly Change {name} Password to -> ||{newpass}||"
            )
            await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title=f"Error, Cant Change {name} Password"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def delplayer(ctx, name):
    try:
        print(f"[LOGS] {ctx.author.display_name} Used $delplayer {name}")
        os.remove(f'save/players/_{name}.json')
        embed = discord.Embed(
            title=f"Successfuly Delete Player {name}"
        )
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title="Error, Cant delete file"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def delworld(ctx, name):
    try:
        print(f"[LOGS] {ctx.author.display_name} Used $delworld {name}")
        os.remove(f'save/worlds/_{name}.json')
        embed = discord.Embed(
            title=f"Successfuly Delete World {name}"
        )
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title="Error, Cant delete file."
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def info(ctx, name):
    print(f"[LOGS] {ctx.author.display_name} Used $info {name}")
    try:
        with open(f'./save/players/_{name}.json') as pip:
            pip1 = json.load(pip)
            lol = f"""Username : {pip1['username']}
Player ID : {pip1['playerid']}
IP Address : {pip1['ip']}
Mac : {pip1['mac']}
Email : {pip1['email']}
Nick : {pip1['nick']}
Suptype : {pip1['subtype']}
Subdate : {pip1['subdate']}
ipID : {pip1['ipID']}
Level : {pip1['level']}"""
        embed=discord.Embed(
            title=f"{name} Info",
            description=lol
        )
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title=f"Error, Cant Check {name} Info"
        )
        await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
    print(f"[LOGS] {ctx.author.display_name} Used $stats")
    try:
        listworldss = len(os.listdir('save/worlds'))
        listplayerss = len(os.listdir('save/players'))
        listguildss = len(os.listdir('save/guilds'))
        embed = discord.Embed(color=0x00ff00, title='Server Stats',
        description=f"**Total Players Create : {listplayerss}\nTotal Guilds Create : {listguildss}\nTotal Worlds Create : {listworldss}**")
        text = await ctx.send(embed=embed)
        time.sleep(1)
        while True:
            listworld = len(os.listdir('save/worlds'))
            listplayers = len(os.listdir('save/players'))
            listguilds = len(os.listdir('save/guilds'))
            newembed = discord.Embed(color=0x00ff00, title='Server Stats',
            description=f"**Total Players Create : {listplayers}\nTotal Guilds Create : {listguilds}\nTotal Worlds Create : {listworld}**")
            edit = threading.Thread(target = await text.edit(embed=newembed))
            edit.start()
            time.sleep(1)
    except:
        embed=discord.Embed(
            title="Error, Cant Check Server Stats"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def banip(ctx, name, ip, *, reason):
    try:
        f = open(f'save/ipbans/ip/{ip}.txt', 'w')
        f.write(f'user who banned this ID: GTPS Controller\nBan-ip reason: {reason}\nBanned user name is: {name}')
        f.close()
        print(f"[LOGS] {ctx.author.display_name} Used $banip {name} with reason {reason}")
        embed = discord.Embed(
            title=f"Successfuly BanIP {ip} with Reason {reason}"
        )
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title=f"Error, Can't BanIP"
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(permission_role_name)
async def unbanip(ctx, ip):
    try:
        print(f"[LOGS] {ctx.author.display_name} Used $unbanip {ip}")
        os.remove(f"save/ipbans/ip/{ip}.txt")
        embed=discord.Embed(
            title=f"Successfuly Unban {ip}"
        )
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            title=f"Error, Cant Unban {ip}"
        )
        await ctx.send(embed=embed)

client.run("BOT TOKEN")
