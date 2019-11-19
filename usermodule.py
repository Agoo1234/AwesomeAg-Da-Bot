#! /usr/bin/env python3
import random
import discord
from discord.ext import commands
import os
import json
import discord
from dotenv import load_dotenv
from discord.utils import get
from discord.ext.commands import bot
import asyncio
import time
import youtube_dl
from ctypes.util import find_library
from discord import opus
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
import itertools
import sys
import traceback
import requests
import uvloop
import config
import time
import math
import time
from time import time, ctime, strftime, gmtime
cooldown_info_path = "cd.pkl"

#load_dotenv()
#token=os.getenv('NjI3MDAzMDI0OTI1MjYxODY2.XZKalg.kN6fuxvYY9vSlDYSGFhrB8vq9rk')

client = discord.Client()

#os.chdir("/Users/Agastya/Documents")




#client.run('NjI3MDAzMDI0OTI1MjYxODY2.XZKalg.kN6fuxvYY9vSlDYSGFhrB8vq9rk')


bot = commands.Bot(command_prefix='aga!', description='LIFE.')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Bot has officially connected to Discord. \n Current host server is: \n Agastya's Den")
    print('------')
    await bot.change_presence(activity=discord.Game(name='aga!help in '+f'{len(bot.guilds)}'+' servers'))
    #channel = bot.get_channel(628435777562476568)
    #await channel.send('I\'m online!')
    #import os, pickle
    #if os.path.exists(cooldown_info_path):  # on the initial run where "cd.pkl" file hadn't been created yet
    #    with open(cooldown_info_path, 'rb') as f:
    #         d = pickle.load(f)
    #         for name, func in self.commands.items():
    #            if name in d:  # if the Command name has a CooldownMapping stored in file, override _bucket
    #                self.commands[name]._buckets = d[name]
    #return await super().start(*args, **kwargs)    
class Bot(commands.Bot):

    async def start(self, *args, **kwargs):
        import os, pickle
        if os.path.exists(cooldown_info_path):  # on the initial run where "cd.pkl" file hadn't been created yet
            with open(cooldown_info_path, 'rb') as f:
                d = pickle.load(f)
                for name, func in self.commands.items():
                    if name in d:  # if the Command name has a CooldownMapping stored in file, override _bucket
                        self.commands[name]._buckets = d[name]
        return await super().start(*args, **kwargs)

    async def logout(self):
        import pickle
        with open(cooldown_info_path, 'wb') as f:
            # dumps a dict of command name to CooldownMapping mapping
            pickle.dump({name: func._buckets for name, func in self.commands.items()}, f)
        return await super().logout()


# or, for watching:
    #activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)
   #$ await client.change_presence(activity=activity)







#this big space is for all the json area. it will end with 2 lines of '#'


def logmemory(userid, cby):
    with open("admin.json", mode="r") as d:
        userdata = json.load(d)
        newuser = "userid_" + userid
        dict_value = {newuser:{"cby":cby,"admin":False}}
        userdata.update(dict_value)
    with open("admin.json", mode="w") as d:
        json.dump(userdata, d)
        # update json
        print(userdata)

def setadmin(userid):
    with open("admin.json", mode="r") as d:
        userdata = json.load(d)
        user = "userid_" + userid
        userdata[user]["admin"] = True
    with open("admin.json", mode="w") as d:
        json.dump(userdata, d)
        # update json
        print(userdata)
def addprofile(userid):
    with open("gp.json", mode="r") as g:
        gp = json.load(g)
        user = "userid_" + str(userid)
        dict_value = {user:{"credits":0,"exp":0}}
        gp.update(dict_value)
    with open("gp.json", mode="w") as g:
        json.dump(gp, g)
        # update json
        print(gp)
    with open("inventory.json", mode="r") as iv:
        inv = json.load(iv)
        user = "userid_" + str(userid)
        dict_value = {user:{"aged_cheese":0,"cookie":0,"pickaxe":0,"charger":0,"computer":0,"phone":0,"loot_box":0,"admin_badge":1, "diamond":0}}
        inv.update(dict_value)
    with open("inventory.json", mode="w") as iv:
        json.dump(inv, iv)
        # update json
        print(inv)
    with open("time.json",mode='r') as lt:
        l = json.load(lt)
        user="userid_"+str(userid)
        t = time()
        dict_value = {user:{"dailytime": t}}
        l.update(dict_value)
    with open('time.json',mode='w') as lt:
        json.dump(l,lt)
#
#def checkforprofile(userid):
#    with open("gp.json", mode="r") as g:
#        gp = json.load(g)
#        user = "userid_" + str(userid)
#        if user not in gp:
#            addprofile(userid);
#            print("Profile " + str(user) + "created");
#            rules = discord.Embed(title=".",description='.')
#            rules.add_field(name="**ADB** profile created!", value=":)")
#            bot.get_user(userid).send(embed=rules)
#        else: print("Profile creation request cancelled")
def checkforprofile(userid):
    with open("gp.json", mode="r") as g:
        gp = json.load(g)
        user = "userid_" + str(userid)
        if user not in gp:
            addprofile(userid);
            print("Profile " + str(user) + "created");
            rules = discord.Embed(title=".",description='.')
            rules.add_field(name="**ADB** profile created!", value=":)")
            bot.get_user(userid).send(embed=rules)
        else: print("Profile creation request cancelled")


def addserver(serverid):
    with open("verification.json", mode="r") as v:
        ver = json.load(v)
        server = "serverid_" + str(serverid)
        dict_value = {server:{}}
        ver.update(dict_value)
    with open("verification.json", mode="w") as v:
        json.dump(ver, v)
        # update json
        print(ver)
