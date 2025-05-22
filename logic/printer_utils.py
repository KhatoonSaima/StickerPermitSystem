# logic/printer_utils.py
#from PyQt5.QtPrintSupport import QPrinter, QPainter
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect

def print_sticker(plate, area, expiry, sticker_type, qr_pixmap):
    printer = QPrinter()
    printer.setPageSize(QPrinter.Custom)
    printer.setFullPage(True)
    printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
    printer.setPaperSize(QPrinter.Custom)
    printer.setOutputFormat(QPrinter.NativeFormat)

    painter = QPainter()
    if not painter.begin(printer):
        print("Error: Unable to open printer")
        return

    try:
        # Draw QR code
        rect = QRect(10, 10, 150, 150)
        painter.drawPixmap(rect, qr_pixmap)

        # Draw text fields
        painter.setFont(QFont("Arial", 10))
        painter.drawText(180, 30, f"Plate: {plate}")
        painter.drawText(180, 60, f"Area: {area}")
        painter.drawText(180, 90, f"Expiry: {expiry}")
        painter.drawText(180, 120, f"Type: {sticker_type}")
    finally:
        painter.end()
