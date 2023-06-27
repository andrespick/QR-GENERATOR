import qrcode

def generar_qr(ruta, nombre_qr, link):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'{ruta}{nombre_qr}')

RUTA = "/home/andresfv/Proyectos-Python/generador-qr/imagenes-qr/"
NOMBREQR = input("Nombre del qr (dejar vacío para no generar qr): ")

if NOMBREQR:
    if not NOMBREQR.endswith('.png'):
        NOMBREQR += '.png'
    website_link = input('Link web: ')
    generar_qr(RUTA, NOMBREQR, website_link)