import qrcode

img = qrcode.make("C:/Users/고객님/Desktop/vaction/pyqrcode/um.jpg")
img.save("C:/Users/고객님/Desktop/vaction/pyqrcode/img/qrimg.png")
print(img.size)
#이미지는 안 되는듯...