import qrcode

img = qrcode.make("헬로우 마더 퍼커")
img.save("C:/Users/고객님/Desktop/vaction/pyqrcode/img/qrtext.png")
print(type(img))
print(img.size)
