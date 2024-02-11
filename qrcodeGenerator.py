# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import qrcode

# Data for the QR code
data = "https://github.com/AbhiSathya?tab=stars"  # You can replace this with your desired data

# Generate QR code
qr = qrcode.QRCode(version=1)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_image.save("qrcode.png")
print("QR code saved as 'qrcode.png'")
