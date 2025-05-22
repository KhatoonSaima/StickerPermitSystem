import qrcode

# Data to encode
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=2,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box (pixel size of each square in the QR code)
    border=4,  # Border thickness
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the QR code as an image file
img.save("example_qr_code.png")

# Optionally, display the QR code
img.show()
