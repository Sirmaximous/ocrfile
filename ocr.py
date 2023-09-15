from PIL import Image
import pytesseract
from progressbar import ProgressBar

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract'
Image.MAX_IMAGE_PIXELS = None

print("converting image to 300 DPI")
im = Image.open("test.tif")
imsave = im.convert("P", palette=Image.ADAPTIVE, colors=256)
im.save("test3.tif", optimize=True, dpi=(300,300), compression="tiff_lzw")

""" im2 = im.resize((300,300), Image.ANTIALIAS)
im2.save("test2.tif", quality=85, optimize=True, dpi=(300,300)) """

""" print("Running OCR")
pdf = pytesseract.image_to_pdf_or_hocr('test2.tif', extension='pdf')
with open('test2.pdf', 'w+b') as f:
    f.write(pdf)  """