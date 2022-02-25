import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
qr.add_data("아무것도 아닌데")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="red")
img.save("C:/Users/고객님/Desktop/vaction/pyqrcode/img/pycus3.png")