# import modules
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
Logo_link = 'fuji lubricants crop.jpg'

logo = Image.open(Logo_link)

# taking base width
basewidth = 150

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://www.facebook.com/fujilubricantsmyn'

#data for VCard

data = '''BEGIN:VCARD

VERSION:3.0

N:Lastname;Surname

FN:Displayname

ORG:EVenX

URL:URL HERE

EMAIL:SOME@EMAIL.COM

TEL;TYPE=voice,work,pref:+49 1234 56788

ADR;TYPE=intl,work,postal,parcel:;;Wallstr. 1;Tehran;;12345;Iran

END:VCARD'''

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
# QRcolor = '#8F2C21'
QRcolor = '#000'

# adding color to QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
# QRimg = QRcode.make_imge(fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('FUJI_lubricants_QR.png')

print('QR code generated!')