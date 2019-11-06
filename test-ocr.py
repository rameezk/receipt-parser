import pytesseract
import PIL.Image
import sys


def process(file):
    print("[..] Processing...")
    image = PIL.Image.open(file)
    text = pytesseract.image_to_string(image)
    return {"text": text}


if len(sys.argv) < 2:
    print("Please provide a path to a file")
    sys.exit(1)

file_path = sys.argv[1]
print(process(file_path))
