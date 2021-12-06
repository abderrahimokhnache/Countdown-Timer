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

#     # if int(M) != '00' and int(H) == '00' :

#     #     time = int(M) * 60 + int(S) 
   
#     # elif int(H) != '00':

#     #     time = int(H) * 3600  + int(M) * 60 + int(S)
 
#     # else :

#     #     time = int(S)

# # get_seconds.bind("<Return>" , set_timer)

# # key , value = range(61) , [i * 60 for i in range(61)]

# # Minutes = dict ( zip (  key  , value  ))

# # print Minutes[59]

# # H1 = range(3601)

# import time , os , sys

# from Fileop import File 

# temp = os.getenv("TMP")


# def options (x):

#     if x == 1:

#         timz = time.time()

#         File(Path = temp + 'Operation.txt' , Mode = 'wb' ,Content = str(timz))

#     elif x == 2 :

#         times =File(Path = temp + 'Operation.txt' , Mode ='r')

#         timee = time.time()

#         c =  timee - float(times)

#         n = time.gmtime(c)

#         print "\n " + str(n.tm_hour).zfill(2) , ':', str( n.tm_min).zfill(2) , ':' ,str( n.tm_sec).zfill(2)

    
# options(1)

# try:
    
#     for x in xrange(10000000):

#         os.system("cls")

#         options(2)

#         print '\n STOP [?] CLR+C'

#         time.sleep(1)

# except KeyboardInterrupt as e:
    
#     sys.exit()


