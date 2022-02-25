import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data("아무것도 아닌데")
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save("C:/Users/고객님/Desktop/vaction/pyqrcode/img/custom.png")