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

#%%
import re
def turm_trainer(n_digits = 4):
    '''
    Copyright (C) SH
    '''
    num = "0"
    # for safety max while loop
    n_max = 10
    n = 0
    # in case there are zeros in number -> draw again
    while len(re.findall(pattern = "0", string = num)) > 0 and n <= n_max:
        num = str(random.randint(10 ** (n_digits - 1), 10 ** (n_digits) - 1))
        n = n + 1
    print("Calculate: {}".format(num))
    start = time.clock()
    input("Press <ENTER> for solution..")
    end = time.clock()
    print("--" * 40)
    tmp = int(num)
    print("\n{} * 2".format(tmp))
    for i in range(2, 10):
        tmp = tmp * i
        if i == 9:
            print("\n{} : 2".format(tmp))
        else:
            print("\n{} * {}".format(tmp, i + 1))
    tmp = tmp / 2
    for i in range(3, 10):
        print("\n{} : {}".format(int(tmp), i))
        tmp = tmp / i
    print("\n{}".format(int(tmp)))
    print("--" * 40)
    print("\nTime: {} sec ({} min)".format(np.round(end-start, 1), np.round((end-start)/60, 2)))
    return(True)
    
    