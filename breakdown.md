# Code Breakdown
- `tkinter` is used to make windows <br>
- `requests` is used for API communication <br>
- `Image Tk` and `Image` are for adding images into a tkinter window <br>
- `BytesIO` converts byte arrays into images 
<br> <br>
- `tkinter.Tk()` makes a window and is assigned to var `root` <br>
- `root.title()` sets the window title <br>
- `root.iconbitmap()` sets a .ico to display
<br> <br>
- `.json()` turns the output of the API into a dictionary <br>
- `['image']` takes the image URL from the dictionary <br>
- download the image data from the URL
- `.content` isolates the byte array
<br> <br>
- turn the byte array -> image with `BytesIO` <br>
- convert the image into one that's compatible with `tkinter` <br>
- add the tkinter-compatible image into a label
- `pack` ((add)) the label to the window
<br> <br>
- `root.mainloop()` keeps the window open until it is closed by the user