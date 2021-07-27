# PATH = ~/sbox/lpthw/mystuff/ageindays.py


from datetime import date
import os
import schedule
import time

t = ''
pronoun = "sir"

text1 =("Good morning %s. it is six oclock..." % (pronoun))

def main():
	speak(text1)
	job(t)


def speak(text):
    os.system(f"say {text}")


def job(t):
    speak("Good morning sir it is six am...", t)
    return

schedule.every().day.at("06:00").do(job,'It is 06:00')

# schedule.every().day.at("23:29").do(job,'It is 23:29')


while True:
    schedule.run_pending()
    time.sleep(5) # wait one minute
 

d0 = date(1977, 4, 22)
d1 = date(2019, 8, 22)
d2 = date(2077, 4, 22)
d3 = date(2022, 6, 18)
d4 = date(2019, 9, 3)

delta = d1 - d0
print(delta.days)

print("you are " + str(delta.days) + " days old")

delta2 = d2 - d0

print("you have " + str(delta2.days) + " days left to live")

delta3 = d3 - d4

print("I estimate " + str(delta3.days) + " days until you graduate")

# print("Today is the %d day of your life") % delta.days


def sixty_sixty_thirty():
	"""A method for pomodoro training, 60 min on is 50 t-time then 10 re-time,
	do this twice then take a thirty minute break, use a timer"""
	pass


if __name__ == '__main__':
	main()