async def checkforserver(serverid):
    with open("verification.json", mode="r") as v:
        ver = json.load(v)
        server = "serverid_" + str(serverid)
        if server not in ver:
            addserver(serverid);
            print("Server " + server + "created");
        else: print("Server creation request cancelled")
#self._waiter
# currency
def checkforitem(userid, itemtypename):
    with open("inventory.json", mode="r") as iv:
        inv = json.load(iv)
        user = "userid_" + str(userid)
    if inv[user][itemtypename] > 0:
        return True
    return False

def additem(userid, itemtypename, n):
    with open("inventory.json", mode="r") as iv:
        inv = json.load(iv)
    with open("inventory.json", mode="w") as iv:
        user = "userid_" + str(userid)
        inv[user][itemtypename] = inv[user][itemtypename] + n
        json.dump(inv, iv)
        # update json
        print(inv)
def addcredits(userid, n):
    with open("gp.json", mode="r") as g:
        gp = json.load(g)
        user = "userid_" + str(userid)
        gp[user]["credits"] = gp[user]["credits"] + n
    with open("gp.json", mode="w") as g:
        json.dump(gp, g)
        # update json
        print(gp)



def addexp(userid, n):
    with open("gp.json", mode="r") as g:
        gp = json.load(g)
        user = "userid_" + str(userid)
        gp[user]["exp"] = gp[user]["exp"] + n
    with open("gp.json", mode="w") as g:
        json.dump(gp, g)
        # update json
        print(gp)














###






@client.event
async def on_member_join(member):
     print(str(member.name) + ' joined ' + str(member.guild))
     await member.send("Hey!!! Welcome to " + str(member.guild) + "!"+""" Here are some rules :notebook_with_decorative_cover: :
1. Do not try to hack the server.
2. We have our bots that we made, use but don't abuse. They are still developing, so deal with it.
3. DO NOT request for roles other than verify. Unless we say they are open in announcments, it's a waste of time for you and me.
4. Nitro Boosts = Rewards. If you help support this server in any way, like nitro boosts, you will get rewarded with roles.
5. I hafta know you really well to give you a high role-- that is if you even get one like I said in rule #3.
Have fun! Be sure to look in the rules, verify, and announcement channel!!""")
     channel = bot.get_channel(443961060601364481)
     await channel.send('<@'+str(member.id)+'> just joined the server! Woop Woop!')




