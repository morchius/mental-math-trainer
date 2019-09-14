import win32com.client as wincl
import numpy as np
import time
import random
speak = wincl.Dispatch("Sapi.SpVoice")

speak.Rate = .01
voices = speak.GetVoices()
# for voice in voices:
#    print(voice.getDescription())

def two_by_two(lang = "de"):
    # set language
    if lang == "en":
        speak.Voice = voices[1]
        times = "times"
    elif lang == "de":
        speak.Voice = voices[0]
        times = "mal"
    else:
        raise Exception("Language needs to be either 'en' or 'de'!")
    rand = np.random.randint(10,100,size=2)
    print()
    print(" {} * {}".format(rand[0], rand[1]))
    print()
    speak.Speak("{} {} {}".format(rand[0], times, rand[1]))
    start = time.clock()
    input("Press <ENTER> for solution")
    print()
    end = time.clock()
    print(" {}".format(rand[0]*rand[1]))
    speak.Speak("{}".format(rand[0]*rand[1]))
    print()
    print("Time: {} sec ({} min)".format(np.round(end-start, 1), np.round((end-start)/60, 2)))

def three_by_one():
    left = np.random.randint(100,1000)
    right = np.random.randint(1,10) 
    print()
    print(" {} * {}".format(left, right))
    print()
    speak.Speak("{} times {}".format(left, right))
    start = time.clock()
    input("Press <ENTER> for solution")
    print()
    end = time.clock()
    print(" {}".format(left*right))
    speak.Speak("{}".format(left*right))
    print()
    print("Time: {} sec ({} min)".format(np.round(end-start, 1), np.round((end-start)/60, 2)))
	
def draw_operation_and_number():
    rand = np.random.randint(low = 10, high = 100, size = 1)
    operation = random.choice([0,1,1])
    print(operation)
    if operation:
        rand = "plus " + str(rand[0])
    else:
        rand = "minus " + str(rand[0])
    return(rand)

def run_training(numb_of_rounds):
    n = 0
    control = "run"
    count = 0
    while (n < numb_of_rounds) and (control == "run"):
        res = draw_operation_and_number()
        speak.Speak(res)
        if res.split()[0] == "minus":
            count = count - int(res.split()[1])
        else:
            count = count + int(res.split()[1])
        key = input("Want to stop? Press 0!\nPress <ENTER> to continue!")
        if key == 0:
            control = "stop"
        n += 1
        if (control == "stop") or (n == numb_of_rounds):
            print("Count is: {}".format(count))
    return(count)

    
#%%
import win32com.client as wincl
import numpy as np
import time
# make mental math trainer class
class MM_trainer:
    def __init__(self):
        self.speak = wincl.Dispatch("Sapi.SpVoice")
        self.speak.Rate = .01
        self.voices = self.speak.GetVoices()
        self.avg_time_sec = 0
        self.total_time_sec = 0
        self.n_questions = 0
        self.times = "mal"
        self.n_correct_questions = 0
        self.answer = None
        self.solution = None
        
    # get two by two question
    def two_by_two(self):
        rand = np.random.randint(10,100,size=2)
        self.solution = str(rand[0] * rand[1])
        print("\n{} * {}".format(rand[0], rand[1]))
        self.speak.Speak("{} {} {}".format(rand[0], self.times, rand[1]))
        start = time.clock()
        self.answer = input("\nEnter solution followed by <ENTER>")
        end = time.clock()
        # check if answer is correct
        if self.solution == self.answer:
            print("\nCorrect answer! Well done!")
            self.speak.Speak("Korrekt, sehr gut, weiter so!")
            self.n_correct_questions = self.n_correct_questions + 1
        else:
            print("\nNot correct :(")
            self.speak.Speak("Falsch, Brudi")
        print("\n{}".format(rand[0] * rand[1]))
        self.speak.Speak("{}".format(rand[0]*rand[1]))
        # update total time needed
        self.total_time_sec = self.total_time_sec + end - start
        # update number of questions
        self.n_questions = self.n_questions + 1
        # update average
        self.avg_time_sec = self.total_time_sec / self.n_questions
        # print results
        print("\nTime: {} sec ({} min)".format(np.round(end-start, 1), np.round((end-start)/60, 2)))
        print("\n--------\nAvg Time: {} sec".format(np.round(self.avg_time_sec, 1)))
    
    def set_language(self, lang = "de"):
        pass
        # self.speak.Voice = 


    
    