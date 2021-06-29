from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ChatRoomAnnouncementContents, OpType, MediaType, ContentType, ApplicationType, TalkException, ErrorCode
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
#from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback, livejson
_session = requests.session()
#==============================================================================#



#nadya = LINE('aykmdn@shayzam.net','az24992499')
#nadya = LINE('eruxdcauz@datasoma.com','az24992499')
#nadya.log("Auth Token : " + str(nadya.authToken))
#channelToken = nadya.getChannelResult()
#nadya = LINE('lumjpqka@datasoma.com','az24992499')

nadya = LINE('musicforyou.freefree@gmail.com','tumz2530')

#ki =  LINE('aykmdn@shayzam.net','az24992499')

#nadya = LINE('estbet.bot002@gmail.com','Tumz2530')

#ki3 = LINE('bot.iseeyou@gmail.com','Tumz2530')


print("\nBOT ꧁༺ஆืਹໂ√န༻꧂.......\nสนใจเช่าบอทติดต่อ\nLineID:vipscanner_win")

nadyaProfile = nadya.getProfile()
#kiProfile = ki.getProfile()
#ki2Profile = ki2.getProfile()
#ki3Profile = ki3.getProfile()

lineSettings = nadya.getSettings()
#kiSettings = ki.getSettings()
#ki2Settings = ki2.getSettings()
#ki3Settings = ki3.getSettings()
#==============================================================================#
nadyaPoll = OEPoll(nadya)
#kiPoll1 = OEPoll(ki)
#ki2Poll2 = OEPoll(ki2)
#ki3Poll3 = OEPoll(ki3)
nadyaMID = nadya.getProfile().mid
#kiMID = ki.getProfile().mid
#ki2MID = ki2.getProfile().mid
#ki3MID = ki3.getProfile().mid

KAC = [nadya]

Bots = [nadyaMID]
creator = ["u5efd3d10f301deb3d04db10d67c940f6",nadyaMID]
Owner = ["u5efd3d10f301deb3d04db10d67c940f6",nadyaMID]
admin = ["u5efd3d10f301deb3d04db10d67c940f6",nadyaMID]
creator = ["Owner.json","admin.json"]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}
DDATE = {}

