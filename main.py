import discum
import time
import multiprocessing
import asyncio
import json
import random
import re
exitr=False
once=False
wbm=[12,16]
class bot:
  owoid=408785106942164992
  channel=None
  token=""
  if token=="":
    token=input("token: ")
  if channel==None:
    channel=input("channel ID: ")
  commands=[
    "owo hunt",
    "owo hunt",
    "owo battle"
    ]
  funcom=[
    "owo zoo",
    "owo money",
    "owo sell all",
    "owo cf 2",
    "owo sell uncommonweapons",
    "owo sell commonweapons",
    "owo sell epicweapons",
    "owo sell mythicweapons",
    "owo level",
    "owo lb all",
    "owo crate all",
    ]
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
client=discum.Client(token=bot.token, log=False)
def issuechecker():
  msgs=client.getMessages(str(bot.channel), num=10)
  msgs=json.loads(msgs.text)
  owodes=0
  for msgone in msgs:
    if msgone['author']['id']==str(bot.owoid):
      owodes=owodes+1
      msgonec=msgone['content']
      if "(2/5)" in str(msgonec):
          return "exit"
      if 'banned' in msgonec:
          print(f'{at()}{bot.color.fail} !!! [BANLANDI] !!! {bot.color.reset} owobotdan banlandı, eğer botun bir sorunu olduğunu düşüyorsanız https://github.com/sudo-do/auto-owo-bot adresinden sorun raporu açın')
          return "exit"
      if 'complete your captcha' in msgonec:
          print(f'{at()}{bot.color.warning} !! [CAPTCHA] !! {bot.color.reset} CAPTCHA   DOĞRULAMASI GEREKLİ {msgonec[-6:]}')
          return "exit"
def runner():
        global wbm
        command=random.choice(bot.commands)
        command2=random.choice(bot.commands)
        client.typingAction(str(bot.channel))
        client.sendMessage(str(bot.channel), command)
        print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} {command}")
        if not command2==command:
          client.typingAction(str(bot.channel))
          time.sleep(1)
          client.sendMessage(str(bot.channel), command2)
          print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} {command2}")
        time.sleep(random.randint(wbm[0],wbm[1]))
def owopray():
  client.sendMessage(str(bot.channel), "owo pray")
  print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} owo pray")
def gems():
  client.typingAction(str(bot.channel))
  time.sleep(2)
  client.sendMessage(str(bot.channel), "owo inv")
  print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} owo inv")
  time.sleep(5)
  msgs=client.getMessages(str(bot.channel), num=5)
  msgs=json.loads(msgs.text)
  for msgone in msgs:
    if msgone['author']['id']==str(bot.owoid) and 'Inventory' in msgone['content']:
      inv=re.findall(r'`(.*?)`', msgone['content'])
  if '50' in inv:
    client.sendMessage(str(bot.channel), "owo lb all")
    print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} owo lb all")
    time.sleep(10)
    gems()
    return
  for item in inv:
    try: 
      if int(item) > 100:
        inv.pop(inv.index(item)) #weapons
    except: #backgounds etc
      inv.pop(inv.index(item))
  tier = [[],[],[]]
  print(f"{at()}{bot.color.okblue} [INFO] {bot.color.reset} Found {len(inv)} gems Inventory")
  for gem in inv:
    gem =int(gem)
    if 50 < gem < 60:
      tier[0].append(gem)
    elif 60 < gem < 70:
      tier[1].append(gem)
    elif 70 < gem < 80:
      tier[2].append(gem)
  for level in range(0,3):
    if not len(tier[level]) == 0:
      client.sendMessage(str(bot.channel), "owo use "+str(max(tier[level])))
      print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} owo use {str(max(tier[level]))}")
      time.sleep(6)
def loopie():
  x=True
  pray = 0
  gem=pray
  main=time.time()
  while x:
      def security():
        if issuechecker() == "exit":
          exit()
      security()
      runner()
      if time.time() - pray > random.randint(300, 500):
        security()
        owopray()
        pray=time.time()
      if time.time() - gem > random.randint(150, 330):
        security()
        gems()
        gem=time.time()
      
      if time.time() - main > random.randint(500, 900):
        time.sleep(random.randint(150, 300))
        security ()
        main=time.time()
@client.gateway.command
def defination1(resp):
  global once
  if resp.event.message:
      if not once: #idk any other way to do this
        once=True
        lol=multiprocessing.Process(target=loopie)
        lol.start()
        #lol.join()
client.gateway.run()
