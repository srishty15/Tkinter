# Uploading Image using Tkinter 

from tkinter import *
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk

root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[(("Picture File","*.jpg;*.png;*.gif"))])  #opens only JPG, PNG or GIF images
img=Image.open(file_path)
img.save("path/image_name.png")  #specify the path in 'path' and image will be saved as image_name.png ; You can edit the image_name to any name 
tkimage=ImageTk.PhotoImage(img)
root.mainloop()

