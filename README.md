# QRcode_python
import qrcode : This line imports the qrcode module, which provides functions and classes to generate QR codes.

obj_qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4) : 
This line creates a QRCode object with some parameters. 
The version parameter specifies the size and complexity of the QR code, from 1 to 40.
The error_correction parameter specifies how much error correction is applied to the QR code, from L (low) to H (high). 
The box_size parameter specifies how many pixels each module (square) of the QR code is.
The border parameter specifies how many modules are added as a white border around the QR code.

obj_qr.add_data("https://www.javatpoint.com/python-tutorial") : 
This line adds the data that will be encoded in the QR code. 
In this case, it is a URL to a Python tutorial website.

obj_qr.make(fit = True) : This line prepares the QR code object for rendering. 
                          The fit parameter tells the object to adjust the size of the QR code according to the data and parameters.
                          
qr_img = obj_qr.make_image(fill_color = "white", back_color = "black") : 
This line creates an image object from the QR code object.
The fill_color and back_color parameters specify the colors of the modules and the background of the image, respectively.

qr_img.save("qr-img2.png") : This line saves the image object as a PNG file with the given name.
