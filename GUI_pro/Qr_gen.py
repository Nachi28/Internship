import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    text = entry.get()
    if text:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        image = qr.make_image(fill="black", back_color="white")
        image = image.resize((400, 400), Image.ANTIALIAS)
        image.save("qrcode.png")  # Save the QR code image
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("500x500")

entry = tk.Entry(window, font=("Arial", 14))
entry.grid(row=0,column=0)

button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
button.grid(row=7,column=9)

label = tk.Label(window)
label.grid(row=9,column=11)      

btn=tk.Button(window,text="Exit",command=window.destroy)
btn.grid(row=11,column=14)

window.mainloop()
