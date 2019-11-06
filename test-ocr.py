import pytesseract
import PIL.Image
import sys
from wand.image import Image as Img


def process_image(file):
    print("[..] Processing...")
    image = PIL.Image.open(file)
    text = pytesseract.image_to_string(image)
    return {"text": text}


def process_pdf(pdf):
    with Img(filename=pdf, resolution=300) as img:
        img.compression_quality = 99
        img.save(filename=f"{pdf}.jpg")


if len(sys.argv) < 2:
    print("Please provide a path to a file")
    sys.exit(1)

file_path = sys.argv[1]

if file_path.lower().endswith(".pdf"):
    process_pdf(file_path)
    process_image(f"{file_path}.jpg")
else:
    print(process_image(file_path))