@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("creeper"):
        await message.channel.send("awwwww man")
        print(str(message.author)+' just used on_message creeper without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith("creepah"):
        await message.channel.send("awwwww man")
        print(str(message.author)+' just used on_message creepah without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith('Hello') or message.content.startswith("hello") or message.content.startswith('Hi') or message.content.startswith("hi"):
        num = random.randint(1,4)
        if message.author == bot.user:
            return
        else:
            if num == 3:
                await message.channel.send(":smiley: :wave: Greetings, <@" + str(message.author.id) + ">")
            else:
                return
        #print(str(message.author)+' just used on_message hello without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith("so we back in the mine") or message.content.startswith("So we back in the mine"):
        await message.channel.send('got our pickaxe swinging from side to side')
        print(str(message.author)+' just used on_message so we back in the mine without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith('side side to side') or message.content.startswith('Side side to side'):
        await message.channel.send('this task a grueling one hope to find some diamonds tonight-night-night')
        print(str(message.author)+' just used on_message side side to side without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith('diamonds tonight'):
        await message.channel.send('heads up! You here a sound and turn around and look up! Total shock fills your body')
        print(str(message.author)+' just used on_message diamonds tonight without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith("oh no it's you again"):
        await message.channel.send("I could never forget those eyes eyes eyes, eyes eyes eyes eyes!")
        print(str(message.author)+' just used on_message oh no its you again without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith("Cuz baby tonight") or message.content.startswith("Cause baby tonight") or message.content.startswith("'Cause baby tonight") or message.content.startswith('cuz baby tonight'):
        await message.channel.send("The creeper's tryin' to steal our stuff again!")
        print(str(message.author)+' just used on_message cuz baby tonight without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith('lol') or message.content.startswith('Lol') or message.content.startswith("LOL") or message.content.startswith('lel') or message.content.startswith('Lel') or message.content.startswith('LEL') or message.content.startswith(':ROFL:') or message.content.startswith(':rofl:') or message.content.startswith(':laughing:'):
        if message.author == bot.user:
            return
        else:
            number=random.randint(1,6)
            if number > 5:
                await message.channel.send(':rofl: :laughing: lol')
            else:
                return
       #     print(str(message.author)+' just used on_message lol without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
#    elif message.content.endswith("the best") or message.content.endswith("da best"):
#        await message.channel.send("I AM THE BESSSST!")
#        print(str(message.author)+' just used on_message the best without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))

#    elif message.content.startswith("say"):
#        if message.content.endswith("Mr.Yi") or message.content.endswith("Mr.Yee"):
#            await message.channel.send("Hello, Mr.Yi")
#        else:
#            await message.channel.trigger_typing()
#        ####################################################
#        await message.channel.send(message.content.replace("say ", '')

    elif message.content.startswith("aga!inv"):
        
        if message.content.startswith("aga!invite") == False:
            inv = " ";
            user = "userid_" + str(message.author.id)
            checkforprofile(message.author.id);
            await message.channel.trigger_typing()
            ####################################################
            inventory = discord.Embed(title=str(message.author.name) + "\'s inventory :briefcase:", color = 0xffa500)
            with open("inventory.json", mode="r") as iv:
                inv = json.load(iv)
            if inv[user]["aged_cheese"] > 0:
                inventory.add_field(name="Aged Cheese :cheese: x" + str(inv[user]["aged_cheese"]), value="-----------------------------------------------", inline=False)
            if inv[user]["cookie"] > 0:
                inventory.add_field(name="Cookie :cookie: x" + str(inv[user]["cookie"]), value="-----------------------------------------------", inline=False)
            if inv[user]["pickaxe"] > 0:
                inventory.add_field(name="Pickaxe :pick: x" + str(inv[user]["pickaxe"]), value="-----------------------------------------------", inline=False)
            if inv[user]["computer"] > 0:
                inventory.add_field(name="Computer :computer: x" + str(inv[user]["computer"]), value="-----------------------------------------------", inline=False)
            if inv[user]["phone"] > 0:
                inventory.add_field(name="Phone :iphone: x" + str(inv[user]["phone"]), value="-----------------------------------------------", inline=False)
            if inv[user]["charger"] > 0:
              inventory.add_field(name="Charger :electric_plug: x" + str(inv[user]["charger"]), value="-----------------------------------------------", inline=False)
            if inv[user]["loot_box"] > 0:
              inventory.add_field(name="Loot Box :gift: x" + str(inv[user]["loot_box"]), value="-----------------------------------------------", inline=False)
            if inv[user]["admin_badge"]>0:
              inventory.add_field(name="Admin Badge :beginner: x" + str(inv[user]["admin_badge"]), value="-----------------------------------------------", inline=False)
            if inv[user]["diamond"]>0:
              inventory.add_field(name="Diamond :gem: x" + str(inv[user]["diamond"]), value="-----------------------------------------------", inline=False)
            await message.channel.send(embed = inventory)

    elif message.content.startswith("aga!admincmd"):
        await message.channel.trigger_typing()
        ####################################################
        with open("admin.json", mode="r") as d:
            userdata = json.load(d)
        if userdata["userid_" + str(message.author.id)]["admin"] == True:
            if message.content.replace("aga!admincmd", '').startswith(" adminset"):
                setadmin(message.content.replace("aga!admincmd", '').replace(" adminset ", ''))
                await message.channel.send(":white_check_mark: <@" + message.content.replace("aga!admincmd", '').replace(" adminset ", '') + "> is successfully an admin")
            if message.content.replace("aga!admincmd", '').startswith(" logmem"):
                logmemory(message.content.replace("aga!admincmd", '').replace(" logmem ", ''), bot.get_user(int(message.content.replace("aga!admincmd", '').replace(" logmem ", ''))).name)
                await message.channel.send(":white_check_mark: " + message.content.replace("aga!admincmd", '').replace(" logmem ", '') + " is logged")
        else:
            await message.channel.send("try man... I\'m not letting you do that dangerous stuff")
            await message.channel.send("so I don\'t care")


    elif message.content.startswith("aga!adminhelp"):
        await message.channel.trigger_typing()
        ####################################################
        with open("admin.json", mode="r") as d:
          userdata = json.load(d)
        if userdata["userid_" + str(message.author.id)]["admin"] == True:
            adminhelp = discord.Embed(title="Admin Help",color = 0x40e0d0)
            adminhelp.add_field(name="`aga!adminhelp`",value=" - this thing")
            adminhelp.add_field(name="`aga!spymode`",value=" - toggles logging messages sent in ADB\'s console")
            adminhelp.add_field(name="`aga!messagelocation`",value=" - view current message\'s location")
            adminhelp.add_field(name="`aga!admincmd`",value="`aga!admincmd logmem <userid>` - add user to `admin.json`\n`aga!admincmd adminset <userid>` - set user as admin")
            await message.author.send(embed=adminhelp)
        else:
            await message.channel.send("No no... this command is only for bot owner(s)")
    elif message.content.startswith("aga!buy"):
        await message.channel.trigger_typing()
        ####################################################
        checkforprofile(message.author.id);
        price = 0;
        addcredits(message.author.id, -(price)); additem(message.author.id, "aged_cheese", 1)
        buyfail = discord.Embed(color = 0xff0000);
        buyfail.add_field(name=":x: Error", value="Invalid Item!")
        buysucc = discord.Embed(color = 0x32CD32);
        if (message.content.replace("aga!buy ", '')) == "aged cheese" or (message.content.replace("aga!buy ", '')) == "Aged Cheese": price = 1; buysucc.add_field(name=":briefcase: Item Bought!", value="Bought x1 `Aged Cheese` :cheese:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "aged_cheese", 1); await message.channel.send(embed=buysucc)
        elif (message.content.replace("aga!buy ", '')) == "cookie" or (message.content.replace("aga!buy ", '')) == "Cookie": price = 5; buysucc.add_field(name=":briefcase: Item Bought!", value="Bought x1 `Cookie` :cookie:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "cookie", 1); await message.channel.send(embed=buysucc)
        elif (message.content.replace("aga!buy ", '')) == "phone" or (message.content.replace("aga!buy ", '')) == "Phone": price = 300; buysucc.add_field(name=":briefcase: Item Bought!", value="Bought x1 `Phone` :iphone:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "cookie", 1); await message.channel.send(embed=buysucc)
        
        else:
            if message.author == bot.user:
                return
            else:
                buyfail = discord.Embed(color = 0xff0000);
                buyfail.add_field(name=":x: Error", value="Invalid Item!")
                price = 0; await message.channel.send(embed=buyfail)

#    elif message.content.startswith("aga!loot"):
#        await message.channel.trigger_typing()
#        ####################################################
#        checkforprofile(message.author.id)
#        addexp(message.author.id, 5)
#        #######################################################################
#        loot_c = random.randint(0, 25)
#        addcredits(message.author.id, loot_c)
#        loot = discord.Embed(Title="Looting :mag:", color = 0x008000)
#        loot.add_field(name="Looting :mag:", value="You got **" + str(loot_c) + "** ADB Coins!")
#        await message.channel.send(embed=loot)


#    elif message.content.startswith("aga!daily"):
#        #@commands.cooldown(1, 86400, commands.BucketType.user)
#        await message.channel.trigger_typing()
#        ####################################################
#        checkforprofile(message.author.id)
#        addexp(message.author.id, 25)
#        #######################################################################
#        addcredits(message.author.id, 150)
#        daily = discord.Embed(Title="Daily ADB Coins :tada:", color=0xd4af37)
#        daily.add_field(name="Daily ADB Coins :tada:", value="You got **150** ADB Coins!")
#        await message.channel.send(embed=daily)

    elif message.content.endswith('aga!use cookie'):
        await message.channel.trigger_typing()
        cookie = discord.Embed(title= 'You Eat A Cookie!', color = 0x964B00)
        cookie.add_field(name='The chocolate chips melt in your mouth. Yum', value=':cookie:')
        await message.channel.send(embed = cookie)
        additem(message.author.id, "cookie", -1)
    elif message.content.startswith('aga!use cheese') or message.content.startswith('aga!use Cheese'):
        await message.channel.trigger_typing()
        cheese = discord.Embed(title= 'You Eat Some Cheese!', color = 0x9B870C)
        cheese.add_field(name='Congrats, I guess... You ate cheese', value=':cheese:')
        await message.channel.send(embed = cheese)
        additem(message.author.id, "aged_cheese", -1)

    elif message.content.startswith("aga!shop"):
        await message.channel.trigger_typing()
        ####################################################
        checkforprofile(message.author.id)
        shop = discord.Embed(title=":shopping_bags: Item Shop", description="`aga!buy` ta waste money on random stuff", color = 0x006994)
        shop.add_field(name="Aged Cheese :cheese: Buy: $1 Sell: $1", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Cookie :cookie: Buy: $5 Sell: $2", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Phone :iphone: Buy: $300 Sell: $175", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Diamond :gem: Buy: N/A Sell: $500", value="-----------------------------------------------", inline=False)
        await message.channel.send(embed=shop)
    elif message.content.startswith("aga!sell"):
        await message.channel.trigger_typing()
        ####################################################
        checkforprofile(message.author.id);
        price = 0;
        addcredits(message.author.id, -(price)); additem(message.author.id, "aged_cheese", -1)
        sellfail = discord.Embed(color=0xff0000);
        sellfail.add_field(name=":x: Error", value="Invalid Item!")
        sellsucc = discord.Embed(color=0x32CD32);
        if (message.content.replace("aga!sell ", '')) == "aged cheese" or (message.content.replace("aga!sell ", '')) == "Aged Cheese": price = -1; sellsucc.add_field(name=":briefcase: Item Sold!", value="Sold x1 `Aged Cheese` :cheese:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "aged_cheese", -1); await message.channel.send(embed=sellsucc)
        elif (message.content.replace("aga!sell ", '')) == "cookie" or (message.content.replace("aga!sell ", '')) == "Cookie": price = -2; sellsucc.add_field(name=":briefcase: Item Sold!", value="Sold x1 `Cookie` :cookie:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "cookie", -1); await message.channel.send(embed=sellsucc)
        elif (message.content.replace("aga!sell ", '')) == "diamond" or (message.content.replace("aga!sell ", '')) == "Diamond": price = 500; sellsucc.add_field(name=":briefcase: Item Sold!", value="Sold x1 `Diamond` :gem:!"); addcredits(message.author.id, price); additem(message.author.id, "diamond", -1); await message.channel.send(embed=sellsucc)
        else:
          await message.channel.send(embed=sellfail)
    elif message.content.startswith('aga!coin'):
      #randomcomment 
      coin = " ";
      user = "userid_" + str(message.author.id)
      checkforprofile(message.author.id);
      #await message.channel.trigger_typing()
      ####################################################
      coin = discord.Embed(title=str(message.author.name) + "\'s coins:", color=0x008080)
      with open("gp.json", mode="r") as g:
        gp = json.load(g)
        if gp[user]["credits"] > 0:
          coin.add_field(name=":money_with_wings:You have " + str(int(gp[user]["credits"])) + " ADB coins:money_with_wings:", value="-----------------------------------------------", inline=False)
        elif gp[user]["credits"] == 0:
          coin.add_field(name=':money_with_wings:I would recommend that we don\'t share the fact that you have...', description='0 ADB coins!!!:money_with_wings:', color=0x008080)
        elif gp[user]["credits"] < 0:
          coin.add_field(name=':money_with_wings:I would recommend that we don\'t share the fact that you have...', description=str(int(gp[user]["credits"])) + " ADB coins!!!:money_with_wings:", color=0x008080)

        await message.channel.send(embed = coin)
      #message.channel.send(embed=coin)
    elif message.content.startswith('aga!exp'):
      exp = discord.Embed(title=str(message.author.name)+'\'s EXP', color = 0x800000)
      coin = " ";
      user = "userid_"+str(message.author.id)
      checkforprofile(message.author.id)
      await message.channel.trigger_typing()

      with open('gp.json',mode='r') as g:
        gp=json.load(g)
        exp.add_field(name=':tada:You have '+str(int(gp[user]["exp"])) + ' ADB EXP points!:tada:', value = "*Use certain commands to gain exp!*", inline = False)
      await message.channel.send(embed = exp)
    elif message.content.startswith("aga!viewdata"):
        await message.channel.trigger_typing()
        ####################################################
        if message.content.replace("aga!viewdata", '').startswith(" backup"):
            with open("admin.json", mode="r") as ud:
                userdata = json.load(ud)
                await message.channel.send(str(userdata))
        elif message.content.replace("aga!viewdata", '').startswith(" v"):
            await message.channel.send("this feature is still unavailable.")
        else:
            with open("admin.json", mode="r") as ud:
                userdata = json.load(ud)
            await message.channel.send("\n```" + str(userdata) + "```\n") # print out admin.json
    elif message.content.replace("aga!use ", '') == "pickaxe" or message.content.replace("aga!use ", '') == "Pickaxe":
            if checkforitem(message.author.id, "pickaxe"):
                print("Item found!")
                loot = random.randint(1, 5)
                moneh = random.randint(10, 200)
                if loot == 1 or loot == 2 or loot == 3 or loot == 4:
                    mine = discord.Embed(
                        title=":pick: mInInG aWaY",
                        description = "You got minerals worth of **" + str(moneh) + "** ADB Coins!", color = 0xd4af37
                    )
                    addcredits(message.author.id, moneh)
                    await message.channel.send(embed=mine)
                if loot == 5:
                    mine = discord.Embed(
                        title = ":pick: mInInG aWaY",
                        description = "You got minerals worth of **" + str(moneh) + "** ADB Coins! **along with `1x` :gem:!**\nUnfortunately, that diamond was very hard to mine and your pick shattered right as u excavated the diamond!"
                    , color = 0xd4af37)
                    addcredits(message.author.id, moneh)
                    additem(message.author.id, "pickaxe", -1)
                    additem(message.author.id, "diamond", 1)
                    await message.channel.send(embed=mine)
    elif message.content.startswith('aga!mine') or message.content.lower == 'aga!mine':
      if checkforitem(message.author.id, "pickaxe"):
                print("Item found!")
                loot = random.randint(1, 5)
                moneh = random.randint(10, 200)
                if loot == 1 or loot == 2 or loot == 3 or loot == 4:
                    mine = discord.Embed(
                        title=":pick: mInInG aWaY",
                        description = "You got minerals worth of **" + str(moneh) + "** ADB Coins!", color = 0xd4af37
                    )
                    addcredits(message.author.id, moneh)
                    await message.channel.send(embed=mine)
                if loot == 5:
                    mine = discord.Embed(
                        title = ":pick: mInInG aWaY",
                        description = "You got minerals worth of **" + str(moneh) + "** ADB Coins! **along with `1x` :gem:!**\nUnfortunately, that diamond was very hard to mine and your pick shattered right as u excavated the diamond!"
                    )
                    addcredits(message.author.id, moneh)
                    additem(message.author.id, "pickaxe", -1)
                    additem(message.author.id, "diamond", 1)
                    await message.channel.send(embed=mine)


    if message.content.startswith("aga!gamble"):
        await message.channel.trigger_typing()
        ####################################################
        checkforprofile(message.author.id)
        with open("gp.json", mode="r") as g:
            gp = json.load(g)
            user = "userid_" + str(message.author.id)
        if message.content == "aga!gamble" or message.content == "aga!gamble ": message.channel.send("Invalid syntax!")
        chance = random.randint(1, 100)
        gamblesucc = discord.Embed(
            Title = ":slot_machine: Gamble ADB Coins",
            color=0x00ff26
    )
        gamblesucc.add_field(name=":slot_machine: Gamble ADB Coins", value="You have won **" + message.content.replace("aga!gamble ", '') + "** coins")
        
        gamblefail = discord.Embed(
            Title = ":slot_machine: Gamble ADB Coins",
            color=0xff0000
        )
        gamblefail.add_field(name=":slot_machine: Gamble ADB Coins", value="You have lost **" + str(int(message.content.replace("aga!gamble ", ''))) + "** coins")

        gambleinvalid = discord.Embed(
            Title = ":slot_machine: Gamble ADB Coins",
            color=0xfffb00
        )
        gambleinvalid.add_field(name=":slot_machine: Gamble ADB Coins", value="Invalid amount!")
        if (int(message.content.replace("aga!gamble ", '')) <= gp[user]["credits"]):
            addexp(message.author.id, int(message.content.replace("aga!gamble ", '')))
            if chance <= 30:
                addcredits(message.author.id, int(message.content.replace("aga!gamble ", ''))*2)
                await message.channel.send(embed=gamblesucc)
                addexp(message.author.id, 21)
            else: addcredits(message.author.id, -(int(message.content.replace("aga!gamble ", '')))); await message.channel.send(embed=gamblefail)
        else:
            await message.channel.send(embed=gambleinvalid)






    await bot.process_commands(message)
@bot.command(pass_context=True)
async def clear(ctx, amount=5):
    amount2=1
    if amount > 25:
        await ctx.send("I'm not gonna let you clear more than 25 messages at a time")
    else:
        await ctx.channel.purge(limit = amount+1)
        await ctx.send('Deleted '+str(amount)+' messages') 
        await asyncio.sleep(2)
        await ctx.channel.purge(limit = amount2)
#        print(ctx.message.author+' just cleared '+str(amount)+' messages.')
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Do ya think that I'm gonna let you just delete messages without permission?\n You're WRONG")
        asyncio.sleep(2)
        await ctx.channel.purge(limit = 2)


@bot.command(pass_context=True)
#@commands.cooldown(1,86400, commands.BucketType.user)
async def daily(ctx):
    #await ctx.send('test')
    ct = time()
    user = "userid_" + str(ctx.author.id)
    checkforprofile(ctx.author.id)
    with open("time.json", mode='r') as lt:
        t = json.load(lt)
        pt = t[user]["dailytime"]
        if ct-pt >= (24*60*60):
           #@commands.cooldown(1, 86400, commands.BucketType.user)
            await ctx.message.channel.trigger_typing()
            ####################################################
            checkforprofile(ctx.message.author.id)
            addexp(ctx.message.author.id, 25)
            #######################################################################
            addcredits(ctx.message.author.id, 150)
            daily = discord.Embed(Title="Daily ADB Coins :tada:", color=0xd4af37)
            daily.add_field(name="Daily ADB Coins :tada:", value="You got **150** ADB Coins!")
            await ctx.send(embed=daily)
            #t[user]["dailytime"] = (t[user]["dailytime"] - pt) + ct
            with open("time.json",mode='w') as lt:
                t[user]["dailytime"] = ((t[user]["dailytime"] - pt) + ct)
                json.dump(t,lt)
        elif ct-pt < (24*60*60):
            l = ct-pt
            poop = 86400-l
            stool = strftime("%H Hours, %M Minutes, and %S Seconds", gmtime(poop))
            await ctx.send("Sorry, but you have to wait **"+str(stool)+ "**before you can use this command again.")
        else:
            l = ct-pt
            poop = 86400-l
            stool = strftime("%H Hours, %M Minutes, and %S Seconds", gmtime(poop))
            await ctx.send("Sorry, but you have to wait **"+str(stool)+ "** before you can use this command again.")
            
       
        
#@daily.error
#async def daily_error(ctx,error):
#  if isinstance(error, commands.CommandOnCooldown):
#    await ctx.send('You can\'t use this command more than once in **24 Hours**\n')
@bot.command(pass_context=True)
@discord.ext.commands.is_owner()
async def ownercommand(ctx):
  addcredits(ctx.author.id, 999)
  ownercmd=discord.Embed(color=0x39ff14)
  ownercmd.add_field(name='MOOLAH!',value=':tada:**999 COINS!**:tada:')
  await ctx.send(embed=ownercmd)
@ownercommand.error
async def ownercommand_error(error,ctx):
    if isinstance(error, NotOwner):
        ctx.send("Hey! You're not the owner, so you can\'t do that!")
@bot.command(pass_context=True)
@commands.cooldown(1,15, commands.BucketType.user)
async def loot(ctx):
  await ctx.message.channel.trigger_typing()
  ####################################################
  await checkforprofile(ctx.message.author.id)
  await addexp(ctx.message.author.id, 5)
#######################################################################
  await addcredits(ctx.message.author.id, loot_c)
  loot = discord.Embed(Title="Looting :mag:", description="--------------------", color = 0x008000)
  loot.add_field(name="Looting :mag:", value="You got **" + str(loot_c) + "** ADB Coins!")
  await ctx.send(embed=loot)
@loot.error
async def loot_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send("You have to wait **15 seconds** before using this command again!")


@bot.command(pass_context=True)
async def add(ctx, a: int, b: int):
     await ctx.send(a+b)
@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Ya forgot to put in a number') 
     
@bot.command(pass_context=True)
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)
   # print(str(message.author)+' just used aga!multiply without trouble')
@bot.command(pass_context=True)
async def greet(ctx):
    await ctx.send(":smiley: :wave: GREETINGS, <@" + str(ctx.message.author.id) + ">")
#    print(str(message.author) +' just used aga!greet without trouble')
@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(name="Invite", color =0xFF4CFA )
    embed.add_field(name=":arrow_down:PRESS IT NOW!!!!!:arrow_down:", value="[------Click To Invite!!------](https://discordapp.com/api/oauth2/authorize?client_id=627003024925261866&permissions=8&scope=bot)", inline = False)
    embed.add_field(name=":arrow_down:THIS FOR THE SERVER!!!!!:arrow_down:", value="[------Click To Join!!------](https://discord.gg/3xdK3QD)")
    await ctx.send(embed=embed)
#    print(str(message.author)+' just used aga!invite without trouble')


@bot.command(pass_context = True)
async def warn(message, member = discord.Member,server = discord.Guild, *, reason=None):
    await member.send('Hey there, <@'+ str(member.id) + '>! How ya doin. You were just warned by '+str(message.author)+' in the server '+str(member.guild)+' reason: '+str(reason)+". Please don't do bad things again, otherwise you can get kicked or banned!")



@bot.command(pass_context=True)
@commands.has_role("Co-Owner") # This must be exactly the name of the appropriate role
async def addadmin(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="Admin")
    await bot.add_roles(member, role)
    #print(str(message.author)+' just used on_message without errors.')




@bot.command(pass_context = True)
async def servers(ctx):
    await ctx.send("I am in:\n" + f'{int(bot.guilds)}'+'servers.')
    await ctx.send('Here is the list:\n'+f'{str(bot.guilds)}.')

 
@bot.command
async def rules(ctx):
    await ctx.send("""1. DO NOT swear, or do anything else in the "BAD" section of chat
2. DON'T try to hack any of the bots
3. Do not spam for any roles and alll that.""")
#@bot.command(pass_context=True)

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles = True)
async def verify(ctx):
    await add_roles(Verified, reason=None, atomic=True)
    await ctx.send("Added role...?")

@verify.error
async def verify_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        ctx.send("You can't add other roles without the permissions in real life")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await member.channel.send("<@"+discord.Member.id+"> was kicked. \n Reason: "+str(reason))
    channel = bot.get_channel(627286906995998740)
    await channel.send("\n \n "+str(ctx.message.author)+" banned "+str(member)+". \n **Reason:** "+str(reason)+("\n\n **In the Server:** ")+str(ctx.message.guild))

@kick.error
async def kick_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send(str(member)+" was kicked. \n Reason: "+str(reason))
        print(str(member)+" was kicked. \n Reason: "+str(reason))
@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    print(str(member)+" was banned. \n Reason: "+str(reason))
    channel = bot.get_channel(627286906995998740)
    await channel.send("\n \n "+str(ctx.message.author)+" banned "+str(member)+". \n **Reason:** "+str(reason)+("\n\n **In the Server:** ")+str(ctx.message.guild))

@bot.command(pass_context=True)
@commands.has_permissions(ban_members = True)
async def unban(ctx, * , member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return
        else:
            return
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('That person is not on this server.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Ya don't have permission to do that. You tried, you failed")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't specify a person.")
    else:
        return
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('That person is either not banned or was never on **this server**')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Ya can't do that. Either ya don'y have the perms, or something else...")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't specify a person.")
#@kick.error
#async def kick_error(ctx, error):
#    if isinstance(error,commands.MissingPermissions):
#        await ctx.send("Don't try to ban people when you don't have permission. At least you tried.")
#    elif isinstance(error, commands.BadArgument):
#        await ctx.send("I can't find that person... You sure they're on **this** server?")
#    elif isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send("You didn't specify a person.")
    

@bot.command(pass_context=True)
async def cat(ctx):
    num=random.randint(1,5)
    if num == 1:  
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    elif num == 2:
        await ctx.send("https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif")
    elif num == 3:
        await ctx.send("https://media.giphy.com/media/C9x8gX02SnMIoAClXa/giphy.gif")
    elif num == 4:
       await ctx.send("https://media.giphy.com/media/8vQSQ3cNXuDGo/giphy.gif")
    elif num == 5:
        await ctx.send("https://media.giphy.com/media/ND6xkVPaj8tHO/giphy.gif")
  #  print(str(message.author)+' just used aga!cat without trouble')

@bot.command(pass_context=True)
async def info(ctx):
    num=random.randint(1,5)
    embed = discord.Embed(title="AwesomeAg Da Bot", description="The best bot ever, made by <@326497976040030208> \n Server Count: " + f'{len(bot.guilds)}',color=0x0000FF)
    await ctx.send(embed=embed)
#    print(str(message.author)+' just used aga!info without trouble')


@bot.command(pass_context = True)
async def mail(ctx,member: discord.Member,mail):
    await ctx.send("Sent mail to <@"+str(member.id)+">!")
    await ctx.author.send("Succesfuly sent mail to "+str(member)+". \n\n Thanks for using ADB express!")
    await ctx.member.send("You have mail! from <@" + str(ctx.author.id)+"> here it is:\n" + str(mail) + "\n\n Thanks for choosing ADB express!")


@bot.command(pass_context=True)
async def icon(ctx):
    await ctx.send("My current icon:")
    await ctx.send(file=discord.File('ADBHalloweenIcon.jpg'))

@bot.command(pass_context=True)
async def dog(ctx):
    num = random.randint(1,5)
    if num == 1:
        await ctx.send("https://media.giphy.com/media/26uf43dkw9ByWsjLi/giphy.gif")
    elif num == 2:
        await ctx.send("https://media.giphy.com/media/mCRJDo24UvJMA/giphy.gif")
    elif num == 3:
        await ctx.send("https://media.giphy.com/media/3o7TKSha51ATTx9KzC/giphy.gif")
    elif num == 4:
        await ctx.send("https://media.giphy.com/media/l4FGjj6pwWJN4dwqY/giphy.gif")
    elif num == 5:
        await ctx.send("They're scratching eachother! :rofl: \n https://media.giphy.com/media/dXxoP55b5UEPm/giphy.gif")
   # print(str(message.author)+' just used aga!dog without trouble')



bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="AwesomeAg Da Bot", description="The best bot around, buddies with Dummy. I will boss you around. \n click on the black things to see the command. \n List of commands and descriptions are:", color=0x0000FF)
    embed.add_field(name = '1', value="||aga!add X Y|| : Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name = '2', value="||aga!multiply X Y|| : Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name = '3', value="||aga!greet|| : Gives a nice greet message", inline=False)
    embed.add_field(name = '4', value="||aga!cat|| : Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name = '5', value="||aga!info|| : Gives a little info about the bot", inline=False)
    embed.add_field(name = '6', value="||aga!help|| : Gives this message", inline=False)
    embed.add_field(name = '7', value="||aga!dog|| : Gives a funny dog GIF just in case you like them better than cats", inline=False)
    embed.add_field(name = '8', value="||aga!invite|| : Gives the invite link so you can invite ADB to another server.", inline=False)
    embed.add_field(name = 'Page 1', value = "Type aga!help2 for the next page.",inline=False)
    await ctx.send(embed=embed)
    print(str(message.author)+' just used aga!help without trouble')
@bot.command()
async def help2(ctx):
    embed = discord.Embed(title="AwesomeAg Da Bot", description="The Best. \n More commands:",color=0x0000FF)
    embed.add_field(name="9",value="||aga!worship|| : Will tell you who you should pray to and thank." , inline=False)
    embed.add_field(name="10",value="||aga!funny|| : A funny gif to lighten your mood")
    embed.add_field(name="11",value="||aga!spam|| : Well, your page will be filled up and you might lag...")
    embed.add_field(name="12",value="||aga!kick <@user>|| : If you have the perms, it will kick someone...")
    embed.add_field(name="13",value="||aga!ban <@user>|| : If you have the perms, it will ban someone...")
    embed.add_field(name="14",value="||aga!icon|| : Shows the current icon for AwesomeAgDaBot")
    embed.add_field(name='Go to aga!help3, or aga!json for more things!')


    await ctx.send(embed=embed)
   # print(str(message.author)+' just used aga!help2 without trouble')

@bot.command()
async def jsonhelp(ctx):
    jsonhelp=discord.Embed(title='JSON help', description='All the JSON-related commands')
    jsonhelp.add_field(name='1', value='aga!daily --- gives you 150 daily coins')
    await ctx.send(embed=jsonhelp)
    
                   

    
@bot.command()
async def worship(ctx):
    await ctx.send("Worship the Creators \n Go and worship and thank the following people for merely existing: \n <@326497976040030208> \n <@429069454601879572> \n <@516325745820303382> \n <@627003024925261866>")
   # print(str(message.author)+' just used aga!worship without trouble')
@bot.command()
async def funny(ctx, num=random.randint(1,5)):

    if num == 1:
        await ctx.send("https://media.giphy.com/media/1hqYk0leUMddBBkAM7/giphy.gif")
    elif num == 2:
        await ctx.send("https://media.giphy.com/media/1wqqlaQ7IX3TXibXZE/giphy.gif")
    elif num == 3:
        await ctx.send("https://media.giphy.com/media/KHJw9NRFDMom487qyo/giphy.gif")
    elif num == 4:
        await ctx.send("https://media.giphy.com/media/nfLpqTrNPpqcE/giphy.gif")
    elif num == 5:
        await ctx.send("https://media.giphy.com/media/l1KVboXQeiaX7FHgI/giphy.gif")
    else:
        await ctx.send("Sorry, there was an error. Please try again later and report this to @AwesomeAg3141 if this is consistent.")
#    print(str(message.author)+' just used aga!funny without trouble')






@bot.command()
async def spam(ctx):
    #num = random.randint(1,5)
    #if num == 1:
     embed = discord.Embed(title='Revenge Remix' , description='''So  we back in the mine
Got our pickaxe swinging from side to side
Side-side to side
This  task, a grueling one
Hope  to find some diamonds tonight, night, night
Diamonds tonight''', inline=False, color=0x00FF00)
     embed.add_field(name='Heads up', value='''
You hear a sound, turn around and look up
Total shock fills your body
Oh, no, it's you again
I  can never forget those eyes, eyes, eyes
Eyes-eye-eyes''', inline=False)
     embed.add_field(name="""'Cause, baby, tonight""",value="""
The creeper's tryna steal all our stuff again
Tonight
You grab your pick, shovel, and bolt again (Bolt again-gain)
And run, run until it's done, done
Until the sun comes up in the morn'""", inline=False)
     embed.add_field(name='Heads up',value="""
Blows up
1-up
Get inside, don't be tardy
That's a nice life you have
That's a-
1-up
Get inside, don't be tardy
That's a nice life you have
That's a-
1-up
Get inside, don't be tardy
Heads up
Blows up
1-up
Get inside, don't be tardy
Eyes
""" , inline=False)
     embed.add_field(name='cont.',value='''Just when you think you're safe
Overhear some hissing from right behind
Right-right behind
That's a nice life you have
Shame it's gotta end at this time, time, time
Time-ti-time-time
Blows up
Then your health bar drops and you could use a one-up
Get inside, don't be tardy
So now you're stuck in there
Half a heart is left, but don't die, die, die
Die-die-die
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
Tonight
''', inline=False)
     embed.add_field(name="You grab your pick, shovel, and bolt again",value=''' (Bolt again-gain)
Dig up diamonds, and craft those diamonds
And make some armor, get it, baby
Go and forge that like you so MLG pro
The sword's made of diamonds, so come at me, bro, huh!
Training in your room under the torchlight
Hone that form to get you ready for the big fight
Every single day and the whole night
Creeper's out prowlin', hoo, alright
Creeper
Aw man
Look up
Total shock fills your body
Eyes, eyes, eyes
Eyes-eye-eyes ('Cause baby tonight)
Look up
Total shock fills your body
Eyes
Eyes, eyes, eyes
Eyes-eyes-eyes ('Cause baby tonight)
Look up
Total shock fills your body
Eyes, eyes, eyes
Eyes-eye-eyes ('Cause baby tonight)
Look up
Total shock fills your body
Eyes, eyes, eyes
Eyes-eye-eyes ('Cause baby tonight)''',inline=False)
     await ctx.send(embed=embed)
     #print(str(message.author)+' just used aga!spam without trouble')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        return
    #elif isinstance(error, commands.ValueError):
     #   await ctx.send("Sorry there was an error. It will be fixed soon...")



bot.run('NjI3MDAzMDI0OTI1MjYxODY2.XZKbCQ.XRcoitdXlp50ndmraV95Znjnw0w')



