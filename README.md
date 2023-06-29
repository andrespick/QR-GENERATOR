# QR-GENERATOR
QR generator in Python using the Qrcode, Pillow and Tkinter libraries

Python 3.10.6

## Generate QR codes
For the program to work correctly you have to install the <a href="https://pypi.org/project/qrcode/" target="_blank">qrcode</a> :

```bash
  pip install qrcode
```
and <a href="https://pypi.org/project/Pillow/" target="_blank">pillow</a> :

```bash
  pip install pillow
```
## What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast
readability and comparatively large storage capacity. The code consists of
black modules arranged in a square pattern on a white background. The
information encoded can be made up of any kind of data (e.g., binary,
alphanumeric, or Kanji symbols)

## Usage
When you already have the local repository, execute the main and you will get a graphical interface where you can put what you want the QR to be called and the link to which you want to link it

## Advanced Usage

```python
def generar_qr(path, name_qr, link):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'{path}/{name_qr}')
```
The ``version`` parameter is an integer from 1 to 40 that controls the size of
the QR Code (the smallest, version 1, is a 21x21 matrix).
Set to ``None`` and use the ``fit`` parameter when making the code to determine
this automatically.

The ``box_size`` parameter controls how many pixels each "box" of the QR code
is.

The ``border`` parameter controls how many boxes thick the border should be
(the default is 4, which is the minimum according to the specs).

``fill_color`` and ``back_color`` can change the background and the painting
color of the QR, when using the default image factory. Both parameters accept
RGB color tuples

