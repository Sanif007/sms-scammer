import requests, os, sys, time, datetime
from requests import get
print("\033[96mCoded by github.com/Sanif007 \033[0m ")
print("\033[93m Version 3.0 \033[0m")
print("\033[91m Checking dependencies... \033[0m")
time.sleep(2)
os.system("bash rq.sh")
def menu() :
    print("\033[91m1. \033[92mSend anonymous sms\033[0m")
    print("\033[91m2. \033[92mCheck status of sms\033[0m")
    print("\033[91m3. \033[92mHelp\033[0m")
    print("\033[91m4. \033[92mExit\033[0m")
def control() :
    ctrl = input("What you want to do : ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    elif ctrl == "3" :
        help()
    elif ctrl == "4" :
        print("thanks for using it.\nplease stay connected with us. github.com/Sanif007")
        exit()
    else :
        print("\033[91mInvalid number\033[0m")
def sms() :
   phone_no = input("enter phone number : ")
   msg = input("message to send : ")

   resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
   })
   print(resp.text)
   time = datetime.datetime.now()
   save = open("sess.txt", "a")
   save.write(f"\nip = {ip} : time = {time} : stats = {resp.text} : phone no.  = {phone_no}")
def status() :
  textID = input("Enter textID of sms : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")
def help() :
    print("please choose your problem from undergiven conditions! ")
    print("A. Can't send sms after one attempt in a to same number!")
    print("B. Can't send sms due to huge usage of website. ")
    print("C. Can't send more than one sms even to different number. ")
    print("D. Other")
    qna = input(">>> ").lower()
    if qna == "a" :
        print("Bcoz this is just a demo version so it can send only 1 sms in a day to same number however you can send to different number by using vpn.")
    elif qna == "b" :
        print("sometimes when website is used in large amount then they disable free sms for sometime. Please wait for sometime...")
    elif qna == "c" :
        print("please check your vpn carefully and use best vpns only. Like nordvpn , protonvpn etc. ")
    elif qna == "d" :
        print("sorry for any problem! Please mail us your problem on hackersacademyofindia@gmail.com or you can mention your problem in github.com/Sanif007")
    else :
        print("Invalid option!! \n exiting.. Sorry..")
        exit()
os.system("clear")
os.system("toilet -f mono12 -F gay Scammer")
print("\033[94m########################## \033[31mVr. 3.0\033[0m \033[94m#########################  ")
print("\033[1;96mCoded by github.com/Sanif007 \033[0m")
ip = get("https://api.ipify.org").text
print(f"\033[1;93mYou are currently using with ip :\033[0m \033[91;107m{ip}\033[0m ")
menu()
control()
