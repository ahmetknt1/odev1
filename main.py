import time
from playsound import playsound
wav_file = "mixkit-city-alert-siren-loop-1008.wav"


def countdown(time_sec):
    while time_sec:
        m, s = divmod(time_sec, 60)
        time_module = '{:02d}:{:02d}'.format(m, s)
        print(time_module, end="\r")
        time.sleep(1)
        time_sec -= 1
    print("wake up")
    playsound(wav_file)


time_sec = int(input("Enter time in seconds: "))

countdown(time_sec)
