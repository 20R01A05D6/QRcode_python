# QRcode_python
The script is mainly used to create a QRcode using URL.

## Code Explaination
<!--Remove the below lines and add yours -->
import qrcode : This line imports the qrcode module, which provides functions and classes to generate QR codes.
 
img = qrcode.make('https://www.google.com') : This statement calls the make() function from the qrcode module and passes a string argument that represents the URL you want to encode in the QR code. The make() function returns an image object that contains the QR code.

img.save('qrcode1.png') : The save() method saves the image object as a PNG file in the current working directory.

img.show() : This statement calls the show() method of the image object, which opens the image file in a default viewer application on your system.

## Prerequisites
<!--Remove the below lines and add yours -->
You only need Python to run this script. You can visit [here](https://www.python.org/downloads/) to download Python.


## How to run the script
<!--Remove the below lines and add yours -->
Running the script is really simple! Just open a terminal in the folder where your script is located and run the following command :

    python QRcode.py


## Sample use of the script
<!--Remove the below lines and add yours -->
```
$ python QRcode.py 

```
![QRcode output1](https://github.com/20R01A05D6/QRcode_python/assets/122285082/56765eb0-0898-4d71-aaa4-52728ee3b641)
