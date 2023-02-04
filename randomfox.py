import tkinter  # makes window
import requests  # for api requests
from PIL import ImageTk, Image  # adding images to window
from io import BytesIO  # bytes --> compatible images

root = tkinter.Tk()  # make + customise window
root.title('[randomfox.ca] Displayer')
root.iconbitmap('icon.ico')
response = requests.get('https://randomfox.ca/floof/').json()
imageurl = response['image']
download = requests.get(imageurl)  # download image data from url
bytearr = download.content  # get byte array
BIOimage = Image.open(BytesIO(bytearr)) 
TKimage = ImageTk.PhotoImage(BIOimage)
foxLabel = tkinter.Label(image=TKimage)
foxLabel.pack()  # add to window

root.mainloop()  # don't close instantly