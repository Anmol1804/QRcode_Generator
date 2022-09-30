import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction= qrcode.ERROR_CORRECT_M, box_size=10, border=4)

qr.add_data("https://anmol1804.github.io/MyPortfolio/")

qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="pink")

img.save("custom_anmolprofile.png")

