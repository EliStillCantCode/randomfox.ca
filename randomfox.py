import tkinter
import requests
from PIL import ImageTk, Image
from io import BytesIO

def display():
    response = requests.get('https://randomfox.ca/floof/').json()
    imageurl = response['image']
    download = requests.get(imageurl)  # download image data from url
    bytearr = download.content  # get byte array
    BIOimage = Image.open(BytesIO(bytearr)) 
    TKimage = ImageTk.PhotoImage(BIOimage)
    foxLabel = tkinter.Label(image=TKimage)
    foxLabel.pack()  # add to window

root = tkinter.Tk()
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


root.mainloop()