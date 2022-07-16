from datetime import datetime
from threading import Thread
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from time import sleep  

#color
bg_color = '#ffffff'
co1="#566FC6"
co2="#000000"

#window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)

#frame Up
frame_line = Frame(window,width=400,height=5,bg=co1)
frame_line.grid(row=0,column=0)

frame_body = Frame(window,width=400,height=290,bg=bg_color)
frame_body.grid(row=1,column=0)

#configure frame body
img=Image.open('alarm.png')
img.resize((100,100))
img=ImageTk.PhotoImage(img)

app_image = Label(frame_body,height=100,image=img,bg=bg_color)
app_image.place(x=10,y=10)

name = Label(frame_body,text="Alarm",height=1,font=('Ivy 10 bold'),bg=bg_color)
name.place(x=125,y=10)

hour = Label(frame_body,text="Hour",height=1,font=('Ivy 10 bold'),bg=bg_color,fg=co1)
hour.place(x=127,y=40)
c_hour = Combobox(frame_body,width=2,font=('ariel 15'))
c_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=58)


min = Label(frame_body,text="Min",height=1,font=('Ivy 10 bold'),bg=bg_color,fg=co1)
min.place(x=177,y=40)
c_min = Combobox(frame_body,width=2,font=('ariel 15'))
c_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
c_min.current(0)
c_min.place(x=180,y=58)


sec = Label(frame_body,text="Sec",height=1,font=('Ivy 10 bold'),bg=bg_color,fg=co1)
sec.place(x=227,y=40)
c_sec = Combobox(frame_body,width=2,font=('ariel 15'))
c_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
c_sec.current(0)
c_sec.place(x=230,y=58)


period = Label(frame_body,text="Period",height=1,font=('Ivy 10 bold'),bg=bg_color,fg=co1)
period.place(x=277,y=40)
c_period = Combobox(frame_body,width=3,font=('ariel 15'))
c_period['values'] = ("Am","Pm")
c_period.current(0)
c_period.place(x=280,y=58)

def activate_alarm():
    t=Thread(target=alarm)
    t.start()
     
def deactivate_alarm():
    print("Alarm Deactivated: ",selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame_body,font=('ariel 10 bold'),value=1,text="Start",bg=bg_color,command=activate_alarm,variable=selected)
rad1.place(x=125,y=95)

def sound_alarm():
    mixer.music.load("as it was.mp3")
    mixer.music.play()
    selected.set(0)
    rad2 = Radiobutton(frame_body,font=('ariel 10 bold'),value=2,text="Snooze",bg=bg_color,command=deactivate_alarm,variable=selected)
    rad2.place(x=187,y=95)


def alarm():
    while 1:
        control = selected.get()
        print(control)
        a_hour=c_hour.get()
        a_min=c_min.get()
        a_sec=c_sec.get()
        a_period=c_period.get()
        a_period=str(a_period).upper()

        now=datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        # print(hour)
        # print(minute)
        # print(second)
        # print(period)

        if control==1:
            if a_period==period:
                if a_hour==hour:
                    if a_min==minute:
                        if a_sec==second:
                            print("Time to take a break")
                            sound_alarm()
                            break
        sleep(1)


mixer.init()
window.mainloop()