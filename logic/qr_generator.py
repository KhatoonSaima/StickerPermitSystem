# logic/qr_generator.py
import qrcode
from PyQt5.QtGui import QPixmap

def generate_qr(data, filename):
    path = f"static/qr_codes/{filename}.png"
    img = qrcode.make(data)
    img.save(path)
    return QPixmap(path)