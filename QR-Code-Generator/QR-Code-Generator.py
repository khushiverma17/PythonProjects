import qrcode
import image

# img = qrcode.make("https://pypi.org/project/qrcode/")
# type(img)
# img.save("qr1.png")

#FOR MORE OPTIONS/CONTROL

qr = qrcode.QRCode(
    version =10, #from 1 to 40 size of qr code also denotes the complexity of the qr code
    box_size=10,
    border=5
)
qr.add_data("https://www.youtube.com/watch?v=EbdPKtu_9Ww")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("qr2.png")