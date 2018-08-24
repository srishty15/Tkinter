# Uploading Image using Tkinter 

from tkinter import *
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk
root = Tk()

file_path = filedialog.askopenfilename(filetypes=[(("Picture File","*.jpg;*.png;*.gif"))])
img=Image.open(file_path)
file_names=str(int(time.time()))
print(file_names)
img.save("C:/Users/9911v/PycharmProjects/Facial Emotion Detector/abc.png")
tkimage=ImageTk.PhotoImage(img)
# imgdisplay.configure(image=tkimage)
# imgdisplay.image=tkimage
root.mainloop()
