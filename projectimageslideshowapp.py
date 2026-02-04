import tkinter as tk
import time
from PIL import Image, ImageTk
#main window
root =tk.Tk()
root.title("ArJa photo slideshow Album")
root.geometry("900x900")

#list of image path
image_path=[
    r"C:\Users\User\OneDrive\Desktop\images\IMG_20230804_174124.jpg"
    r"C:\Users\User\OneDrive\Desktop\images\IMG_20240810_124136.jpg"
    r"C:\Users\User\OneDrive\Desktop\images\IMG_20241031_205121.jpg"
]

image_size =(700, 600)
image =[]
for path in image_path:
    img = Image.open(path)
    img = image.resize()
    image.append(img) #addig each imagein list
#convert pil image into tkinter compatable image:
final_image=[]
for img in image:
    photo = ImageTk.photoIamge(img) 
    final_image.append(photo)
#label widget to photo:
image_label = tk.label(root)
image_label.pack(pady=30)
#slideshow function:
def start_slideshow():
    for photo in final_image:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)
#button 
play_button=tk.button(
    root,
    text ="play the ArJa slide show",
    # font=("Arial",17),
    command = start_slideshow
)        
play_button.pack(pady=40)
root.mainloop() # this is to keep window open


