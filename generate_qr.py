# generate_qr.py
import qrcode

# Create the QR code
data = "https://github.com/jewellfrv/IS601-homework-3"
qr = qrcode.make(data)

# Save the QR code
qr.save("/app/qr_code.png")
print("QR code generated and saved as qr_code.png")
