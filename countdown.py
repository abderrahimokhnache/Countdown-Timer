from tkinter import *

from tkinter import ttk

#GLOBAL VARS

root , font , bg , fg  = Tk() , ("Century Gothic" , 15) , "#333" , '#fff'

#WINDOW CONFIGURES

root.geometry("400x300")
root.title('countdown')
root.configure(bg = "gray1")
# root.iconbitmap('count.ico')


def set_timer():
   
    global H , S , M
   
    H , M , S = get_seconds.get().split(':')

def countdown():

    Start_btn['stat'] = 'disabled'
    
    global S , M , H

    if  int(M) != 0 and int(H) != 0:
        H = int(H)
        M =int(M) 
        S = 59
        M = 59
        H -=1
        M -= 1

    if int(S) == 0 and int(H) == 0 and int(M) == 0 :

        Start_btn['stat'] = 'normal'

        count_lb['text'] = "00:00:00"
        
        H , S , M = 0,0,0 
        #here you can add something to happen when count hit's 0 like an alerting sound
    elif int(S) == 0 :

        S = 59
        M = int(M)
        M -=1
        count_lb['text'] = "%s:%s:%s" % (H , int(M) , S ) 

        countdown()       
   
    else:
        
        timz = ( str(int(H)).zfill(2) , str(int(M)).zfill(2) , str(S).zfill(2))
        
        time_str = '%s:%s:%s' % timz 

        count_lb['text'] = time_str

        S = int(S) -1

        count_lb.after(1000,countdown)


def luanch():

    set_timer()

    countdown()

count_lb = Label(root,text = "00:00:00", fg=fg, bg = "#000" , font = (font[0] , 40))

count_lb.place(relx= 0.2 , rely = 0.3 , relwidth = 0.6, relheight = 0.15)


Start_btn= Button(root , text = "SET" ,font = font ,command = luanch , fg= fg, bg = bg ,relief ='flat')

Start_btn.place(relx= 0.65 , rely = 0.8 , relwidth = 0.25 , relheight = 0.15)


get_seconds = ttk.Entry(root ,font = font)

get_seconds.place(relx= 0.05 , rely = 0.8 , relwidth = 0.6 , relheight = 0.15)

get_seconds.insert(0,"00:00:00")


root.mainloop() 


