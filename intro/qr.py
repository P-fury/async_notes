import qrcode

data = """"""

qr = qrcode.make(data)
qr.save('qr_no_photo.png')