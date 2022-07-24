"""                               Healthy programmer
Assume that a programmer works at the office from 9am-5 pm. We have to take care of his health and remind him three
things,

To drink a total of 3.5-liter water after some time interval between 9-5 pm.
To do eye exercise after every 30 minutes.
To perform physical activity after every 45 minutes.
                                     INSTRUCTIONS
The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he has
done the task.
For Water, the user should enter “Drank”
For Eye Exercise, the user should enter “EyDone”
For Physical Exercise, the user should enter “ExDone”
After the user enters the input, a file should be created for every task separately, which contains the details about
the time when the user performed a certain task.
"""
from pygame import mixer
import datetime
import time

def music_play(sound,stopper):
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    while True:
        b = input().capitalize()
        if b == stopper:
            mixer.music.stop()
            break

def log(string):
    with open("myLog.txt","a") as f:
        f.write(f"{string} at {datetime.datetime.now()}\n")


if __name__ == "__main__":
    eyessec = time.time()
    watersec = time.time()
    physicalexsec = time.time()
    while True:

        if time.time() - eyessec > 30*60:
            print('Time to do some eye exercise\nEnter stop to stop the alarm')
            music_play("Eyes.mp3","Stop")
            eyessec = time.time()
            log("Eye Exercise done")

        elif time.time() - watersec>50*60:
            print('Time to drink water\nEnter stop to stop the alarm')
            music_play("Water.mp3","Stop")
            watersec = time.time()
            log("Drank Water")

        elif time.time() - physicalexsec >45*60:
            print("Time to do some exercise\nEnter stop to stop the alarm")
            music_play("physical_ex.mp3","Stop")
            physicalexsec = time.time()
            log("Physical exercise done")












