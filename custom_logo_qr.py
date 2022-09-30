import qrcode
from PIL import Image

logo_path = "alogo.png"
logo = Image.open(logo_path)

basewidth = 100

# image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int(float(logo.size[1])*float(wpercent))

logo = logo.resize((basewidth, hsize))

qr = qrcode.QRCode(error_correction= qrcode.constants.ERROR_CORRECT_H)

qr.add_data("https://anmol1804.github.io/MyPortfolio/")

qr.make(fit=True)

img = qr.make_image(fill_color="darkblue", back_color="white")

pos = ((img.size[0] - logo.size[0])//2 , (img.size[1] - logo.size[1])//2)

img.paste(logo, pos)
img.save("custom_logoQr.png")