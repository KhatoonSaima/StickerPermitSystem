# main.py

import os
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5 import QtWidgets, uic
from logic.qr_generator import generate_qr
from logic.database import save_record
from logic.printer_utils import print_sticker
from logic.sticker_manager import save_sticker_as_image



class StickerPermitApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_window.ui", self)

        # Connect buttons to functions
        self.generateQRButton.clicked.connect(self.handle_generate_qr)
        self.printStickerButton.clicked.connect(self.handle_print_sticker)
        self.saveStickerButton.clicked.connect(self.handle_save_sticker)
        self.saveRecordButton.clicked.connect(self.handle_save_record)
         

    def handle_generate_qr(self):
        plate = self.plateNumberInput.text()
        area = self.areaInput.text()
        expiry = self.expiryDateInput.date().toString("yyyy-MM-dd")
        sticker_type = self.stickerTypeCombo.currentText()

        data = f"{plate}|{area}|{expiry}|{sticker_type}"
        qr_path = generate_qr(data, plate)

        self.qrCodeLabel.setPixmap(qr_path)

    def handle_print_sticker(self):
        plate = self.plateNumberInput.text()
        area = self.areaInput.text()
        expiry = self.expiryDateInput.date().toString("yyyy-MM-dd")
        sticker_type = self.stickerTypeCombo.currentText()
        qr_pixmap = self.qrCodeLabel.pixmap()

        if qr_pixmap is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please generate a QR code before printing.")
            return

        print_sticker(plate, area, expiry, sticker_type, qr_pixmap)


    def handle_save_sticker(self):
        plate = self.plateNumberInput.text()
        area = self.areaInput.text()
        expiry = self.expiryDateInput.date().toString("yyyy-MM-dd")
        sticker_type = self.stickerTypeCombo.currentText()
        save_sticker_as_image(plate, area, expiry, sticker_type)

    def handle_save_record(self):
        plate = self.plateNumberInput.text()
        area = self.areaInput.text()
        expiry = self.expiryDateInput.date().toString("yyyy-MM-dd")
        sticker_type = self.stickerTypeCombo.currentText()
        save_record(plate, area, expiry, sticker_type)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StickerPermitApp()
    window.show()
    sys.exit(app.exec_())

