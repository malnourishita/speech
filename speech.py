import speech_recognition as sr

r = sr.Recognizer()

keyWord = 'hello'

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
