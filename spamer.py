# -*- coding: utf-8 -*-
# waoh okay lets gop
import subprocess, sys, urllib, requests, json, time, os
from pathlib import Path

#make us have a shell
def yeas(cmd):
    subprocess.call(cmd, shell=True)
 
yeas("clear")
 # look for paths
auth = Path("./auth.txt")
sign = Path("./sign.txt")
 
if auth.is_file():
    with open('auth.txt', 'r') as file:
        auth=file.readline().rstrip('\n')
        print("[!] Found File Named: auth.txt. Using It")
else:
    file = open('auth.txt', 'w')
    auth = raw_input("Authorization: ")
    file.write(auth)
    print('[!] File written: ./auth.txt')
    file.close()
 
if sign.is_file():
    with open('sign.txt', 'r') as file:
        sign=file.readline().rstrip('\n')
        print("[!] Found File Named: sign.txt. Using It")
else:
    file = open('sign.txt', 'w')
    sign = raw_input("Signature: ")
    file.write(sign)
    print('[!] File written: ./sign.txt')
    file.close()
 
yeas("clear")
logo = '''
AYE YO, its yo boi UrBogan, henno all I miss chu all, been looking
at old hdds and found this thought i might let it free all you need
is fiddler or httpdebugger and send a party invt on xbl app and get
the Signature and Authorization so ez ez ily all <3
############################# CHOICES #############################
| 1. Get The Dump Of A GamerTag "Uxid, GamerPic, Bio, ect".       |
| 2. Spams The Uxid With Party Invites. Time Out Of 5 Second      |
| 3. Spams The Uxid With Party Invites. No Time Out               |
| 4. Exits This Program.                                          |
###################################################################
'''
print(logo)
x = raw_input("Enter option: ")
if  x == '1':
        gt = raw_input("GamerTag: ")
        headerss = {
            "x-xbl-contentrestrictions": "eyJ2ZXJzaW9uIjoyLCJkYXRhIjp7Imdlb2dyYXBoaWNSZWdpb24iOiJBVSIsIm1heEFnZVJhdGluZyI6MjU1LCJwcmVmZXJyZWRBZ2VSYXRpbmciOjI1NSwicmVzdHJpY3RQcm9tb3Rpb25hbENvbnRlbnQiOmZhbHNlfX0=",
            "Signature": ""+sign+"",
            "Authorization": ""+auth+"",
            "x-xbl-contract-version": "3",
            "Accept-Encoding": "gzip; q=1.0, deflate; q=0.5, identity; q=0.1",
            "Accept": "application/json",
            "Accept-Language": "en-GB, en",
            "Content-Type": "application/json",
            "Connection": "Keep-Alive",
        }
        print("Dumping Gamertag: ")
        print(gt)
        time.sleep(5)
        r = requests.get("https://profile.xboxlive.com/users/gt("+gt+")/profile/settings", headers=headerss, params=(("settings", "GameDisplayPicRaw,Gamerscore,Gamertag,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,TenureLevel,Watermarks,Location,IsDeleted,ShowUserAsAvatar"),))
        print(r.content)
        print("")
        print('look for this, after id is the uxid {"profileUsers":[{"id":"')
elif x == '2':
    xuid = raw_input("Xuid: ")
    name = raw_input("name: ")
    gt = raw_input("Gamertag: ")
    x = 1
    while True:
        headers = {
                "Signature": ""+sign+"",
                "Authorization": ""+auth+"",
                "X-XBL-Contract-Version": "105",
                "X-XBL-Correlation-Id": "4BE48DFE-E362-4110-A333-0FA70F2819EF",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "*/*",
                "If-Match": "*",
                "Accept-Language": "en-GB, en",
                "Content-Type": "application/json",
                "Connection": "Keep-Alive",
        }
        data = "{\"type\":\"invite\",\"sessionRef\":{\"scid\":\"7492BACA-C1B4-440D-A391-B7EF364A8D40\",\"templateName\":\"chat\",\"name\":\""+name+"\"},\"invitedXuid\":\""+xuid+"\"}"
        print'\x1b[1;31m[\x1b[1;35mXBOX\x1b[1;31m] \x1b[1;32mSending Party Invite To ~~~\x1b[1;35m> \x1b[1;31m[\x1b[1;35m%s\x1b[1;31m]\x1b[0m' % (gt)
        print'\x1b[1;31m[\x1b[1;35mXBOX\x1b[1;31m] \x1b[1;32mSent Party Invite No.~~~\x1b[1;35m> \x1b[1;31m[\x1b[1;35m%d\x1b[1;31m]\x1b[0m' % (x)
        r = requests.post('https://sessiondirectory.xboxlive.com/handles', timeout=5, headers=headers, data=data)
        print(r.status_code)
        time.sleep(5)
        x += 1
elif x == '3':
    xuid = raw_input("Xuid: ")
    name = raw_input("name: ")
    gt = raw_input("Gamertag: ")
    x = 1
    while True:
        headers = {
                "Signature": ""+sign+"",
                "Authorization": ""+auth+"",
                "X-XBL-Contract-Version": "105",
                "X-XBL-Correlation-Id": "4BE48DFE-E362-4110-A333-0FA70F2819EF",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "*/*",
                "If-Match": "*",
                "Accept-Language": "en-GB, en",
                "Content-Type": "application/json",
                "Connection": "Keep-Alive",
        }
        data = "{\"type\":\"invite\",\"sessionRef\":{\"scid\":\"7492BACA-C1B4-440D-A391-B7EF364A8D40\",\"templateName\":\"chat\",\"name\":\""+name+"\"},\"invitedXuid\":\""+xuid+"\"}"
        print'\x1b[1;31m[\x1b[1;35mXBOX\x1b[1;31m] \x1b[1;32mSending Party Invite To ~~~\x1b[1;35m> \x1b[1;31m[\x1b[1;35m%s\x1b[1;31m]\x1b[0m' % (gt)
        print'\x1b[1;31m[\x1b[1;35mXBOX\x1b[1;31m] \x1b[1;32mSent Party Invite No.~~~\x1b[1;35m> \x1b[1;31m[\x1b[1;35m%d\x1b[1;31m]\x1b[0m' % (x)
        r = requests.post('https://sessiondirectory.xboxlive.com/handles', timeout=5, headers=headers, data=data)
        print(r.status_code)
        x += 1
elif x == '4':
    print("GoodBye")
    sys.exit()
else:
    print("Invaild Option Exiting....")
    sys.exit()
 
