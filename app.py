from tkinter import *
import pyttsx3
import speech_recognition as sr
import pydub
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox
import sys
import os
import subprocess

# from tkinter (object)
root = Tk()
root.title('Employee App By [HESHAM]')

#size window and centre the window
root.geometry('500x470+500+100')
root.resizable(False,False)


# welcome sound:
def welcome():
    music = AudioSegment.from_wav("sounds/welcome.wav")
    play(music)
# thanks sound :
def ThankYou():
    music = AudioSegment.from_wav("sounds/thanks.wav")
    play(music)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# [0] >> internal mic
engine.setProperty('voice' ,voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def TakeCommands():
    rec = sr.Recognizer()
    with sr.Microphone() as mic :
        rec.phrase_threshold = 0.1
        audio = rec.listen(mic)
        try:
            voice = rec.recognize_google(audio)
        except Exception as Error :
            print(Error)
        return voice.lower()
    
# button save action and make QRCode with data
def Saving():
    namefile = ESave.get()
    na = EName.get()
    jo = EJob.get()
    co = EContract.get()
    cy = ECity.get()
    ph = EPhone.get()
    
    # check if Entry == null :
    if namefile == "" or  na =="" or jo == "" or co == "" or cy == "" or ph == "":
        messagebox.showinfo('Data Missing!' , 'Please insert data in required fields !')
 
    else:
        
        qr = qrcode.make(f'Employee Name : {na}\nJob Profile : {jo}\nContract Type : {co}\nPhone number : {ph}\nCity : {cy}')
        qr.save("employees/"+namefile+".jpg")
        engine.say("Saved Successfully")   
        messagebox.showinfo('Saved Successfully 👌' , 'Saved ['+namefile+'] Employee')
        engine.runAndWait()
  

# buttons actions:
def B_Name():
    query = TakeCommands()
    name = query
    EName.insert(0,name)        

def B_Job():
    query = TakeCommands()
    name = query
    EJob.insert(0,name)   
    
def B_Contract():
    query = TakeCommands()
    name = query
    EContract.insert(0,name)       

def B_City():
    query = TakeCommands()
    name = query
    ECity.insert(0,name)   

def B_Phone():
    query = TakeCommands()
    name = query
    EPhone.insert(0,name)
        
# Logo
photo = PhotoImage(file = 'logo.png')
l_img = Label(root,image= photo)
l_img.place(x=8,y=0,width=500,height=150)

# labels and font 
name = Label(root , text = "Employee name :", font= ("Tajawal",16))
name.place(x= 10 ,y=170)

job = Label(root , text = "Job Profile :", font= ("Tajawal",16))
job.place(x=10  ,y=210)

contract = Label(root , text = "Contract type :", font= ("Tajawal",16))
contract.place(x= 10 ,y=250)

phone = Label(root , text ="Phone :" , font = ('Tajawal' , 16))
phone.place(x=10 , y= 290)

city = Label(root , text = "City :", font= ("Tajawal",16))
city.place(x= 10 ,y=330)

# notice : 
LNotice = Label(root , text='All data is required' ,font=('arial' , 12) , fg='navy' )
LNotice.place(x=181, y=139)

# Entry Labels:
EName = Entry(root , font= ("Tajawal",16))
EName.place(x=200,y=170)

EJob= Entry(root , font= ("Tajawal",16))
EJob.place(x=200,y=210)

EContract = Entry(root , font= ("Tajawal",16))
EContract.place(x=200,y=250)

EPhone = Entry(root , font=('Tajawal' ,16))
EPhone.place(x=200,y=290)

ECity = Entry(root , font= ("Tajawal",16))
ECity.place(x=200,y=330)

# Buttons to speak:
BName = Button(root , text='🔊', bg = 'navy' , fg='white' ,font=('Tajawal',11) , command= B_Name)
BName.place(x=450,y=168)

BJob = Button(root , text='🔊', bg = 'navy' , fg='white' ,font=('Tajawal',11) , command= B_Job)
BJob.place(x=450,y=208)

BContract = Button(root,text='🔊', bg = 'navy' , fg='white' ,font=('Tajawal',11), command= B_Contract)
BContract.place(x=450,y=248)

BPhone = Button(root,text= '🔊' ,bg='navy' , fg= 'white' ,font=('tajawal', 11),  command=B_Phone)
BPhone.place(x=450, y=288)

BCity = Button(root , text='🔊', bg = 'navy' , fg='white' ,font=('Tajawal',11) , command= B_City)
BCity.place(x=450,y=328)
  
# Label save :
LSave = Label(root , text = 'File Name :' , font= ('Tajawal' , 16))
LSave.place(x=10,y=380)
LReq = Label(root,text = '(Required)' , font =('Tajawal',8) , fg='red')
LReq.place(x=135, y=385)

# Entry Save
ESave = Entry(root, font=('Tajawal',16), width=16)
ESave.place(x=200,y=380)

# Button save
Bsave = Button(root, text='Save✅' ,fg='white' , bg='navy', font=('Tajawal' ,14 ), command= Saving)
Bsave.place(x=400 , y=375)

# Developer
LRights= Label(root , text='Developed By HESHAM' , font = ("Arial",10))
LRights.place(x=180,y=450)

# Run :
welcome()
root.mainloop()
ThankYou()
