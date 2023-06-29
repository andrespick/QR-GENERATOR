import qrcode
import tkinter as tk
from tkinter import filedialog

def generar_qr(path, name_qr, link):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'{path}/{name_qr}')

def generate_qr():
    path = filedialog.askdirectory(title="Select Path")
    name_qr = entry_name.get()
    website_link = entry_link.get()
    if name_qr:
        if not name_qr.endswith('.png'):
            name_qr += '.png'
        generar_qr(path, name_qr, website_link)
        label_status.config(text="QR code generated successfully.")
    else:
        label_status.config(text="Please enter a name for the QR code.")

window = tk.Tk()
window.title("QR Code Generator")

label_name = tk.Label(window, text="Name QR:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_link = tk.Label(window, text="Link web:")
label_link.pack()
entry_link = tk.Entry(window)
entry_link.pack()

button_generate = tk.Button(window, text="Generate QR Code", command=generate_qr)
button_generate.pack()

label_status = tk.Label(window, text="")
label_status.pack()

window.mainloop()
