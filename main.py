botonline = 0
#! /usr/bin/env python3

#<a:loadinggif:649364279782408215>
global rareevent1
#global botonline
rareevent1 = False
#import deepfry
#from PIL import Image, ImageDraw, ImageFont
from itertools import cycle
import adbbadwords
import keep_alive
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
import datetime
from datetime import datetime as d
import youtube_dl
from discord import opus
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
import itertools
import sys
import traceback
import requests

import config
import time
import math
import time
from time import time, ctime, strftime, gmtime
#import secret
import aiohttp
import urllib.parse, urllib.request, re
from random import shuffle
import sys
#import pynacl
cooldown_info_path = "cd.pkl"




client = discord.Client()





bot = commands.Bot(command_prefix=['aga!','adb!'], description='LIFE.')
@bot.event
async def on_ready():
    ct = time()
    with open("bottime.json",mode="r") as lt:
        t = json.load(lt)
        pt = t["bottime"]["time"]
        global botonline
        botonline = t["bottime"]["time"]

    with open("bottime.json",mode='w') as lt:
                t["bottime"]["time"] = ((t["bottime"]["time"] - t["bottime"]["time"] ) + ct)
                json.dump(t,lt)
    print("Loaded time onto bottime.json")
    print(f"Running on version discord.py rewrite {sys.version_info.major}.{sys.version_info.minor}{sys.version_info.micro}")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Bot has officially connected to Discord. \n Current host server is: \n Agastya's Den")
    print('------')
    maketrue  = 5
    
    while maketrue == 5:
        shouldi = checkoffline()
        if shouldi == False:
          await bot.change_presence(activity=discord.Game(name=open("status.txt", "r").read().format(str(len(bot.guilds))), type=1))
          await asyncio.sleep(5)
          changeoffline(False)
       



# or, for watching:
    #activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)
   #$ await bot.change_presence(activity=activity)





async def change_status():
  status = ["Msg1","Msg2","Msg3"]
  await bot.wait_until_ready()
  msgs=cycle(status)
  while not bot.is_closed:
    current_status = next(msgs)
    await bot.change_presence(game=discord.Game(name=current_status))
    await asyncio.sleep(5)

#this big space is for all the json area. it will end with 2 lines of '#'
#changeoffline(a), checkoffline()
def checkoffline():
  with open("offline.json", mode="r") as o:
    of = json.load(o)
    isoffline = of["bot"]["offline"]
    if isoffline==0:
      return False
    else:
      return True
def changeoffline(a):
    with open("offline.json", mode="r") as v:
        ol = json.load(v)
        if a==False:
          boi=0
        elif a==True:
          boi=1
        hi=ol["bot"]["offline"]
        ol["bot"]["offline"] = hi-hi+boi
    with open("offline.json", mode="w") as v:
        json.dump(ol, v)
        # update json
        #print(ol)