responsename = nadya.getProfile().displayName
#responsename2 = ki.getProfile().displayName
#responsename3 = ki2.getProfile().displayName
#responsename4 = ki3.getProfile().displayName
#==============================================================================#
waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
#settingsOpen = codecs.open("temp.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
sets = {
    'autoCancel':{"on":False,"members":1},	
    "pict": False,
    "sti2": False,
    "tags": False,
    "Aip": True,
    "tagsticker": False,
    "checkSticker": False,
    "Sticker": False,
    "checkPost": True,
    "checkContact": True,
    "autoJoinTicket": False,
    "image": {
        "name": "",
    },
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
    "ilstpict": {},
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "วิธีตั้งแทค \n- ตั้งแทค ข้อความที่ต้องการ",
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
#    "b": "บัญชีนี้ถูกป้องกันด้วย แม้คนายมันหล่อ  ระบบได้บล็อคบัญชีคุณอัตโนมัติ >_<",
    "m": "สวัสดีครับ ผมมุดลิ้งมานะครับ >_<",
}
apalo = {
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
apalo = {
    "bc":{},
    "bc1":{},
    "bc2":{},
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#CC0033","t": "#000000"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

user1 = nadyaMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = nadya.getProfile() 
backup = nadya.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

#settings["myProfile"]["displayName"] = nadyaProfile.displayName
#settings["myProfile"]["statusMessage"] = nadyaProfile.statusMessage
#settings["myProfile"]["pictureStatus"] = nadyaProfile.pictureStatus
cont = nadya.getContact(nadyaMID)
#settings["myProfile"]["videoProfile"] = cont.videoProfile
#coverId = nadya.getProfileDetail()["result"]["objectId"]
#settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = nadyaProfile.statusMessage
ProfileMe["pictureStatus"] = nadyaProfile.pictureStatus
coverId = nadya.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
with open('creator.json', 'r') as fp:
    creator = json.load(fp)

with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
myProfile = {
        "displayName": "",
        "statusMessage": "",
        "pictureStatus": ""
}

Cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

ProtectMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ","ปลิว","ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้เรส","ไอ้เหี้ยเรส","ไอ่เรส","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ","บอทเหี้ย","บอทควย","ควยบอท","บอทนรก","เหี้ยบอท"]

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = nadya.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    nadya.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    nadya.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = nadya.getContact(mid)
    if contact.videoProfile == None:
        nadya.cloneContactProfile(mid)
    else:
        profile = nadya.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        nadya.updateProfile(profile)
        pict = nadya.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = nadya.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = nadya.getProfileDetail(mid)['result']['objectId']
    nadya.updateProfileCoverById(coverId)
def backupProfile():
    profile = nadya.getContact(nadyaMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = nadya.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = nadya.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        nadya.updateProfileAttribute(8, profile.pictureStatus)
        nadya.updateProfile(profile)
    else:
        nadya.updateProfile(profile)
        pict = nadya.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = nadya.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    nadya.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        nadya.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = nadya.getGroup(msg.to).name
    sd = nadya.waktunjir()
    nadya.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = nadya.getContact(to)
        profile = nadya.profile
        profileName = nadya.profile
        profileStatus = nadya.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        nadya.updateProfile(profileName)
        nadya.updateProfile(profileStatus)
        profile.pictureStatus = nadya.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if nadya.getProfileCoverId(to) is not None:
            nadya.updateProfileCoverById(nadya.getProfileCoverId(to))
        nadya.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return nadya.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        nadya.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
#maxg = "ua053fcd4c52917706ae60c811e39d3ea"
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(nadya.getContact(nadyaMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(nadya.getContact(nadyaMID).pictureStatus)
        ticket = "https://line.me/ti/p/z7CqVLtFII"
        nadya.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nadya.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@STEVENEVERDIE  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    nadya.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(nadya.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + nadya.getContact("ua053fcd4c52917706ae60c811e39d3ea").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = nadya.genOBSParams({'oid': nadyaMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = nadya.server.postContent('{}/talk/vp/upload.nhn'.format(str(nadya.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        nadya.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = nadya.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = nadya.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    nadya.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nadya.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nadya.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = nadya.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        nadya.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nadya.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
#    with open("stickerz.json","r") as fp:
#        stickerz = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    nadya.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': nadya.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + nadya.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    nadya.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            nadya.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
def uhelp():
    uHelp = """╔══════════════════┓
╠═✪〘♥ ✿คำสั่งบอท✿ ♥〙
╠══════════════════┛
╠►❤ ❤ ❤ ❤ คำสั่ง ❤ ❤ ❤ ❤
╠═════════✪
╠❋►เชิญ (+ส่งคอนแทค)
╠❋►เปิดลิ้ง
╠❋►ปิดลิ้ง
╠❋►.เพิ่มแอด @
╠❋►เพิ่มแอด @
╠❋►me
╠❋►แทค
╠❋►sp
╠❋►รูป
╠❋►จับอ่าน
╠❋►ปิดจับ
╠❋►ตรวจสอบคำหยาบ
╠❋►ปิดตรวจสอบคำหยาบ
╠❋►bk @ เตะแล้วเชิญกลับด้วย
╠❋►เปิดระบบป้องกัน
╠❋►ปิดระบบป้องกัน
╠❋►ปฏิทิน,เวลา,30
╠❋►เทส
╠❋►สปีด 
╠❋►bye @
╠❋►บินด่วน @
╠❋►เพิ่มดำ (ส่งคอนแทค)
╠❋►เพิ่มขาว (ส่งคอนแทค)
╠❋►บัญชีดำ
╠❋►แบน @
╠❋►ล้างบัญชีดำ
╠❋►เตะดำ
╰═Ξ❋★ຜู้คุມ★Ξ︻╦̵̵͇̿̿̿̿╤──

B⃠ O⃠ T⃠  B⃠ Y⃠ 
🅰ⅅℳℐℕ T🆄M🆉 >DZ💯™
Ξ★ຜู้คุມUon★Ξ︻╦̵̵͇̿̿̿̿╤──"""
    return uHelp
        
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
  #      backup = settings
#        f = codecs.open('temp.json','w','utf-8')
 #       json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def nadyaBot(op):
    try:
        if settings["restartPoint"] != None:
            nadya.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                nadya.sendMessage(op.param1, "สวัสดี {} ขอบคุณที่แอดมา".format(str(nadya.getContact(op.param1).displayName)))
#                nadya.sendMessage(op.param1, str(settings["welcome"]))
                nadya.sendMessage(op.param1, str(settings["สน"]))
#                nadya.sendMessage(op.param1, "ต้องการบอทแทค.. ท่านสามารถเชิญผมเข้ากลุ่มได้เลย\n\nแล้วใช้คำสั่ง แทค หรือ /1 ก็สามารถแท็กคนทั้งกลุ่มได้เลยครับ")
#        if op.type == 5:
 #           if settings["autoAdd"] == True:
  #            if op.param2 in admin:
   #               return
    #          nadya.findAndAddContactsByMid(op.param1)
     #         nadya.sendMessage(op.param1, "สวัสดี {} ขอบคุณที่แอดมา".format(str(nadya.getContact(op.param1).displayName)))
      #        msgSticker = sets["messageSticker"]["listSticker"]["add"]
       #       if msgSticker != None:
        #          sid = msgSticker["STKID"]
         #         spkg = msgSticker["STKPKGID"]
          #        sver = msgSticker["STKVER"]
           #       nadya.sendMessage(op.param1, str(settings["สน"]))
            #      sendSticker(op.param1, sver, spkg, sid)
             # print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              if op.param2 in admin:
                  return
              nadya.sendMessage(op.param1,tagadd["b"])
          #    msgSticker = sets["messageSticker"]["listSticker"]["block"]
          #    if msgSticker != None:
          #        sid = msgSticker["STKID"]
          #        spkg = msgSticker["STKPKGID"]
          #        sver = msgSticker["STKVER"]
          #        sendSticker(op.param1, sver, spkg, sid)
                    #nadya.sendMessage(op.param1,tagaad["b"])
              nadya.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")        
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = nadya.getGroup(op.param1)
            if settings["autoJoin"] == True:
                nadya.acceptGroupInvitation(op.param1)
#                nadya.sendMessage(op.param1, str(settings["welcome"]))
                nadya.sendMessage(op.param1, str(settings["commet"]))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            group = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            if settings["autoJoin"] == True:
                if settings["autoCancel"]["on"] == True:
                    if len(group.members) > settings["autoCancel"]["members"]:
                        nadya.acceptGroupInvitation(op.param1)
                    else:
                        nadya.rejectGroupInvitation(op.param1)
                else:
                    nadya.acceptGroupInvitation(op.param1)
            gInviMids = []
            for z in group.invitee:
                if z.mid in op.param3:
                    gInviMids.append(z.mid)
            listContact = ""
            if gInviMids != []:
                for j in gInviMids:
                    name_ = nadya.getContact(j).displayName
                    listContact += "\n      + {}".format(str(name_))
        if op.type == 13:
            if nadyaMID in op.param3:
                G = nadya.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if sets["autoCancel"]["on"] == True:
                        if len(G.members) <= sets["autoCancel"]["members"]:
                            nadya.acceptGroupInvitation(op.param1)
                        else:
                            nadya.leaveGroup(op.param1)
                    else:
                        nadya.acceptGroupInvitation(op.param1)
                elif sets["autoCancel"]["on"] == True:
                    if len(G.members) <= sets["autoCancel"]["members"]:
                        nadya.acceptGroupInvitation(op.param1)
                        nadya.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    nadya.acceptGroupInvitation(op.param1, matched_list)
                    nadya.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")                 
        if op.type == 15:
                          if settings["Leave"] == True:
                            if op.param2 in admin:
                                return
                            g = nadya.getGroup(op.param1)
                            contact = nadya.getContact(op.param2)
                            cover = nadya.getProfileCoverURL(op.param2)
                            gname = g.name
                            names = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            ss = ["#FF69B4"]
                            s = ["#FF69B4"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#FFCCFF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#666666"}, #"separator": True, "separatorColor": "#333333"}
                                        "body": {"backgroundColor": "#FFCCFF"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ลาก่อน {}".format(names),
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                      },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "เสียใจ จากใจ : ทีมงาน",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type":"text",
                                                "text":"กลุ่ม : {}".format(gname),
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"text",
                                                "text": "ติดต่อเช่าบอท",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~bot.tumz"
                                                },
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type":"text",
                                                "text":"ติดต่อ Slot Thai",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://line.me/ti/p/~bot.tumz"
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Ξ★ຜู้คุມ★Ξ︻╦̵̵͇̿̿̿̿╤──",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(op.param1, data)
        if op.type == 17:
                          if settings["Welcome"] == True:
                            if op.param2 in admin:
                                return
                            g = nadya.getGroup(op.param1)
                            contact = nadya.getContact(op.param2)
                            cover = nadya.getProfileCoverURL(op.param2)
                            gname = g.name
                            names = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            ss = ["#FF69B4"]
                            s = ["#FF69B4"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#FFCCFF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#666666"}, #"separator": True, "separatorColor": "#333333"}
                                        "body": {"backgroundColor": "#FFCCFF"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "สวัสดี {}".format(names),
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                      },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ยินดีตอนรับ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type":"text",
                                                "text":"เข้ากลุ่ม : {}".format(gname),
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"text",
                                                "text": "ติดต่อเช่าบอท",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type":"text",
                                                "text":"หาเพจเล่น คลิก",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://allslot.crayon.world"
                                                },
                                            },
                                        ]
                                    },
                                },

                            ]

                            data = {
                                "type": "flex",
                                "altText": "Ξ★ຜู้คุມ★Ξ︻╦̵̵͇̿̿̿̿╤──",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(op.param1, data)
        if op.type == 18:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            cover = nadya.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                        "type": "box",
                        "layout": "vertical",
                         "contents": [
                             {
                                 "type": "image",
                                 "url": "https://profile.line-scdn.net/" + str(pp),
                                 "size": "lg"
                             },
                             {
                                 "type":"text",
                                 "text":" "
                             },
                             {
                                 "type":"text",
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#CC0033",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#CC0033",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = nadya.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = nadya.getContact(nadyaMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
#=====================================================================
#        if op.type in [25,26]:
   #         msg = op.message
      #      text = str(msg.text)
         #   msg_id = msg.id
            #receiver = msg.to
#            sender = msg._from
   #         if msg.to not in unsendchat:
      #          unsendchat[msg.to] = {}
         #   if msg_id not in unsendchat[msg.to]:
#                unsendchat[msg.to][msg_id] = msg_id
   #         msgdikirim[msg_id] = {"text":text}
      #      to = msg.to
         #   isValid = True
            #cmd = command(text)
#            setkey = settings['keyCommand'].title()
   #         if settings['setKey'] == False: setkey = ''
      #      if isValid != False:
         #       if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
            #        try:
               #         if msg.to not in wait['Unsend']:
                  #          wait['Unsend'][msg.to] = {'B':[]}
                     #   if msg._from not in [nadyaMID]:
                        #    return
                  #      wait['Unsend'][msg.to]['B'].append(msg.id)
                    #except:pass
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != nadyaMID: to = sender
                else: to = receiver
                if msg._from not in nadyaMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        nadya.sendMention(to, "คุณติดดำผมอยู่นะครับ @! :)","",[msg._from])
                        nadya.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          nadya.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          nadya.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          nadya.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          nadya.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        print ("AutoLikeCommat")
                        try:
                            if settings["autolike"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                if purl[1] not in wait['postId']:
                                    nadya.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                if settings["com"] == True:
                                    nadya.createComment(purl[0], purl[1], settings["commet"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if settings["autolike"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    if purl[1] not in wait['postId']:
                                        nadya.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    if settings["com"] == True:
                                        nadya.createComment(msg._from, purl[1], settings["commet"])
                                        wait['postId'].append(purl[1])
                                    else:pass
                
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                nadya.leaveRoom(op.param1)
#-------------------------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        nadya.sendMessage(msg.to,"มีรายชื่อในบัญชีอยู่แล้ว")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        nadya.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        nadya.sendMessage(msg.to,"มีรายชื่อในบัญชีอยู่แล้ว")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        nadya.sendMessage(msg.to,"มีรายชื่อในบัญชีอยู่แล้ว")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 13:
                if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = nadya.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 nadya.sendMessage(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 nadya.sendMessage(msg.to,"ขออภัย, " + _name +" บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 nadya.sendMessage(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     nadya.findAndAddContactsByMid(target)
                                     nadya.inviteIntoGroup(msg.to,[target])
                                     nadya.sendMessage(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         nadya.findAndAddContactsByMid(invite)
                                         nadya.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         nadya.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
                                         
        if op.type in [25,26]:
#            print ("[ 💫 คำสั่งทั่วไป 💫 ]")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == "help":
                    cover = nn.getProfileCoverURL(nn.profile.mid)
                    pp = nn.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn.getProfile().displayName
                    status = nn.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={
					'type':'flex',
					'altText':"help message",
					'contents':{
					"type":"carousel",
					"contents":[
					{
					"hero":{
					"type":"image",
					"action":{
					"type":"uri","uri":"line://app/1643557392-pe8AQomG?type=profile"
					},
					"url":profile,"size":"full",
					"aspectMode":"cover",
					"aspectRatio":"1:1"},
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"type":"bubble","body":{
					"type":"box","layout":"vertical",
					"spacing":"xs",
					"contents":[
					{"type":"box",
					"margin":"md",
					"layout":"baseline",
					"contents":[
					{
					"type":"text",
					"size":"xl",
					"align":"end",
					"color":"#CC0000",
					"text":"鈩潗擆潗勷潗�饾悓 饾悂饾悗饾悡 饾悡饾悢饾悓饾悪鉁�"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"https://line.me/ti/p/~"+nn.getProfile().userid,
					},
					"url":"https://www.img.live/images/2019/09/12/deep-web-dark-web-internet-spam-hack-cyber-security.jpg"
					},
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔勦赋喔副喙堗竾"
					},
					"url":"https://www.img.live/images/2019/09/12/sytech-dr-1.png",
					},
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔傕箟喔浮喔灌弗"
					},
					"url":"https://www.img.live/images/2019/09/12/sytech-dr-1.png",
					},
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喙�喔娻竸喔勦箞喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/sytech-dr-1.png",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔曕复喔斷笗喙堗腑喔勦笝喔福喙夃覆喔囙笟喔笚"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔勦赋喔副喙堗竾"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔傕箟喔浮喔灌弗"
					},
					{
					"type":"text",
					"size":"xs",
					"color":"#66FFFF",
					"text":"喙�喔娻竸喔勦箞喔�"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔腑喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔｀傅喔氞腑喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=me"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔腑喔�"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔｀傅喔氞腑喔�"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"me"
					}
					]
					}
					]
					}
					]
					}
					},
					{
					"type":"bubble",
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"body":{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"baseline",
					"contents":[
					{
					"type":"icon",
					"size":"md",
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"icon",
					"size":"md",
					"url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"flex":0,
					"text":"  岽吹刷 4G"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"align":"end",
					"text":"鈴� 22/10/19 鈩�"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔傕箟喔浮喔灌弗"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔｀腹喔涏箑喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔勦笚喙�喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔傕箟喔浮喔灌弗"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔｀腹喔涏箑喔｀覆"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔勦笚喙�喔｀覆"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喙勦腑喔斷傅喙�喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔娻阜喙堗腑喙�喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔曕副喔箑喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喙勦腑喔斷傅喙�喔｀覆"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔娻阜喙堗腑喙�喔｀覆"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔曕副喔箑喔｀覆"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔｀腹喔涏箑喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔о傅喔斷傅喙傕腑喙�喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔涏竵喙�喔｀覆"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔｀腹喔涏箑喔｀覆"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔о傅喔斷傅喙傕腑喙�喔｀覆"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔涏竵喙�喔｀覆"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔｀傅喔氞腑喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔腑喔�1"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=/喔ム笟喔｀副喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔｀傅喔氞腑喔�"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔腑喔�1"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"/喔ム笟喔｀副喔�"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喙�喔娻竸"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔⑧竵喙�喔娻复喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=喔椸副喔�"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喙�喔娻竸"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔⑧竵喙�喔娻复喔�"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"喔椸副喔�"
					}
					]
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"md",
					"contents":[
					{
					"type":"text",
					"text":"鉂�鉂�鉂�",
					"align":"center",
					"size":"xs",
					"weight":"bold",
					"color":"#F8F8FF"
                if msg.text in ('/help','/Help','/คำสั่ง'):
#                  if msg._from in admin and Owner:
                    uHelp = uhelp()
                    nadya.sendMessage(to, str(uHelp))
                    nadya.sendContact(to, "ud5fdef9ea2694215378d0f9718a632e6")
                elif msg.text.lower().startswith("แปล "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    nadya.sendMessage(msg.to, A)

                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    nadya.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    nadya.sendMessage(to, str(helpTranslate))
#=============COMMAND KICKER===========================#
                elif msg.text in ('sp','Sp','สปีด'):
                    start = time.time()
                    nadya.sendMessage(to, "รอสักครู่...")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'bot off':
                  if msg._from in admin and Owner:
                    nadya.sendMessage(to, "กำลังประมวณผล...")
                    time.sleep(5)
                    nadya.sendMessage(to, "เรียบร้อย")
                    restartBot()
                elif text.lower() == 'บอทออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == 'ข้อมูลบอท':
                    try:
                        arr = []
                        owner = "u24d5f93f9113c991342c079005467e2f"
                        creator = nadya.getContact(owner)
                        contact = nadya.getContact(nadyaMID)
                        grouplist = nadya.groups
                        contactlist = nadya.getAllContactIds()
                        blockedlist = nadya.getBlockedContactIds()
                        ret_ = "╔══[ ข้อมูลบอท ]"
                        ret_ += "\n╠ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n╠ กลุ่ม : 278"
#                        ret_ += "\n╠ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ เพื่อน : 178"
#                        ret_ += "\n╠ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ สถานะ Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ ผู้สร้างบอท : {}".format(creator.displayName)
                        ret_ += "\n╚══[เช่าบอท Line ID: vipscanner_win]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
                elif "เทส" == msg.text.lower():
                  if msg._from in admin:
                    nadya.sendMessage(to,"ŚẾL₣ВΌŦLÍŇỀ\n(｡◕‿◕｡)")
                    nadya.sendMessage(to,"LOADING:▒...0%")  
                    nadya.sendMessage(to,"█▒... 10.0%")       
                    nadya.sendMessage(to,"██▒... 20.0%")
                    nadya.sendMessage(to,"███▒... 30.0%")
                    nadya.sendMessage(to,"████▒... 40.0%")
                    nadya.sendMessage(to,"█████▒... 50.0%")
                    nadya.sendMessage(to,"██████▒... 60.0%")
                    nadya.sendMessage(to,"███████▒... 70.0%")
                    nadya.sendMessage(to,"████████▒... 80.0%")
                    nadya.sendMessage(to,"█████████▒... 90.0%")
                    nadya.sendMessage(to,"███████████..100.0%")                    
                    nadya.sendMessage(to,"(｡◕‿◕｡)\nบอทยังทำงานคับท่าน😁")       
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["protect"] == True: ret_ += "\n╠ Protect ✅"
                        else: ret_ += "\n╠ Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠ Qr Protect ✅"
                        else: ret_ += "\n╠ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ Invite Protect ✅"
                        else: ret_ += "\n╠ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n╠ Cancel Protect ✅"
                        else: ret_ += "\n╠ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        ret_ += "\n╚══[ Status ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif text.lower() == 'เช็ค':
                  if msg._from in admin:
                    try:
                        ret_ = "╔════[ ❋การตั้งค่า❋ ]═════┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠❋ ตอบรับเพื่อนออโต้ ✅"
                        else: ret_ += "\n╠❋ ตอบรับเพื่อนออโต้ ❌"
                        if settings["autoBlock"] == True: ret_ += "\n╠❋ ออโต้บล็อคเปิด ✅"
                        else: ret_ += "\n╠❋ ออโต้บล็อคปิด   ❌ "
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠❋ มุดลิ้งเปิด ✅"
                        else: ret_ += "\n╠❋ มุดลิ้งปิด ❌ "
                        if settings["autoJoin"] == True: ret_ += "\n╠❋ เข้ากลุ่มออโต้เปิด ✅"
                        else: ret_ += "\n╠❋ เข้ากลุ่มออโต้ปิด ❌ "
                        if settings["Api"] == True: ret_ += "\n╠❋ ข้อความApiเปิด ✅"
                        else: ret_ += "\n╠❋ ข้อความApiปิด ❌ "
                        if settings["Aip"] == True: ret_ += "\n╠❋ ตรวจคำสั่งบินเปิด✅"
                        else: ret_ += "\n╠❋ ตรวจคำสั่งบินปิด ❌ "
                        if settings["Welcome"] == True: ret_ += "\n╠❋ ข้อความต้อนรับเปิด ✅"
                        else: ret_ += "\n╠❋ ข้อความต้อนรับปิด  ❌ "
                        if settings["Leave"] == True: ret_ += "\n╠❋ ข้อความคนออกเปิด ✅"
                        else: ret_ += "\n╠❋ ข้อความคนออกปิด ❌ "
                        if settings["Nk"] == True: ret_ += "\n╠❋ ข้อความแจ้งเตือนคนลบเปิด ✅"
                        else: ret_ += "\n╠❋ ข้อความแจ้งเตือนคนลบปิด ❌ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠❋ ปฏิเสธเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✅"
                        else: ret_ += "\n╠❋ ปฏิเสธกลุ่มเชิญปิด    ❌ "
                        if settings["autoLeave"] == True: ret_ += "\n╠❋ ออกแชทรวมออโต้เปิด✅"
                        else: ret_ += "\n╠❋ ออกแชทรวมออโต้ปิด ❌ "
                        if settings["autoRead"] == True: ret_ += "\n╠❋ อ่านออโต้เปิด ✅"
                        else: ret_ += "\n╠❋ อ่านออโต้ปิด ❌"
                        if settings["checkContact"] == True: ret_ += "\n╠❋ อ่านคทเปิด ✅"
                        else: ret_ += "\n╠❋ อ่านคทปิด   ❌ "
                        if settings["checkPost"] == True: ret_ += "\n╠❋ เช็คโพสเปิด ✅"
                        else: ret_ += "\n╠❋ เช็คโพสปิด   ❌ "
                        if settings["checkSticker"] == True: ret_ += "\n╠❋ เช็คStickerเปิด ✅"
                        else: ret_ += "\n╠❋ เช็คStickerปิด  ❌ "
                        if settings["detectMention"] == True: ret_ += "\n╠❋ ตอบกลับคนแทคเปิด ✅"
                        else: ret_ += "\n╠❋ ตอบกลับคนแทคปิด ❌ "
                        if settings["potoMention"] == True: ret_ += "\n╠❋ แสดงภาพ+คท คนแทคเปิด ✅"
                        else: ret_ += "\n╠❋ แสดงภาพ+คท คนแทค ปิด ❌ "
                        if settings["kickMention"] == True: ret_ += "\n╠❋ เตะคนแทคเปิด ✅"
                        else: ret_ += "\n╠❋ เตะคนแทคปิด ❌ "
                        if settings["delayMention"] == True: ret_ += "\n╠❋ แทคกลับคนแทคเปิด ✅"
                        else: ret_ += "\n╠❋ แทคกลับคนแทคปิด ❌ "
                        if settings["inviteprotect"] == True: ret_ += "\n╠❋ กันเชิญเปิด ✅"
                        else: ret_ += "\n╠❋ กันเชิญปิด ❌ "
                        if settings["cancelprotect"] == True: ret_ += "\n╠❋ กันยกเชิญเปิด ✅"
                        else: ret_ += "\n╠❋ กันยกเชิญปิด ❌ "
                        if settings["protect"] == True: ret_ += "\n╠❋ ป้องกันเปิด ✅"
                        else: ret_ += "\n╠❋ ป้องกันปิด ❌ "
                        if settings["qrprotect"] == True: ret_ += "\n╠❋ ป้องกันเปิดลิ้งเปิด ✅"
                        else: ret_ += "\n╠❋ ป้องกันเปิดลิ้งปิด ❌ "
                        if settings["qrprotect"] == True: ret_ += "\n╠❋ ป้องกันสมาชิกเปิด ✅"
                        else: ret_ += "\n╠❋ ป้องกันสมาชิกปิด ❌ "
                        if settings["inviteprotect"] == True: ret_ += "\n╠❋ ป้องกันคนนอกเข้ากลุ่ม ✅"
                        else: ret_ += "\n╠❋ ป้องกันคนนนอกเข้ากลุ่ม ❌ "
                        ret_ += "\n╚════[Hack Scan Win]═════┛"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดลิ้ง':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "ปิดลิ้งเรียบร้อย")
#-------------------------------------------------------------------------------
                elif text.lower() == "เปิดไลค์":
                    settings["autolike"] = True
                    nadya.sendMessage(to,"เปิดแล้ว >_<")
                elif text.lower() == "ปิดไลค์":
                    settings["autolike"] = False
                    nadya.sendMessage(to,"ปิดแล้ว >_<")
                elif text.lower() == 'เข้า/ออก on':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["Leave"] = True
                        settings["Welcome"] = True
                        nadya.sendMessage(msg.to,"➲ เปิดระบบต้อนรับสมาชิก เข้า-ออก")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")
                elif text.lower() == 'เปิดติ้กใหญ่':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["Sticker"] = True
                        nadya.sendMessage(msg.to,"➲ เรียบร้อย")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")

                elif text.lower() == 'ปิดติ้กใหญ่':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["Sticker"] = False
                        nadya.sendMessage(msg.to,"➲ ปิดแล้ว")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")

                elif text.lower() == 'เข้า/ออก off':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["Welcome"] = False
                        settings["Leave"] = False
                        nadya.sendMessage(msg.to,"➲ ปิดระบบต้อนรับสมาชิก เข้า-ออก")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")
                elif text.lower() == 'จับ/กลุ่ม off':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["checkPost"] = False
                        settings["checkContact"] = False
                        nadya.sendMessage(msg.to,"➲ ปิดระบบเรียบร้อย")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")
                elif text.lower() == 'จับ/กลุ่ม on':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["checkPost"] = True
                        settings["checkContact"] = True
                        nadya.sendMessage(msg.to,"➲ เปิดระบบเรียบร้อย")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")


                elif text.lower() == 'เปิดเข้า':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["autoJoin"] = True
                        nadya.sendMessage(msg.to,"➲ เรียบร้อย")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")

                elif text.lower() == 'ปิดเข้า':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["autoJoin"] = False
                        nadya.sendMessage(msg.to,"➲ ปิดแล้ว")
                    else:
                        nadya.sendMessage(msg.to,"ไม่มีสิทธิสั่ง")
                elif msg.text in ["เปิดแทค"]:
                  if msg._from in admin:
                    settings['detectMention'] = True
                    nadya.sendMessage(msg.to,"Respon enabled.")
                elif msg.text in ["เปิดแทค"]:
                  if msg._from in admin:
                    settings['detectMention'] = True
                    nadya.sendMessage(msg.to,"Respon enabled.")
                elif msg.text in ["เปิดแทค"]:
                  if msg._from in admin:
                    settings['detectMention'] = True
                    nadya.sendMessage(msg.to,"Respon enabled.")
                elif msg.text in ["รีแอด"]:
                  if msg._from in admin:
                    settings['admin'] = {}
                    nadya.sendMessage(msg.to,"done")
                elif msg.text in ["เปิดแทค"]:
                  if msg._from in admin:
                    settings['detectMention'] = True
                    nadya.sendMessage(msg.to,"Respon enabled.")

                elif msg.text in ["ตรวจสอบคำหยาบ"]:
                  if msg._from in admin:
                    settings["Aip"] = True
                    nadya.sendMessage(msg.to,"เปิดระบบตรวจสอบคำหยาบกับบอทบิน  ^ω^")

                elif msg.text in ["ปิดตรวจสอบคำหยาบ"]:
                  if msg._from in admin:
                    settings["Aip"] = False
                    nadya.sendMessage(msg.to,"ปิดระบบตรวจสอบคำหยาบกับบอทบินแล้วʕ•ﻌ•ʔ")

                elif msg.text in ["เปิดพูด"]:
                  if msg._from in admin:
                    settings["Api"] = True
                    nadya.sendMessage(msg.to,"😁 เปิดระบบบอทตอบโต้ 😁")

                elif msg.text in ["ปิดพูด"]:
                  if msg._from in admin:
                    settings["Api"] = False
                    nadya.sendMessage(msg.to,"😂 ปิดระบบบอทตอบโต้ 😂")
                elif "รัน: " in msg.text.lower():
                        key = msg.text[-33:]
                        nadya.findAndAddContactsByMid(key)
                        contact = nadya.getContact(key)
                        nadya.createGroup("Ħ͙͕͙͠Ꝁ͙͕͙͠ S͙͕͙͠Ɇ͙͕͙͠Ł͙͕͙͠F͙͕͙͠Ƀ͙͕͙͠Ø͙͕͙͠Ŧ͙͕͙͠",[key])
                        nadya.sendText(msg,to,"❋ทำการรัน สำเร็จ❋")
#==============================================================================#
                elif "ปวดตับ" in msg.text:
                     if msg._from in Owner:
                         _name = msg.text.replace("ปวดตับ","")
                         gs = nadya.getGroup(receiver)
                         nadya.sendMessage(receiver,"ต้องรีบไปหาหมอ ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             nadya.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                                 if not target in admin:
                                     try:
                                         k = [nadya,ki,ki2,ki3,ki4]
                                         random.choice(k).kickoutFromGroup(receiver,[target])
                                         print ((receiver,[g.mid]))
                                     except:
                                         nadya.sendMessage(receiver,"ไปก่อนนะ")
                                         print ("คลีนิค ปิดเรียบร้อย")
#==============================================================================#

                elif text.lower() == 'ติ้ก on':
                    settings["checkSticker"] = True
                    nadya.sendMessage(to, "❥เปิดระบบเช็คสติ้กเกอร์ ❋")
                elif text.lower() == 'ติ้ก off':
                    settings["checkSticker"] = False
                    nadya.sendMessage(to, "❥ปิดระบบเช็คสติ้กเกอร์ ❋")
                elif text.lower() == 'เปิดแอด':
                  if msg._from in admin:
                    settings["autoAdd"] = True
                    nadya.sendMessage(to, "เปิดแล้ว!!")
                elif text.lower() == 'ปิดแอด':
                  if msg._from in admin:
                    settings["autoAdd"] = False
                    nadya.sendMessage(to, "ปิดแล้ว!!")
                elif text.lower() == 'เปิดบล็อค':
                  if msg._from in admin:
                    settings["autoBlock"] = True
                    nadya.sendMessage(to, "เปิดใช้งานออโต้บล็อคแล้ว.")
                elif text.lower() == 'ปิดบล็อค':
                  if msg._from in admin:
                    settings["autoBlock"] = False
                    nadya.sendMessage(to, "ปิดใช้งานออโต้บล็อคแล้ว")
                elif text.lower() == 'เปิดลิ้งแชร์':
                  if msg._from in admin:
                    settings["timeline"] = True
                    nadya.sendMessage(to, "เปิดลิ้งแชร์แล้ว.")
                elif text.lower() == 'ปิดลิ้งแชร์':
                  if msg._from in admin:
                    settings["timeline"] = False
                    nadya.sendMessage(to, "ปิดลิ้งแชร์แล้ว.")
                elif text.lower() == 'เปิดตรวจสอบ':
                  if msg._from in admin:
                    settings["checkContact"] = True
                    nadya.sendMessage(to, "ตรวจสอบ สมาชิก ถูกเปิดแล้ว")
                elif text.lower() == 'เปิดตอบ':
                  if msg._from in admin:
                    settings["delayMention"] = True
                    nadya.sendMessage(to, "ตรวจสอบ สมาชิก ถูกปิดแล้ว")
#==============================================================================#
#                elif text.lower() == 'kk':
 #                 if msg._from in Owner:
  #                  nadya.sendMessage(msg.to, str(settings["กสิกร"]))

                #el#if msg.text.lower().startswith("/เปิดวาป "):
                elif text.lower() == 'kk':
                  if msg._from in admin and nadyaMID:
                    groups = nadya.groups
                    for group in groups:
                        if not group in g:
                            try:
                                nadya.sendMessage(group, str(settings["กสิกร"]))
                                nadya.sendMessage(group, str(settings["kung"]))
                            except:
                           #     time.sleep(10)
                            #    naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                                nadya.sendMessage(msg.to, "เรียบร้อย")

                elif text.lower() == ".หาเพจ":
                  if msg._from in admin and nadyaMID:
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            sas = ["https://www.img.in.th/images/880fe23a719d874f58b0fac7710527b4.gif"]
                            data = {
                                "type": "template",
                                "altText": "༺ஆืਹໂ√န༻",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "http://bit.ly/3iEVrJi"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(group, data)

                elif text.lower() == "หาเพจ":
                            sas = ["https://www.img.in.th/images/880fe23a719d874f58b0fac7710527b4.gif"]
                            data = {
                                "type": "template",
                                "altText": "༺ஆืਹໂ√န༻",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "http://bit.ly/3iEVrJi"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == '#ประกาศ':
                  if msg._from in admin and nadyaMID:
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            try:
                                nadya.sendImageWithURL(group, str(settings["B1"]))
                                nadya.sendMessage(group, str(settings["B2"]))
                            except:
                                nadya.sendMessage(msg.to, "เรียบร้อย")
                elif text.lower() == '/ประกาศ':
                  if msg._from in admin and nadyaMID:
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            try:
                                nadya.sendImageWithURL(group, str(settings["B1"]))
                                nadya.sendMessage(group, str(settings["B2"]))
                            except:
                                nadya.sendMessage(msg.to, "เรียบร้อย")
                elif 'B1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('B1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["B1"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'B2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('B2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["B2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif text.lower() == '/ส่ง':
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            try:
                                nadya.sendImageWithURL(group, str(settings["P1"]))
                                nadya.sendMessage(group, str(settings["K1"]))
                                nadya.sendImageWithURL(group, str(settings["P2"]))
                                nadya.sendMessage(group, str(settings["K2"]))
                            except:
                                nadya.sendMessage(msg.to, "เรียบร้อย")
                elif 'P2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P2"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'K2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('K2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["K2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P1"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'K1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('K1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["K1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'S1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('S1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["S1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'S2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('S2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["S2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'S3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('S3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["S3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))


                elif text.lower() == 's1':
                    nadya.sendMessage(msg.to, str(settings["S1"]))
                elif text.lower() == 's2':
                    nadya.sendMessage(msg.to, str(settings["S2"]))
                elif text.lower() == 's3':
                    nadya.sendMessage(msg.to, str(settings["S3"]))
                elif text.lower() == '':
                    nadya.sendMessage(msg.to, str(settings[""]))
            
                elif text.lower() == 'b1':
                    nadya.sendImageWithURL(to, str(settings["B1"]))
                elif text.lower() == 'b2':
                    nadya.sendMessage(msg.to, str(settings["B2"]))
                elif text.lower() == 'p1':
                    nadya.sendImageWithURL(to, str(settings["P1"]))
                elif text.lower() == 'k1':
                    nadya.sendMessage(msg.to, str(settings["K1"]))
                elif text.lower() == 'p2':
                    nadya.sendImageWithURL(to, str(settings["P2"]))
                elif text.lower() == 'k2':
                    nadya.sendMessage(msg.to, str(settings["K2"]))
                elif text.lower() == '':
                    nadya.sendImageWithURL(to, str(settings[""]))
                elif text.lower() == '':
                    nadya.sendMessage(msg.to, str(settings[""]))
                elif text.lower() == '':
                    nadya.sendImageWithURL(to, str(settings[""]))
                elif text.lower() == '':
                    nadya.sendMessage(msg.to, str(settings[""]))
                elif text.lower() == '':
                    nadya.sendImageWithURL(to, str(settings[""]))
                elif text.lower() == '':
                    nadya.sendMessage(msg.to, str(settings[""]))

                elif text.lower() == '9':
                    nadya.sendImageWithURL(to, str(settings["Pic"]))
                elif text.lower() == 'กฎกลุ่ม':
                    nadya.sendImageWithURL(to, str(settings["Pic"]))
                elif text.lower() == 'pic':
                    nadya.sendImageWithURL(to, str(settings["Pic"]))
                elif text.lower() == 'กฏกลุ่ม':
                    nadya.sendImageWithURL(to, str(settings["Pic"]))
                elif text.lower() == 'รอส':
                    nadya.sendMessage(msg.to, str(settings["รอส"]))
                elif text.lower() == 'ks':
                    nadya.sendMessage(msg.to, str(settings["kung"]))
#                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == 'hi':
                    nadya.sendMessage(msg.to, str(settings["hi"]))
 #                   nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == 'สน':
                    nadya.sendMessage(msg.to, str(settings["สน"]))
  #                  nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == 'รอบที่3':
                    nadya.sendMessage(msg.to, str(settings["mm"]))
   #                 nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
    
                elif 'rgt: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('rgt: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["00"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'รอส: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รอส: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["รอส"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ks: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ks: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["kung"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'รูปเข้า: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูปเข้า: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["รูปเข้า"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'w: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('w: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["welcome"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#0: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#0: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#0"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#4: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#4"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#5: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#5: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#5"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#6: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#6: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#6"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#7: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#7: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#7"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#8: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#8: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#8"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#9: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#9: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#9"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#10: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#10: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#10"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#11: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#11: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#11"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#12: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#12: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#12"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#13: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#13: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#13"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'คท: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('คท: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["คอนแทค"] = spl
                          nadya.sendContact(to, "{}".format(str(spl)))
                elif 'ตั้งกฎ: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งกฎ: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Pic"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'n: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('n: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["new"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'เพิ่มกลุ่ม: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('เพิ่มกลุ่ม: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["จำนวนกลุ่ม"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'kk: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('kk: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["กสิกร"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'สน: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('สน: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["สน"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'hi: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('hi: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["hi"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'kick: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('kick: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["kick"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'cm: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('cm: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["comment"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
#-------------------------------------------------------------------------------

                elif msg.text in ["byenakub"]:
                    if msg._from in admin:
                        gs = nadya.getGroup(msg.to)
                        targets = [sender]
                        for target in targets:
                                try:
                                   # nadya.sendMessage(msg.to,"Boss ขอมา > Bot จัดให้ *-*")
                                    nadya.kickoutFromGroup(msg.to,[sender])
                                    time.sleep(900)
                                    nadya.findAndAddContactsByMid(target)
                                    nadya. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass




                elif msg.text.lower().startswith("เพิ่มแอด "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"☢-Bot-☢\nจดจำ\nเรียบร้อยคับ")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")

                elif msg.text.lower().startswith("ลบแอด "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"☢-Bot-☢\nลบออก\nเรียบร้อย")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith(".เพิ่มแอด "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codop0ecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"☢-Bot-☢\nจดจำ\nเรียบร้อยคับ")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")

                elif msg.text.lower().startswith(".ลบแอด "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"☢-Bot-☢\nลบออก\nเรียบร้อย")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("line "):
                            a = removeCmd("line", text)
                            b = nadya.findContactsByUserid(a)
                            line = b.mid
                            nadya.sendMessage(msg.to,"line://ti/p/~" + a)
                            nadya.sendContact(to, line)                                                                                           
                            nadya.sendMessage(to,str(hasil))

                elif text.lower() == 'เปิดป้องกัน':
                    if msg._from in admin:
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Already On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Set To On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Already On")
                                
                elif text.lower() == 'ปิดป้องกัน':
                    if msg._from in admin:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Set To Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Already Off")

                elif text.lower() == "เปลี่ยนดิส":
                    settings["changePictureProfile"] = True
                    nadya.sendMessage(to, "❋ส่งรูปภาพลงมา❋")
                elif text.lower() == "เปลี่ยนรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        nadya.sendMessage(to, "❋ส่งรูปภาพลงมา❋")

#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดระบบป้องกัน':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        settings["autoRead"] = True
                        settings["autoAdd"] = True
                        settings["autoJoinTicket"] = True
                        settings["Nk"] = True
                        settings["Lv"] = True
                        settings["Wc"] = True
                        settings["autoBlock"] = True
                        settings["Aip"] = True
                        settings["detectMention"] = True
                        nadya.sendMessage(msg.to,"➲ All Protect Set To On")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
                        		            
                elif text.lower() == 'ปิดระบบป้องกัน':
                    if msg._from in admin:
                        group = nadya.getGroup(to)
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        nadya.sendMessage(msg.to,"➲ All Protect Set To Off")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
#==============================================================================#
                elif text.lower() == "ทีม":
                    nadya.sendMessage(msg.to,responsename)
                    ki.sendMessage(msg.to,responsename2)
                    ki2.sendMessage(msg.to,responsename3)
                    ki3.sendMessage(msg.to,responsename4)
                    ki4.sendMessage(msg.to,responsename5)
                    
                elif msg.text.lower() == 'mybot':
                    if msg._from in Owner:
                        nadya.sendContact(to, nadyaMID)
                        ki.sendContact(to, kiMID)
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        
                elif text.lower() in ["บายน้องเลขา"]:
                  if msg._from in Owner:    
                    nadya.leaveGroup(msg.to)
                elif text.lower() in ["บายบอท"]:
                  if msg._from in Owner:    
#                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
 #                   ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
               #
                elif text.lower() in ["บอทเข้ามา"]:
                  if msg._from in Owner:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Ticket = nadya.reissueGroupTicket(msg.to)
   #                 ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    nadya.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    nadya.updateGroup(G)
                elif text.lower() in ["บอทตรวจสอบเข้ามา"]:
                  if msg._from in admin and nadyaMID:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Ticket = nadya.reissueGroupTicket(msg.to)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    nadya.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    nadya.updateGroup(G)
                
                elif msg.text.lower().startswith("แปล: "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    nadya.sendMessage(msg.to, A)
#==============================================================================#
 #               elif msg.text in ProtectMessage:
  #                  settings["Aip"] == True
   #                 random.choice(KAC).kickoutFromGroup(receiver,[sender])
    #                nadya.sendMessage(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม\n           หรือ\n ตรวจพบคำพูดหยาบคายไม่สุภาพ\nจำเป็นต้องนำออกเพื่อความปลอดภัย\nและความสงบสุขของสมาชิก (｀・ω・´)")
#==============================================================================#
                elif msg.text in ["สแปม"]:
                    if msg._from in admin and nadyaMID:
                         group = nadya.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             nadya.sendMessage(receiver,"❋ไม่พบในกลุ่มนี้❋")
                         else:
                             for jj in matched_list:
                                 try:
                                     random.choice(KAC).kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     nadya.sendMessage(receiver,"❋👋 ")
                                     print ("Blacklist di Kick")

                elif text.lower() == '//me':
                    nadya.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                elif text.lower() == 'mymid':
                    contact = nadya.getContact(sender)
                    mi_d = contact.mid
                    nadya.sendMessage(msg.to,"[MID]\n" +  mi_d)

                elif text.lower() == 'ชื่อ':
                    me = nadya.getContact(sender)
                    nadya.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == '.me':
                    me = nadya.getContact(sender)
                    dan = nadya.getContact(sender)
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + dan.pictureStatus)
                    nadya.sendMessage(msg.to,"[ชื่อ]\n\n" + me.displayName + "\n[สเตตัส]\n\n" + me.statusMessage)
                    nadya.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                elif text.lower() == 'สเตตัส':
                    me = nadya.getContact(sender)
                    nadya.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    dan = nadya.getContact(sender)
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + dan.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    dan = nadya.getContact(sender)
                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + dan.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = nadya.getContact(nadyaMID)
                    cover = nadya.getProfileCoverURL(nadyaMID)    
                    nadya.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("ขอคอนแทค "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        nadya.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text in ("Gs","GS","G01"):
                    nadya.sendMessage(msg.to, str(settings["#G01"]))
                    nadya.sendMessage(msg.to, str(settings["#G02"]))
                    nadya.sendMessage(msg.to, str(settings["#G03"]))
                    nadya.sendMessage(msg.to, str(settings["#G04"]))
                    nadya.sendMessage(msg.to, str(settings["#G05"]))
                    nadya.sendMessage(msg.to, str(settings["#G06"]))
                elif 'save1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('save1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#G01"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'save2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('save2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#G02"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'save3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('save3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#G03"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'save4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('save4: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#G04"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'save5: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('save5: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#G05"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'save6: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('save6: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["#G06"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl))) 


                elif msg.text.lower().startswith("ดูสถานะ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "[ ข้อความสถานะคือ ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("ข้อมูล "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                           try:
                               arr = []
                               owner = "u24d5f93f9113c991342c079005467e2f"
                               creator = nadya.getContact(owner)
                               contact = nadya.getContact(ls)
                               grouplist = nadya.getGroupIdsJoined(ls)
                               contactlist = nadya.getAllContactIds(ls)
                               blockedlist = nadya.getBlockedContactIds(ls)
                               ret_ = "╔══[ ข้อมูลบอท ]"
                               ret_ += "\n╠ ชื่อ : {}".format(contact.displayName)
                               ret_ += "\n╠ กลุ่ม : {}".format(str(ls(grouplist)))
                               ret_ += "\n╠ เพื่อน : {}".format(str(ls(contactlist)))
                               ret_ += "\n╠ Blocked : {}".format(str(ls(blockedlist)))
                               ret_ += "\n╠══[ สถานะ Selfbot ]"
                               ret_ += "\n╠ Version : Premium"
                               ret_ += "\n╠ ผู้สร้างบอท : {}".format(creator.displayName)
                               ret_ += "\n╚══[เช่าบอท Line ID: vipscanner_win]"
                               nadya.sendMessage(to, str(ret_))
                           except Exception as ls:
                               nadya.sendMessage(msg.to, str(ls))
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.nadya.naver.jp/" + nadya.getContact(ls).pictureStatus
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.nadya.naver.jp/" + nadya.getContact(ls).pictureStatus + "/vp"
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = nadya.getProfileCoverURL(ls)
                                nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("แปลงร่าง "):
                  if msg._from in Owner:    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            nadya.cloneContactProfile(contact)
                            nadya.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            nadya.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'คืนร่าง':
                  if msg._from in Owner:    
                    try:
                        nadyaProfile.displayName = str(myProfile["displayName"])
                        nadyaProfile.statusMessage = str(myProfile["statusMessage"])
                        nadyaProfile.pictureStatus = str(myProfile["pictureStatus"])
                        nadya.updateProfileAttribute(8, nadyaProfile.pictureStatus)
                        nadya.updateProfile(nadyaProfile)
                        nadya.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        nadya.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                  if msg._from in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            nadya.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            nadya.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                  if msg._from in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            nadya.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            nadya.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        nadya.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+nadya.getContact(mi_d).displayName
                        nadya.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                  if msg._from in admin:
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            nadya.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            nadya.sendMessage(msg.to,"Reply Message off")

                elif msg.text in ["จับอ่าน"]:
                  if msg._from in admin:
                    try:
                        del Cctv['point'][msg.to]
                        del Cctv['sidermem'][msg.to]
                        del Cctv['cyduk'][msg.to]
                    except:
                        pass
                    Cctv['point'][msg.to] = msg.id
                    Cctv['sidermem'][msg.to] = ""
                    Cctv['cyduk'][msg.to]=True
                    nadya.sendMessage(msg.to,"เปิดระบบเช็คคนอ่านอัตโนมัติ❋")
                elif msg.text in ["ปิดจับ"]:
                  if msg._from in admin:
                    if msg.to in Cctv['point']:
                        Cctv['cyduk'][msg.to]=False
                        #line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    #else:
                        nadya.sendMessage(msg.to, "ปิดระบบเช็คคนอ่านแล้ว❋")
#==============================================================================#
                elif text.lower() == 'ผู้สร้างกลุ่ม':
                  if msg._from in admin:
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendContact(to, GS)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "[ชื่อกลุ่มคือ : ]\n" + gid.name)
                elif text.lower() == 'ลื้งกลุ่ม':
                  if msg._from in admin:
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendMessage(to, "[ ลิ้ง ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            nadya.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                    
                elif msg.text.lower().startswith(": "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    nadya.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
                elif text.lower() == '.มุด':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == '.ปิดมุด':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                  if msg._from in admin:
                    group = nadya.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(nadya.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลกลุ่ม ]"
                    ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
#                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
 #                   ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม : {}".format(gTicket)
                    ret_ += "\n╚══[ 🔥Hack Scan 🔔Win🔔 ]"
                    nadya.sendMessage(to, str(ret_))
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิก':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "╔══[ รายชื่อสมาชิก ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวนทั้งหมด {} ]".format(str(len(group.members)))
                        nadya.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("/ข้อมูล "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        groups = []
                        for mention in mentionees:
                            if mention["M"] not in groups:
                                groups.append(mention["M"])
                        for ls in groups:
                            groups = nadya.groups(ls)
                            ret_ = "╔══[ Group List ]"
                            no = 0 + 1
                            for ls in groups:
                                group = nadya.getGroup(ls)
                                ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╚══[ ทั้งหมด {} กลุ่ม ]".format(str(len(groups)))
                            nadya.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("/พิกัด "):
                  if msg._from in admin and nadyaMID:
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    gid = "{}".format(str(settings["พิกัด"]))
                    groups = nadya.groups
                    for group in groups:
                        if group in gid:
                            try:
                                nadya.sendMessage(group, "{}".format(str(text_)))
                            except:
                                naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                elif 'พิกัด: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('พิกัด: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["พิกัด"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif msg.text.lower().startswith("/พิกัด: "):
                  if msg._from in admin and nadyaMID:
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    gid = "{}".format(str(settings["พิกัด1"]))
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            try:
                                nadya.sendMessage(group, "{}".format(str(text_)))
                            except:
                                naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                elif 'ตั้งพิกัด ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งพิกัด ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["พิกัด1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                #el#if msg.text.lower().startswith("/เปิดวาป "):
                elif text.lower() == 'kkk':
                  if msg._from in admin and nadyaMID:
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            try:
                                nadya.sendMessage(group, str(settings["กสิกร"]))
                         #       nadya.sendMessage(group, str(settings["kung"]))
                            except:
                           #     time.sleep(10)
                            #    naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                                nadya.sendMessage(msg.to, "เรียบร้อย")
                elif 'รูป4 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป4 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Pic4"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'รูป4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป4: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Piic4"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))

#=======================================================================================

                elif msg.text in ["#ยิง"]:
                  if msg._from in admin and nadyaMID:
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["weeb"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic2"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["weeb"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic3"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["weeb"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic4"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["LiineID"])),
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "การันตี",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic5"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["LiineID2"])),
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "การันตี",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in ["ยิง","พรีเซน"]:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["weeb"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic2"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["weeb"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic3"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["weeb"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic4"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["LiineID"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic5"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["LiineID2"])),
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "การันตี",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif 'รูป5: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป5: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Pic5"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))

                elif msg.text in ["/หยิน/",".mylove"]:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic"])),
                                        #"https://www.img.in.th/images/d30c1a1e2dcc0e16a7f2f1e551675866.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ติดต่อ"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "อัพเดทโดย\n┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
 
                elif msg.text in [".หยิน",".mylove"]:
                 #   gid = "{}".format(str(settings["พิกัด"]))
                    groups = nadya.groups
                    for group in groups:
                        if group in groups:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic"])),
                                        #"https://www.img.in.th/images/d30c1a1e2dcc0e16a7f2f1e551675866.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ติดต่อ"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "อัพเดทโดย\n┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)

                elif msg.text in ["#amb"]:
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง1"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic2"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง2"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic3"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง3"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic4"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง4"])),
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "การันตี",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif 'ตั้งเว็ป4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["web4"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif text.lower() == "เกมส์จับผิด":
                            sas = ["https://www.img.in.th/images/9bdc2be96a8eb9deac45e7af3c40215e.png"]
                            ytv = ["line://app/1602687308-GXq4Vvk9?type=text&text=รักพี่ตั้ม","line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มหล่อที่สุด"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(random.choice(ytv)),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["amb","/ยิง","amb1689","/เพจแนะนำ"]:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง1"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic2"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง2"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Pic3"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง3"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["Piic4"])),

                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ลิ้ง4"])),
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "การันตี",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#                            dataProfile = [
#                                {
#                                    "type": "bubble",
#                                    "styles": {
   #                                     "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
#                                    },
#                                    "hero": {
#                                        "type": "image",
#                                        "url": "{}".format(str(settings["การันตี"])),
#                                        "margin": "xxl",
#                                        "aspectMode": "cover",
#                                        "aspectRatio": "3:4",
#                                        "size": "full",
#                                        "action": {
#                                            "type": "uri",
#                                            "uri": "{}".format(str(settings["LineID2"])),
#                                        },
#                                    },
#                                },
#                            ]
#                            data = {
#                                "type": "flex",
#                                "altText": "การันตี",
#                                "contents": {
#                                    "type": "carousel",
#                                    "contents": dataProfile
#                                }
#                            }
#                            sendTemplate(to, data)
                elif msg.text in ["บัญชีหยิน"]:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.img.in.th/images/779414aeac1efbb3de3edecec8e2d155.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=9790373058",
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.img.in.th/images/1aa33879e17dd47d874b61bf003849d6.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=9790373058",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "บัญชีหยิน",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["เลขออย"]:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                       # "url": "https://sv1.picz.in.th/images/2021/06/02/PaLSlI.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=0371692967",
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.img.in.th/images/688b361ee35baf74d4f745290b49dbf1.jpg",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=0371692967",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "บัญชี",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
 
 
                elif msg.text in ["บัญชีฟอด","เลขฟอด"]:
                           # dan = ["uf3310c3940c511d231cdc22e2fb0fc61"]

                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                      #  "url": "http://dl.profile.line-cdn.net/" + dan.pictureStatus,
                                        "url": "https://sv1.picz.in.th/images/2021/06/02/PaLSlI.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=5070999796",
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.img.in.th/images/6fe6216347988c28736d7368ca37479f.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=5070999796",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "บบัญชีฟอด",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["เลขเจ้จอย","เลขเจ๊จอย","เจ้จอย","เจ๊จอย"]:
                           # dan = ["u7ff49be297d593db62733ae062f45ab7"]

                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://sv1.picz.in.th/images/2021/06/10/sSETUl.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=6992047591",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ข้อมูลธนาคาร",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                if text.lower() == "ssp" or text.lower() == "speed":
                    start = time.time()
                    nadya.sendMessage("u21d04f683a70ee8776c4c58a0358c204","test speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "ความเร็ว : %.3f วินาที" % (took)
                    data = {
                        "type": "flex",
                        "altText": "BotSpeed",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type":"image",
                                "url":"https://i.pinimg.com/originals/f8/c8/70/f8c8701da82c73db661668e32446d880.jpg",
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": a,
                                        "wrap": True,
                                        "color":"#CC0033",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "「 เวลาออน 」\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(nadya.getContact(nadyaMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(nadyaMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ua053fcd4c52917706ae60c811e39d3ea"
                        }
                    }
                    sendTemplate(to, data)

                elif 'ตั้ม: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้ม: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ตั้ม"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))


                elif msg.text in ["Bank","บัญชี","บัญชีตั้ม"]:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["ตั้ม"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ติดต่อ"])),
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.img.in.th/images/9a19ed95328b70134e280bdca0c40524.jpg",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=0808415410",
                                        },
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.img.in.th/images/d00795ae8d3da875a229c9f9a3f48b8f.jpg",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {

                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=0007865772",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ข้อมูลธนาคารตั้ม",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["เรียกกำลังเสริม","Invite"]:
#                  if msg._from in Owner and nadya:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Ticket = nadya.reissueGroupTicket(msg.to)
   #                 ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
#                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    nadya.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    nadya.updateGroup(G)

                elif text.lower() == '/กลุ่ม':
                    if msg._from in admin:
                        groups = nadya.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {}".format(str(no), str(group.name))
                            no += 1
                        ret_ += "\n╚══[ ทั้งหมด {} กลุ่ม ]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))
                elif text.lower() == '/ไอดีกลุ่ม':
                    if msg._from in admin:
                        groups = nadya.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {}".format(str(no), str(group.id))
                            no += 1
                        ret_ += "\n╚══[ ทั้งหมด {} กลุ่ม ]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))

                elif text.lower() == '//กลุ่ม':
                    if msg._from in admin:
                        groups = nadya.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {} \n╠ {}".format(str(no), str(group.name), str(group.id))
                            no += 1
                        ret_ += "\n╚══[ ทั้งหมด {} กลุ่ม ]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))
                elif text.lower() == '/เพื่อน':
                  if msg._from in admin:
                    contactlist = nadya.getAllContactIds()
                    kontak = nadya.getContacts(contactlist)
                    num=1
                    msgs="❋รายชื่อเพื่อนทั้งหมด❋"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n❋รายชื่อเพื่อนทั้งหมด❋\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    nadya.sendMessage(msg.to, msgs)
                elif msg.text in ["ไอดีเพื่อน"]: 
                  if msg._from in admin:
                    gruplist = nadya.getAllContactIds()
                    kontak = nadya.getContacts(gruplist)
                    num=1
                    msgs="═════════ไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    nadya.sendMessage(receiver, msgs)
                elif msg.text.lower().startswith("แปลไทย "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    nadya.sendMessage(msg.to, A)
#=======================================================================================
                elif "gift " in msg.text.lower():
                    red = re.compile(re.escape('gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    nadya.sendMessage(msg)
#=======================================================================================
                elif "รัน: " in msg.text.lower():
                        key = msg.text[-33:]
                        nadya.findAndAddContactsByMid(key)
                        contact = cl.getContact(key)
                        nadya.createGroup("꧁༺ஆืਹໂ√န༻꧂",[key])
                        nadya.sendText(msg,to,"❋ทำการรัน สำเร็จ❋")
                elif "bk " in msg.text:
                        vkick0 = msg.text.replace("bk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = nadya.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    nadya.kickoutFromGroup(msg.to,[target])
                                    nadya.findAndAddContactsByMid(target)
                                    nadya. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass

                elif msg.text in ["ขอลา","ลาทุกคน "]:
                    if msg._from in admin:
                        gs = nadya.getGroup(msg.to)
                        targets = [sender]
                        for target in targets:
                                try:
                                    nadya.sendMessage(msg.to,"Boss ขอมา > Bot จัดให้ *-*")
                                    nadya.kickoutFromGroup(msg.to,[sender])
                                    time.sleep(10)
                                    nadya.findAndAddContactsByMid(target)
                                    nadya. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass


                elif "โทร" == msg.text.lower():
                    nadya.inviteIntoGroupCall(msg.to,[uid.mid for uid in nadya.getGroup(msg.to).members if uid.mid != nadya.getProfile().mid])
                    nadya.sendMessage(msg.to,"➠เชิญเข้าร่วมการโทรสำเร็จ (｡◕‿◕｡) ")
#=======================================================================================
                elif msg.text.lower().startswith("bye "):
                    if msg._from in admin:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           if not target in admin:
                               try:
                                   random.choice(KAC).kickoutFromGroup(msg.to,[target])
                               except:
                                   random.choice(KAC).sendMessage(msg.to,"Error")
#=======================================================================================
#=======================================================================================
                elif msg.text.lower().startswith("บินด่วน "):
                    if msg._from in admin:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           if not target in admin:
                               try:
                                   nadya.kickoutFromGroup(msg.to,[target])
                               except:
                                   nadya.sendMessage(msg.to,"Error")
#=======================================================================================

                elif text.lower() == 'ล้างบัญชีดำ':
                    if msg._from in admin:
                        settings["blacklist"] = {}
                        nadya.sendMessage(msg.to,"ล้างเรียบร้อย")
                    else:
                        nadya.sendMessage(msg.to,"คุณไม่มีอำนาจสั่ง")
    
                elif text.lower() == 'เพิ่มดำ':
                    if msg._from in admin:
                        settings["wblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
                    else:
                        nadya.sendMessage(msg.to,"คุณไม่มีอำนาจสั่ง")
         
                elif msg.text in ["เพิ่มขาว"]:
                    if msg._from in admin:
                        settings["dblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
                    else:
                        nadya.sendMessage(msg.to,"คุณไม่มีอำนาจสั่ง")
#-------------------------------------------------------------------------------
                elif msg.text.lower() == "ล้างเชิญ":
                    if msg._from in admin:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(msg.to,[i])
                        else:
                            nadya.sendMessage(msg.to, "*เรียบร้อย*")
                elif msg.text in ["เชิญ"]:
                    if msg._from in admin:
                        settings["winvite"] = True
                        nadya.sendMessage(msg.to,"ส่งคอนแทคเพื่อเชิญได้เลยคับ")
                    else:
                        nadya.sendMessage(msg.to,"คุณไม่มีอำนาจสั่ง")
#-------------------------------------------------------------------------------
                elif text.lower() == 'บัญชีดำ':
                    if msg._from in admin:
                        if settings["blacklist"] == {}:
                            nadya.sendMessage(msg.to,"ไม่พบผู้ติดดำ")
                        else:
                            nadya.sendMessage(msg.to,"กำลังโหลด......")
                            num=1
                            msgs="══════════List Blacklist═════════"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, nadya.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n══════════List Blacklist═════════\n\nผู้ติดบัญชีดำทั้งหมด :  %i" % len(settings["blacklist"])
                            nadya.sendMessage(msg.to, msgs)
#=======================================================================================
                elif "แบนหมด" in msg.text:
                  if msg._from in Owner:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("แบนหมด","")
                           gs = nadya.getGroup(msg.to)
                           nadya.sendMessage(msg.to,"แบนสมาชิกทุกคนในกลุ่มนี้❋")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                nadya.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in admin:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           nadya.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")

#----------------------------ปักหมุดเฟก BY: NN-------------------------------------------------------------------#                                      
                elif msg.text in ["ลิสหมุด"]:
                    a = nadya.groups
                    ret_ = " 📌รายชื่อกลุ่มที่ปักหมุด📌"
                    num = 1
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            group = nadya.getGroup(manusia)
                            ret_ += "\n {}. {} | {}".format(str(num), str(group.name), str(len(group.members)))
                            num=(num+1)					
                    nadya.sendMessage(to, str(ret_))
#----------------------------------------------------------------------------#
                elif msg.text in ["ปักหมุด"]:
                    apalo["bc"][receiver] = True
                    nadya.sendMessage(receiver,"「📌 ปักหมุดกลุ่มนี้เรียบร้อย 」")
                   
                elif msg.text in ["ลบหมุด"]:
                    try:
                        del apalo["bc"][receiver]
                        nadya.sendMessage(receiver,"「📌 ลบหมุดออกเรียบร้อย 」")
                    except:
                        nadya.sendMessage(receiver,"「📌 ลบหมุดออกเรียบร้อย 」")
#----------------------[บอกหมุด 4 รูปแบบ]------------------------------------------------------#                 
                elif "บอกหมุด: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด: ", "")
                    a = nadya.groups
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nadya.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    nadya.sendMessage(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")  
               
                elif "บอกหมุด2: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด2: ", "")
                    a = nadya.groups
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nadya.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    sendTemplate(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")
             
                elif "บอกหมุด3: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด3: ", "")
                    a = nadya.groups
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nadya.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    nadya.sendMessage(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")
             
                elif "บอกหมุด4: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด4: ", "")
                    a = nadya.groups
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nn4(manusia,(bctxt))
                            time.sleep(1)
                    nadya(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")                   

#----------------------------------------------------------------------------#                                
                elif msg.text.lower().startswith("ค้น "):
#                        if settings["detectMention"] == True:
                            a = removeCmd("", text)
#                            contact = nadya.getContact(sender)
                            b = nadya.findContactsByUserid(a)
                            line = b.mid
                            nadya.sendMessage(msg.to, """🔎 รอสักครู่...
💻 บอทกำลังค้นหาให้ท่าน""")
                            time.sleep(5)
                            nadya.sendMessage(msg.to, "ตรวจพบลิ้งไลน์และคอนแทคนี้")
                            nadya.sendMessage(msg.to,"https://line.me/ti/p/~" + a)
                            nadya.sendContact(to, line)                                                                                           
                            nadya.sendMessage(to,str(hasil))
#----------------------------------------------------------------------------#                                
                elif msg.text.lower().startswith("ไอดีไลน์ "):
#                        if settings["detectMention"] == True:
                            a = removeCmd("", text)
#                            contact = nadya.getContact(sender)
                            b = nadya.findContactsByUserid(a)
                            line = b.mid
                            nadya.sendMessage(msg.to, """🔎 รอสักครู่...
💻 บอทกำลังค้นหาให้ท่าน""")
                            time.sleep(5)
                            nadya.sendMessage(msg.to, "ตรวจพบลิ้งไลน์และคอนแทคนี้")
                            nadya.sendMessage(msg.to,"https://line.me/ti/p/~" + a)
                            nadya.sendContact(to, line)                                                                                           
                            nadya.sendMessage(to,str(hasil))

                elif 'แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               nadya.sendMessage(msg.to,"ทำการแบน สำเร็จ❋")
                               print ("Banned User")
                           except:
                               nadya.sendMessage(msg.to,"ผิดพลาด")
                elif msg.text in ["เตะดำ"]:
                    if msg._from in admin:
                         group = nadya.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             nadya.sendMessage(receiver,"❋ไม่พบคนติดแบนในกลุ่มนี้❋")
                         else:
                             for jj in matched_list:
                                 try:
                                     tumz=[nadya]
                                     kicker=random.choice(tumz)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     nadya.sendMessage(receiver,"❋bye 👋 ")
                                     print ("Blacklist di Kick")
                elif msg.text in ["เตะแบน"]:
                    if msg._from in admin:
                         group = nadya.getGroup(group)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             nadya.sendMessage(receiver,"❋ไม่พบคนติดแบนในกลุ่มนี้❋")
                         else:
                             for jj in matched_list:
                                 try:
                                     tumz=[nadya]
                                     kicker=random.choice(tumz)
                                     kicker.kickoutFromGroup(group,[jj])
                                     print((group,[jj]))
                                 except:
                                     nadya.sendMessage(receiver,"❋bye 👋 ")
                                     print ("Blacklist di Kick")
#=======================================================================================
                elif msg.text.lower().startswith("คท "):
                            a = removeCmd("คท", text)
                            b = nadya.findContactsByUserid(a)
                            line = b.mid
                            nadya.sendMessage(msg.to,"line://ti/p/~" + a)
                            nadya.sendContact(to, line)
                            nadya.sendMessage(to,str(hasil))
                elif msg.text.lower().startswith("แดก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = nadya.getContact(receiver)
                                RhyN_(to, contact.mid)

                elif text.lower() == '//owner':
                    if msg._from in admin:
                        if Owner == []:
                            nadya.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            nadya.sendMessage(msg.to,"กำลังโหลด...")
                            mc = "╔═══════════════\n╠♥ ✿✿✿ 🔥Hack Scan 🔔Win🔔  ✿✿✿ ♥\n╠══✪〘 Owner List 〙✪═══\n"
                            for mi_d in Owner:
                                mc += "╠✪ " +nadya.getContact(mi_d).displayName + "\n"
                            nadya.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 line.me/ti/p/~vipscanner_win 〙\n╚═══════════════")
#=======================================================================================
                elif msg.text in ["ผู้ดูแล","ผู้ควบคุม","ผู้สร้าง"]:
                    if msg._from in admin:
                        if creator == []:
                            nadya.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            nadya.sendMessage(msg.to,"กำลังโหลด...")
                            mc = "╔═══════════════\n╠♥ ✿ผู้ควบคุมบอท✿ ♥\n╠══✪〘 ผู้ควบคุมบอท 〙✪═══\n"
                            for mi_d in creator:
                                mc += "╠✪ " +nadya.getContact(mi_d).displayName + "\n"
                            nadya.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 line.me/ti/p/~botlinegroup 〙\n╚═══════════════")
#=======================================================================================
                elif msg.text in ('บัญชีจอม'):
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                  #      "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                       # "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {

                                        "type": "image",
                                        #"url": "https://www.img.in.th/images/4d060bff76ecd07d7e662bcea76669ec.png",
                                        "url": "https://www.img.in.th/images/60826e9bef9cb0b6eab4b012a5fa952e.png",
                                       # "margin": "xs",
                                       # "aspectMode": "cover",
                                        "aspectRatio": "2:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=0271246609",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ข้อมูลธนาคาร",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ("เลขเจน"):
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                  #      "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                       # "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {

                                        "type": "image",
                                        #"url": "https://www.img.in.th/images/4d060bff76ecd07d7e662bcea76669ec.png",
                                        "url": "https://sv1.picz.in.th/images/2021/06/10/sSUFC9.png",
                                       # "margin": "xs",
                                       # "aspectMode": "cover",
                                        "aspectRatio": "2:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=7862084793",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ข้อมูลธนาคาร",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ("หยิน","เจ๊หยิน","เจ้หยิน","เจ้","เจ๊"):
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                  #      "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                       # "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {

                                        "type": "image",
                                        #"url": "https://www.img.in.th/images/4d060bff76ecd07d7e662bcea76669ec.png",
                                        "url": "https://www.img.in.th/images/b15b8cf7e36b672348463b7516d9e9e8.png",
                                       # "margin": "xs",
                                       # "aspectMode": "cover",
                                        "aspectRatio": "2:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=9790373058",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ข้อมูลธนาคาร",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)


#=======================================================================================
                elif text.lower() == 'เลขตั้ม':
                    run = "[>ตั้ม<]\nนิพนธ์ ฤกษ์มงคลศิลป์"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "080-8-41541-0 รับเลขคลิก",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0808415410"
                        }

                    }
                    sendTemplate(to, data)

                elif text.lower() == 'เลขเบ้นซ์':
                    run = "[เบ้นซ์]\nอรรถสิทธิ์  รอดทับ"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "001-3-38050-3 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=001-3-38050-3"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขแบงค์':
                    run = "[>แบงค์<]\nดิลก หงษ์ทอง"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "0311204270 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0311204270"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขจอม':
                    run = "[>จอม<]\nกิตติศักดิ์  ศรีนุรจน์"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "0271246609 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0271246609"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขแจ็ค':
                    run = """[แจ็ค]
ปราโมทย์ สถิตธำมรงค์"""

                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "0338932480 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0338932480"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขโบว์':
                    run = """[โบว์]
นลินธรณ์ โรจนศศิพงศ์"""
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "0331639001 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0331639001"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขส้ม':
                    run = """[ส้ม] 
อธิตา แก้วมณี"""
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "0641349372 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0641349372"
                        }
                    }
                    sendTemplate(to, data)

                elif text.lower() == 'เลขแนน':
                    run = """[แนน] 
ชนกานต์ บุญประเสริฐ"""
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "020236687586 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/4b61daef4841d446e4dc5e9d09505190.png",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=020236687586"
                        }
                    }
                    sendTemplate(to, data)

#
                elif text.lower() == 'เลขซัน':
                    run = "[>ซัน<]\nทิตยา ใจชุ่มใจ"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "6612381319 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/42a80ac996c9aac14a3dd11de15290c3.png",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=6612381319"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขนุ่น':
                    run = "[>นุ่น<]\nศิริพร แสงตะวัน"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "0628491704 รับเลขคลิก",
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=0628491704"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขหยิน':
                    run = "[>หยิน<]\nวิยดา มาลามาศ"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "9790373058 รับเลขคลิก",
                            # "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(sender).pictureStatus),
                             "iconUrl": "https://www.img.in.th/images/4f810683e3cce4699b6db8b33124a07c.png",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=9790373058"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขกิ๊ก':
                    run = "[กิ๊ก]\nปุณยนุช ขำเนตร์"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "015-3-14111-8 รับเลขคลิก",
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=015-3-14111-8"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'เลขอ๋อง':
                    run = "[อ๋อง]\nเจษฎากร แก้วขาว"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "601-2-19869-6 รับเลขคลิก",
                             "iconUrl": "https://www.img.in.th/images/2f3f4ac5d805bad1a66cff336a7e3739.jpg",
                             "linkUrl": "line://app/1602687308-GXq4Vvk9?type=text&text=601-2-19869-6"
                        }
                    }
                    sendTemplate(to, data)
      
                elif '#แจก ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#แจก ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings[".แจก"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif '#แจก1 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#แจก1 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings[".แจก1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
      
                elif 'แจก: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('แจก: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["แจก"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'แจก1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('แจก1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["แจก1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'เป้าหมาย: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('เป้าหมาย: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["เป้าหมาย"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif  msg.text in ["/แจก","/กิจกรรม","/post"]:
                            #sas = ["https://www.img.in.th/images/c35313bd1b4410a6dae4e48943f51186.png","https://www.img.in.th/images/17b9dd5a84b1ef50cb963e87f34ebc36.png","https://www.img.in.th/images/7f0ed42c0091e52357a5ad87f1e1e587.png","https://www.img.in.th/images/ff4f68d14275272b0397d5a3c2a1a0da.png","https://www.img.in.th/images/e1aa1420a2514782dd5d118c2f1326d5.png","https://www.img.in.th/images/8f3dbb90b70cf3fb4a6cdcb0844160ed.png","https://www.img.in.th/images/2d7c522b8b4ad5361ad8dba97a8ab073.png","https://sv1.picz.in.th/images/2021/04/05/DIlg0n.gif"]

                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["send"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["send1"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "อัพเดทโดย\n┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
      
                elif 'ps: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ps: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["send"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'ps1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ps1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["send1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif  msg.text in [".send"]:
                  if msg._from in admin and nadyaMID:
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["send"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["send1"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "อัพเดทโดย\n┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in ["#send2","#sp"]:
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
                            sa = "{}".format(str(settings["Pic"]))
                            os = "{}".format(str(settings["naname"]))
                            sas = "{}".format(str(settings["Pic2"]))
                            sasa = "{}".format(str(settings["Pic3"]))
                            ew = "{}".format(str(settings["ขนาดภาพ"]))
                            sr = "{}".format(str(settings["sms"]))
                            sk = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                            spp = "{}".format(str(settings["ปุ่มขวา"]))
                            sx = "{}".format(str(settings["LineID"]))
                            sxx = "{}".format(str(settings["link"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
      
                elif 'es: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('es: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["es"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif msg.text in [".แจก","/bonus",".กิจกรรม","/send2"]:
                    gid = "c58baa9af098deb91f3a9965bc9cc52f2"
                    groups = nadya.groups
                    for group in groups:
                        if not group in gid:
#                            try:
 #                               nadya.sendMessage(group, "{}".format(str(text_)))
                            data = {
                                "type": "template",
                                "altText": "✨ Bonus For You\nBy. ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings["แจก"])),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings["แจก1"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in [".คำคม"]:
                    groups = nadya.groups
                    for group in groups:
                        if group in groups:
#                            try:
 #                               nadya.sendMessage(group, "{}".format(str(text_)))
                            data = {
                                "type": "template",
                                "altText": "✨  ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings[".แจก"])),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings[".แจก1"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in ["#คำคม"]:
                    groups = nadya.groups
                    for manusia in apalo["bc"]:
                        if manusia in groups:
#                            try:
 #                               nadya.sendMessage(group, "{}".format(str(text_)))
                            data = {
                                "type": "template",
                                "altText": "✨  ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings[".แจก"])),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings[".แจก1"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(manusia, data)


                elif msg.text in ["คำคม"]:
                            data = {
                                "type": "template",
                                "altText": "✨  ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings[".แจก"])),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings[".แจก1"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)



                elif msg.text in [".แจก","/bonus",".กิจกรรม","/send"]:
                  if msg._from in admin and nadyaMID:
                    gid = "{}".format(str(settings["พิกัด"]))
                    groups = nadya.groups
                    for group in groups:
                        if group in gid:
#                            try:
 #                               nadya.sendMessage(group, "{}".format(str(text_)))
                            data = {
                                "type": "template",
                                "altText": "✨ Bonus For You\nBy. ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings["แจก"])),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings["แจก1"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(group, data)
#                        except:
 #                           naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))

                elif  msg.text in ["#แจก","ระวังมิจฉาชีพ","#post"]:
                            #sas = ["https://www.img.in.th/images/c35313bd1b4410a6dae4e48943f51186.png","https://www.img.in.th/images/17b9dd5a84b1ef50cb963e87f34ebc36.png","https://www.img.in.th/images/7f0ed42c0091e52357a5ad87f1e1e587.png","https://www.img.in.th/images/ff4f68d14275272b0397d5a3c2a1a0da.png","https://www.img.in.th/images/e1aa1420a2514782dd5d118c2f1326d5.png","https://www.img.in.th/images/8f3dbb90b70cf3fb4a6cdcb0844160ed.png","https://www.img.in.th/images/2d7c522b8b4ad5361ad8dba97a8ab073.png","https://sv1.picz.in.th/images/2021/04/05/DIlg0n.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ Bonus For You\nBy. ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings["แจก"])),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings["แจก1"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif  msg.text in ["#sos","#no",".live"]:
                            #sas = ["https://www.img.in.th/images/c35313bd1b4410a6dae4e48943f51186.png","https://www.img.in.th/images/17b9dd5a84b1ef50cb963e87f34ebc36.png","https://www.img.in.th/images/7f0ed42c0091e52357a5ad87f1e1e587.png","https://www.img.in.th/images/ff4f68d14275272b0397d5a3c2a1a0da.png","https://www.img.in.th/images/e1aa1420a2514782dd5d118c2f1326d5.png","https://www.img.in.th/images/8f3dbb90b70cf3fb4a6cdcb0844160ed.png","https://www.img.in.th/images/2d7c522b8b4ad5361ad8dba97a8ab073.png","https://sv1.picz.in.th/images/2021/04/05/DIlg0n.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ Bonus For You\nBy. ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://www.img.in.th/images/4e195f020b1fa6dc814be79b64810b00.gif",
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup",
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif  msg.text in ["#sos","#no","#live"]:
                            #sas = ["https://www.img.in.th/images/c35313bd1b4410a6dae4e48943f51186.png","https://www.img.in.th/images/17b9dd5a84b1ef50cb963e87f34ebc36.png","https://www.img.in.th/images/7f0ed42c0091e52357a5ad87f1e1e587.png","https://www.img.in.th/images/ff4f68d14275272b0397d5a3c2a1a0da.png","https://www.img.in.th/images/e1aa1420a2514782dd5d118c2f1326d5.png","https://www.img.in.th/images/8f3dbb90b70cf3fb4a6cdcb0844160ed.png","https://www.img.in.th/images/2d7c522b8b4ad5361ad8dba97a8ab073.png","https://sv1.picz.in.th/images/2021/04/05/DIlg0n.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ Bonus For You\nBy. ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/05/29/P6qiGJ.gif",
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup",
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif  msg.text in ["#sos","#สด","#livenow"]:
                            sas = ["https://www.img.in.th/images/84a1fa9bd0cba4e9e13917c610a3a534.gif"]
#                            sas = ["https://www.img.in.th/images/910c439798f50b46e57a3a0de83cd28d.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ Bonus For You\nBy. ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "1:1",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup",
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

      
                elif msg.text in ('/1','แทค'):
                      if msg._from in admin:
                        group = nadya.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//20
                        for a in range(k+1):
                            txt = u''
                            s=0
                            b=[]
                            for i in group.members[a*20 : (a+1)*20]:
                                b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                s += 7
                                txt += u'@Alin \n'
                            nadya.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        else:
#                            nadya.sendMessage(to, "ทั้งหมด {}  คน".format(str(len(nama))))          
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "แทคแล้ว ทั้งหมด {}  คน".format(str(len(nama))),
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900"
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#999999",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#FF00FF",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อเช่าบอท",
                                                    "uri": "https://line.me/ti/p/~botlinegroup",
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "เรียกสมาชิกทุกท่าน",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=======================================================================================
                elif msg.text in ["ปฏิทิน","วัน","วันที่","วันนี้","วันอะไร","วันที่เท่าไร","ลืมวันที่","เวลา","30","กด30","กด 30"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "🌴ปฏิทินโดย 🔥Hack Scan 🔔Win🔔🌴\n\n🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\n🍁" + hasil + "\n🍁 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🍁 เวลา :[ " + timeNow.strftime('%H:%M:%S') + " ]" + "🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\nBY: 🔥Hack Scan 🔔Win🔔➣ "
                    nadya.sendMessage(msg.to, readTime)
#=======================================================================================
                elif text.lower() == 'เปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                nadya.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            nadya.sendMessage(msg.to, "เริ่มจับ คนอ่าน :\n" + readTime)
                            
                elif text.lower() == 'ปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        nadya.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        nadya.sendMessage(msg.to, "ปิดเรียบร้อย:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        nadya.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        nadya.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'ใครอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            nadya.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = nadya.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ คนที่อ่าน ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ ขณะนี้เวลา ]: \n" + readTime
                        try:
                            nadya.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        nadya.sendMessage(receiver,"กรุณาเปิดคำสั่ง ก่อนทำรายการ .")
                        
#==============================================================================#
                elif text.lower() == 'กลับมา':
                    ginvited = nadya.ginvited
                    if ginvited != [] and ginvited != None:
                        for gid in ginvited:
                            nadya.rejectGroupInvitation(gid)
                            nadya.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                    else:
                        nadya.sendMessage(to, "Tidak ada undangan yang tertunda")
                elif text.lower() == 'ล้างแชท':
                  if msg._from in admin:
                    nadya.removeAllMessages(op.param2)
                    nadya.sendMessage(to, "Berhasil hapus semua chat")

                elif text.lower() == 'time':
                    nadya.sendMessage(to, "Goblok cek sendiri di tanggal jangan manja")

                    
                elif msg.text.lower().startswith(".ประกาศ "):
                                delcmd = msg.text.split(" ")
                                get = msg.text.replace(delcmd[0]+" ","").split(">")
                                kw = get[0]
                                ans = get[1]
                           # groups = nadya.groups
                         #   for group in groups:
                                sa = "{}".format(str(kw))
                                data = {
                                    "type": "flex",
                                    "altText": "🌸ประกาศสำคัญ🌸",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                   "type": "text",
                                                   "text": sa,
                                                   "wrap": True,
                                                   "align": "center",
                                                   "gravity": "center",
                                                   "size": "md"
                                               },
                                               {  
                                                   "type":"text",
                                                   "text":" "
                                               },
                                               {
                                                   "type":"button",
                                                   "style":"primary",
                                                   "color":"#CC0033",
                                                   "action": {
                                                       "type": "uri",
                                                       "label": "คลิ๊ก",
                                                       "uri": "{}".format(ans),
                                                   }
                                               }
                                           ]
                                        }
                                    }
                                }
                                sendTemplate(to, data)
                elif msg.text in ["สแกน","สแกนสล็อต"]:
                            sas = ["https://www.img.in.th/images/f97f5f17be8ff782d0c487d530b99883.gif"]
                                   #https://www.img.in.th/images/bb3c66ad84f297e0eb658d005e03000a.gif","https://www.img.in.th/images/acaf2cf7699fe1b13bf3237d7ad39cad.gif","https://www.img.in.th/images/38f937b92768be3c2f899f8ec7582d28.gif","https://www.img.in.th/images/e597526245a456cd067ecd344eac0c0d.gif","https://www.img.in.th/images/88ada2d29e2ab54f7f77b8b00db09d59.gif","https://www.img.in.th/images/d8529da83ea57b87bef874f3efcaef65.gif","https://www.img.in.th/images/fc57501b3e1e28e130bb0f594ac582d7.gif","https://www.img.in.th/images/48951edff3a50ad9c0bda847041a23e0.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "http://bit.ly/3dNU4rj"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "หิว":
                            sas = ["https://www.img.in.th/images/d8c770a968ead3ecab9107daee2c109e.gif"]
                            data = {
                                "type": "template",
                                "altText": "┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["บรื้อ"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxb8ru.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["สุดยอด"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxbrU0.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["นอนนะ"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxbnNR.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["หรา"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxbup8.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["เอาที่สบายใจ"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxbCjz.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["แดนซ์"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxb29q.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["ฮ่าๆ"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxbPma.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["ชิ"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/22/sxbAsf.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================
                if text.lower().startswith("ลบเวลา "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del DDATE[getx]
                        nadya.sendMessage(msg.to, "ประกาศเวลา " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('time.json','w','utf-8')
                        json.dump(DDATE, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
#----------------------------------------------------------------------------#                        
                if text.lower().startswith("ประกาศ4 "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        DDATE[kw] = ans
                        f=codecs.open('time.json','w','utf-8')
                        json.dump(DDATE, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nadya.sendMessage(msg.to,"เวลา: " + str(kw) + "\nประกาศ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
#----------------------------------------------------------------------------#                        
                if text.lower() == "เช็คเวลา":
                    lisk = "เช็คดูประกาศเวลา"
                    for i in DDATE:
                        lisk+="\nเวลา: "+str(i)+"\nประกาศ: "+str(DDATE[i])
                    nadya.sendMessage(to, str(lisk))
#----------------------------------------------------------------------------#                    
#--------------------------------------------------------------------------------------------------------#                            
                if text.lower() == "ประกาศ4":
                    ret = "วิธีการใช้ประกาศกำหนดเวลา :\n"
                    ret += "ประกาศ เวลา:นาที:วินาที;;ข้อความประกาศ\n"
                    ret += "ดูตัวอย่าง เช่น :\n"
                    ret += "ประกาศ4 08:30:00;;มอนิ่งครับ\n"
                    ret += "แบบนี้ก็จะประกาศตอนที่ 08:30:00\n"
                    nadya.sendMessage(to, str(ret))
#----------------------------------------------------------------------------#                    
                elif msg.text in ["หา","หาา","หาาา","เล้ง","เล๊ง","ไอ้เล้ง","ไอ้เล๊ง","หาาาา"]:
                            sas = ["https://sv1.picz.in.th/images/2021/06/26/sbtujy.gif","https://sv1.picz.in.th/images/2021/06/26/sbhuIR.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["วอท","what","What","อะไร"]:
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://sv1.picz.in.th/images/2021/06/17/swBQOg.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif text.lower() == "gif":
                            sas = ["https://www.img.in.th/images/bb3c66ad84f297e0eb658d005e03000a.gif","https://www.img.in.th/images/acaf2cf7699fe1b13bf3237d7ad39cad.gif","https://www.img.in.th/images/38f937b92768be3c2f899f8ec7582d28.gif","https://www.img.in.th/images/e597526245a456cd067ecd344eac0c0d.gif","https://www.img.in.th/images/88ada2d29e2ab54f7f77b8b00db09d59.gif","https://www.img.in.th/images/d8529da83ea57b87bef874f3efcaef65.gif","https://www.img.in.th/images/fc57501b3e1e28e130bb0f594ac582d7.gif","https://www.img.in.th/images/48951edff3a50ad9c0bda847041a23e0.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "Avt":
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/e8e7684d54067d37f6c15af6bda0b0c8.png",
                                                "margin": "xxl",
                                                "aspectMode": "cover",
                                                "aspectRatio": "1:1",
                                                "size": "full",
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/3a6ff09edfd992a564fdf5a6a550e890.jpg",
                                                "margin": "xxl",
                                                "aspectMode": "cover",
                                                "aspectRatio": "1:1",
                                                "size": "full",
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/7acb043dcbb7932cd85ab60cb1b4c7cd.png",
                                                "margin": "xxl",
                                                "aspectMode": "cover",
                                                "aspectRatio": "1:1",
                                                "size": "full",
                                            },
                                        ]
                                    },
                                },

                            ]
                            data = {
                                "type": "flex",
                                "altText": "SLOT THAI",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif 'คำสอน: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('คำสอน: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["คำสอน"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ติดต่อ: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ติดต่อ: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ติดต่อ"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif msg.text.lower().startswith(".แจ้งข่าว "):
                  if msg._from in admin and nadyaMID:
                    delcmd = msg.text.split(" ")
                    get = msg.text.replace(delcmd[0]+" ","").split(">")
                    kw = get[0]
                    ans = get[1]
                    sa = "{}".format(str(kw))
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            data = {
                                "type": "template",
                                "altText": "✨ แจ้งข่าวสารโดย\n ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(kw)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(ans)),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text.lower().startswith("#แจ้งข่าว "):
                  if msg._from in admin and nadyaMID:
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split(">")
                            kw = get[0]
                            ans = get[1]
                            data = {
                                "type": "template",
                                "altText": "✨ แจ้งข่าวสารโดย\n ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(kw)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(ans)),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)


                elif text.lower() == ".ติดต่อ":
                  if msg._from in admin and nadyaMID:
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            sas = ["https://www.img.in.th/images/c35313bd1b4410a6dae4e48943f51186.png","https://www.img.in.th/images/17b9dd5a84b1ef50cb963e87f34ebc36.png","https://www.img.in.th/images/7f0ed42c0091e52357a5ad87f1e1e587.png","https://www.img.in.th/images/ff4f68d14275272b0397d5a3c2a1a0da.png","https://www.img.in.th/images/e1aa1420a2514782dd5d118c2f1326d5.png","https://www.img.in.th/images/8f3dbb90b70cf3fb4a6cdcb0844160ed.png","https://www.img.in.th/images/2d7c522b8b4ad5361ad8dba97a8ab073.png","https://sv1.picz.in.th/images/2021/04/05/DIlg0n.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ แจ้งข่าวสารโดย\n ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "3:4",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings["ติดต่อ"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in ["ติดต่อ","Contact me","""Bot not working
Please Contact me"""]:
                            sas = ["https://www.img.in.th/images/c35313bd1b4410a6dae4e48943f51186.png","https://www.img.in.th/images/17b9dd5a84b1ef50cb963e87f34ebc36.png","https://www.img.in.th/images/7f0ed42c0091e52357a5ad87f1e1e587.png","https://www.img.in.th/images/ff4f68d14275272b0397d5a3c2a1a0da.png","https://www.img.in.th/images/e1aa1420a2514782dd5d118c2f1326d5.png","https://www.img.in.th/images/8f3dbb90b70cf3fb4a6cdcb0844160ed.png","https://www.img.in.th/images/2d7c522b8b4ad5361ad8dba97a8ab073.png","https://sv1.picz.in.th/images/2021/04/05/DIlg0n.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ แจ้งข่าวสารโดย\n ┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "margin": "xxl",
                                            "aspectMode": "cover",
                                            "aspectRatio": "3:4",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "{}".format(str(settings["ติดต่อ"])),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == 'me':
                    contact = nadya.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "꧁༺ஆืਹໂ√န༻꧂","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#FF69B4","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1636169025-yQ7bGMVA?type=profile"},"type":"text","text":"꧁༺ஆืਹໂ√န༻꧂","align":"center","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#FF69B4","size":"xs","wrap":True,"action":{"type":"uri","uri":"https://line.me/ti/p/~bot.tumz"},"type":"text","text":"ติดต่อเช่าบอท","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#FFD2E6"},"body":{"backgroundColor":"#ffffff"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://i.ibb.co/ZXzddDh/Pics-Art-01-07-05-35-09.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.ibb.co/GdwQtdS/Screenshot-2018-1215-233501.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://media.giphy.com/media/qqWB4u3mrTlrG/giphy.gif"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.pinimg.com/originals/a6/94/ec/a694ec9773292abec803f07befd73e74.gif"},{"type":"separator","color":"#FF69B4"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"ข้อมูล สมาชิก","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#FF69B4","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#422002"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})
#=======================================================================================
                elif msg.text in ("ข้อความ1"):
                    nadya.sendMessage(msg.to, str(settings["sms"]))
                elif msg.text in ("ข้อความ2"):
                    nadya.sendMessage(msg.to, str(settings["sms1"]))
                
                elif 'L2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["link2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["link3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif 'รูป2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Pic2"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'รูป3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Pic3"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
#                          nadya
                elif 'ข้อความ2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["sms1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ2/2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ2/2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["sms2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ2/3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ2/3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["sms3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["sms"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ1/2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ1/2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["sms02"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ1/3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ1/3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["sms03"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'รูปปก: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูปปก: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["รูปปก"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))


                elif 'ตั้งรูป: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งรูป: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Pic"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
#                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ID: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ID: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["LineID"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ID2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ID2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["LineID2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ID3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ID3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["LineID3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ชื่อโชว์: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ชื่อโชว์: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["naname"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปรับขนาด: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปรับขนาด: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ขนาดภาพ"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งเว็ป: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["web"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งเว็ป2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["web2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งเว็ป3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["web3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้งรูป: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้งรูป: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["link"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งลิ้ง2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งลิ้ง2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["link2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งลิ้ง3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งลิ้ง3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["link3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif 'G: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('G: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["gid"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#ข้อความ#2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#ข้อความ#2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ3/2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ3/2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อความ3/3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อความ3/3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#ข้อความ#3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#ข้อความ#3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#ข้อความ#1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#ข้อความ#1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มซ้าย: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มซ้าย: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มซ้าย"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มซ้าย2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มซ้าย2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มซ้าย2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มซ้าย3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มซ้าย3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มซ้าย3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มขวา: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มขวา: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มขวา"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มขวา2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มขวา2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มขวา2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มขวา3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มขวา3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มขวา3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'สีบน: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('สีบน: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["color"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'สีกลาง: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('สีกลาง: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["color1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'สีล่าง: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('สีล่าง: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["color2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'สี: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('สี: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["color3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif text.lower() == "feeling":
                           # sas = ["https://www.img.in.th/images/bb3c66ad84f297e0eb658d005e03000a.gif","https://www.img.in.th/images/acaf2cf7699fe1b13bf3237d7ad39cad.gif","https://www.img.in.th/images/38f937b92768be3c2f899f8ec7582d28.gif","https://www.img.in.th/images/e597526245a456cd067ecd344eac0c0d.gif","https://www.img.in.th/images/88ada2d29e2ab54f7f77b8b00db09d59.gif","https://www.img.in.th/images/d8529da83ea57b87bef874f3efcaef65.gif","https://www.img.in.th/images/fc57501b3e1e28e130bb0f594ac582d7.gif","https://www.img.in.th/images/48951edff3a50ad9c0bda847041a23e0.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "https://www.img.in.th/images/4d2beb3dc472b1ec54e9b2a1ab5e52ef.gif",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup",
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["#send","#sp"]:
                  if msg._from in admin and nadyaMID:
                    gid = "{}".format(str(settings["พิกัด"]))
                    groups = nadya.groups
                    for group in groups:
                        if group in gid:
                            sa = "{}".format(str(settings["Pic"]))
                            os = "{}".format(str(settings["naname"]))
                            sas = "{}".format(str(settings["Pic2"]))
                            sasa = "{}".format(str(settings["Pic3"]))
                            ew = "{}".format(str(settings["ขนาดภาพ"]))
                            sr = "{}".format(str(settings["sms"]))
                            sk = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                            spp = "{}".format(str(settings["ปุ่มขวา"]))
                            sx = "{}".format(str(settings["LineID"]))
                            sxx = "{}".format(str(settings["link"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in ["*post",""]:
                            sa = "{}".format(str(settings["Pic"]))
                            os = "{}".format(str(settings["naname"]))
                            sas = "{}".format(str(settings["Pic2"]))
                            sasa = "{}".format(str(settings["Pic3"]))
                            ew = "{}".format(str(settings["ขนาดภาพ"]))
                            sr = "{}".format(str(settings["sms"]))
                            sk = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                            spp = "{}".format(str(settings["ปุ่มขวา"]))
                            sx = "{}".format(str(settings["LineID"]))
                            sxx = "{}".format(str(settings["link"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["#888","spr","spr"]:
                            sa = "{}".format(str(settings["Pic"]))
                            os = "{}".format(str(settings["naname"]))
                            sas = "{}".format(str(settings["Pic2"]))
                            sasa = "{}".format(str(settings["Pic3"]))
                            ew = "{}".format(str(settings["ขนาดภาพ"]))
                            sr = "{}".format(str(settings["sms"]))
                            sr2 = "{}".format(str(settings["sms02"]))
                            sr3 = "{}".format(str(settings["sms03"]))
                            sk = "{}".format(str(settings["web"]))
                            sk2 = "{}".format(str(settings["web2"]))
                            sk3 = "{}".format(str(settings["web3"]))
                            ks = "{}".format(str(settings["color"]))
                            kk = "{}".format(str(settings["color1"]))
                            kkk = "{}".format(str(settings["color2"]))
                            kkkk = "{}".format(str(settings["color3"]))
                            sw = "{}".format(str(settings["sms1"]))
                            sw2 = "{}".format(str(settings["sms2"]))
                            sw3 = "{}".format(str(settings["sms3"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            sb2 = "{}".format(str(settings["ปุ่ม2"]))
                            sb3 = "{}".format(str(settings["ปุ่ม3"]))
                            sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                            sp2 = "{}".format(str(settings["ปุ่มซ้าย2"]))
                            sp3 = "{}".format(str(settings["ปุ่มซ้าย3"]))
                            spp = "{}".format(str(settings["ปุ่มขวา"]))
                            spp2 = "{}".format(str(settings["ปุ่มขวา2"]))
                            spp3 = "{}".format(str(settings["ปุ่มขวา3"]))
                            sx = "{}".format(str(settings["LineID"]))
                            sx2 = "{}".format(str(settings["LineID2"]))
                            sx3 = "{}".format(str(settings["LineID3"]))
                            sxx = "{}".format(str(settings["link"]))
                            sxx2 = "{}".format(str(settings["link2"]))
                            sxx3 = "{}".format(str(settings["link3"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr2,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sas,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx2),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw2,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb2,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp2),
                                                    "uri": "{}".format(sk2),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp2),
                                                    "uri": "{}".format(sx2),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr3,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sasa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx3),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw3,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb3,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp3),
                                                    "uri": "{}".format(sk3),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp3),
                                                    "uri": "{}".format(sx3),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=======================================================================================
                elif msg.text.lower().startswith("/เปิดวาป: "):
                  if msg._from in admin and nadyaMID:
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                  #  gid = ["c262893d7c26ee5bc2f7401d0efb0492c","c6b2c6391f5132d14b5738ea84c1abb9b","c6fa1b8da81d7ad3b3bde7ba5fab3732e","c815d106dd352db79686cd48c88941b2b","c22f1f5fb7745c967dc4bf9cfc9627a77","cf647371dc18910667e02008be2060e2a","cd0dbba09fed52adf079f23b61a64b15f","c1db995a182ca749b83557c1c2bde2c88","ceb1fbba1d2e06c30bac6d226c8f27b87"]
                    groups = nadya.groups
                    for group in groups:
                        if group in group:
                            try:
                                nadya.sendMessage(group, "{}".format(str(text_)))
                            except:
                              #  time.sleep(10)
                            #    naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                                nadya.sendMessage(msg.to, "ส่งแล้ว ทั้งหมด 278 กลุ่ม")
                elif msg.text.lower().startswith("#ประกาศ: "):
                  if msg._from in admin and nadyaMID:
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    gid = ["{}".format(str(settings["gid"]))]
                    groups = nadya.groups
                    for group in groups:
                        if group in gid:
                            try:
                                nadya.sendMessage(group, "{}".format(str(text_)))
                            except:
                                naya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))

                elif 'การันตี: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('การันตี: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["การันตี"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))


                elif msg.text in ["#888","amb1689","1689"]:
                            sa = "{}".format(str(settings["Piic"]))
                            os = "{}".format(str(settings["naname"]))
                            sas = "{}".format(str(settings["Piic2"]))
                            sasa = "{}".format(str(settings["Piic3"]))
                            ew = "{}".format(str(settings["ขนาดภาพ"]))
                            sr = "{}".format(str(settings["smms"]))
                            sr2 = "{}".format(str(settings["smms02"]))
                            sr3 = "{}".format(str(settings["smms03"]))
                            sk = "{}".format(str(settings["weeb"]))
                            sk2 = "{}".format(str(settings["weeb2"]))
                            sk3 = "{}".format(str(settings["weeb3"]))
                            ks = "{}".format(str(settings["color"]))
                            kk = "{}".format(str(settings["color1"]))
                            kkk = "{}".format(str(settings["color2"]))
                            kkkk = "{}".format(str(settings["color3"]))
                            sw = "{}".format(str(settings["smms1"]))
                            sw2 = "{}".format(str(settings["smms2"]))
                            sw3 = "{}".format(str(settings["smms3"]))
                            sb = "{}".format(str(settings["aปุ่ม"]))
                            sb2 = "{}".format(str(settings["aปุ่ม2"]))
                            sb3 = "{}".format(str(settings["aปุ่ม3"]))
                            sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                            sp2 = "{}".format(str(settings["ปุ่มซ้าย2"]))
                            sp3 = "{}".format(str(settings["ปุ่มซ้าย3"]))
                            spp = "{}".format(str(settings["ปุ่มขวา"]))
                            spp2 = "{}".format(str(settings["ปุ่มขวา2"]))
                            spp3 = "{}".format(str(settings["ปุ่มขวา3"]))
                            sx = "{}".format(str(settings["LiineID"]))
                            sx2 = "{}".format(str(settings["LiineID2"]))
                            sx3 = "{}".format(str(settings["LiineID3"]))
                            sxx = "{}".format(str(settings["liink"]))
                            sxx2 = "{}".format(str(settings["liink2"]))
                            sxx3 = "{}".format(str(settings["liink3"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr2,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sas,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx2),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw2,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb2,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp2),
                                                    "uri": "{}".format(sk2),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp2),
                                                    "uri": "{}".format(sx2),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr3,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sasa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx3),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw3,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb3,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp3),
                                                    "uri": "{}".format(sk3),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp3),
                                                    "uri": "{}".format(sx3),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif 'รูป2 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป2 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Piic2"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif 'รูป3 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูป3 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Piic3"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
#                          nadya
                elif 'ข้อ2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["smms1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ2/2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ2/2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["smms2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ2/3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ2/3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["smms3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["smms"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ1/2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ1/2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["smms02"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ1/3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ1/3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["smms03"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'รูปปก: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('รูปปก: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["รูปปก"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))


                elif 'ตั้งรูป ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งรูป ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Piic"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
#                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ID ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ID ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["LiineID"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ID2 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ID2 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["LiineID2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ID3 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ID3 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["LiineID3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ชื่อโชว์: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ชื่อโชว์: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["naname"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปรับขนาด: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปรับขนาด: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ขนาดภาพ"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งเว็ป ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["weeb"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งเว็ป2 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป2 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["weeb2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งเว็ป3 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งเว็ป3 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["weeb3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้งรูป ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้งรูป ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["liink"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งลิ้ง2 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งลิ้ง2 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["liink2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ตั้งลิ้ง3 ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตั้งลิ้ง3 ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["liink3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif '#ข้อความ#2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#ข้อความ#2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["aปุ่ม"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ3/2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ3/2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["aปุ่ม2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ข้อ3/3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ข้อ3/3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["aปุ่ม3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#ข้อความ#3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#ข้อความ#3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '#ข้อความ#1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('#ข้อความ#1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่ม1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มซ้าย: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มซ้าย: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มซ้าย"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มซ้าย2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มซ้าย2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มซ้าย2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มซ้าย3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มซ้าย3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มซ้าย3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มขวา: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มขวา: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มขวา"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มขวา2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มขวา2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มขวา2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ปุ่มขวา3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ปุ่มขวา3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ปุ่มขวา3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))


#=======================================================================================
                elif msg.text in ["#sp","/sp","gsp"]:
                    sa = "{}".format(str(settings["Pic"]))
                    os = "{}".format(str(settings["naname"]))
                    sas = "{}".format(str(settings["Pic2"]))
                    sasa = "{}".format(str(settings["Pic3"]))
                    ew = "{}".format(str(settings["ขนาดภาพ"]))
                    sr = "{}".format(str(settings["sms"]))
                    sk = "{}".format(str(settings["web"]))
                    ks = "{}".format(str(settings["color"]))
                    kk = "{}".format(str(settings["color1"]))
                    kkk = "{}".format(str(settings["color2"]))
                    kkkk = "{}".format(str(settings["color3"]))
                    sw = "{}".format(str(settings["sms1"]))
                    sb = "{}".format(str(settings["ปุ่ม"]))
                    sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                    spp = "{}".format(str(settings["ปุ่มขวา"]))
                    sx = "{}".format(str(settings["LineID"]))
                    sxx = "{}".format(str(settings["link"]))
                    gid = ["cac46207f6f78386e1fac59f0305c1a94","c354133f66740a7d6f3a9018df567ad6e","c6a439fd9d0ffaef2a38344f8d4088df7","c23321553d8bd5d5b7545b0980d19dc6b","c4640380e64d1dd8c4fd1c9772db2fbb5","ce8eeccbbd084e9ec2685e922f4fed65a","cae38d1640dfcf06815f8ec473b8e111b","cc6c05c367aa51734dfac615171073b75","c0ee3727b3b0e148e6189eadda476c4d1","c2b4211f9458ac14b2237a89513fe9858","c3a7e92cafa09a167bd0ffe2076b56b81","c4ea9f4e5869b1c2a1692ac74b40c0b2f","cdf1fa504b2e017039ba8cd5e47aa4c1c","ca2dee44b898d55ae0acacba384054b4a","c629259e662877e3f5fb8eb27f6f01a13","c0d282576f555daccdc630683b7bcf021","cf9bf57de6b8b362ed73af090e365b5e6","c059f2ea994a8e795f1f28ad2fdf0959d","ca3607ad81b1e0e5644494c460b4e9273","c2240bac4752782029428592de1c12b88","c7d536c169ecbb5ca8c560b116340fe37", "cabae7dcba42b97d65a723ba6fd1a031c","ca987d67f8784cda7cb581f4016e00ab1","ccf2f4f27506805a6bbb0e31a46406bb3","c1fddb14f162784ecad0587bbabfb65f9","c6c1441766ca531132a1b9daccdd92c68","cc60cacae74ba9fa92ece8a69fbf1e6a2","c4ca2e24cd1af3b2ee05c3be6c3771694","cc2e0649f096c32c2d236088b2e0b9c10","c2ec313e61c136302bbaf211ae55cd5fc","c418bbba853b267757acb88d5ec816668","c2a03997236fc3c77b314fdb04ab3e33f","c0209cea5412a5a04cf8f438acaa57d2b","c10f85c4ba099b3155c6dfe9f063b9f95","cbb70b9e307f643a8920a256ce8fbbb75","c467c36113d978139d68a73a1b830134","c42dd587c1b91459a60b7b10f2db32163","c7d6c821cc34512f125221df047f7231f","c912f108e78c0a6633806059cd238d7ba","c496682ac1570d02bf381534c2f990427","c303ebefa0d3174f985754e468b87d7b9","c38e761eeb7a3fe94e1ab52baf3962f68","c3c7d4cd551045d45eb94c1927a37f660","cb127030cf9c7f3d42f53b94a18ff174e","cbbef9d9662daa6eed29d6777479f8720","c64d9f9370c996c98fc8f069bfee87485","cf39fb2883995e9529c370851119cb5ad","cd5411af1eff4064165a9617c251aac8f","cc51c5862664c85205ba1f57bfd0c6ef3","cb408ae181d75421618d6d4051d104eeb","c279d914d8ceb47dec88c18df11c9aed7","cfb915c5e310ebe56f7dd43d828c26935","c0eb56ee674c52876e5c2ab83125b404a","ce23892feebfeb2326da1326e6d2cf10d","c751db47ba43eb623a071193d0af72b17","cd6e2567922a803c4c36d6af27eda9864","cf647371dc18910667e02008be2060e2a","cd21b8c67bc64e1718cd35465f93953a3","c0ae690ac4a36f71c4e7597f7ba8d0d59","c8d0bc07e17a046d45ee1ef30acba0ce4","c249f80fb321fe7e41bc09b4c22060672","c4e837df9fafeb596c01bf542fd3f9521","c4ca2e24cd1af3b2ee05c3be6c3771694","cd5411af1eff4064165a9617c251aac8f","ca6509282665faa470ccb5ea3a8235572","cac46207f6f78386e1fac59f0305c1a94","cf44a1789897314549b09a5451320de49","cb006095a77cd43f72bea4211bdc9e1af","cdf14ce8ed0dc49d503788057dddcb5bb","c85e09e59d3ca5f0b81825f7bf225b02c","c059f2ea994a8e795f1f28ad2fdf0959d","c279d914d8ceb47dec88c18df11c9aed7","c02d725e0da6c38850ffd673583c26aca","c6c1441766ca531132a1b9daccdd92c68","ccfd912f1bda431470b6c0dc384a9a806","c3a7e92cafa09a167bd0ffe2076b56b81","c15113bf5e31b647e2b29797ffa0286b2","cabc08ba15cd55900beb1240d048e02a8","cc2e0649f096c32c2d236088b2e0b9c10","c3ae0bf84cbbe540d2578c0718f7c6eaa","cdc50a6afd5e0ad2cd8761e47913840e4","c69c7e348775236f690392df349d9875a","c303ebefa0d3174f985754e468b87d7b9","c20be9ce3929a03acec119af296ce2d6f","c924372a7f078b783ae482a99f4736984","c6e57f9b2872d16cfe55029a770773b8e","c3813a2c0ca3db9ce5a7d065c177ea406","c6e6cc4f2a4e4e057dbc360fb1d38246e","cec5b3531b359ae5bf02656f7a84597dd","cec97a2975131c3f919371cbec87400a3","cfce29ca97498fa6349f2f3b46de81a01","caa3fd51a7d1f7dee5a396be567c72fe1","c1927688c5b56698d4e29382e8e866454","c81653f3431216839ad449d7c8e47277e","cc60cacae74ba9fa92ece8a69fbf1e6a2","c73253f2b25e2235da0e31d9ba905f726","c23321553d8bd5d5b7545b0980d19dc6b","cb340597fb363a68d877ceb78e84f29be","c674d743f641a91cb89b08dc9c4ab902c","cb5ecd483978befcc81d5c628fe7e9940","c304b8a643ea118eb1aa1358670949bf7","c1fc890dd23fd0ca610fe39dff3669202","cb980433e52186897632a0a346aff1171","c2ec313e61c136302bbaf211ae55cd5fc","cf9bf57de6b8b362ed73af090e365b5e6","c5c40cb4187d5976e43fdf3ce471f08f0","c629259e662877e3f5fb8eb27f6f01a13","c1ba7c32a076924a31ae21e395448e955","cec8ea6305a85b396f40baeb45233d423","c75cf8db690caadf1544ed66ee6e7f216","c6a439fd9d0ffaef2a38344f8d4088df7","c6b1d27983de2361435ac3da3df10fb02","c375781c112d6da8afc93a11b7d6a3cca"]
                    groups = nadya.groups
                   # groups = nadya.groups
                    for group in groups:
                        if group in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sas,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif text.lower() == "ตู้ปลา":
#                            sas = ["https://www.img.in.th/images/d16b7a33e0912e40107afeb7737a23c7.gif"]
                            data = {
                                "type": "template",
                                "altText": "༺ஆืਹໂ√န༻",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(str(settings["ตู้ปลา"])),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Something.-I-can't-say-here"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif 'ตู้ปลา: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ตู้ปลา: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ตู้ปลา"] = spl
                          nadya.sendImageWithURL(to, "{}".format(str(spl)))
                elif msg.text.lower().startswith(".#ประกาศ "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split(">")
                            kw = get[0]
                            ans = get[1]
                            groups = nadya.groups
                            for group in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "🌸ประกาศสำคัญ🌸",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "color":"#000000",
                                            "contents": [
                                                {
                                                   "type": "image",
                                                   "url": "{}".format(str(settings["รูปปก"])),
                                                   "size": "full"
                                               },
                                               {
                                                   "type": "text",
                                                   "text": "{}".format(str(kw)),
                                                   "wrap": True,
                                                   "align": "center",
                                                   "gravity": "center",
                                                   "size": "md"
                                               },
       
                                               {  
                                                   "type":"text",
                                                   "text":" "
                                               },
                                               {
                                                   "type":"button",
                                                   "style":"primary",
                                                   "color":"#CC0033",
                                                   "action": {
                                                       "type": "uri",
                                                       "label": "คลิ๊ก",
                                                       "uri": "{}".format(ans),
                                                   }
                                               }
                                           ]
                                        }
                                    }
                                }
                                sendTemplate(group, data)
                elif msg.text.lower().startswith(".#ประกาส "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split(">")
                            kw = get[0]
                            ans = get[1]
                            groups = nadya.groups
                            for group in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "🌸ประกาศสำคัญ🌸",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "color":"#000000",
                                            "contents": [
                                                {
                                                   "type": "image",
                                                   "url": "{}".format(str(settings["รูปปก"])),
                                                   "size": "full"
                                               },
                                               {
                                                   "type": "text",
                                                   "text": "{}".format(str(kw)),
                                                   "wrap": True,
                                                   "align": "center",
                                                   "gravity": "center",
                                                   "size": "md"
                                               },
       
                                               {  
                                                   "type":"text",
                                                   "text":" "
                                               },
                                               {
                                                   "type":"button",
                                                   "style":"primary",
                                                   "color":"#CC0033",
                                                   "action": {
                                                       "type": "uri",
                                                       "label": "คลิ๊ก",
                                                       "uri": "{}".format(ans),
                                                   }
                                               }
                                           ]
                                        }
                                    }
                                }
                                sendTemplate(to, data)



                elif msg.text in ["#spr","/spr","gspr"]:
                        sa = "{}".format(str(settings["Pic"]))
                        os = "{}".format(str(settings["naname"]))
                        sas = "{}".format(str(settings["Pic2"]))
                        sasa = "{}".format(str(settings["Pic3"]))
                        ew = "{}".format(str(settings["ขนาดภาพ"]))
                        sr = "{}".format(str(settings["sms"]))
                        sr2 = "{}".format(str(settings["sms02"]))
                        sr3 = "{}".format(str(settings["sms03"]))
                        sk = "{}".format(str(settings["web"]))
                        sk2 = "{}".format(str(settings["web2"]))
                        sk3 = "{}".format(str(settings["web3"]))
                        ks = "{}".format(str(settings["color"]))
                        kk = "{}".format(str(settings["color1"]))
                        kkk = "{}".format(str(settings["color2"]))
                        kkkk = "{}".format(str(settings["color3"]))
                        sw = "{}".format(str(settings["sms1"]))
                        sw2 = "{}".format(str(settings["sms2"]))
                        sw3 = "{}".format(str(settings["sms3"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        sb2 = "{}".format(str(settings["ปุ่ม2"]))
                        sb3 = "{}".format(str(settings["ปุ่ม3"]))
                        sp = "{}".format(str(settings["ปุ่มซ้าย"]))
                        sp2 = "{}".format(str(settings["ปุ่มซ้าย2"]))
                        sp3 = "{}".format(str(settings["ปุ่มซ้าย3"]))
                        spp = "{}".format(str(settings["ปุ่มขวา"]))
                        spp2 = "{}".format(str(settings["ปุ่มขวา2"]))
                        spp3 = "{}".format(str(settings["ปุ่มขวา3"]))
                        sx = "{}".format(str(settings["LineID"]))
                        sx2 = "{}".format(str(settings["LineID2"]))
                        sx3 = "{}".format(str(settings["LineID3"]))
                        sxx = "{}".format(str(settings["link"]))
                        sxx2 = "{}".format(str(settings["link2"]))
                        sxx3 = "{}".format(str(settings["link3"]))
                        groups = nadya.groups
                        for group in groups:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp),
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp),
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr2,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sas,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx2),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw2,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb2,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp2),
                                                    "uri": "{}".format(sk2),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp2),
                                                    "uri": "{}".format(sx2),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "{}".format(ks)}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"{}".format(kk)},
                                        "footer": {"backgroundColor": "{}".format(kkk)}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "{}".format(kkkk)}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr3,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sasa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(sxx3),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw3,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb3,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC0033",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(sp3),
                                                    "uri": "{}".format(sk3),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "{}".format(spp3),
                                                    "uri": "{}".format(sx3),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(os),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text.lower().startswith("#gbc "):
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(">")
                        kw = get[0]
                        ans = get[1]
                        sa = "{}".format(str(kw))
                        sw = "{}".format(str(settings["sms"]))
                        sr = "{}".format(str(settings["sms1"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        ss = ["#006600","#FF0000","#CC0033"]
                        s = ["#006600","#CC0033","#FF0000"]
                        groups = nadya.groups
                        for group in groups:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(sa),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "line://ti/p/~{}".format(ans),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text.lower().startswith("#fbc "):
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(">")
                        kw = get[0]
                        ans = get[1]
                        sa = "{}".format(str(kw))
                        sw = "{}".format(str(settings["sms"]))
                        sr = "{}".format(str(settings["sms1"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        ss = ["#006600","#FF0000","#CC0033"]
                        s = ["#006600","#CC0033","#FF0000"]
                        gid = nadya.getAllContactIds()
                        for i in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(sa),
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "line://ti/p/~{}".format(ans),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(i, data)
                elif msg.text in ["ทีมแอด","admin","แอด","แอดมิน","Admin"]:
                            a = "{}".format(str(settings["gig"]))
                            b = "{}".format(str(settings["aog"]))
                            c = "{}".format(str(settings["tar"]))
                            d = "{}".format(str(settings["som"]))
                            e = "{}".format(str(settings["aoo"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ADMIN TAEM",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/6b104ad15c635d1c1aed1ed29620d82d.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แอดมิน",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"text",
                                                "text":"☣️Ꭿ🅓ℳℐℕ☣️🅱️Ios☢️",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อคลิก",
                                                    "uri": "line://ti/p/~{}".format(b),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ADMIN TAEM",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/153a2ac84714232237812ac04b3a4cd0.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แอดมิน",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"text",
                                                "text":"🅰dmin💋Slot Thai🎰",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อคลิก",
                                                    "uri": "line://ti/p/~{}".format(a),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ADMIN TAEM",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/1f4c0c83cf31daec918542ee76b5e3ad.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แอดมิน",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"text",
                                                "text":"🅰ZH3tAR.KS~`ต้าST💯™",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อคลิก",
                                                    "uri": "line://ti/p/~{}".format(c),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ADMIN TAEM",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/3f06135215c424b58858dcbd03ca329d.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แอดมิน",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"text",
                                                "text":"😽••พิ๊-เหมียว••😽",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อคลิก",
                                                    "uri": "line://ti/p/~{}".format(d),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ADMIN TAEM",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/e37dd709797ab625cfd939b61c6c6e88.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แอดมิน",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"text",
                                                "text":"AONGAENG",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อคลิก",
                                                    "uri": "line://ti/p/~{}".format(e),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ขับเคลื่อนโดย",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/b83a2e888bb70421d480fc770d46e2ee.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "ผู้สร้างบอท",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"text",
                                                "text":"꧁༺ஆืਹໂ√န༻꧂",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "เช่าบอทคลิก",
                                                    "uri": "line://ti/p/~bot.tumz",
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "แอดมิน",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text.lower().startswith("#bc "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split(">")
                            kw = get[0]
                            ans = get[1]
                            sa = "{}".format(str(kw))
                            sw = "{}".format(str(settings["sms"]))
                            sr = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            ss = ["#006600","#FF0000","#CC0033"]
                            s = ["#006600","#CC0033","#FF0000"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(sa),
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "line://ti/p/~{}".format(ans),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == ".sl":
                            sa = "{}".format(str(settings["Pic"]))
                            sv = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms"]))
                            sc = "{}".format(str(settings["LineID"]))
                            sr = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            ss = ["#006600","#FF0000","#CC0033"]
                            s = ["#006600","#CC0033","#FF0000"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                         "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
#                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "image",
                                                "url": sa,
                                                "size": "full",
#                                                "aspectRatio":"1:1",
 #                                               "aspectMode":"cover",
                                            },
                                            {
                                                "type": "text",
                                                "text": "ข้อมูลโปรโมชั่น",
                                                "size": "xl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
 #                                              "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xxl",
                                                "text": sw,
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/680f2ce6dab7761f900a491f19d96675.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แจ้งข่าวสารอัพเดทเพจโกง",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"text",
                                                "text":"🕹️สอบถามเพจเล่นได้/ถอนได้",
                                                "wrap": True,
                                                "gravity": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"text",
                                                "text":"🕹️แหล่งข่าวจากข้อมูลผู้ใช้จริง",
                                                "wrap": True,
                                                "gravity": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"text",
                                                "text":"🕹️สอบถามข้อมูลเพิ่มเติมได้ที่",
                                                "wrap": True,
                                                "gravity": "center",
                                                "color": "#CC0033",
#                                            },
 #                                           {
  #                                              "type": "text",
   #                                             "text": " "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อ Slot Thai",
                                                    "uri": "line://ti/p/~@slotthai"
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif text.lower() == "#ตร":
                    if msg._from in admin and Owner:
                            sas = ["https://www.img.in.th/images/08c93acf413674c3e3025f8dccb88214.gif","https://www.img.in.th/images/116a923cf71637ef18fedeea8e38146d.gif","https://www.img.in.th/images/ad92c15131b3230f1edda868638500c6.gif","https://www.img.in.th/images/760f726e78b6bbe96b7e54fb55704573.gif"]
                            sv = "{}".format(str(settings["web"]))
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#สายย่อ":
                            sas = ["https://www.img.in.th/images/cd10e920da9f56b3868272defcb76bc4.gif"]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#สายเปย์":
                            sas = ["https://www.img.in.th/images/10ad235df208808142c00135e864bc4c.gif"]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
#                                                "uri": sv
                                                "uri": "line://ti/p/~bot.tumz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#โย่วๆ":
                            sas = ["https://www.img.in.th/images/c2b9760f5bf31785c30e020daf59d459.gif"]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
#                                                "uri": sv
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#จัดไป":
                            sas = ["https://www.img.in.th/images/5a0003d21e2a1f6426c61509e1bf5831.gif"]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
#                                                "uri": sv
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#จะเอา":
                            sas = [""]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
#                                                "uri": sv
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#หยอกๆ":
                            sas = ["https://www.img.in.th/images/ca684e4ef0eec96070b6a541978a896f.gif"]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
#                                                "uri": sv
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#100":
                            sas = ["https://www.img.in.th/images/9f8809cc2c8ed473af105398ff68123e.gif","https://www.img.in.th/images/dbf6a67c60673f34e332fa207c4ff210.jpg","https://www.img.in.th/images/fb0775ed84e38eeb4dbace4fd10890f5.gif"]
                            sv = ["line://ti/p/~bot.tumz"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~bot.tumz"
#                                                "uri": sv
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["/sll","sl","sll"]:
                            sa = "{}".format(str(settings["Pic"]))
                            sv = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms"]))
                            sc = "{}".format(str(settings["LineID"]))
                            sr = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            ss = ["#FF69B4"]
                            s = ["#FF69B4"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#FFFFFF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FFCCFF"}, #"separator": True, "separatorColor": "#333333"}
                                        "body": {"backgroundColor": "#FFFFFF"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                      },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                                "gravity": "center"
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"text",
                                                "text": "สมัครคลิกที่นี่",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type":"text",
                                                "text": "แจ้งปัญหาคลิก",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == ".แนะนำ":
                            ck = "{}".format(str(settings["Pic"]))
                            sv = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms"]))
                            sc = "{}".format(str(settings["LineID"]))
                            sr = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            ss = ["#FF69B4"]
                            s = ["#FF69B4"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/addd36cac27e589323df5e9dd85f2088.jpg",
                                                "aspectMode":"cover",
                                                "size": "full",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/a75eba87fad30f4b228e1ff1fd5e33b5.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "line://ti/p/~@jokerlucky"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/265c705c9a20396cd857b19bd79623b4.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "http://king189.com/register?XOSLT68076"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/9fb0e4956ff902521e8e3ee13f9baff0.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://lin.ee/vIKkbM2"
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": "https://www.img.in.th/images/6b22441e7f6f6ca881a8dbd81be9ab57.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://www.hiallbet.com/aff?aff=2485"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                             {
                                                "type": "image",
                                                "url": "{}".format(ck),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/addd36cac27e589323df5e9dd85f2088.jpg",
                                                "aspectMode":"cover",
                                                "size": "full",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/a75eba87fad30f4b228e1ff1fd5e33b5.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "line://ti/p/~@jokerlucky"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/265c705c9a20396cd857b19bd79623b4.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "http://king189.com/register?XOSLT68076"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/9fb0e4956ff902521e8e3ee13f9baff0.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://lin.ee/vIKkbM2"
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": "https://www.img.in.th/images/6b22441e7f6f6ca881a8dbd81be9ab57.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://www.hiallbet.com/aff?aff=2485"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                             {
                                                "type": "image",
                                                "url": "{}".format(ck),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/addd36cac27e589323df5e9dd85f2088.jpg",
                                                "aspectMode":"cover",
                                                "size": "full",
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/a75eba87fad30f4b228e1ff1fd5e33b5.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "line://ti/p/~@jokerlucky"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/265c705c9a20396cd857b19bd79623b4.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "http://king189.com/register?XOSLT68076"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/9fb0e4956ff902521e8e3ee13f9baff0.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://lin.ee/vIKkbM2"
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": "https://www.img.in.th/images/6b22441e7f6f6ca881a8dbd81be9ab57.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://www.hiallbet.com/aff?aff=2485"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(ck),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "xxl",
                                        "contents": [
                                            {
                                                "type":"text",
                                                "text":"สนใจเช่ารูปแบบโฆษณา",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type":"uri",
                                                    "uri":"https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#FF69B4",
#                                                "wrap":True,
                                                "action": {
                                                    "type": "uri",
                                                    "label": "⫸ คลิกที่นี่ ⫷",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text in ["#est","est",".est"]:
                            sa = "{}".format(str(settings["Pic"]))
                            ew = "{}".format(str(settings["ขนาดภาพ"]))
                            sw = "{}".format(str(settings["sms"]))
                            sk = "{}".format(str(settings["web"]))
                            sr = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            sx = "{}".format(str(settings["LineID"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                      },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC6633",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC6633",
                                            },
                                        ]
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สมัครคลิกที่นี่",
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "แจ้งปัญหาคลิก",
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["gest","gbc","/est"]:
                        sa = "{}".format(str(settings["Pic"]))
                        ew = "{}".format(str(settings["ขนาดภาพ"]))
                        sw = "{}".format(str(settings["sms"]))
                        sk = "{}".format(str(settings["web"]))
                        sr = "{}".format(str(settings["sms1"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        sx = "{}".format(str(settings["LineID"]))
                        groups = nadya.groups
                        for group in groups:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "{}".format(ew),
                                        "size": "full",
                                      },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC6633",
                                            },
                                            {
                                                "type": "text",
                                                "text": sb,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#CC6633",
                                            },
                                        ]
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color":"#999900",
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สมัครคลิกที่นี่",
                                                    "uri": "{}".format(sk),
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#66CC33",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "แจ้งปัญหาคลิก",
                                                    "uri": "{}".format(sx),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif msg.text in ["gsll","gsl","/gsll"]:
                    sa = "{}".format(str(settings["Pic"]))
                    sw = "{}".format(str(settings["sms"]))
                    sv = "{}".format(str(settings["web"]))
                    sc = "{}".format(str(settings["LineID"]))
                    sr = "{}".format(str(settings["sms1"]))
                    sb = "{}".format(str(settings["ปุ่ม"]))
                    ss = ["#FF69B4"]
                    s = ["#FF69B4"]
                    gid = ["c262893d7c26ee5bc2f7401d0efb0492c","c6b2c6391f5132d14b5738ea84c1abb9b","c6fa1b8da81d7ad3b3bde7ba5fab3732e","c815d106dd352db79686cd48c88941b2b","c22f1f5fb7745c967dc4bf9cfc9627a77","cf647371dc18910667e02008be2060e2a","cd0dbba09fed52adf079f23b61a64b15f","c1db995a182ca749b83557c1c2bde2c88","ceb1fbba1d2e06c30bac6d226c8f27b87","cef1da2594d4b64dcebfdad0712d127e4"]
                    groups = nadya.groups
                    for group in groups:
                        if group in gid and groups:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#FFFFFF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FFCCFF"}, #"separator": True, "separatorColor": "#333333"}
                                        "body": {"backgroundColor": "#FFFFFF"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": sa,
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                      },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                                "gravity": "center"
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type":"text",
                                                "text": "สมัครคลิกที่นี่",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                            {
                                                "type":"separator",
                                                "color":"#FF69B4"
                                            },
                                            {
                                                "type":"text",
                                                "text": "แจ้งปัญหาคลิก",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "https://line.me/ti/p~@ESTBET1"
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif text.lower() == ".gsll/":
                    sa = "{}".format(str(settings["Pic"]))
                    sw = "{}".format(str(settings["sms"]))
                    sv = "{}".format(str(settings["web"]))
                    sc = "{}".format(str(settings["LineID"]))
                    sr = "{}".format(str(settings["sms1"]))
                    sb = "{}".format(str(settings["ปุ่ม"]))
                    ss = ["#006600","#FF0000","#CC0033"]
                    s = ["#006600","#CC0033","FF0000"]
                    gid = ["c262893d7c26ee5bc2f7401d0efb0492c","c6b2c6391f5132d14b5738ea84c1abb9b","c6fa1b8da81d7ad3b3bde7ba5fab3732e","c815d106dd352db79686cd48c88941b2b","c22f1f5fb7745c967dc4bf9cfc9627a77","cf647371dc18910667e02008be2060e2a","cd0dbba09fed52adf079f23b61a64b15f","c1db995a182ca749b83557c1c2bde2c88","ceb1fbba1d2e06c30bac6d226c8f27b87"]
                    groups = nadya.groups
                    for group in groups:
                        if group in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
#                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "image",
                                                "url": sa,
 #                                               "aspectRatio":"1:1",
#                                                "aspectMode":"cover",
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ข้อมูลโปรโมชั่น",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "xxl",
                                                "text": sw,
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://www.img.in.th/images/680f2ce6dab7761f900a491f19d96675.jpg",
                                                "aspectRatio":"1:1",
                                                "aspectMode":"cover",
                                                "size": "full",

                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "size": "xl",
                                                "text": "แจ้งข่าวสารอัพเดทเพจโกง",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF0000",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"text",
                                                "text":"🕹️สอบถามเพจเล่นได้/ถอนได้",
                                                "wrap": True,
                                                "gravity": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"text",
                                                "text":"🕹️แหล่งข่าวจากข้อมูลผู้ใช้จริง",
                                                "wrap": True,
                                                "gravity": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"text",
                                                "text":"🕹️สอบถามข้อมูลเพิ่มเติมได้ที่",
                                                "wrap": True,
                                                "gravity": "center",
                                                "color": "#CC0033",
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#006600",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อ Slot Thai",
                                                    "uri": "line://ti/p/~@slotthai"
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif 'P5: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P5: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P5"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง5: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง5: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง5"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P6: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P6: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P6"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง6: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง6: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง6"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P7: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P7: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P7"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง7: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง7: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง7"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P8: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P8: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P8"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง8: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง8: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง8"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P9: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P9: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P9"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง9: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง9: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง9"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P10: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P10: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P10"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง10: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง10: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง10"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P11: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P11: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P11"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง11: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง11: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง11"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P12: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P12: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P12"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง12: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง12: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง12"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P13: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P13: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P13"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง13: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง13: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง13"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P14: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P14: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P14"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง14: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง14: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง14"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P15: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P15: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P15"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง15: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง15: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง15"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P16: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P16: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P16"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง17: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง17: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง17"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P18: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P18: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P18"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง18: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง18: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง18"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P19: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P19: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P19"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง19: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง19: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง19"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P20: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P20: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P20"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง20: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง20: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง20"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P21: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P21: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P21"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง21: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง21: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง21"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P22: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P22: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P22"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง22: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง22: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง22"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P23: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P23: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P23"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง23: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง23: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง23"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P24: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P24: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P24"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง24: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง24: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง24"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P17: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P17: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P17"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง16: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง16: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง16"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'N1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('N1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["hi"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'M1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('M1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["hial"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'N2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('N2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["N26"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'M2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('M2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["M26"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'M3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('M3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["M36"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'N3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('N3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["N36"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'หยาบ: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('หยาบ ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["Fuckyou"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'P3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'P4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P4: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P4"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง4: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง4"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'hi: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('hi: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["hi"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'hial: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('hial: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["hial"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))          
                elif 'ขนาดรูป: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ขนาดรูป: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ขนาดรูป"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L0: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L0: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L00"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L1"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L2"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L3: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L3: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L3"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L4: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L4: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L4"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'U1: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('U1: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง111"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))

                elif 'U: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('U: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง00"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'U2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('U2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง222"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง33: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง33: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง333"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'ลิ้ง44: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง44: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง444"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'L5: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L5: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L5"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง55: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง55: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง55"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'L6: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('L6: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["L6"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง66: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง66: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง66"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'P77: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P77: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P77"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง77: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง77: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง77"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'P88: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P88: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P88"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง88: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง88: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง88"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            
                elif 'P99: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('P99: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["P99"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ลิ้ง99: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ลิ้ง99: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessa.ge(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["ลิ้ง99"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
            

                elif text.lower() == "lk":
                            ขนาดรูป = "{}".format(str(settings["ขนาดรูป"]))
                            P1 = "{}".format(str(settings["P1"]))
                            ลิ้ง1 = "{}".format(str(settings["ลิ้ง1"]))
                            P5 = "{}".format(str(settings["P5"]))
                            ลิ้ง5 = "{}".format(str(settings["ลิ้ง5"]))
                            P6 = "{}".format(str(settings["P6"]))
                            ลิ้ง6 = "{}".format(str(settings["ลิ้ง6"]))
                            P7 = "{}".format(str(settings["P7"]))
                            ลิ้ง7 = "{}".format(str(settings["ลิ้ง7"]))
                            P8 = "{}".format(str(settings["P8"]))
                            ลิ้ง8 = "{}".format(str(settings["ลิ้ง8"]))
                            P9 = "{}".format(str(settings["P9"]))
                            ลิ้ง9 = "{}".format(str(settings["ลิ้ง9"]))
                            hi = "{}".format(str(settings["hi"]))
                            hial = "{}".format(str(settings["hial"]))

                            dataProfile = [

                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": hi,
                                                #"https://sv1.picz.in.th/images/2020/03/17/QwTTwg.jpg",
                                                "aspectMode":"cover",
                                                "aspectRatio": "{}".format(ขนาดรูป),                                                
                                                "size": "full",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": hial
                                                },                                                
                                            },
                                        ]
                                    },

                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(P1),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": ลิ้ง1
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(str(settings["P2"])),
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(str(settings["ลิ้ง2"]))
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(str(settings["P3"])),
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri":"{}".format(str(settings["ลิ้ง3"]))
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": "{}".format(str(settings["P4"])),
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri":"{}".format(str(settings["ลิ้ง4"]))
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P5),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(ลิ้ง5)
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P6),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง6),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                             {
                                                "type": "image",
                                                "url": "{}".format(P7),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(ลิ้ง7),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P8),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง8),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P9),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง9),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text in ["/แนะนำ","ML","ls"]:
                            ขนาดรูป = "{}".format(str(settings["ขนาดรูป"]))
                            P1 = "{}".format(str(settings["P1"]))
                            ลิ้ง1 = "{}".format(str(settings["ลิ้ง1"]))
                            P5 = "{}".format(str(settings["P5"]))
                            ลิ้ง5 = "{}".format(str(settings["ลิ้ง5"]))
                            P6 = "{}".format(str(settings["P6"]))
                            ลิ้ง6 = "{}".format(str(settings["ลิ้ง6"]))
                            P7 = "{}".format(str(settings["P7"]))
                            ลิ้ง7 = "{}".format(str(settings["ลิ้ง7"]))
                            P8 = "{}".format(str(settings["P8"]))
                            ลิ้ง8 = "{}".format(str(settings["ลิ้ง8"]))
                            P9 = "{}".format(str(settings["P9"]))
                            ลิ้ง9 = "{}".format(str(settings["ลิ้ง9"]))
                            P10 = "{}".format(str(settings["P10"]))
                            ลิ้ง10 = "{}".format(str(settings["ลิ้ง10"]))
                            P11 = "{}".format(str(settings["P11"]))
                            ลิ้ง11 = "{}".format(str(settings["ลิ้ง11"]))
                            P12 = "{}".format(str(settings["P12"]))
                            ลิ้ง12 = "{}".format(str(settings["ลิ้ง12"]))
                            P13 = "{}".format(str(settings["P13"]))
                            ลิ้ง13 = "{}".format(str(settings["ลิ้ง13"]))
                            P14 = "{}".format(str(settings["P14"]))
                            ลิ้ง14 = "{}".format(str(settings["ลิ้ง14"]))
                            P15 = "{}".format(str(settings["P15"]))
                            ลิ้ง15 = "{}".format(str(settings["ลิ้ง15"]))
                            P16 = "{}".format(str(settings["P16"]))
                            ลิ้ง16 = "{}".format(str(settings["ลิ้ง16"]))
                            P17 = "{}".format(str(settings["P17"]))
                            ลิ้ง17 = "{}".format(str(settings["ลิ้ง17"]))
                            P18 = "{}".format(str(settings["P18"]))
                            ลิ้ง18 = "{}".format(str(settings["ลิ้ง18"]))
                            P19 = "{}".format(str(settings["P19"]))
                            ลิ้ง19 = "{}".format(str(settings["ลิ้ง19"]))
                            P20 = "{}".format(str(settings["P20"]))
                            ลิ้ง20 = "{}".format(str(settings["ลิ้ง20"]))
                            P21 = "{}".format(str(settings["P21"]))
                            ลิ้ง21 = "{}".format(str(settings["ลิ้ง21"]))
                            P22 = "{}".format(str(settings["P22"]))
                            ลิ้ง22 = "{}".format(str(settings["ลิ้ง22"]))
                            P23 = "{}".format(str(settings["P23"]))
                            ลิ้ง23 = "{}".format(str(settings["ลิ้ง23"]))
                            P24 = "{}".format(str(settings["P24"]))
                            ลิ้ง24 = "{}".format(str(settings["ลิ้ง24"]))
                            hi = "{}".format(str(settings["hi"]))
                            hial = "{}".format(str(settings["hial"]))
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": hi,
                                                #"https://sv1.picz.in.th/images/2020/03/17/QwTTwg.jpg",
                                                "aspectMode":"cover",
                                                "aspectRatio": "{}".format(ขนาดรูป),                                                
                                                "size": "full",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": hial
                                                },                                                
                                            },
                                        ]
                                    },

                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(P1),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": ลิ้ง1
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(str(settings["P2"])),
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(str(settings["ลิ้ง2"]))
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(str(settings["P3"])),
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri":"{}".format(str(settings["ลิ้ง3"]))
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": "{}".format(str(settings["P4"])),
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri":"{}".format(str(settings["ลิ้ง4"]))
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P5),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(ลิ้ง5)
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P6),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง6),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                             {
                                                "type": "image",
                                                "url": "{}".format(P7),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(ลิ้ง7),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P8),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง8),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P9),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง9),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(str(settings["N26"])),
                                                #"https://sv1.picz.in.th/images/2020/03/17/QwTTwg.jpg",
                                                "aspectMode":"cover",
                                                "aspectRatio": "{}".format(ขนาดรูป),                                                
                                                "size": "full",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(str(settings["M26"]))
                                                },                                                
                                            },
                                        ]
                                    },

                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(P10),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(ลิ้ง10),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": P11,
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": ลิ้ง11
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": P12,
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": ลิ้ง12
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": P13,
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": ลิ้ง13
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": P14,
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": ลิ้ง14
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": P15,
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง15),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                             {
                                                "type": "image",
                                                "url": "{}".format(P16),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": ลิ้ง16
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P17),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง17),
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P18),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง18),
                                                },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                        "header": {"backgroundColor":"#000000"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
#                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "{}".format(str(settings["N36"])),
                                                #"https://sv1.picz.in.th/images/2020/03/17/QwTTwg.jpg",
                                                "aspectMode":"cover",
                                                "aspectRatio": "{}".format(ขนาดรูป),                                                
                                                "size": "full",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": "{}".format(str(settings["M36"]))
                                                },                                                
                                            },
                                        ]
                                    },
                                    "hero": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": P19,
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": ลิ้ง19
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": P20,
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": ลิ้ง20
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": P21,
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": ลิ้ง21
                                                },
                                            },
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
#                                        "layout": "vertical",
                                        "layout":"horizontal",
                                        "spacing": "lg",
                                        "contents": [
                                            {
                                                "type": "image",
#                                                "url": "{}".format(ck),
                                                "url": P22,
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": ลิ้ง22
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P23),
                                                "size": "lg",
                                                "action":{
                                                    "type": "uri",
                                                    "uri": ลิ้ง23,
                                                },
                                            },
                                            {
                                                "type": "image",
                                                "url": "{}".format(P24),
#                                                "url": "https://www.img.in.th/images/ec343f6e2cea5cea727ff1ba8a917f05.jpg",
                                                "size": "lg",
                                                "action":{
                                                    "type":"uri",
                                                    "uri": "{}".format(ลิ้ง24),
                                                },
                                            },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout":"horizontal",
                                        "spacing": "xxl",
                                        "contents": [
                                            {
                                                "type":"text",
                                                "text":"สนใจเช่ารูปแบบโฆษณา",
                                                "align":"center",
                                                "weight":"bold",
                                                "color":"#FF69B4",
                                                "size":"xs",
                                                "wrap":True,
                                                "action":{
                                                    "type":"uri",
                                                    "uri":"https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#FF69B4",
#                                                "wrap":True,
                                                "action": {
                                                    "type": "uri",
                                                    "label": "⫸ คลิกที่นี่ ⫷",
                                                    "uri": "https://line.me/ti/p/~botlinegroup"
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                         #   time.sleep(10)
                            sendTemplate(to, data)

                elif text.lower() == "/fbc":
                        sa = "{}".format(str(settings["Pic"]))
                        sw = "{}".format(str(settings["sms"]))
                        sc = "{}".format(str(settings["LineID"]))
                        sr = "{}".format(str(settings["sms1"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        ss = ["#006600","#FF0000","#CC0033"]
                        s = ["#006600","#CC0033","#FF0000"]
                        gid = nadya.getAllContactIds()
                        for i in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": sa,
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "line://ti/p/~{}".format(sc),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(i, data)
                elif text.lower() == "ว่าง":
                            sas = ["https://sv1.picz.in.th/images/2021/06/26/sb15zV.gif"]
                                #"https://www.img.in.th/images/e5131eba5abab7582e6c2e635ccbe34f.gif"]
#                                   https://www.img.in.th/images/693f9ea95810a45dafe8456e3ae1561a.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "งง":
                            sas = ["https://www.img.in.th/images/10f81cdf97ee886ddbca1db0ccfae833.gif","https://www.img.in.th/images/dbe7db54eefee9bb5f0b51c57c807129.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "#นาวขอ":
                            sas = ["https://www.img.in.th/images/817b95184bfaf08a8e0bfd7c2a68436c.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif text.lower() == "#ว่าง":
                            sas = ["https://www.img.in.th/images/3ff93ff49144e876c75697e66d838307.gif","https://www.img.in.th/images/0d6394736e9aaf4319d3398dddedee75.gif"]
                            data = {
                                "type": "template",
                                "altText": "✨ ꧁༺ஆืਹໂ√န༻꧂ ✨",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(sas)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~botlinegroup"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)

                elif text.lower() == "/wbc":
                            sa = "{}".format(str(settings["Pic"]))
                            sv = "{}".format(str(settings["web"]))
                            sw = "{}".format(str(settings["sms"]))
                            sc = "{}".format(str(settings["LineID"]))
                            sr = "{}".format(str(settings["sms1"]))
                            sb = "{}".format(str(settings["ปุ่ม"]))
                            ss = ["#006600","#FF0000","#CC0033"]
                            s = ["#006600","#CC0033","#FF0000"]
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": sa,
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
#                                                    "uri": "line://ti/p/~{}".format(scb),
                                                    "uri": "http://{}".format(sv),
#                                                    "uri": scb,
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "/wgbc":
                        sa = "{}".format(str(settings["Pic"]))
                        sv = "{}".format(str(settings["web"]))
                        sw = "{}".format(str(settings["sms"]))
                        sc = "{}".format(str(settings["LineID"]))
                        sr = "{}".format(str(settings["sms1"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        ss = ["#006600","#FF0000","#CC0033"]
                        s = ["#006600","#CC0033","#FF0000"]
                        groups = nadya.groups
                        for group in groups:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": sa,
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "http://{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
                elif text.lower() == "/wfbc":
                        sa = "{}".format(str(settings["Pic"]))
                        sv = "{}".format(str(settings["web"]))
                        sw = "{}".format(str(settings["sms"]))
                        sc = "{}".format(str(settings["LineID"]))
                        sr = "{}".format(str(settings["sms1"]))
                        sb = "{}".format(str(settings["ปุ่ม"]))
                        ss = ["#006600","#FF0000","#CC0033"]
                        s = ["#006600","#CC0033","#FF0000"]
                        gid = nadya.getAllContactIds()
                        for i in gid:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": sa,
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "http://{}".format(sv),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(i, data)
                elif text.lower() == "/f1bc":
                     sa = "{}".format(str(settings["Pic"]))
                     sw = "{}".format(str(settings["sms"]))
                     sc = "{}".format(str(settings["LineID"]))
                     sr = "{}".format(str(settings["sms1"]))
                     sb = "{}".format(str(settings["ปุ่ม"]))
                     FT = "{}".format(str(settings["find"]))
                     ss = ["#006600","#FF0000","#CC0033"]
                     s = ["#006600","#CC0033","#FF0000"]
                     gid = nadya.getAllContactIds()
                     for i in gid:
                         if freinds in FT:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": sa,
                                                "size": "full"

                                            },
                                            {
                                                "type": "text",
                                                "text": sw,
                                                "size": "xxl",
#                                                "text": "🇹🇭 Hi Allbet 🇹🇭",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "{}".format(random.choice(s)),
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sr,
                                                "color": "{}".format(random.choice(s)),
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            {
                                                "type":"text",
                                                "text":" "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"{}".format(random.choice(ss)),
#                                                "color":"#CC0033",
                                                "action": {
                                                    "type": "uri",
                                                    "label": sb,
                                                    "uri": "line://ti/p/~{}".format(sc),
                                                },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ประกาศสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(FT, data)
                elif msg.text.lower().startswith("#pbc "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split(">")
                            kw = get[0]
                            ans = get[1]
                            sa = "{}".format(str(kw))
                            data = {
                                "type": "template",
                                "altText": "Norak Lo !",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(sa),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~{}".format(ans),
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
        

                elif text.lower() == "/me":
                            contact = nadya.getContact(sender)
                            cover = nadya.getProfileCoverURL(sender)

                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "body": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        #"https://www.img.in.th/images/d30c1a1e2dcc0e16a7f2f1e551675866.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ติดต่อ"])),
                                        },
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": "#FF0000",
                                                "size": "lg",
                                                'flex': 1
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        #"https://www.img.in.th/images/d30c1a1e2dcc0e16a7f2f1e551675866.png",
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["ติดต่อ"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "ข้อมูลสำคัญ",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)

                elif msg.text.lower().startswith("#ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
#                            rr = json.loads(data)
                            if r["items"] != []:
                                ret_ = []
                                yt = []
                                for music in r["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#000000"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#000000",
                                                "separator": True,
                                               "separatorColor": "#000000"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#CC0033",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#CC0033"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#CC0033",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#CC0033",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#CC0033",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#CC0033",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#CC0033",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                elif msg.text.lower().startswith(" "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = nadya.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = nadya.getContact(she);ClonerV2(she)
              #                      sendMention(to, contact.mid, "=͟͟͞͞➳ คุณกำลังก็อปปี้", "สำเร็จแล้ว >_<");nadya.sendContact(to, str(BackupProfile.mid));nadya.sendContact(to, str(contact.mid))

                elif msg.text.lower().startswith("cp "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = nadya.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = nadya.getContact(she);ClonerV2(she)
              #                      sendMention(to, contact.mid, "=͟͟͞͞➳ คุณกำลังก็อปปี้", "สำเร็จแล้ว >_<");nadya.sendContact(to, str(BackupProfile.mid));nadya.sendContact(to, str(contact.mid))
                elif text.lower() == "กลับร่าง":
                            try:
                                nadyastatus = nadya.getProfile()
                                nadyaName = nadya.getProfile()
                                nadyaName.statusMessage = ProfileMe["statusMessage"]
                                nadyaName.pictureStatus = str(ProfileMe["pictureStatus"])
                                nadya.updateProfile(nadyastatus)
                                nadyaName.displayName = ProfileMe["NameMe"]
                                nadya.updateProfile(nadyaName)
                                path = nadya.downloadFileURL(ProfileMe["PictureMe"])
                                nadya.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                nadya.updateProfileCoverById(coverId)
                                BackupProfile = nadya.getContact(nadyaMID)
                                sendMention(to, BackupProfile.mid, "=͟͟͞͞➳ กลับบัญชีเดิมเรียบร้อย", ">_<");nadya.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                nadya.sendMessage(to,"คุณยังไม่ได้ก็อปปี้ User >_<")


                elif "ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.google.com/search?q=", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.google.com/search?q={}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        nadya.sendMessage(to, str(ret_))                    


#-------------------------------------------------------------------------------
#===============================================================================[nadyaMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT NADYA MESSAGE")
            try:
                if op.param3 in nadyaMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki2MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki3MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki4MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[kiMID nadyaMID]
                if op.param3 in kiMID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki4MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki2MID nadyaMID]
                if op.param3 in ki2MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki4MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki3MID nadyaMID]
                if op.param3 in ki3MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki4MID nadyaMID]
                if op.param3 in ki4MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    nadya.sendMessage(op.param1,"Qr under protect")
            else:
                nadya.sendMessage(op.param1,"")
#==============================================================================#
                if msg.contentType == 1:
                    if sets["pict"] == True:
                        path = nadya.downloadObjectMsg(msg_id)
                        sets["pict"] = False
                        sets["listpict"] = str(path)
                #    f = codecs.open("image.json","w","utf-8")
                #    json.dump(path, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nadya.sendMessage(to, "")
           #     if msg.toType == 2:
            #        if to in sets["pictGroup"]:
             #           path = nadya.downloadObjectMsg(msg_id)
              #          sets["pictGroup"].remove(to)
                      #  line.updateGroupPicture(to, path)
              #          nadya.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
            #    elif msg.contentType == 1:
            #        if settings["addImage"]["status"] == True and sender == nadyaMID:
            #            path = nadya.downloadObjectMsg(msg_id)
            #            images[settings["addImage"]["name"]] = str(path)
            #            f = codecs.open("image.json","w","utf-8")
            #            json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
            #            nadya.sendMessage(to, "picture {} in list".format(str(settings["addImage"]["name"])))
            #            settings["addImage"]["status"] = False
            #            settings["addImage"]["name"] = ""
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if nadyaMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = nadya.getContact(sender)
                                    nadya.sendMessage(to, "       **-™ระบบตอบอัตโนมัติ™-**\n\n      แทคมาทัก....หรือแทคมารักจ๊ะ\n\n            「™Auto Respon」 ")
#                                    sendMessageWithMention(to, contact.mid)
                                    nadya.sendContact(to, contact.mid)
                                    break
                if msg.contentType == 0:
                    if text is None:
                        return
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = nadya.findGroupByTicket(ticket_id)
                                nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                                ki.acceptGroupInvitationByTicket(group.id,ticket_id)
                                ki2.acceptGroupInvitationByTicket(group.id,ticket_id)
#                                nadya.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
                                break
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nadya.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver

            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ VҜ ŚẾL₣ВΌŦ ]"
                    naadya.sendMessage(to, str(ret_))
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = nadya.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    nadya.updateProfilePicture(path)
                    nadya.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = nadya.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        nadya.updateGroupPicture(to, path)
                        nadya.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ VҜ ŚẾL₣ВΌŦ ]"
                    line.sendMessage(to, str(ret_))

            #    elif msg.contentType == 1:
            #        if sets["pict"] == True:
             #           path = nadya.downloadObjectMsg(msg.id)
                      #  sets["image"]["name"] = str(path)
               #         sets["pict"] = False
               #         nadya.sendMessage(to, "Done..")
                    #    sets["pict"] == False
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            nadya.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            nadya.sendMessage(to, str(ret_))
                        except Exception as error:
                            nadya.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in nadyaMID:
                            try:
                                nadya.kickoutFromGroup(msg.to,[sender])
                                nadya.sendMessage("บอกแล้อย่าพิมไม่เชื่อจุกไปสิ55555")
                            except Exception as e:
                                print(e)
                    for image in images:
                        if msg.text.lower() == image:
                            nadya.generateReplyMessage(msg.id)
                            nadya.sendReplyImage(msg.id, to, images[image])
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == False:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = nadya.findGroupByTicket(ticket_id)
                                nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                                nadya.sendMessage(group.id,str(tagadd["m"]))
                                msgSticker = sets["messageSticker"]["listSticker"]["join2"]
                                if msgSticker != None:
                                    sid = msgSticker["STKID"]
                                    spkg = msgSticker["STKPKGID"]
                                    sver = msgSticker["STKVER"]
                                    sendSticker(group.id, str(sver), str(spkg), str(sid))
                                nadya.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
#            elif msg.contentType == 7: # Content type is sticker
#                if settings['checkSticker']:
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                            sendTemplate(to, data)

#=====================================================================
#========================================================================
        if op.type in [ 25,26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nadya.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            elif msg.contentType == 7:  #Content type is sticker
                if sets['sti2']:
                    nadya.unsendMessage(msg.id)
                    if 'STKOPT' in msg.contentMetadata:
                        contact = nadya.getContact(nadyaMID)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        nadya.unsendMessage(msg.id)
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = nadya.getContact(nadyaMID)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        nadya.unsendMessage(msg.id)
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nadya.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == ".........................":
                    nadya.sendMessage(to,"[ STEVE Botline ]\nadmin :\nline.me/ti/p/z7CqVLtFII")
#========================================================================
            elif msg.contentType == 7:  #ontent type is sticker
                if settings['Sticker'] == True:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = nadya.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = nadya.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
             #   elif msg.contentType == 7:
                if msg.toType == 0 and sender != nadyaMID: to = sender
                else: to = receiver
            #    elif msg.contentType == 7:
            #        if "/ti/g/" in msg.text.lower():
            #            if sets["autoJoinTicket"] == True:
            #                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
            #                links = link_re.findall(text)
            #                n_links = []
            #                for l in links:
            #                    if l not in n_links:
            #                        n_links.append(l)
            #                for ticket_id in n_links:
            #                    group = nadya.findGroupByTicket(ticket_id)
            #                    nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                                #
             #                   nadya.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tags"] == True:
                            contact = nadya.getContact(msg._from) 
                            pict = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if nadyaMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "{}".format(tagadd["tag"]),
                                         "contents": {
                                             "type": "bubble",
                                             "styles": {
                                                 "body": {
                                                     "backgroundColor": '#000000'
                                                  },
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "text",
                                                         "text": "{}".format(tagadd["tag"]),
                                                         "wrap": True,
                                                         "color": "#CC0033",
                                                         "align": "start",
                                                         "gravity": "center",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tagss"] == True:
                            contact = nadya.getContact(sender)
                            cover = nadya.getProfileCoverURL(sender)
                            names = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if nadyaMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "tagall",
                                         "contents": {
                                             "type": "bubble",
                                             'styles': {
                                                 "body": {
                                                     "backgroundColor": '#000000'
                                                 },
                                             },
                                             "hero": {
                                                 "type":"image",
                                                 "url": cover,
                                                 "size":"full",
                                                 "aspectRatio":"20:13",
                                                 "aspectMode":"cover"
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "image",
                                                         "url": "https://profile.line-scdn.net/" + str(pp),
                                                         "size": "lg"
                                                     },
                                                     {
                                                          "type":"text",
                                                          "text":" "
                                                     },
                                                     {
                                                         "type":"text",
                                                         "text":"{}".format(names),
                                                         "size":"xl",
                                                         "weight":"bold",
                                                         "color":"#000000",
                                                         "align":"center"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": status,
                                                         "wrap": True,
                                                         "align": "center",
                                                         "gravity": "center",
                                                         "color": "#CC0033",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if nadyaMID in mention["M"]:
                                      contact = nadya.getContact(nadyaMID)
                                      a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = nadya.getContact(nadyaMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = nadya.getContact(nadyaMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
#        if op.type == 19:
   #         if nadyaMID in op.param3:
      #          apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   nadya.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type in  [25,26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nadya.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("แปลงคท "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    nadya.sendContact(msg.to,str(getx))
            #    if msg.text.lower().startswith("/exec "):
            #        delcmd = msg.text.split(" ")
            #        getx = msg.text.replace(delcmd[0] + " ","")
            #        data = data="{}".format(getx)
            #        sendTemplate(to, data)
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(">")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nadya.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        nadya.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "STEVE Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(nadya.getContact(nadyaMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u266f0d1211f905b2ca386024d9d4e165"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type in [25,26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            nadya.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = True
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = True
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == True: setKey = ''
            if isValid != True:
                if msg.toType == 0 and sender != nadyaMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["send"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["send1"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "อัพเดทโดย\n┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            time.sleep(15)                            
                            sendTemplate(to, data)
                        except:
                            nadya.sendMessage(to, "^^")
            elif msg.contentType == 13:              
                  if settings["checkContact"] == True:
                    try:
                        contact = nadya.getContact(msg.contentMetadata["mid"])
                        if nadya != None:
                            cover = nadya.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            nadya.sendImageWithURL(to, str(pathh))
                        except:
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(settings["send"])),
                                        "margin": "xxl",
                                        "aspectMode": "cover",
                                        "aspectRatio": "3:4",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "{}".format(str(settings["send1"])),
                                            #"line://app/1602687308-GXq4Vvk9?type=text&text=พี่ตั้มคนนี้ให้อภัยและรอหนูตลอดไป",
                                        },
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "อัพเดทโดย\n┈━═☆𝓐𝓭𝓶𝓲𝓷 𝓣𝓾𝓜𝔃 ☆═━┈",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            time.sleep(15)                            
                            sendTemplate(to, data)
                    except:
                        nadya.sendMessage(to, "^^")
        if op.type == 26:
          msg = op.message
          if op.param1 not in admin:
            if settings ["Aip"] == True:
                if msg.text in ProtectMessage:
                    targets = [sender]
                    for target in targets:
                        if not target in admin:
                            try:
                                nadya.sendMessage(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม\n           หรือ\n ตรวจพบคำพูดหยาบคายไม่สุภาพ\nจำเป็นต้องนำออกเพื่อความปลอดภัย\nและความสงบสุขของสมาชิก (｀・ω・´)")
                                nadya.kickoutFromGroup(receiver,[sender])
                            except:
                                nadya.choice(KAC).sendMessage(msg.to,"Error")
        if op.type == 26:
          msg = op.message
          if op.param1 not in admin:
            if settings ["Api"] == True:
                if msg.text in ["55","555","5555","55555","ฮ่า","ฮ่า"]:
                    Mes = ["ขำไร..เหม็นขี้ฟัน","ท่าทางจะบ้า","ตลกหรอสาส","หัวเราะวันละนิดจิตแจ่มใส","หัวเราะคนเดียวก็เป็น","ตลกมากหรอสาส"]
                    nadya.sendMessage(msg.to, str(random.choice(Mes)))
#            if settings ["Api"] == True:
 #                if msg.text in ["666"]:
                   # random.choice(KAC).kickoutFromGroup(receiver,[sender])
         #           nadya.sendMessage(msg.to,"ขำไรวะ")
                if msg.text in ["ใช่","ใช่มั้ย"]:
                    nadya.sendMessage(msg.to, "ใช่..ไม่ใช่.ถามใคร..มีสมองคิดเองสิ")
                elif msg.text in ["งงเลย","งงมั้ย","งงอะไร"]:
                    nadya.sendMessage(msg.to, "ไม่อยากงง.แดกแบรนดยอะๆสิ")
                elif msg.text in ["จ้า","จร้า"]:
                    nadya.sendMessage(msg.to, "จ๊ะ จ๊ะ จ๊ะ")
                elif msg.text in ["บอท"]:
                    nadya.sendMessage(msg.to, "มีอะไรให้รับใช้คับ")
                elif msg.text in ["บอทโง่","โง่","โง่วะ"]:
                    nadya.sendMessage(msg.to, "มืงอ่ะโง่")
                elif msg.text in ["นอน","นอนแล้ว","ไปนอน","ขอตัวนอน","ง่วงนอน"]:
                    nadya.sendMessage(msg.to, "นอนก็นอนสิ.ใครห้ามมืง")
                elif msg.text in ["บ้า","บ้าไปแล้ว","บอทบ้า"]:
                    nadya.sendMessage(msg.to, "มืงล่ะบ้า")
                elif msg.text in ["แอด","แจ็ค","พี่แจ็ค","แอดคับ","แอดมิน","พี่หมี","แอดอยู่มั้ย","จอม","พี่จอม","ออย","พี่ออย","เจน","นุ่น"]:
                    CZ = ["ไม่ตอบกลัวท่านยืมเงิน","น่าจะกดอยู่","อย่าพึ่งเรียกเกมส์กำลังแตก","คนที่ท่านเรียก ไม่มีแรงมาตอบได้ในขณะนี้\nเนื่องจากของขาดมาหลายชั่วโมงแล้ว","ไม่ทราบว่าท่านได้จองคิวนัดไว้ป่ะ\nเพราะตอนนี้คนที่ท่านเรียกติดรำอยู่","ไม่ว่างจ้า กำลังเติม"]
                    nadya.sendMessage(msg.to, str(random.choice(CZ)))
                elif msg.text in ["คับ","ครับ"]:
                    nadya.sendMessage(msg.to, "หลวม")
                elif msg.text in ["บอทอะไร","คือไร","คืออะไร"]:
                    nadya.sendMessage(msg.to, "ไม่บอกปล่อยให้งง")
                elif msg.text in ["กวนตีน","กวน","บอทกวนตีน"]:
                    nadya.sendMessage(msg.to, "ต่อยกับลูกพี่ผมป่ะล่ะ")
                elif msg.text in ["ถถ","ถถถ","ถถถถ","ถถถถถ"]:
                    nadya.sendMessage(msg.to, "ถถถ หาพระแสงหรอจ๊ะ")
                elif msg.text in ["รำ","ลำ","ใครรำ","กุรำ"]:
                    nadya.sendMessage(msg.to, "อืมก็รำสิ")






        if op.type == 65:
            if op.param1 not in admin:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = nadya.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                nadya.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    nadya.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        nadya.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            nadya.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                nadya.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    nadya.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        nadya.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
#                else:
 #                   print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
        if op.type == 55:
            try:
                if Cctv['cyduk'][op.param1]==True:
                    if op.param1 in Cctv['point']:
                        Name = nadya.getContact(op.param2).displayName
                        if Name in Cctv['sidermem'][op.param1]:
                            pass
                        else:
                            Cctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=["อ่านแล้ว","แอบอ่าน","คนซุ่มอ่าน","เข้ามาอ่าน","หลอยอ่าน","ยอมอ่าน","คิดได้แล้วมาอ่าน","ทนไม่ไหวต้องอ่าน"]
#                            sendMessageWithMention(op.param1, op.param2)
                            random.choice(KAC).sendMessage(op.param1, (Name+' '+str(random.choice(pref))))
 #                           line.sendContact(op.param1, op.param2)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if Cctv['cyduk'][op.param1]==True:
                    if op.param1 in Cctv['point']:
                        Name = nadya.getContact(op.param2).displayName
                        if Name in Cctv['sidermem'][op.param1]:
                            pass
                        else:
                            Cctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                                nick = Name.split(' ')
                            if len(nick) == 2:
                                nadya.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
        if op.type == 55:
            print ("[ 🅷ᴬᶜᴷ 🆂ᶜᴬᴺ 🆆ᴵᴺ ]")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = nadyaPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(nadyaBot(op))
                   nadyaPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()

