from asyncio import constants
import qrcode
from PIL import Image

um_img = Image.open('C:/Users/고객님/Desktop/vaction/pyqrcode/um.jpg')

um_img.thumbnail((60, 60))
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://www.youtube.com/channel/UCVThcKfZaJc-Fxwdp2x9HgQ')
qr.make()
um_youtube = qr.make_image().convert('RGB')
pos = ((um_youtube.size[0] - um_img.size[0]) //2 , (um_youtube.size[1] - um_img.size[1]) // 2)

um_youtube.paste(um_img, pos)
um_youtube.save("C:/Users/고객님/Desktop/vaction/pyqrcode/img/qrum.png")
print(um_youtube.size)