def triggerfy(original):
  im = Image.open(original)
  triggered_im = Image.open('triggered.png').convert("RGBA")
  def image_overlay(src, color, alpha):
    overlay= Image.new(src.mode,src.size, color)
    return Image.blend(src,overlay,alpha)
  im = image_overlay(im, "#ff0000",0.3)
  x, y = im.size
  trig_x, trig_y = im.size
  triggered_im.thumbnail((x,y), Image.ANTIALIAS)
  #triggered_im.save('triggered_edited.png')
  imgs=[]
  for _ in range(10):
    imgs.append(im.copy())
  shake_amount=3
  img_shake_amount=10
  for i in range(len(imgs)):
    text_move_y=random.randint(-shake_amount, shake_amount)
    text_move_x = random.randint((y-y//5.12)-shake_amount,(y-y//5.12)+shake_amount)
    img_move_y = random.randint(-img_shake_amount, img_shake_amount)
    img_move_x = random.randint(-img_shake_amount, img_shake_amount)
    im = imgs[i]
    zoom_x = 1-(img_shake_amount/x)
    zoom_y = 1-(img_shake_amount/y)
    im = im.transform(im.size, Image.AFFINE, (zoom_x, 0, img_move_x+img_shake_amount//2,0,zoom_y,img_move_y+img_shake_amount))
    im.paste(triggered_im, (text_move_y, text_move_x),triggered_im)
    imgs[i]=im
  with io.BytesIO() as output:
    imgs[0].save(
      output,
      format="GIF",
      save_all=True,
      append_images=imgs[1:],
      duration=0,
      loop=0
    )
    output.seek(0)
    value=output.getvalue()
  del im
  del triggered_im
  return value
    

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
        dict_value = {user:{"aged_cheese":0,"cookie":0,"pickaxe":1,"charger":0,"computer":0,"phone":0,"loot_box":0,"admin_badge":1, "diamond":0}}
        inv.update(dict_value)
    with open("inventory.json", mode="w") as iv:
        json.dump(inv, iv)
        # update json
        print(inv)
    with open("time.json",mode='r') as lt:
        l = json.load(lt)
        user="userid_"+str(userid)
        t = time()
        dict_value = {user:{"dailytime": t, "begtime":t, "worktime":0, "job" : 0}}
        l.update(dict_value)
    with open('time.json',mode='w') as lt:
        json.dump(l,lt)
def addprofilewarn(userid, serverid):
    with open("warn.json", mode="r") as w:
        warn = json.load(w)
        user = "userid_" + str(userid)+f"_serverid_{serverid}"
        dict_value = {user:{"normal":0,"minor":0,"major":0}}
        warn.update(dict_value)
    with open("warn.json", mode="w") as w:
        json.dump(warn, w)
        # update json
        print(warn)
def checkwarns(userid, serverid, warntype):
  with open("warn.json", mode="r") as w:
    warn = json.load(w)
    user = f"userid_{userid}_serverid_{serverid}"
    warns = warn[user][warntype]
    return int(warns)
def checkforprofilewarn(userid, serverid):
    with open("warn.json", mode="r") as w:
        warn = json.load(w)
        user = "userid_" + str(userid)+f"_serverid_{serverid}"

        if user not in warn:
            addprofilewarn(userid, serverid);
            print("Profile " + str(user) + "created in warn.json");
            #bot.get_user(userid).send(embed=rules))
            #loo.send(embed=rules)
        else: print("Warn profile creation request cancelled")
def addwarns(userid,serverid,warntype,n):
    with open("warn.json", mode="r") as w:
        warn = json.load(w)
        user = "userid_" + str(userid)+f"_serverid_{serverid}"
        warn[user][warntype] = warn[user][warntype] + n
    with open("warn.json", mode="w") as w:
        json.dump(warn, w)
        # update json

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
            #bot.get_user(userid).send(embed=rules))
            #loo.send(embed=rules)
        else: print("Profile creation request cancelled")
def checkforjob(userid):
  global personjob
  with open("time.json",mode='r') as x:
    xy = json.load(x)
    user = f"userid_{userid}"
    if user not in xy:
      addprofile(userid)
    else:
      personjob = xy[user]["job"]
      print(f"Job {personjob} for {userid}")


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
    with open("inventory.json", mode="r") as i:
        inv = json.load(i)
    with open("inventory.json", mode="w") as i:
        user = "userid_" + str(userid)
        inv[user][itemtypename] = inv[user][itemtypename] + n
        json.dump(inv, i)
        # update json
        #print(inv)
def addcredits(userid, n):
    with open("gp.json", mode="r") as g:
        gp = json.load(g)
        user = "userid_" + str(userid)
        gp[user]["credits"] = gp[user]["credits"] + n
    with open("gp.json", mode="w") as g:
        json.dump(gp, g)
        # update json




def addexp(userid, n):
    with open("gp.json", mode="r") as g:
        gp = json.load(g)
        user = "userid_" + str(userid)
        gp[user]["exp"] = gp[user]["exp"] + n
    with open("gp.json", mode="w") as g:
        json.dump(gp, g)
        # update json
        #print(gp)
def jobchange(userid, job):
  with open("time.json", mode = 'r') as y:
    ly = json.load(y)
    user = "userid_"+ str(userid)
    llll = ly[user]["job"]
    ly[user]["job"] = ((((ly[user]["job"])-int(llll))+int(job)))
  with open("time.json",mode="w") as y:
    json.dump(ly,y)

 
    














###






#@bot.event
#async def on_member_join(member):
#     print(str(member.name) + ' joined ' + str(member.guild))
#     await member.send("Hey!!! Welcome to " + str(member.guild) + "!"+""" Here are some rules :notebook_with_decorative_cover: :
#1. Do not try to hack the server.
#2. We have our bots that we made, use but don't abuse. They are still developing, so deal with it.
#3. DO NOT request for roles other than verify. Unless we say they are open in announcments, it's a waste of time for everyone!
#4. Nitro Boosts = Rewards. If you help support this server in any way, like nitro boosts, you will get rewarded with roles.
#Have fun! Be sure to look in the rules, verify, and announcement channel!!""")
     #channel = bot.get_channel(443961060601364481)
     #await channel.send('<@'+str(member.id)+'> just joined the server! Woop Woop!')
     #await asyncio.sleep(120)
     #rolex = member.guild.get_role(443945526442983425)
     #await member.add_roles(rolex, reason=None)
     #print("TEST SUCCESS")


default_emojis = [
    "\N{GRINNING FACE}",
 #   "\N {KEYCAP DIGIT ONE}"
    
]

custom_emojis = [
    #"thrinking"
    "pbjtime"
]


@bot.event
async def on_command_completion(ctx):
  checkforprofile(ctx.author.id)
  addexp(ctx.author.id, 5)
@bot.event
async def on_message(message):
    def spymode():
      if message.channel.guild.id == "437048931827056642":
        return
      else:
        spy=open("spymode.txt",mode="r")
        isspymode = spy.read()
        if str(isspymode) == "true":
          print(f"{message.channel.guild.name}: {message.channel.name} {message.author.name}: {message.content}")
        else:
          return "done"
    spymode()
    if message.channel.type == 'DMChannel':
      #await message.channel.send("This cannot be done in a DM channel")
      return "DM"
    try:
      filterchannels=[443530263637655554,682998601211052037,695027267948249218]
      if message.channel.guild.id in filterchannels:
        
        global bad_words
        bad_words = adbbadwords.badwords()
        
        chat_filter=[bad_words]
        bypass_list=[]
        contents = message.content.split(" ") #contents is a list type 
        for word in contents: 
         if word.lower() in bad_words: 
           if message.author.id not in bypass_list: 
            try: 

               await message.channel.purge(limit=1)
               newm = message.content.replace(word, f"||{word}||")
               
               await message.channel.send(f"**Hey, <@{message.author.id}>!** Watch that profanity!") 
              
            except AttributeError: 
              pass
    except AttributeError:
      pass
    if message.author.name == "AwesomeAg#3141":
      r = random.randint(1,5)
      if r == 3:
        await react(message)
      else:
        return
    if message.author == client.user:
        return
    
        
    elif message.content.startswith("creeper"):
        await message.channel.send("awwwww man")
        print(str(message.author)+' just used on_message creeper without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    elif message.content.startswith("creepah"):
        await message.channel.send("awwwww man")
        print(str(message.author)+' just used on_message creepah without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith('Hello') or message.content.startswith("hello") or message.content.startswith('Hi') or message.content.startswith("hi"):
   #     num = random.randint(1,4)
   #     if message.author == bot.user:
   #         return
   #     else:
   #         if num == 3:
   #             await message.channel.send(":smiley: :wave: Greetings, <@" + str(message.author.id) + ">")
  #          else:
  #              return
        #print(str(message.author)+' just used on_message hello without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith("so we back in the mine") or message.content.startswith("So we back in the mine"):
        #await message.channel.send('got our pickaxe swinging from side to side')
        #print(str(message.author)+' just used on_message so we back in the mine without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith('side side to side') or message.content.startswith('Side side to side'):
        #await message.channel.send('this task a grueling one hope to find some diamonds tonight-night-night')
        #print(str(message.author)+' just used on_message side side to side without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith('diamonds tonight'):
        #await message.channel.send('heads up! You here a sound and turn around and look up! Total shock fills your body')
        #print(str(message.author)+' just used on_message diamonds tonight without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith("oh no it's you again"):
        #await message.channel.send("I could never forget those eyes eyes eyes, eyes eyes eyes eyes!")
        #print(str(message.author)+' just used on_message oh no its you again without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith("Cuz baby tonight") or message.content.startswith("Cause baby tonight") or message.content.startswith("'Cause baby tonight") or message.content.startswith('cuz baby tonight'):
        #await message.channel.send("The creeper's tryin' to steal our stuff again!")
        #print(str(message.author)+' just used on_message cuz baby tonight without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
    #elif message.content.startswith('lol') or message.content.startswith('Lol') or message.content.startswith("LOL") or message.content.startswith('lel') or message.content.startswith('Lel') or message.content.startswith('LEL') or message.content.startswith(':ROFL:') or message.content.startswith(':rofl:') or message.content.startswith(':laughing:'):
     #   if message.author == bot.user:
     #       return
     #   else:
     #       number=random.randint(1,6)
     #       if number > 5:
     #           await message.channel.send(':rofl: :laughing: lol')
     #       else:
     #           return
     #  #     print(str(message.author)+' just used on_message lol without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))
#    elif message.content.endswith("the best") or message.content.endswith("da best"):
#        await message.channel.send("I AM THE BESSSST!")
#        print(str(message.author)+' just used on_message the best without errors. In the channel '+str(message.channel)+' In the server '+str(message.guild))

    #elif message.content.startswith("say"):
        #if "say hello to mr.yi" in message.content.lower() or "say hello to mr.yee" in message.content.lower():
            #await message.channel.send("Hello, Mr.Yi")
            #return
        #elif "say hello to mr.yi" not in message.content.lower() or "say hello to mr.yee" not in message.content.lower():
            #await message.channel.trigger_typing()
        ####################################################
        #await message.channel.send(message.content.replace("say ", ''))

    #elif message.content.startswith("aga!inv"):
        
    #    if message.content("aga!invite") == False:
    #        inv = " ";
    #        user = "userid_" + str(message.author.id)
    #        checkforprofile(message.author.id);
    #        await message.channel.trigger_typing()
    #        ####################################################
    #        inventory = discord.Embed(title=str(message.author.name) + "\'s inventory :briefcase:", color = 0xffa500)
    #        with open("inventory.json", mode="r") as iv:
    #            inv = json.load(iv)
    #        if inv[user]["aged_cheese"] > 0:
    #            inventory.add_field(name="Aged Cheese :cheese: x" + str(inv[user]["aged_cheese"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["cookie"] > 0:
    #            inventory.add_field(name="Cookie :cookie: x" + str(inv[user]["cookie"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["pickaxe"] > 0:
    #            inventory.add_field(name="Pickaxe :pick: x" + str(inv[user]["pickaxe"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["computer"] > 0:
    #            inventory.add_field(name="Computer :computer: x" + str(inv[user]["computer"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["phone"] > 0:
    #            inventory.add_field(name="Phone :iphone: x" + str(inv[user]["phone"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["charger"] > 0:
    #          inventory.add_field(name="Charger :electric_plug: x" + str(inv[user]["charger"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["loot_box"] > 0:
    #          inventory.add_field(name="Loot Box :gift: x" + str(inv[user]["loot_box"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["admin_badge"]>0:
    #          inventory.add_field(name="Admin Badge :beginner: x" + str(inv[user]["admin_badge"]), #value="-----------------------------------------------", inline=False)
    #        if inv[user]["diamond"]>0:
    #          inventory.add_field(name="Diamond :gem: x" + str(inv[user]["diamond"]), #value="-----------------------------------------------", inline=False)
    #        await message.channel.send(embed = inventory)

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
                await message.channel.send(":white_check_mark: <@" + message.content.replace("aga!admincmd", '').replace(" logmem ", '') + "> is logged")
            if message.content.replace("aga!admincmd","").startswith(" spymode"):
              spymode=open("spymode.txt",mode="r")
              isspy=spymode.read()
              if str(isspy) == "false":
                print("Spymode on")
                await message.channel.send("Spymode is now turned on :white_check_mark: :detective:")
                spymode.close()
                spymode=open("spymode.txt",mode="w")
                spymode.truncate()
                #spymode.write("false")
                spymode.write("true")
              elif str(isspy)=="true":
                print("Spymode off")
                await message.channel.send("Turned off spymode :x: :detective:")
                spymode.close()
                spymode=open("spymode.txt",mode="w")
                spymode.truncate()
                #spymode.write("true")
                spymode.write("false")
        else:
            await message.channel.send("try man... I\'m not letting you do that dangerous stuff")
            await message.channel.send("so I don\'t care")

    elif message.content.startswith("aga!meme reccomondation"):
      plop = message.content.replace('aga!meme reccomondation', ' ')
      channel = bot.get_channel(628435777562476568)
      await channel.send("Meme rec./link " + str(plop))
      await message.channel.send("Thanks for your meme reccomondation!")
    elif message.content.startswith("aga!adminhelp"):

        await message.channel.trigger_typing()
        ####################################################
        with open("admin.json", mode="r") as d:
          userdata = json.load(d)
        if userdata["userid_" + str(message.author.id)]["admin"] == True:
            adminhelp = discord.Embed(title="Admin Help",color = 0x40e0d0)
            adminhelp.add_field(name="`aga!adminhelp`",value=" - this thing")
            adminhelp.add_field(name="`aga!admincmd spymode`",value=" - toggles logging messages sent in ADB\'s console")
            adminhelp.add_field(name="`aga!messagelocation`",value=" - view current message\'s location")
            adminhelp.add_field(name="`aga!admincmd`",value="`aga!admincmd logmem <userid>` - add user to `admin.json`\n`aga!admincmd adminset <userid>` - set user as admin")
            await message.author.send(embed=adminhelp)
            await message.channel.send(":white_check_mark: Sent you the admin help embed")
        else:
            await message.channel.send("No no... this command is only for bot owner(s)")

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
        theshop = discord.Embed(title=":shopping_bags: Item Shop", description="`aga!buy` ta waste money on random stuff", color = 0x006994)
        shop.add_field(name="Aged Cheese :cheese: Buy: $1 Sell: $1", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Cookie :cookie: Buy: $5 Sell: $2", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Phone :iphone: Buy: $300 Sell: $175", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Diamond :gem: Buy: N/A Sell: $500", value="-----------------------------------------------", inline=False)
        shop.add_field(name="Computer :computer: Buy: $1000 Sell: $750", value="-----------------------------------------------", inline=False)
        shop.add_field(name="ADMIN BADGE :beginner: Buy: $50 Sell: N/A", value="-----------------------------------------------", inline=False)
        theshop.add_field(name="Items:",value='''
        ```md
[ AGED CHEESE ][ KEY: CHEESE ]
< BUY: $1 > < SELL: $1 >
> YUMMY?

[ COOKIE ][ KEY: COOKIE ]
< BUY: $5 > < SELL: $2 >
> Careful! Hot!

[ PHONE ][ KEY: PHONE ]
< BUY: $300 > < SELL: $175 >
> GET DISCORD ON YOUR PHONE!

[ DIAMOND ][ KEY: DIAMOND ]
< BUY: N/A > < SELL: $500 >
> SHINY!

[ COMPUTER][ KEY: COMPUTER ]
< BUY: $1000 > < SELL: $750 >
> AREN'T YOU ALREADY ON ONE?

[ ADMIN BADGE ][ KEY: ADMIN ]
< BUY: $50 > < SELL: N/A >
> YAY! YOU GOT NOTHING!
```
        ''', inline=False)
        await message.channel.send(embed=theshop)
    #elif message.content.startswith("aga!sell"):
       # await message.channel.trigger_typing()
        ####################################################
       # checkforprofile(message.author.id);
        #price = 0;
        #addcredits(message.author.id, -(price)); additem(message.author.id, "aged_cheese", -1)
        #sellfail = discord.Embed(color=0xff0000);
        #sellfail.add_field(name=":x: Error", value="Invalid Item!")
        #sellsucc = discord.Embed(color=0x32CD32);
        #if (message.content.replace("aga!sell ", '')) == "aged cheese" or (message.content.replace("aga!sell ", '')) == "Aged Cheese": price = -1; sellsucc.add_field(name=":briefcase: Item Sold!", value="Sold x1 `Aged Cheese` :cheese:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "aged_cheese", -1); await message.channel.send(embed=sellsucc)
        #elif (message.content.replace("aga!sell ", '')) == "cookie" or (message.content.replace("aga!sell ", '')) == "Cookie": price = -2; sellsucc.add_field(name=":briefcase: Item Sold!", value="Sold x1 `Cookie` :cookie:!"); addcredits(message.author.id, -(price)); additem(message.author.id, "cookie", -1); await message.channel.send(embed=sellsucc)
        #elif (message.content.replace("aga!sell ", '')) == "diamond" or (message.content.replace("aga!sell ", '')) == "Diamond": price = 500; sellsucc.add_field(name=":briefcase: Item Sold!", value="Sold x1 `Diamond` :gem:!"); addcredits(message.author.id, price); additem(message.author.id, "diamond", -1); await message.channel.send(embed=sellsucc)
        #else:
        #  await message.channel.send(embed=sellfail)
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
          coin.add_field(name=':money_with_wings:I would recommend that we don\'t share the fact that you have... '+'0 ADB coins!!!:money_with_wings:',value='-----------------------------------------------')
        elif gp[user]["credits"] < 0:
          coin.add_field(name=':money_with_wings:I would recommend that we don\'t share the fact that you have... '+str(int(gp[user]["credits"])) + " ADB coins!!!:money_with_wings:",value='-----------------------------------------------')

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
        if message.content.replace("aga!viewdata", '').startswith("backup"):
            with open("admin.json", mode="r") as ud:
                userdata = json.load(ud)
                await message.channel.send(str(userdata))
        elif message.content.replace("aga!viewdata", '').startswith(" v"):
            await message.channel.send("this feature is still unavailable.")
        else:
            with open("admin.json", mode="r") as ud:
                userdata = json.load(ud)
            await message.channel.send("\n```json\n" + str(userdata) + "```\n") # print out admin.json
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
      checkforprofile(message.author.id)
      hi=True
      if checkforitem(message.author.id, "pickaxe"):
      #if hi:
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
                        description = "You got minerals worth of **" + str(moneh) + "** ADB Coins! **along with `1x` :gem:!**\nUnfortunately, that diamond was very hard to mine and your pick shattered right as u excavated the diamond!", color = 0xd4af37
                    )
                    addcredits(message.author.id, moneh)
                    additem(message.author.id, "pickaxe", -1)
                    additem(message.author.id, "diamond", 1)
                    await message.channel.send(embed=mine)
      else:
        nope=discord.Embed(title="Hold up!",description="You don't have a pickaxe! Use `aga!search` to get a pickaxe.", color=0xff0000)
        nope.set_footer(text="If you think there is a problem, contact AwesomeAg#3141")

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
    elif message.content.lower() == 'aga!work':
       checkforjob(message.author.id)
       addexp(message.author.id, 5)
       #await message.channel.send(f"Under construction. Coming soon.")
       if personjob == 0:
         await message.channel.send("You currently don't have a job, or your job doesn't exist! Type \"aga!changejob\" to change or set your job")
       if personjob == 1:
         activities=["Top ten videos = $", "Pewdiepie","Earn that moolah","Song videos are where the money is at","Ads make you a lot of money", "Top ten videos are where the money is at","Hit that notification bell!", "Ad revenue please!"]
         act = random.choice(activities)
         #await message.channel.send("Hold it there YouTuber! This command is still under construction!")
         await message.channel.send(f"Type the following phrase into the chat:\n**{act}**")
         channel = message.channel
         def check(m):
              return m.content.lower() == act.lower() and m.channel == channel and m.author == message.author
         msg = await bot.wait_for('message', check=check)
         praises=["GFY","Good for you","congrats","lucky you"]
         praise = random.choice(praises)
         ytdl = ["",'','',"*BTW, Susan Wojcicki is the CEO of YouTube*","Use aga!changejob to change your job"]
         ll = random.choice(ytdl)
         await message.channel.send(f'**Susan Wojcicki:**  {praise}\n\nYou got `500` ADB coins for working!\n\n{ll}')
         addcredits(message.author.id, 500)
         addexp(message.author.id, 10)
       elif personjob == 2:
         whone = random.randint(1,2)
         if whone == 1:
              #print(l)
              await message.channel.trigger_typing()
              activities = ["Cooking is fun", "Sell food for $10","Taco Bell still is food","Taco Bell is better than McDonalds","McDonalds is better than Taco Bell"]
              act = random.choice(activities)
              await message.channel.send(f"Type the following phrase into the chat:\n\n**{act}**")
              channel = message.channel
              def check(m):
                   return m.content.lower() == act.lower() and m.channel == channel and m.author == message.author
              msg = await bot.wait_for('message', check=check)
              praises=["GFY","Good for you","congrats","lucky you","Yummy food ya made right there","Good job"]
              praise = random.choice(praises)
              ytdl = ["",'','',"Use aga!changejob to change your job","Use aga!changejob to change your job"]
              people=["Gordon Ramsay","Chris Cornell","David Burtka"]
              person = random.choice(people)
              ll = random.choice(ytdl)
              await message.channel.send(f'**{person}:** {praise}\n\nYou got `500` ADB coins for working!\n\n{ll}')
         else:
           channel = message.channel
           def shuffle_word(word):
              word = list(word)
              shuffle(word)
              return ''.join(word)
           LLL = ['food', 'cooking', 'chef','taco bell','kitchen','chicken','restraunt','dominoes','pizza','burritos','dumplings']
           L = random.choice(LLL)
           LL = [shuffle_word(L)]
           LL = str(LL)
           LLL = LL.strip("'[")
           LLL = str(LLL)
           LL= LLL.strip("']")
           poo = await message.channel.send(f"Unscramble the following sequence:\n`{LL}`\nBe sure to memorize it- it will disappear in 5 seconds...")
           await asyncio.sleep(1)
           await poo.edit(content=f"Unscramble the following sequence:\n`{LL}`\nBe sure to memorize it- it will disappear in 4 seconds...")
           await asyncio.sleep(1)
           await poo.edit(content=f"Unscramble the following sequence:\n`{LL}`\nBe sure to memorize it- it will disappear in 3 seconds...")
           await asyncio.sleep(1)
           await poo.edit(content=f"Unscramble the following sequence:\n`{LL}`\nBe sure to memorize it- it will disappear in 2 seconds...")
           await asyncio.sleep(1)
           await poo.edit(content=f"Unscramble the following sequence:\n`{LL}`\nBe sure to memorize it- it will disappear in 1 second...")
           await asyncio.sleep(1)
           await poo.edit(content=f"Unscramble the following sequence:\n`{LL}`\nBe sure to memorize it- it will disappear in 0 seconds...")
           await poo.edit(content='Ok. GUESS')
           def check(m):
                   return m.content.lower() == L.lower() and m.channel == channel
           msg = await bot.wait_for('message', check=check)
           praises=["I'm proud of you!","GFY","Good for you","congrats","lucky you","Yummy food ya made right there","Good job"]
           praise = random.choice(praises)
           ytdl = ["",'','',"Use aga!changejob to change your job","Use aga!changejob to change your job"]
           people=["Gordon Ramsay","Chris Cornell","David Burtka","Boss"]
           person = random.choice(people)
           ll = random.choice(ytdl)
           await message.channel.send(f'**{person}:** {praise}\n\nYou got `500` ADB coins for working!\n\n{ll}')
           await asyncio.sleep(2)
           await message.channel.purge(limit=4)
         addcredits(message.author.id, 500)
         addexp(message.author.id, 10)
         #message.channel.purge(limit=2)
       elif personjob == 3:
         await message.channel.trigger_typing()
         activities = ["Coding away","I code python","Google assistant is better than siri","Pixel 4 just came out","www.google.com","Type to make the all new ultimate google device","alt+F4 on windows, or cmd+Q on mac to hack google","Type this in to earn $500 for nothing","Type this to get free food"]
         act = random.choice(activities)
         await message.channel.send(f"Type the following phrase into the chat:\n\n**{act}**")
         channel = message.channel
         def check(m):
              return m.content.lower() == act.lower() and m.channel == channel and m.author == message.author
         msg = await bot.wait_for('message', check=check)
         praises=["GFY","Good for you","congrats",":computer: nIcE","You get a promotion","Good job","New pixel phone thanks to you"]
         praise = random.choice(praises)
         ytdl = ["",'','',"Use aga!changejob to change your job","Use aga!changejob to change your job"]
         people=["Larry Page","Sundar Pichai","Sergey Brin","Susan Wojcicki "]
         person = random.choice(people)
         ll = random.choice(ytdl)
         await message.channel.send(f'**{person}:** {praise}\n\nYou got `500` ADB coins for working!\n\n{ll}')
         addcredits(message.author.id, 500)
         addexp(message.author.id, 10)
       elif personjob == 4:
         await message.channel.trigger_typing()
         activities = ["Coding away","I code python","discord.py discord.js","Type this to make a new discord bot"]
         act = random.choice(activities)
         await message.channel.send(f"Type the following phrase into the chat:\n\n**{act}**")
         channel = message.channel
         def check(m):
              return m.content.lower() == act.lower() and m.channel == channel and m.author == message.author
         msg = await bot.wait_for('message', check=check)
         praises=["GFY","Good for you","congrats",":computer: nIcE","You get a promotion","Good job","New pixel phone thanks to you"]
         praise = random.choice(praises)
         ytdl = ["",'','',"Use aga!changejob to change your job","Use aga!changejob to change your job"]
         people=["Larry Page","Sundar Pichai","Sergey Brin","Susan Wojcicki "]
         person = random.choice(people)
         ll = random.choice(ytdl)
         await message.channel.send(f'**{person}:** {praise}\n\nYou got `500` ADB coins for working!\n\n{ll}')
         addcredits(message.author.id, 500)
         addexp(message.author.id, 10) 
      
#Search up solo learning for python
      
               #sg = bot.wait_for('message', check=check)

    try:
          allowedguilds=[443530263637655554,695027267948249218]
          if message.channel.guild.id in allowedguilds and message.author.id != 627003024925261866:
                if rareevent1 != True:
                      rareevent = True
                      will = random.randint(1,100)
                      if will == 5:
                            acts =['hithere','hehe hehe hehehhehehe', 'client.on("message", msg => { if(msg.author.id != client.user.id && msg.content.indexOf("hehe") > -1) msg.channel.send("hehe") });']
                            act = random.choice(acts)
                            hi = await message.channel.send(f"A rare event occured! Whoever typed the last message has to type \n `{act}` in 10 seconds before they lose 9999 ADB coins!")
          #await hi.edit(content="Send!")
                            
                            channel = message.channel
                            author = message.author
                            def check(m):
                                 return m.content.lower() == act.lower() and m.channel == channel and m.author == author
                            try:
                                 msg = await bot.wait_for('message', check=check, timeout = 10)
                                 await message.channel.send(f":white_check_mark: <@{message.author.id}> **won** `9999 ADB coins` instead of losing because they completed in time! :white_check_mark:")
                                 addcredits(message.author.id, 9999)
                            except asyncio.TimeoutError:
                                 await hi.edit(content=":x:You failed:x:")
                                 await message.channel.send(f"<@{message.author.id}> **lost** `9999 ADB coins` because they didn't type `{act}` in time :-(")
                                 checkforprofile(message.author.id)
                                 addcredits(message.author.id, -9999) 
                                 rareevent = False 
                elif rareevent1 == True:
                     pass
    except Exception as e:
      print(e)



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
@bot.command()
async def changejob(ctx):
  await ctx.send(f"""
**JOB OPTIONS FOR {ctx.author.name}**
1. **YouTuber**
2. **Chef**
3. **Google Worker**
4. **Discord Bot Dev**
**Type in the option you want (either the number or the full name)**
""")
	
  try:
    author = ctx.author
    def check(m):
		    return m.author == author
    response = await bot.wait_for('message', timeout = 180.0, check=check)
    contents = response.content.split(" ") #contents is a list type 
    print(response.content)
    print(contents)
    
    for word in contents:
      #print(response)
    	print(word)
    	if "chef" == word.lower() or "2" == word.lower():
    		  jobchange(ctx.author.id, 2)
    		  await ctx.send(f"Succesfully changed {ctx.author.name}'s job to **Chef**")
    		  break
    	elif "youtuber" == word.lower() or "1" == word.lower():
    		  jobchange(ctx.author.id, 1)
    		  await ctx.send(f"Succesfully changed {ctx.author.name}'s job to **YouTuber**")
    		  break
          
    	elif "google" == word.lower() or "3" == word.lower() or "worker" == word.lower():
    		  jobchange(ctx.author.id, 3)
    		  await ctx.send(f"Succesfully changed {ctx.author.name}'s job to **Google Worker**")
    		  break
    	elif "discord" == word.lower() or "4" == word.lower() or "bot" == word.lower() or "dev" == word.lower():
	    	  jobchange(ctx.author.id, 4)
	    	  await ctx.send(f"Succesfully changed {ctx.author.name}'s job to **Discord Bot Dev**")
	    	  break
          
    	else :
          if str(response).lower().endswith == word.lower():
            #await ctx.send(f"Invalid option -- the bot could not detect a job option in the sentence: {contents}")
            await ctx.send(f"Invalid option! Could not find valid option in your message. Try again!")
          else :
            print("HI")
          
      
      
  
  except asyncio.TimeoutError:
    pass
@bot.command()
@discord.ext.commands.is_owner()
async def kill(ctx):
  await ctx.send("Bye bye")
  await bot.logout()
@bot.command()
@discord.ext.commands.is_owner()
async def logout(ctx):
  await ctx.send("Bye bye")
  await bot.logout()
@bot.command()
@discord.ext.commands.is_owner()
async def protest(ctx,channel:discord.TextChannel=702245299825016902, content:str="We want our perms back.\nWe demand rights!\nBring back Hithere#1!"):
  await ctx.send("Protesting!")
  print(content)
  theotheramazingchannel = bot.get_channel(channel.id)
  hi = True
  content=content.replace("_"," ")
  content=content.replace()
  while True:
    await asyncio.sleep(2)
    await theotheramazingchannel.send(f"{content}")
@bot.command()
async def testt(ctx):
  #test to change an embed for new help menu
  embed1 = discord.Embed(title="1")
  embed2 = discord.Embed(title="2")
  msg = await ctx.send(embed=embed1)
  await asyncio.sleep(3)
  await msg.edit(embed=embed2)
@bot.command()
async def beg(ctx):
  ct = time()
  user = "userid_"+str(ctx.author.id)
  checkforprofile(ctx.author.id)
  with open("time.json",mode="r") as lt:
    t = json.load(lt)
    pt = t[user]["begtime"]
    if ct-pt >= 60:
      await ctx.message.channel.trigger_typing()
      checkforprofile(ctx.message.author.id)
      addexp(ctx.author.id, 25)
      m=random.randint(1,78)
      msg=["**Lil Mayo:** Be gone, THOT!",f"**Ur mom** donated {m} ADB coins to you"]
      addcredits(ctx.author.id, m)
      await ctx.send(random.choice(msg))
      with open("time.json",mode='w') as lt:
                t[user]["begtime"] = ((t[user]["begtime"] - pt) + ct)
                json.dump(t,lt)
    else: 
      
      l = ct-pt
      poop = 60-l
      stool = strftime("%S Seconds", gmtime(poop))
      await ctx.send(f"You have to wait **{stool}** seconds before you can use this command again")
      


@bot.command()
async def leaders(ctx, page=1):
  #IDK what to do now
  # ok so what do you want to make a ledaderboard for
  # so you know Chocolate the bot, right?
  #I want a leaderboard like that that shows the exp and the coins
  # What is chocalatet he bot
  # Ok you know coffee? The bot...
  # Oh the cafe bot
  # ok yea see the ~leaders command
  # I haven't been on it in such a long time... I'll go see what the leaderboard looks like
  # .O. its pretty complicated | ok. thanks
  # which servers is this bot o
  # no like what servers is this bot on
  # oh. Still the replit server. prefix is aga! | thanks in advance ur helping me out big time :-)
  #Also, there is a file called gp.json. That is what the info for exp and coins is on.
  embed = discord.Embed(title='Leaderboard', description='breh read the title') # np i like helping people owo
  with  open('gp.json', 'r') as f:
    content = json.load(f)
  #await ctx.send(f'raw data={content}') # yeah im back lol
  
  print(content)
  credits = []
  for items in content: 
    credits.append(content[items]['credits'])
  credits.sort(reverse=True)
  textToPrint = []
  i = 1
  for items in credits: # aight actually gtg bye
    print(items)
    for stuff in content:
      
      if content[stuff]['credits'] == items:
        id = stuff[7:] # uh oh
        user = bot.get_user(id=int(id))
        textToPrint.append(f'User with id {id} has {items} credits, and {content[stuff]["exp"]} exp') 
        #textToPrint.append(f'User with id {username.name} has {items} credits, and {content[stuff]["exp"]} exp') 
        if i > 10:
          break
        i+=1
        print(i)
  print(textToPrint)
  textToPrint = textToPrint[:10] # get the top ten leaders
  i = 1
  for items in textToPrint:
    embed.add_field(name=f'#{i}', value=items, inline=False)
    i+=1
  
  await ctx.send(content=None, embed=embed)
@bot.command()
async def test(ctx):
  with  open('items.json', 'r') as i:
    content = json.load(i)
  
  await ctx.send(content=content)
  credits=discord.Embed(color=0xFFFFFF)
  #credits = []
  for item in content: 
    credits.add_field(name=content["name"],value="------------------------------",inline=True)
  await ctx.send(embed=credits)
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
            ##############################  #########################################
            addcredits(ctx.message.author.id, 500)
            daily = discord.Embed(Title="Daily ADB Coins :tada:", color=0xd4af37)
            daily.add_field(name="Daily ADB Coins :tada:", value="You got **500** ADB Coins!")
            await ctx.send(embed=daily)
            #t[user]["dailytime"] = (t[user]["dailytime"] - pt) + ct
            with open("time.json",mode='w') as lt:
                t[user]["dailytime"] = ((t[user]["dailytime"] - pt) + ct)
                json.dump(t,lt)
        elif ct-pt < (24*60*60):
            l = ct-pt
            poop = 86400-l
            stool = strftime("%H Hours, %M Minutes, and %S Seconds", gmtime(poop))
            await ctx.send("Sorry, but you have to wait **"+str(stool)+ "** before you can use this command again.")
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
async def loot(ctx):
  emoji = '\U0001F44D'
# or '\U0001f44d' or '👍'
  #await ctx.message.add_reaction(emoji)
  await ctx.message.channel.trigger_typing()
  loot_c = random.randint(0,25)
  ####################################################
  checkforprofile(ctx.message.author.id)
  addexp(ctx.message.author.id, 5)
#######################################################################
  addcredits(ctx.message.author.id, loot_c)
  loot = discord.Embed(color = 0x008000)
  loot.add_field(name="Looting :mag:\n--------------------", value ="You got **" + str(loot_c) + "** ADB Coins!")
  botmes = await ctx.send(embed=loot)
  await botmes.add_reaction(emoji)
@bot.command()
async def inventory(ctx, person:discord.Member=None):
  inv = " ";
  if person != None:

    user = "userid_" + str(person.id)
    checkforprofile(person.id)
    inventory = discord.Embed(title = str(person.name)+"\'s inventory :briefcase:\n",color = random.randint(0x000000,0xFFFFFF))
    inventory.set_thumbnail(url=person.avatar_url)
    
  else:
    user = "userid_"+str(ctx.author.id)
    checkforprofile(ctx.author.id)
    person = ctx.author.id
    inventory = discord.Embed(title = str(ctx.author.name)+"\'s inventory :briefcase:\n",color = random.randint(0x000000,0xFFFFFF))
    inventory.set_thumbnail(url=ctx.author.avatar_url)
    
  await ctx.message.channel.trigger_typing()
  inv = " ";
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
  #await ctx.send("<@"+str(person)+">" + "\'s inventory :briefcase:")
  await ctx.send(embed = inventory)

@bot.command()
async def inv(ctx, person:discord.Member=None):
  inv = " ";
  if person != None:

    user = "userid_" + str(person.id)
    checkforprofile(person.id)
    inventory = discord.Embed(title = str(person.name)+"\'s inventory :briefcase:\n",color = random.randint(0x000000,0xFFFFFF))
    inventory.set_thumbnail(url=person.avatar_url)
    
  else:
    user = "userid_"+str(ctx.author.id)
    checkforprofile(ctx.author.id)
    person = ctx.author.id
    inventory = discord.Embed(title = str(ctx.author.name)+"\'s inventory :briefcase:\n",color = random.randint(0x000000,0xFFFFFF))
    inventory.set_thumbnail(url=ctx.author.avatar_url)
    
  await ctx.message.channel.trigger_typing()
  inv = " ";
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
  #await ctx.send("<@"+str(person)+">" + "\'s inventory :briefcase:")
  await ctx.send(embed = inventory)




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
    embed.add_field(name=":arrow_down:PRESS IT NOW!!!!!:arrow_down:", value="[------Click To Invite!!------](https://discordapp.com/api/oauth2/authorize?client_id=627003024925261866&permissions=2147483127&scope=bot)", inline = False)
    embed.add_field(name=":arrow_down:THIS FOR THE SERVER!!!!!:arrow_down:", value="[------Click To Join!!------](https://discord.gg/dPFrRkE)")
    await ctx.send(embed=embed)
#    print(str(message.author)+' just used aga!invite without trouble')











@bot.command(pass_context = True)
async def servers(ctx):
    
    await ctx.send("I am in:\n" + f'{str(len(bot.guilds))}'+' servers.')
   # guilds = await bot.fetch_guilds(limit=150).flatten()
   # await ctx.send('Here is the list:\n'+str(guilds))
    #await ctx.send("Here\'s a list:\n"+str(ljames))
    await ctx.send("Here\'s a list:\n*note: it might take a bit of time to list all of them*\n\n\n\n")
    async for guild in bot.fetch_guilds(limit=150):
      await ctx.send(guild.name)

 
@bot.command
async def rules(ctx):
    await ctx.send("""1. DO NOT swear, or do anything else in the "BAD" section of chat
2. DON'T try to hack any of the bots
3. Do not spam for any roles and alll that.
4. Don't hack""")
#@bot.command(pass_context=True)





@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,reason=None):
    await member.kick(reason=reason)
    await member.channel.send("<@"+discord.Member.id+"> was kicked. \n Reason: "+str(reason))
    channel = bot.get_channel(627286906995998740)
    await channel.send("\n \n "+str(ctx.message.author)+" banned "+str(member)+". \n **Reason:** "+str(reason)+("\n\n **In the Server:** ")+str(ctx.message.guild))
    await ctx.send('Kicked '+str(member)+ ' reason: '+str(reason))

@kick.error
async def kick_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Something went wrong :-(")
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    print(str(member)+" was banned. \n Reason: "+str(reason))
    log = bot.get_channel(627286906995998740)
    author=str(ctx.message.author)
    member=str(member)
    reason=str(reason)
    guild=str(ctx.message.guild)
    ban=discord.Embed(title=f"\n \n{author} banned {member}. \n **Reason:** {reason}\n\n **In the Server:** {guild}",color=0x36393F)
    #ban.set_thumbnail(url=member.avatar_url)
    await log.send(embed=ban)

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
#@ban.error
#async def ban_error(ctx, error):
#    if isinstance(error, commands.BadArgument):
#        await ctx.send('That person is not on this server.')
#    elif isinstance(error, commands.MissingPermissions):
#        await ctx.send("Ya don't have permission to do that. You tried, you failed")
#    elif isinstance(error, commands.MissingRequiredArgument):
#       await ctx.send("You didn't specify a person.")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('That person is either not banned or is not on **this server**')
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
@bot.command()
async def meme(ctx):
  images=["https://preview.redd.it/h7azaxmxkls41.jpg?width=640&crop=smart&auto=webp&s=350a8b45c98d1b1d97fb231a3e6289f1b56abd88","https://media.discordapp.net/attachments/449074874305085440/657707584408780820/image0.gif","https://media.discordapp.net/attachments/449074874305085440/644329209249923102/ic99zf6w2bq11.png","https://i.imgur.com/mjV6mef.jpg","https://i.imgur.com/MGqLmRX.jpg","https://i.imgur.com/4Cpc6r7.jpg","https://i.imgur.com/1jYAPVE.jpg","https://i.imgur.com/awwT1gC.jpg","https://i.imgur.com/qs7ktAq.jpg","https://i.imgur.com/0Xrh1ez.jpg","https://i.imgur.com/l95tZ03.jpg","https://i.imgur.com/fEUfpBF.jpg","https://i.imgur.com/qwbqgAk.jpg","https://i.imgur.com/fiWvPce.jpg","https://i.imgur.com/DxRrzC3.jpg","https://media.discordapp.net/attachments/552981468188770325/642147647737823242/wf3zwhmnkwv31.jpg","https://media.discordapp.net/attachments/552981468188770325/642147627701633065/ivgo1q7et8u31.jpg","https://media.discordapp.net/attachments/552981468188770325/642147588568645672/453ni0np34u31.jpg","https://i.imgur.com/jp6VvDf.jpg","https://preview.redd.it/f2dhulcckgx31.gif?width=640&format=mp4&s=8497585abc236bceee984868a6b8d21df89eae9d","https://i.redd.it/wvbvqa91mfx31.jpg","https://preview.redd.it/n8lz64fpmgx31.jpg?width=640&crop=smart&auto=webp&s=1a0cbfa35d1bad987ac1a56d9f7be81884581dac","https://preview.redd.it/xi4eeut8bgx31.jpg?width=640&crop=smart&auto=webp&s=ef7177927db0b3ae652addfbdd8640767c8fc1d5","https://preview.redd.it/2eclj4o68gx31.jpg?width=640&crop=smart&auto=webp&s=2af8d8360dc822166a09618e86a1bd01a133092c","https://i.imgur.com/4hDgKBE.jpg","https://i.imgur.com/jyIbNRL.jpg","https://i.imgur.com/ghDjbxC.jpg","https://i.imgur.com/LagNdVE.jpg","https://i.imgur.com/VSs0Xd1.jpg","https://i.imgur.com/Ch7LVqz.jpg","https://i.imgur.com/71mNkS1.jpg","https://i.imgur.com/oQJWntF.jpg","https://i.imgur.com/5OSz2nh.jpg","https://i.imgur.com/a0HeDHN.jpg","https://i.imgur.com/F7InAno.png","https://i.imgur.com/fUmRTP1.png","https://i.imgur.com/uXS4Obu.jpg","https://i.imgur.com/NGe7StT.jpg","https://i.imgur.com/hSN9aB3.jpg","https://media.discordapp.net/attachments/449074874305085440/642913941881749504/image0.jpg","https://images-ext-1.discordapp.net/external/MzJ3Eq8Gv_5JORAi-f4pQaRX4tzItaom9RMLmjCI_P0/https/i.redd.it/m5ysyjorivx31.jpg?width=375&height=300","https://images-ext-2.discordapp.net/external/cJ2XHiNgtFFGhBZ7cEgAwfmFNnc08wle2AVHmRciOF8/https/i.redd.it/5ktd1pop3wx31.jpg?width=174&height=300","https://images-ext-1.discordapp.net/external/50cLsLw9BAzSFrbj4BLJD2yDAbgSpkvGRWwu8sUdPqA/https/i.redd.it/inkjtflqhrx31.jpg?width=256&height=300","https://images-ext-2.discordapp.net/external/VTp-gcKWys-RTzAY5rPhtJOSwxh9S4LfjTNStBfZOwE/https/i.redd.it/pq7aryvi8qx31.jpg?width=226&height=301","https://images-ext-1.discordapp.net/external/UBkxx0t48YUKo43aiaXHe4fnWY9CZEbaYZ1I_BR-Q88/https/i.redd.it/9bsawd8bzux31.jpg?width=218&height=301","https://images-ext-1.discordapp.net/external/qbwiqSR9plNXtffglbcHykKobHFbXu4b_wOxfztzkzs/https/i.redd.it/476dlzikprx31.jpg?width=329&height=521","https://images-ext-1.discordapp.net/external/YniD-Acv2F-g89H8LjN-DNz-PS22ZteIInVIbAxWzzA/https/i.redd.it/eh8qlgna2sx31.jpg?width=257&height=300","https://images-ext-1.discordapp.net/external/jG4nSdV2tO-uRG6iSPJQLJUbd736hE17raz-LKkw7lw/https/i.imgur.com/tpuwvSA.jpg?width=371&height=520","https://images-ext-2.discordapp.net/external/2Rn--ISiooEGI7z9whaHfGYD0y8aVhgNurDG6--qll0/https/i.redd.it/wfdox42nwsx31.png?width=504&height=521"]
  url=random.choice(images)
  meme = discord.Embed(description=f"[Meme]({url})",color = random.randint(0x000000,0xFFFFFF))
  meme.set_image(url=url)
 # url=random.choice(images)
  await ctx.send(embed = meme) 
  
 
@bot.command()
async def sorry(ctx):
  async with aiohttp.ClientSession() as session:
        async with session.get('https://api.tenor.com/v1/search?q=sorry&key=BY3WL2700Z5V&limit=20') as r:
            if r.status == 200:
                js = await r.json()
                number = random.randint(0, 19)
                zero = 0
                print(number)
                link = 1

            embed = discord.Embed(color = discord.Color(random.randint(0x000000, 0xFFFFFF)), title= f"sorry")
            #embed.set_image(js['results'][int(number)]['media'][0]['gif']['url'])
            embed.set_image(js[int(number)]['gif']['url'])
            await ctx.send(embed=embed)
            await ctx.send(js["results"][1]['url']["media[0]gif.url"])

@bot.command()
async def search(ctx, person:discord.Member=None):
  #await ctx.send("Sorry this is under maintenance!")
  if person == None:
    person = ctx.author.id
  else:
    person = person.id
  lll=["cookie","aged_cheese","phone","admin_badge","diamond","computer","loot_box","charger","admin_badge","pickaxe","item_name","nothing","nothing","nothing","nothing","nothing"]
  
  l=random.randint(1,5)
  item=random.choice(lll)
  if item == 'nothing':
    message=["You got nothing!","Be gone, thot!","Oh NONONONONO NOTHING 4 U","You got nothing!!!","Ya didn't get anything!","BE GONE, THOT!"]
    await ctx.send(str(random.choice(message)))
  else:
    additem(person, item, l)
    await ctx.send("<@"+str(person)+"> found "+str(l)+" "+str(item)+"(s)!")#'''
@bot.command()
async def updatestatus(ctx):
   addexp(ctx.message.author.id, 15)
   await bot.change_presence(activity=discord.Game(name=open("status.txt", "r").read().format(str(len(bot.guilds))), type=1))
   await ctx.send("Status Updated!")
@bot.command()
async def hack(ctx, user:discord.Member):
    msg = await ctx.send(f"Hacking {user.name}       <a:loadinggif:649364279782408215>")
    await asyncio.sleep(1.5)
    await msg.edit(content="Connecting to slave devices... <a:loadinggif:649364279782408215>")  
    await asyncio.sleep(1.5) 
    await msg.edit(content=f"Connecting to slave devices... <a:loadinggif:649364279782408215>\n\nConnecting to satellites <a:loadinggif:649364279782408215> \n\nConnecting to www.hackweb.net... <a:loadinggif:649364279782408215>")  
    await asyncio.sleep(2)
    await msg.edit(content=f"Connected to slave devices... :white_check_mark:\n\nConnected to satellites :white_check_mark: \n\nConnecting to www.hackweb.net... <a:loadinggif:649364279782408215>")  
    await asyncio.sleep(1.7)
    await msg.edit(content=f"Connected to slave devices... :white_check_mark:\n\nConnected to satellites :white_check_mark: \n\nConnected to www.hackweb.net... :white_check_mark:") 
    await asyncio.sleep(1.3)
    await msg.edit(content=f"Sending hack code to satellite... <a:loadinggif:649364279782408215>") 
    await asyncio.sleep(2)
    await msg.edit(content=f"Satellite has received hack code . :white_check_mark:\n\nHacking the satellite using code    <a:loadinggif:649364279782408215>") 

#@bot.event
#@discord.ext.commands.has_role(bot.get_role(443945526442983425))
#async def on_raw_reaction_add(ctx):
#  if ctx.reaction.guild.id == 443530263637655554:
#    rolex = ctx.guild.get_role(443945526442983425)
#    author:discord.Member = ctx.author
#    await author.add_roles(rolex, reason=None, atomic = None)
#    await author.send("You got verified in {ctx.guild.name} by adding a reaction and proving you're not a bot!")
#    print(f"reaction role verified : {author}")
@bot.command()
@discord.ext.commands.has_permissions(manage_roles=True)
async def verify(ctx, member:discord.Member):
  rolex = ctx.guild.get_role(443945526442983425)
  await member.add_roles(rolex, reason=None, atomic=True)
  await ctx.send(f"Succesfully gave verified role to <@{str(member.id)}>!")
  print(f"Verified {member}")
  await member.send(f"Hey! Just sayin, {ctx.author} verified you in {ctx.channel.guild.name}")
@bot.command()
@discord.ext.commands.has_permissions(manage_roles=True)
async def mod(ctx, member:discord.Member):
  rolex = ctx.guild.get_role(625389784520720384)
  await member.add_roles(rolex, reason=None, atomic=True)
  await ctx.send(f"Succesfully gave Moderator role to <@{str(member.id)}>!")
  print(f"Mod {member}")
  await member.send(f"Hey! Just sayin, {ctx.author} gave you the Moderator role in {ctx.channel.guild.name}")

@bot.command(pass_context=True)
async def get(ctx, message):
  await ctx.send("+Bal")
  await asyncio.sleep(4)
  await ctx.send(f"+Buy 5 {message}")
bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
        help1 = discord.Embed(title="AwesomeAg Da Bot", description="A bot hosted on repl.it and made by AwesomeAg. \n List of commands and descriptions are:",  color=0x0000FF)
        help1.add_field(name = '1', value="||aga!add X Y|| : Gives the addition of **X** and **Y**")
        help1.add_field(name = '2', value="||aga!multiply X Y|| : Gives the multiplication of **X** and **Y**")
        help1.add_field(name = '3', value="||aga!greet|| : Gives a nice greet message")
        help1.add_field(name = '4', value="||aga!cat|| : Gives a cute cat gif to lighten up the mood.")
        help1.add_field(name = '5', value="||aga!info|| : Gives a little info about the bot")
        help1.add_field(name = '6', value="||aga!help|| : Gives this message")
        help1.add_field(name = '7', value="||aga!dog|| : Gives a funny dog GIF just in case you like them better than   cats")
        help1.add_field(name = '8', value="||aga!invite|| : Gives the invite link so you can invite ADB to another server.")
        help1.add_field(name = 'Page 1', value = "Type aga!help2 for the next page.")
        help2 = discord.Embed(title="AwesomeAg Da Bot", description="The Best. \n More commands:",color=0x0000FF)
        help2.add_field(name="9",value="||aga!exp|| : Shows your current exp.")
        help2.add_field(name="10",value="||aga!funny|| : A funny gif to lighten your mood")
        help2.add_field(name="11",value="||aga!spam|| : Well, your page will be filled up and you might lag...")
        help2.add_field(name="12",value="||aga!kick <@user>|| : If you have the perms, it will kick someone...")
        help2.add_field(name="13",value="||aga!ban <@user>|| : If you have the perms, it will ban someone...")
        help2.add_field(name="14",value="||aga!icon|| : Shows the current icon for AwesomeAgDaBot")
        help2.add_field(name='Go to aga!help3 for more things!',value="-------------------------")
        help3 = discord.Embed(Title="Help", description = "Page 3", color=random.randint(0x000000,0xFFFFFF))
        help3.add_field(name="15", value="||aga!daily|| : Gives you 500 daily ADB coins with 24 hour cooldown limit")
        help3.add_field(name="16",value="||aga!loot|| : Gives you a random amount of ADB coins")
        help3.add_field(name="17", value="||aga!search <@user>||: The user part is optional- will find things for you or the user you put in")
        help3.add_field(name="18", value="||aga!inventory <@user>|| : once again, the user is optional, and you can see you or another persons inventory")
        help3.add_field(name="19", value="||aga!mine|| : Use a pickaxe to get money")
        help3.add_field(name="20", value="||aga!use <item>|| : Uses an item if you have it- currently supported items:\n`cheese`/`aged_cheese`/`aged cheese`, `cookie`, `pickaxe`")
        help3.add_field(name="21", value="||aga!shop|| : shows exchange rate for items that can be found in your inventory")
        help3.add_field(name="22",value="||aga!buy <item>|| : buys an item-exchange rate in aga!shop *note: not all items are supported yet*")
        help3.add_field(name="23",value="||aga!sell <item>|| : sells an item-exchange rate in aga!shop *note: not all items are supported yet*")
        help3.add_field(name="24",value="||aga!meme|| : Gets random meme; use ||aga!meme reccomondation|| to suggest meme(s)")
        help3.add_field(name="25", value="||aga!work|| : Use to work and get money.")
        help3.add_field(name="26",value="||aga!changejob|| : Changes your job")
        help3.add_field(name="27", value="||aga!members<limit>|| : Lists all members in the guild. Limit default as none, but you can make it so you don't spam.")
        helppage = 1
        channel = ctx.message.channel
        botm = await ctx.send(embed=help1)
        await botm.add_reaction('1️⃣')
        await botm.add_reaction('2️⃣')
        await botm.add_reaction('3️⃣')
        
        kealive = 1
        while kealive < 600:
          def check(reaction, user):
              return user == ctx.message.author#and str(reaction.emoji) == ''

          try:
              reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=check)
              if str(reaction.emoji) == '1️⃣':
                await botm.edit(embed=help1)
                helppage = 1
                
             
              if str(reaction.emoji) == '2️⃣':
                await botm.edit(embed = help2)
                helppage = 2
              if str(reaction.emoji) == '3️⃣':
                await botm.edit(embed = help3)
                helppage = 3
            
            
          except asyncio.TimeoutError:
              #await channel.send('👎')
              break
          else:
              #await botm.edit(content='👍')
              pass
          kealive = kealive+5
@help.error
async def help_error(error, ctx):
  await ctx.send("Internal error, please try again in a second.")
@bot.command(pass_context=True)
async def create_invite(ctx):
  
  await ctx.send("For the server or the channel?")
  #await ctx.send("<:gachiWoke:482272059506950144>")
  def check(m):
    return m.author == ctx.author and m.channel == ctx.channel
  response = await bot.wait_for('message',check=check,timeout=690)
  response = str(response.content)
  if "guild" in response.lower() or "server" in response.lower():
    link = await ctx.channel.create_invite(max_age = 300)
    await ctx.send(f"Too bad -- it's for the channel.\n\n")
    stall = await ctx.send("Loading your invite... <a:loadinggif:649364279782408215>")
    
    await asyncio.sleep(4)
    #link = await bot.create_invite()
    await stall.edit(content=f"Instant invite to **{ctx.message.channel.guild}** created :white_check_mark: \n{link}")
  elif "channel" in response.lower():
    link = await ctx.channel.create_invite(max_age = 300)
    await ctx.send(f"Instant invite to **{ctx.message.channel.guild} {ctx.message.channel}** created :white_check_mark:\n {link}")
  else:
    await ctx.send(":x: INVALID OPTION!")

@bot.command(pass_context=True)
@discord.ext.commands.is_owner()
async def python(ctx, code):
  print(None)
  msg = await ctx.send("Running your command... <a:loadinggif:649364279782408215>")
  try:
    #coded = exec(code)
    #code = code.replace('"',"'")
    try:
      exec(code)
     

      msg2 = await msg.edit(content=f"Your code output:\n```python\n{str(exec(code))}```\n")


    except discord.ext.commands.errors.UnexpectedQuoteError:
      await msg.edit(content="Please use single quotes and not double quotes!")

  except Exception as e:
    await msg.edit(content=f"Your code: ```python\n{code}```\n did not work. The exception raised was:\n```{e}```")
@bot.command()
@discord.ext.commands.is_owner()
async def awaken(ctx):
  changeoffline(False)
  await ctx.send("I am AWAKE")

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

@bot.command()
async def ping(ctx):
  start = d.timestamp(d.now())
    	# Gets the timestamp when the command was used
  msg = await ctx.send('Pinging')
    	# Sends a message to the user in the channel the message with the command was received.
    	# Notifies the user that pinging has started

  hi = (d.timestamp( d.now() ) - start ) * 1000
  hi = round(hi)
  await msg.edit(content=f'Pong!\n>>> *One message took about {hi} milliseconds.*')
  spam = 5
  while spam == 5:
    await msg.edit(content=f'Pong!\n>>> *One message took about {hi} milliseconds.*\n:ping_pong:')
    	# Ping completed and round-trip duration show in ms
    	# Since it takes a while to send the messages
    	# it will calculate how much time it takes to edit an message.
    	# It depends usually on your internet connection speed
	#return

@bot.command(pass_context=True)
async def info(ctx):
    num=random.randint(1,5)
    life = botonline
    bruh = strftime("%D", gmtime(life))
    bottonline = int(time()) - int(botonline)
    stool = strftime("%H Hours %M Minutes %S Seconds Ago", gmtime(bottonline))
    embed = discord.Embed(title="AwesomeAg Da Bot", description="The best bot ever, made by <@326497976040030208> \n Server Count: " + f'{len(bot.guilds)}\n\n** Last Restart Was On {bruh} --- {stool}**',color=0x0000FF)
    await ctx.send(embed=embed)
#    print(str(message.author)+' just used aga!info without trouble')
@bot.command(pass_context=True)
async def members(ctx, listlimit=99999999):
    listlimit = str(listlimit)
    listlimit = listlimit.replace("limit","")
    listlimit = listlimit.replace("=","")
    listlimit = listlimit.replace(" ","")
    try:
      listlimit = int(listlimit)
    except BadArgument:
      await ctx.send("Could not convert paramater `limit` to integer. Please try again with only number.")
    if listlimit == 99999999:
      limits = ""
    else:
      limits = f" (limit = {listlimit})"
    memberlist=f"**Members in {ctx.guild.name}{limits}:**\n\n"
    person = 1
    async for member in ctx.guild.fetch_members(limit=listlimit):
      if person == 1:
        memberlist=f"{memberlist}{member.name}"
      else:
        memberlist=f"{memberlist}, {member.name}"
      person = person+1
    try:
      await ctx.send(str(memberlist))
    except Exception:
      await ctx.send(f"Hey there, {ctx.author.name}! Looks like there are too many people in this server (list length = {len(memberlist)}), so Discords restrictions cannot let me type them all. Try adding a number like {random.randint(1,50)} after aga!members so you can see that many members.")


@bot.command(pass_context = True)
async def mail(ctx,member: discord.Member,mail):
    await ctx.send("Sent mail to <@"+str(member.id)+">!")
    await ctx.author.send("Succesfuly sent mail to "+str(member)+". \n\n Thanks for using ADB express!")
    await member.send("You have mail!\nFrom: <@" + str(ctx.author.id)+f"> \nTo: <@{member.id}>\nContents:\n" + str(mail) + "\n\n\n*Thanks for choosing ADB express!*")
@mail.error
async def mail_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
      await ctx.send("Sorry, couldn't get that person. Try again or don't use a DM server.")
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Look again... did you forget something?")
@bot.command()
async def giveaway(ctx):
  await ctx.send("Give a channel ID to start the giveaway in!")
  def check(m):
    return m.author.id == ctx.author.id and m.channel == ctx.message.channel
  channeel = await bot.wait_for("message",check=check)
  await ctx.send(":+1: got it!\n\nNow please give me how long it will last in seconds\n\nQuick help key: 1 minute = 60 Seconds\n\n1 hour = 3600 Seconds\n\n 1 day = 86400 Seconds.\n\nGo ahead and take your time and use a calculator.")
  duration:int = await bot.wait_for("message" , check=check)
  await ctx.send(f":+1: Got it for {duration.content} seconds\nNow please send the maximum amount of possible winners")
  poss:int = await bot.wait_for("message",check=check)
  await ctx.send(f":+1: Set for maximum of {poss.content} winners!\nLastly, please send me the prize for the giveaway")
  prize = await bot.wait_for("message",check=check)
  
#async def giveaway(ctx, channel:discord.TextChannel, messagee:discord.Message, duration:int, poss:int, prize:str):
  await ctx.send(f"**Okay! Set a giveaway with {poss.content} winners, that lasts for {duration.content} seconds, and  the prize is: {prize.content}**\n\nReact with thumbsup on the message I sent to enter")
  end = int(time()) + int(duration.content)
  timme = strftime("%H:%M", gmtime(end))
  print(f"test: {timme}")
  givveaway = discord.Embed(title = "Active Giveaway!",description=f"**Server: {ctx.message.guild}**",color = 0xB19CD9)
  #channel = channeel.content
  #chaneeel = bot.get_channel(channel.id)
  cchannel = channeel.content
  channell = int(cchannel)
  channel = bot.get_channel(channell)
  mesagee = await channel.send("test")
  
  await mesagee.add_reaction('👍')
  emoji = '👍'
  await asyncio.sleep(int(duration.content))
  users = await mesagee.reactions.users().flatten()
  # users is now a list of User...
  #chooses max amount and sends the message declaring that they won
  allReactions = message.reactions
  async for reaction in allReactions:
		#print(str(reaction.emoji))
    if str(reaction.emoji) == emoji:
      thisKindOfReactions = await bot.get_reaction_users(reaction)
      for i in range(pos):
        winner = random.choice(users)
        await channel.send('{} has won the raffle.'.format(winner))

@bot.command(pass_context=True)
async def icon(ctx):
    #await ctx.send("My current icon:")
    #await ctx.send(file=discord.File('ADBHalloweenIcon.jpg'))
    await ctx.send(f"Sorry, {ctx.author.name}, but this command is currently unavailible right now. Please try another time!")
@bot.command()
async def youtube(ctx,*,search,amount=0):

  query_string = urllib.parse.urlencode({
    'search_query':search
  })
  htm_content = urllib.request.urlopen('https://www.youtube.com/results?'+str(query_string)
  )
  search_results=re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
  await ctx.send("https://youtube.com/watch?v="+search_results[int(amount)])

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






#why am I streamiinggggg?




@bot.command(pass_context=True)
async def helpp(ctx):
    embed = discord.Embed(title="AwesomeAg Da Bot", description="The best bot around, buddies with Dummy. I will boss you around. \n click on the black things to see the command. \n List of commands and descriptions are:", color=0x0000FF)
    embed.add_field(name = '1', value="||aga!add X Y|| : Gives the addition of **X** and **Y**")
    embed.add_field(name = '2', value="||aga!multiply X Y|| : Gives the multiplication of **X** and **Y**")
    embed.add_field(name = '3', value="||aga!greet|| : Gives a nice greet message")
    embed.add_field(name = '4', value="||aga!cat|| : Gives a cute cat gif to lighten up the mood.")
    embed.add_field(name = '5', value="||aga!info|| : Gives a little info about the bot")
    embed.add_field(name = '6', value="||aga!help|| : Gives this message")
    embed.add_field(name = '7', value="||aga!dog|| : Gives a funny dog GIF just in case you like them better than cats")
    embed.add_field(name = '8', value="||aga!invite|| : Gives the invite link so you can invite ADB to another server.")
    embed.add_field(name = 'Page 1', value = "Type aga!help2 for the next page.")
    await ctx.send(embed=embed)
    #print(str(message.author)+' just used aga!help without trouble')
@bot.command()
async def help2(ctx):
    embed = discord.Embed(title="AwesomeAg Da Bot", description="The Best. \n More commands:",color=0x0000FF)
    embed.add_field(name="9",value="||aga!worship|| : Will tell you who you should pray to and thank.")
    embed.add_field(name="10",value="||aga!funny|| : A funny gif to lighten your mood")
    embed.add_field(name="11",value="||aga!spam|| : Well, your page will be filled up and you might lag...")
    embed.add_field(name="12",value="||aga!kick <@user>|| : If you have the perms, it will kick someone...")
    embed.add_field(name="13",value="||aga!ban <@user>|| : If you have the perms, it will ban someone...")
    embed.add_field(name="14",value="||aga!icon|| : Shows the current icon for AwesomeAgDaBot")
    embed.add_field(name='Go to aga!help3 for more things!',value="-------------------------")
    


    await ctx.send(embed=embed)
@bot.command()
async def help3(ctx):
  help3 = discord.Embed(Title="Help", description = "Page 3", color=random.randint(0x000000,0xFFFFFF))
  help3.add_field(name="15", value="||aga!daily|| : Gives you 500 daily ADB coins with 24 hour cooldown limit")
  help3.add_field(name="16",value="||aga!loot|| : Gives you a random amount of ADB coins")
  help3.add_field(name="17", value="||aga!search <@user>||: The user part is optional- will find things for you or the user you put in")
  help3.add_field(name="18", value="||aga!inventory <@user>|| : once again, the user is optional, and you can see you or another persons inventory")
  help3.add_field(name="19", value="||aga!mine|| : Use a pickaxe to get money")
  help3.add_field(name="20", value="||aga!use <item>|| : Uses an item if you have it- currently supported items:\n`cheese`/`aged_cheese`/`aged cheese`, `cookie`, `pickaxe`")
  help3.add_field(name="21", value="||aga!shop|| : shows exchange rate for items that can be found in your inventory")
  help3.add_field(name="22",value="||aga!buy <item>|| : buys an item-exchange rate in aga!shop *note: not all items are supported yet*")
  help3.add_field(name="23",value="||aga!sell <item>|| : sells an item-exchange rate in aga!shop *note: not all items are supported yet*")
  help3.add_field(name="24",value="||aga!meme|| : Gets random meme; use ||aga!meme reccomondation|| to suggest meme(s)")
  help3.add_field(name="25", value="||aga!work|| : Use to work and get money.")
  help3.add_field(name="26",value="||aga!changejob|| : Changes your job")
  await ctx.send(embed=help3)

 
 

@bot.command()
async def sell(ctx, item=None, amount=1):
  checkforprofile(ctx.author.id)
  if item == None:
    wut = discord.Embed(color=0xFF0000)
    wut.add_field(name=":x: Error! :x:",value="You need to put an option such as `aga!sell cookie` or `aga!sell cookie 3`")
    await ctx.send(embed=wut)
    return "done"
  with open("items.json",mode="r") as i:
    items = json.load(i)
    if item.lower() == "cheese":
      newitem = "aged_cheese"
    if item.lower() == "admin":
      newitem = "admin_badge"
    else:
      newitem=item.lower()
    if item.lower() in items:
      sellprice = items[item]["sell"]
      emoji = items[item]["emoji"]
      if sellprice == None:
        sellfail = discord.Embed(color=0xFF0000)
        sellfail.add_field(name="Error :x:",value="You cannot sell that item.")
        await ctx.send(embed=sellfail)
        return "cannot sell"
      if checkforitem(ctx.author.id, newitem.lower()):
        item=item.lower()
        additem(ctx.author.id, newitem, -1*amount)
        addcredits(ctx.author.id, sellprice*amount)
        sold = discord.Embed(color=0x32CD32)
        sold.add_field(name=":briefcase: Item sold!", value=f"Sold `{amount}` x `{newitem}(s)` {emoji} for a total profit of: `${amount*sellprice}`")
        await ctx.send(embed=sold)
      else:
        sellfail = discord.Embed(color=0xFF0000)
        sellfail.add_field(name="Error :x:",value="You don't have that item!")
        await ctx.send(embed=sellfail)
    else:
      sellfail = discord.Embed(color=0xFF0000)
      sellfail.add_field(name="Error :x:",value="That item does not exist! Please use the key word like `admin` if you wanted to sell an admin badge.")
      await ctx.send(embed=sellfail)

@bot.command()
async def buy(ctx, item=None, amount=1):
  checkforprofile(ctx.author.id)
  if item == None:
    wut = discord.Embed(color=0xFF0000)
    wut.add_field(name=":x: Error! :x:",value="You need to put an option such as `aga!buy cookie` or `aga!buy cookie 3`")
    await ctx.send(embed=wut)
    return
  with open("gp.json",mode="r") as g:
    gp = json.load(g) 
    usercredits = gp[f"userid_{ctx.author.id}"]["credits"]
  with open("items.json",mode="r") as i:
    items = json.load(i)
    
    if item.lower() == "cheese":
      newitem = "aged_cheese"
    if item.lower() == "admin":
      newitem="admin_badge"
    else:
      newitem=item
    if item.lower() in items:
      buyprice = items[item]["buy"]
      price = buyprice
      emoji = items[item]["emoji"]
      if buyprice == None:
        sellfail = discord.Embed(color=0xFF0000)
        sellfail.add_field(name="Error :x:",value="That item cannot be bought!")
        await ctx.send(embed=sellfail)
      if usercredits>=amount*price:
        item=item.lower()
        additem(ctx.author.id, newitem, 1*amount)
        addcredits(ctx.author.id, -1*buyprice*amount)
        sold = discord.Embed(color=0x32CD32)
        sold.add_field(name=":briefcase: Item bought!", value=f"Bought `{amount}` x `{newitem}(s)` {emoji} for a total cost of: `${amount*buyprice}`")
        await ctx.send(embed=sold)
      else:
        sellfail = discord.Embed(color=0xFF0000)
        sellfail.add_field(name="Error :x:",value="You don't have that much money!")
        await ctx.send(embed=sellfail)
    else:
      sellfail = discord.Embed(color=0xFF0000)
      sellfail.add_field(name="Error :x:",value="That item does not exist! Please use the key word like `admin` if you wanted to buy an admin badge.")
      await ctx.send(embed=sellfail)



#@bot.command()
#async def worship(ctx):
#    await ctx.send("Worship the Creators \n Go and worship and thank the following people for merely existing: \n <@326497976040030208> \n <@429069454601879572> \n <@516325745820303382> \n <@627003024925261866>")
   # print(str(message.author)+' just used aga!worship without trouble')

@bot.command()
async def warns(ctx, member:discord.Member=None):
  if member==None:
    checkforprofilewarn(ctx.author.id,ctx.guild.id)
    normal=checkwarns(ctx.author.id, ctx.guild.id, "normal")
    major=checkwarns(ctx.author.id, ctx.guild.id, "major")
    minor=checkwarns(ctx.author.id, ctx.guild.id, "minor")
    warns = discord.Embed(title=f"{ctx.author.name}'s warns",color=0xFF0000)
    warns.add_field(name="Your major warns:",value=str(major),inline=False)
    warns.add_field(name="Your normal warns:",value=str(normal),inline=False)
    warns.add_field(name="Your minor warns:",value=str(minor),inline=False)
    await ctx.send(embed=warns)
  else:
    checkforprofilewarn(ctx.author.id,ctx.guild.id)
    normal=checkwarns(ctx.author.id, ctx.guild.id, "normal")
    minor=checkwarns(ctx.author.id, ctx.guild.id, "minor")
    major=checkwarns(ctx.author.id, ctx.guild.id, "major")
    warns=discord.Embed(title=f"{member.name}'s warns",color=0xFF0000)
    warns.add_field(name=f"{member.name}'s minor warns:",value=str(minor),inline=False)
    warns.add_field(name=f"{member.name}'s normal warns:",value=str(normal),inline=False)
    warns.add_field(name=f"{member.name}'s major warns:",value=str(major),inline=False)
    await ctx.send(embed=warns)
@bot.command()
@commands.has_permissions(kick_members=True)
async def removewarns(ctx, user:discord.Member, amount):
  await ctx.send("Which kind of warn do you want to remove?")
  def check(m):
    return m.author==ctx.author and m.channel == ctx.channel
  kind= await bot.wait_for("message",check=check, timeout=300)
  kind=kind.content
  warntypes=["minor","normal","major"]
  if kind.lower() in warntypes:
    checkforprofilewarn(user.id, ctx.guild.id)
    addwarns(user.id, ctx.guild.id, kind, 0-int(amount))
    success=discord.Embed(color=0x32cd32)
    success.add_field(name=":white_check_mark_: Success!",value=f"Successfully removed {amount} warns(s) from {user.name}")
    await ctx.send(embed=success)
  else:
    nope=discord.Embed(title=":x:Invalid option!",color=0xFF0000)
    nope.add_field(name="That does not seem to be an option.",value="Be sure to try `major`,`minor`, or `normal`",inline=False)
    await ctx.send(embed=nope)
@bot.command()
async def warndata(ctx):
  with open("warn.json",mode="r") as w:
    warn=json.load(w)
    await ctx.send(f"```json\n{warn}\n```")

@bot.command()
async def warnkey(ctx):
  warnkey=discord.Embed(title="Warn Key", description="The information of all the types od=f warns in one embed", color=random.randint(0x000000,0xFFFFFF))
  warnkey.add_field(name="minor warnings",value="Minor warnings should be used for things that slightly break a rule, or things that can be reversed. Such things would be minor swearing, or spam.",inline=True)
  warnkey.add_field(name="normal warnings",value="Normal warnings should be used for the same things as minor warns, but should be used in cases where it is repetetive. So instead of giving out a 3rd minor warning for the same reason, you should give a normal warning. If you can't decide what warning to use, use normal warning.",inline=True)
  warnkey.add_field(name="major warnings",value="Major warnings should be used in cases such as racial slurs, threats, hacking, or things that have a lasting impact on the server or on people. Major warnings should be though through before given to people because sometimes it's just too much, especially for servers who have auto kick enabled.",inline=True)
  warnkey.set_footer(text="Remember at the end, the choice is yours. Warns can be undone by using aga!removewarns",icon_url="https://cdn.discordapp.com/emojis/451912829142827008.png")
  await ctx.send(embed=warnkey)
@bot.command()
async def triggered(msgdata):
  message = msgdata['message']
  args=msgdata['args']
  client=msgdata['client']
  if len(args) == 0:
    userid = message.author.id
  else:
    try:
      print(args[0])
      userid=utilities.get_userid(args[0])
    except AssertionError:
      return await message.channel.send("Invalid User")
  async with message.channel.trigger_typing():
    async with aiohttp.ClientSession() as s:
      img_size = 128
      user = bot.get_user(userid)
      with io.BytesIO() as output:
        await user.avatar_url_as(static_format='png',size=img_sizw,).save(output)
        output.seek(0)
        img_bytes = output.getvalue()
    with concurrent.futures.ThreadPoolExecutor() as pool:
      img = await bot.loop.run_in_executor(pool, triggerfy, io.BytesIO(img_pytes))
      filename = f'triggered.gif'
      img_file = discord.File(fp=io.BytesIO(img), filename=filename)
      await message.channel.send(file=img_file)
@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user:discord.Member):
  await ctx.send(f"Give the reason to warn <@{user.id}>")
  def check(m):
    return m.author.id==ctx.author.id and m.channel==ctx.channel
  reason = await bot.wait_for('message', check=check, timeout=300)
  reason = reason.content
  await ctx.send("Would you like to give a minor, major, or normal warn? Enter only one word (normal, minor, or major). See `aga!warnkey` for the ranking of each.")
  warntype=await bot.wait_for('message', check=check, timeout=300)
  warn=warntype.content.lower()
  warntypes=["minor","major","normal"]
  if warn in warntypes:
    checkforprofilewarn(user.id,ctx.message.channel.guild.id)
    addwarns(user.id, ctx.message.channel.guild.id, warn,n=1)
    warned = discord.Embed(title=f"**Warned {user.name}**",color=0x32cd32)
    warned.add_field(name=f"{user.name} Has been given a warning",value=f"The reason given was", inline=True)
    warned.add_field(name=":",value=f"{reason}", inline=True)
    await ctx.send(embed=warned)
    #await ctx.send(f"Succesfully gave {user.name} a {warntype} warning. They have been notified that they were warned. Note: this warn only is active for this server.\nReason: {reason}")
    userwarn = discord.Embed(title="You've been warned!",color=0xFF0000)
    userwarn.add_field(name=f"{ctx.author.name} gave you a {warntype} warning",value="the server was {ctx.guild}{ctx.author.name} gave the reason for warning you: {reason}.")
    userwarn.add_field(name=" Please do not do this again or you may be kicked or banned.",value="If you think this is a mistake, contact a server admin and ask them to reverse it.",inline=False)
    userwarn.set_footer(icon_url="https://cdn.discordapp.com/emojis/451912829142827008")
    await user.send(embed=userwarn)
    #await user.send(f"Hey there! Just to let you know, you've been given a {warntype} warning in the server {ctx.guild.name}. This was given to you by <@{ctx.author.id}> and they gave a reason: {reason}. If you think this is an error, contact a server admin and they can reverse it.")
  else:
    await ctx.send(":x: Invalid option. See `aga!warnkey` for the kinds of warns and examples.")
  
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



# Start the server
keep_alive.keep_alive()

# Finally, login the bot
bot.run(os.getenv("TOKEN"))