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

  Label(screen1, text = "Successfully Changed the Key Word", fg = "green" ,font = ("calibri", 11)).pack()

def numberc():

  global number
  number = num.get()
  print(number)

  Label(screen3, text = "Successfully Changed the Number", fg = "green" ,font = ("calibri", 11)).pack()

def texttest():

  account_sid = 'AC640d4d2febaa2031e29932c6dcfc360c'
  auth_token = '18be2a8de7b4df74e34b414bbb80ae79'
  client = Client(account_sid, auth_token)

  message = client.messages \
                .create(
                     body= (messagew),
                     from_="+14697897154",
                     to= number
                 )

  print(message.sid)

def messageq():

  global messagew
  messagew = message.get()
  print(messagew)

  Label(screen4, text = "Successfully Changed the Message", fg = "green" ,font = ("calibri", 11)).pack()

 
def ckeyword():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("CHANGE KEY WORD") 
  screen1.geometry("640x480")
   
  global keyword
  global keyword_entry
  keyword = StringVar()
 
  Label(screen1, text = "Please enter your desired keyword to activate the product:").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "CHANGE KEY WORD", font = ("Arial Bold", 15), fg = "green").pack()
  keyword_entry = Entry(screen1, textvariable = keyword)
  keyword_entry.pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "NOTE: Use words/phrases that are not hard to pronounce", font = ("Arial Bold Italic", 8), fg = "red").pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Change", width = 20, height = 1, bg= "white", font = ("Arial", 10), command = register_user).pack()

def start():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Start speaking...")
  screen2.geometry("300x250")
  Label(screen2, text = "Listening.....").pack()
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

  account_sid = 'AC640d4d2febaa2031e29932c6dcfc360c'
  auth_token = '18be2a8de7b4df74e34b414bbb80ae79'
  client = Client(account_sid, auth_token)

  message = client.messages \
                .create(
                     body= (messagew),
                     from_="+14697897154",
                     to= number
                 )

  print(message.sid)

  account_sid = 'AC640d4d2febaa2031e29932c6dcfc360c'
  auth_token = '18be2a8de7b4df74e34b414bbb80ae79'
  client = Client(account_sid, auth_token)
  
  call = client.calls.create(
                        url="http://demo.twilio.com/docs/voice.xml",
                        to= number ,
                        from_="+14697897154"
                    )

  print(call.sid)
  main_screen


def changetext():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("CHANGE MESSAGE")
  screen4.geometry("640x480")
   
  global message
  global message_entry
  message = StringVar()
 
  Label(screen4, text = "Please enter your desired message bellow:").pack()
  Label(screen4, text = "").pack()
  Label(screen4, text = "CHANGE MESSAGE", font = ("Arial Bold", 15), fg = "green").pack()
  message_entry = Entry(screen4, width=30, textvariable = message)
  message_entry.pack()
  Label(screen4, text = "").pack()
  Label(screen4, text = "NOTE: It is recommended to state your address and name in the text", font = ("Arial Bold Italic", 8), fg = "red").pack()
  Label(screen4, text = "").pack()
  Button(screen4, text = "Change", width = 20, height = 1, bg= "white", font = ("Arial", 10), command = messageq).pack()
  Label(screen4, text = "").pack()
  Button(screen4, text = "Send Test Text Message", width = 20, height = 1, bg= "white", font = ("Arial", 10), command = texttest).pack()

def changenumber():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("CHANGE NUMBER")
  screen3.geometry("640x480")
   
  global num
  global num_entry
  num = StringVar()
 
  Label(screen3, text = "Please enter your number below:").pack()
  Label(screen3, text = "").pack()
  Label(screen3, text = "CHANGE NUMBER", font = ("Arial Bold", 15), fg = "green").pack()
  num_entry = Entry(screen3, textvariable = num)
  num_entry.pack()
  Label(screen3, text = "").pack()
  Label(screen3, text = "NOTE: Write +63 and then your number", font = ("Arial Bold Italic", 8), fg = "red").pack()
  Label(screen3, text = "EXAMPLE : +639999999999", font = ("Arial Bold Italic", 8), fg = "red").pack()
  Label(screen3, text = "").pack()
  Button(screen3, text = "Change", width = 20, height = 1, bg= "white", font = ("Arial", 10), command = numberc).pack()
  Label(screen3, text = "").pack()
  

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("1920x1080")
  screen.title("SPEECH RECOGNIZER SECURITY SYSTEM")
  Label(text = "SPEECH RECOGNIZER SECURITY SYSTEM", width = "300", height = "2", font = ("Arial Bold Italic", 45)).pack()
  Label(text = "").pack()
  Button(text = "Change Key Word",height = "3", width = "30", bg = "white", font = ("Arial Bold", 10), command = ckeyword).pack()
  Label(text = "").pack()
  Button(text = "Change Number",height = "3", width = "30", bg = "white", font = ("Arial Bold", 10), command = changenumber).pack()
  Label(text = "").pack()
  Button(text = "Change Message",height = "3", width = "30", bg = "white", font = ("Arial Bold", 10), command = changetext).pack()
  Label(text = "").pack()
  Button(text = "Test Text",height = "3", width = "30", bg = "white", font = ("Arial Bold", 10), command = make_call).pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Button(text = "START",height = "2", width = "40", bg = "black", fg="white", font = ("Arial Bold", 35), command = start).pack()
 
  screen.mainloop()
 
main_screen()
  
