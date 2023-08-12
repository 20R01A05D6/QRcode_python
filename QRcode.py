# importing the qrcode module  
import qrcode  
# using the make() function  
img=qrcode.make('https://www.google.com')
# saving the QR code image 
img.save('qrcode1.png')
# showing the QR code image
img.show()
  
