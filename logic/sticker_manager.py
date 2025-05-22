# logic/sticker_manager.py

from PyQt5.QtGui import QPixmap, QPainter, QFont
from PyQt5.QtCore import QRect
import os

def save_sticker_as_image(plate, area, expiry, sticker_type):
    width, height = 400, 300
    output_dir = "static/stickers"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{plate}_sticker.png")

    pixmap = QPixmap(width, height)
    pixmap.fill()

    painter = QPainter(pixmap)
    font = QFont("Arial", 14)
    painter.setFont(font)

    # Draw basic info
    painter.drawText(QRect(20, 20, 360, 30), 0, f"Plate: {plate}")
    painter.drawText(QRect(20, 60, 360, 30), 0, f"Area: {area}")
    painter.drawText(QRect(20, 100, 360, 30), 0, f"Expiry: {expiry}")
    painter.drawText(QRect(20, 140, 360, 30), 0, f"Type: {sticker_type}")

    # Load QR if exists
    qr_path = f"static/qr_codes/{plate}.png"
    if os.path.exists(qr_path):
        qr = QPixmap(qr_path).scaled(100, 100)
        painter.drawPixmap(280, 180, qr)

    painter.end()

    pixmap.save(path)
    print(f"Sticker saved at: {path}")
