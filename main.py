import qrcode

def generar_qr(path, name_qr, link):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'{path}{name_qr}')

PATH = "/home/andresfv/Proyectos-Python/generador-qr/imagenes-qr/" #path where you want the files to be
NAMEQR = input("Name QR (dejar vacío para no generar qr): ")

if NAMEQR:
    if not NAMEQR.endswith('.png'):
        NAMEQR += '.png'
    website_link = input('Link web: ')
    generar_qr(PATH, NAMEQR, website_link)