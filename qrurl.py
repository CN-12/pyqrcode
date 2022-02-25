import qrcode

img_url = qrcode.make("https://namu.wiki/w/%EC%97%84%EC%A4%80%EC%8B%9D")
img_url.save("C:/Users/고객님/Desktop/vaction/pyqrcode/img/qrurl.png")
print(img_url.size)
