# Generate QR Code
import pyqrcode
import png
from pyqrcode import QRCode

QRString = input("Please input URL here:")
url = pyqrcode.create(QRString)
url.png('qr.png', scale=8)
