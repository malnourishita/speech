import speech_recognition as sr
from tkinter import *
r = sr.Recognizer()
word = 1

def register_user():

  global word
  word = keyword.get()
  print(word)

  Label(screen1, text = "Change Key Word Success", fg = "green" ,font = ("calibri", 11)).pack()
 
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
                import make_call
                
        except Exception as e:
            print('Please speak again.')

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("SPEECH RECOGNIZER SECURITY SYSTEM")
  Label(text = "SPEECH RECOGNIZER SECURITY SYSTEM", bg = "yellow", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Change Key Word",height = "2", width = "30", command = ckeyword).pack()
  Label(text = "").pack()
  Button(text = "START",height = "2", width = "30", command = start).pack()
 
  screen.mainloop()
 
main_screen()
  
