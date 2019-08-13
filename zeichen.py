from PIL import Image, ImageFilter, ImageTk
import os
import PIL
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkinter
import cv2
import random
from tkinter import *
import pynput
from pynput.keyboard import Key, Controller
from time import sleep

#os.chdir("./hiragana")
#hiragana = os.listdir(".")
"""
for hira in hiragana:
	im = Image.open(hira)
	#im.show()
	plt.imshow(np.asarray(im))
	plt.draw()
	plt.pause(10)
	
for hira in hiragana:
	img=mpimg.imread(hira)
	imgplot = plt.imshow(img)
	plt.show()
	"""
"""
for hira in hiragana:
	im = Image.open(hira)
	im.show()
	#plt.pause(10)
	break
"""

#All Information
#Database, Learning Style, Trys, Score, Length, Number of symb
stats = ["","",0,0,0,0]

got_text_from_box = False
text_from_box = ""
answer = 0
symbol = 0
new = False


keyboard = Controller()

def beginning():
	print("Choose an Alphabet:")
	print("Now only Hiragana works")
	print("1) Hiragana")
	print("2) Katagana")
	print("3) Both")
	phase_1 = True
	while phase_1:
		x = input()
		if(x == "1"):
			stats[0] = "hiragana"
			phase_1 = False
		elif(x == "2"):
			stats[0] = "katagana"
			phase_1 = False
		elif(x == "3"):
			stats[0] = "both"
			phase_1 = False
		else:
			print("Please enter a valid input")


	print("Enter a Number between 1,1000 as max symb:")
	phase_2b = True
	while phase_2b:
		x = input()
		n = int(x)
		if((n < 1001) and (n > 0)):
			stats[4] = n
			phase_2b = False
		else:
			print("Please enter a valid input")

	print(stats)
	return 0



def send_text(e1):

	global data
	global window
	global answer
	global cv_img

	if (stats[1] == "Reverse"):
		pass #TODO

	phase_3 = True
	got_text_from_box = False

	x = e1
	if(len(x) > 0):
		while (x[-1]==" "):
			x = x[:-1]
	next_one = False
	end = False

	stats[2] += 1

	if (x == answer):
		stats[3] += 1
		print("Richtig")
		next_one = True
	elif(x == "x"): 
		stats[2] -= 1
		end = True
		print("The correct answer was ",answer)
		print(stats)
	elif (x == "c"):
		next_one = True
		print("The correct answer was ",answer)
		sleep(5)
	else:
		print("That was wrong try again or skip or quit:")
	#window.destroy()
	if(stats[5] >= stats[4]):
		end = True

	if end:
		print("Final score:")
		print("You tried ",stats[2]," times")
		print("Of that you have guessed ",stats[3]," correctly")
		print("Thats a ratio of: ",stats[3]/stats[2]*100," %")
		sleep(20)
		window.destroy()

	if next_one:
		stats[5] += 1
		symbol = random.choice(data)
		answer = symbol[:-4]
		window.destroy()
		window = tkinter.Tk()
		window.title("Guess")
		window.geometry("500x500-500+200")
		symbol = random.choice(data)
		answer = symbol[:-4]
		cv_img = cv2.imread("./"+stats[0]+"/"+symbol)
		height, width, no_channels = cv_img.shape
		canvas = tkinter.Canvas(window, width = width, height = height)
		canvas.pack()
		photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
		canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
		cv_img = cv2.imread("./"+stats[0]+"/"+symbol)

		Label(window, text="Skip with c")
		Label(window, text="Quit with x")


		e1 = Entry(window)
		e1.pack()
		e1.focus_set()
		#e1.bind('<Return>',event(e1.get()))

		b1 = Button(window, text="Send", command=lambda : send_text(e1.get()))
		b1.pack()
		Button(window, text="Quit", command=window.quit).pack()
		mainloop()

		window.update()

	return 0



beginning()

print("Prepare Database")

if stats[0] == "both":
	pass #TODO Implement both

data = os.listdir("./"+stats[0])

print("Start learning:")

new = False
learning = True

window = tkinter.Tk()
window.title("Guess")
window.geometry("500x500-500+200")
symbol = random.choice(data)
answer = symbol[:-4]
cv_img = cv2.imread("./"+stats[0]+"/"+symbol)
height, width, no_channels = cv_img.shape
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

e1 = Entry(window)
e1.pack()
e1.focus_set()
e1.bind('<Return>',send_text(e1.get()))

b1 = Button(window, text="Send", command=lambda : send_text(e1.get()))
b1.pack()
Button(window, text="Quit", command=window.quit).pack()


print("Input an answer")
print("Press x to quit")
print("Press c to skip")

window.mainloop( )






"""


	print("Input an answer:")
	print("Press x to quit:")
	print("Press c to skip:")


	phase_3 = True
	while phase_3:
		x = input()
		stats[2] += 1
		if (x == answer):
			stats[3] += 1
			phase_3 = False
		elif (x == "x"): 
			stats[2] -= 1
			print("The correct answer was ",answer)
			learning = False
			phase_3 = False
		elif (x == "c"):
			print("The correct answer was ",answer)
			phase_3 = False
			print("Write something to continue")
			y=input()
		else:
			print("That was wrong try again or skip or quit:")
	stats[5] += 1
	#window.destroy()
	if(stats[5] >= stats[4]):
		learning = False

print(stats)
print("Final score:")
print("You tried ",stats[2]," times")
print("Of that you have guessed ",stats[3]," correctly")
print("Thats a ratio of: ",stats[3]/stats[2]*100," %")



"""








"""

#Create a window
window = tkinter.Tk()
window.title("Guess")
window.geometry("500x500-500+200")
# Load an image using OpenCV
cv_img = cv2.imread("./a.jpg")
#cv2.imshow("Guess",img)
#cv2.moveWindow("Guess",500,500)
# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape
# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()
# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
# Run the window loop
Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()
"""