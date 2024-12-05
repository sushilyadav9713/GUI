from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Cute Puppies")
root.iconbitmap('sun_with_random_colors.ico')

my_img1 = ImageTk.PhotoImage(Image.open('images/cute_dog.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/cute_dog2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/cute_dog3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/cute_dog4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('images/cute_dog5.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('images/cute_dog6.jpg'))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<",command=back,state=DISABLED)
button_quit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()