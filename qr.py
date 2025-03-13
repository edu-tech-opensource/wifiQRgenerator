import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def generate_qr_code(ssid: str, password: str):
    """
    Generates a WiFi QR code that allows users to connect directly.
    
    :param ssid: WiFi network name
    :param password: WiFi password
    :return: QR code image
    """
    qr_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    return img

def save_qr_code(img):
    """Allows the user to save the QR code image."""
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        img.save(file_path)
        print(f"QR code saved as {file_path}")

def download_qr_code(img):
    """Allows the user to download the QR code image."""
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")], title="Download QR Code")
    if file_path:
        img.save(file_path)
        print(f"QR code downloaded as {file_path}")

def create_ui():
    """Creates a UI for user input and QR code display."""
    def generate_and_display():
        ssid = ssid_entry.get()
        password = password_entry.get()
        if ssid and password:
            img = generate_qr_code(ssid, password)
            img_tk = ImageTk.PhotoImage(img)
            qr_label.config(image=img_tk)
            qr_label.image = img_tk
            save_button.config(command=lambda: save_qr_code(img))
            save_button.pack()
            download_button.config(command=lambda: download_qr_code(img))
            download_button.pack()
    
    root = tk.Tk()
    root.title("WiFi QR Code Generator")
    
    tk.Label(root, text="Enter WiFi SSID:").pack()
    ssid_entry = tk.Entry(root)
    ssid_entry.pack()
    
    tk.Label(root, text="Enter WiFi Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    
    generate_button = tk.Button(root, text="Generate QR Code", command=generate_and_display)
    generate_button.pack()
    
    qr_label = tk.Label(root)
    qr_label.pack()
    
    save_button = tk.Button(root, text="Save QR Code")
    download_button = tk.Button(root, text="Download QR Code")
    
    root.mainloop()

if __name__ == "__main__":
    create_ui()
