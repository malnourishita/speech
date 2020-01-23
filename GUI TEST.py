import speech_recognition as sr
from tkinter import *
from twilio.rest import Client
r = sr.Recognizer()
word = "hello"
number = "+639437057481"
messagew = "Help Me!"

def register_user():

  global word
  word = keyword.get()
  print(word)

  Label(screen1, text = "Change Key Word Success", fg = "green" ,font = ("calibri", 11)).pack()

def numberc():

  global number
  number = num.get()
  print(number)

  Label(screen3, text = "Change Number Success", fg = "green" ,font = ("calibri", 11)).pack()

def messageq():

  global messagew
  messagew = message.get()
  print(messagew)

  Label(screen4, text = "Change Text Success", fg = "green" ,font = ("calibri", 11)).pack()

 
def ckeyword():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
   
  global keyword
  global keyword_entry
  keyword = StringVar()
 
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "New Key Word").pack()
  keyword_entry = Entry(screen1, textvariable = keyword)
  keyword_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Change", width = 10, height = 1, command = register_user).pack()

def start():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()
  keyWord = word
  print(word)
  
  with sr.Microphone() as source:
      print('Please start speaking..\n')
      while True: 
        audio = r.listen(source)  
        try:
            text = r.recognize_google(audio)
            if keyWord.lower() in text.lower():
                print('Keyword has been succesfully detected.'),
                make_call()
                return sum
                
        except Exception as e:
            print('Please speak again.')

def make_call():

  account_sid = 'AC010e724d12614998b71d426c3068c5db'
  auth_token = 'a084f0fbb12393ef1c02564cf9ad037b'
  client = Client(account_sid, auth_token)

  message = client.messages \
                .create(
                     body= (messagew),
                     from_="+13237451127",
                     to= number
                 )

  print(message.sid)

def changetext():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("CHANGE TEXT")
  screen4.geometry("300x250")
   
  global message
  global message_entry
  message = StringVar()
 
  Label(screen4, text = "Please enter details below").pack()
  Label(screen4, text = "").pack()
  Label(screen4, text = "CHANGE NUMBER").pack()
  message_entry = Entry(screen4, textvariable = message)
  message_entry.pack()
  Label(screen4, text = "").pack()
  Button(screen4, text = "Change", width = 10, height = 1, command = messageq).pack()

def changenumber():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("CHANGE NUMBER")
  screen3.geometry("300x250")
   
  global num
  global num_entry
  num = StringVar()
 
  Label(screen3, text = "Please enter details below").pack()
  Label(screen3, text = "").pack()
  Label(screen3, text = "CHANGE NUMBER").pack()
  num_entry = Entry(screen3, textvariable = num)
  num_entry.pack()
  Label(screen3, text = "").pack()
  Button(screen3, text = "Change", width = 10, height = 1, command = numberc).pack()

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("640x480")
  screen.title("SPEECH RECOGNIZER SECURITY SYSTEM")
  Label(text = "SPEECH RECOGNIZER SECURITY SYSTEM", bg = "yellow", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Change Key Word",height = "2", width = "30", bg = "white", command = ckeyword).pack()
  Label(text = "").pack()
  Button(text = "TEST TEXT",height = "2", width = "30", bg = "white", command = make_call).pack()
  Label(text = "").pack()
  Button(text = "CHANGE NUMBER",height = "2", width = "30", bg = "white", command = changenumber).pack()
  Label(text = "").pack()
  Button(text = "CHANGE MESSAGE",height = "2", width = "30", bg = "white", command = changetext).pack()
  Label(text = "").pack()
  Button(text = "START",height = "4", width = "60", bg = "black", fg="white", font = ("Arial", 25), command = start).pack()
 
  screen.mainloop()
 
main_screen()
  
