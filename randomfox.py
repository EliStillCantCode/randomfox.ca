# import modules
import tkinter
import requests
from PIL import ImageTk, Image
from io import BytesIO

# make window - add title and icon
root = tkinter.Tk()
root.title('Your Random Fox')
root.iconbitmap('icon.ico')

# API
dict = requests.get('https://randomfox.ca/floof/').json()
imageurl = dict['image']
download = requests.get(imageurl)
bytearray = download.content

# convert and add to window
BIOimage = Image.open(BytesIO(bytearray)) 
TKimage = ImageTk.PhotoImage(BIOimage)
foxLabel = tkinter.Label(image=TKimage)
foxLabel.pack()

# keep window open until closed by user
root.mainloop()