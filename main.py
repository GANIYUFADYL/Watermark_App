import tkinter as tk
from tkinter import filedialog, ttk
import os
from PIL import Image, ImageDraw, ImageFont


def open_file():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg")))
    entry.delete(0, tk.END)
    entry.insert(0, file)

def add_watermark():
    img = Image.open(file)
    img = img.convert('RGB')
    width, height = img.size
    draw = ImageDraw.Draw(img)
    text = "fadyl"
    font = ImageFont.truetype("arial.ttf", 50)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # width of the text
    text_height = text_bbox[3] - text_bbox[1]  # height of the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), text, font=font, fill="white")  # You can specify a fill color
    img.save("watermarked_image.jpg", 'JPEG')



root = tk.Tk()
root.title("Image Watermarking")
root.geometry("500x500")

label = ttk.Label(root, text='Select an Image')
label.pack()

entry = ttk.Entry(root, width=50)
entry.get()
entry.pack()

button_1 = ttk.Button(root, text='Browse', command=open_file)
button_1.pack()

button_2 = ttk.Button(root, text='Add Watermark', command=add_watermark)
button_2.pack()

root.mainloop()