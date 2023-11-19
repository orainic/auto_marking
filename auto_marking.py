from PIL import Image
import pytesseract
from pathlib import Path


# Function to preprocess the image
def preprocess_image(image_path):
    img = Image.open(image_path)
    # Convert to grayscale
    img = img.convert("L")
    return img


# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load and preprocess the image
image_path = Path("static/images/en_article1.png")
# image_path = Path("static/images/en_article2.jpg")
# image_path = Path("static/images/en.png")
# img = preprocess_image(image_path)
img = Image.open(image_path)

# Convert image to grayscale
gray_img = img.convert('L')

# Binarize image (i.e., convert to black and white)
threshold = 200
bw_img = gray_img.point(lambda x: 0 if x<threshold else 255, '1')

# Use pytesseract to do OCR on the image with psm 3
text = pytesseract.image_to_string(img)
# text = pytesseract.image_to_string(
#     img, lang="eng", config="--psm 3 -c min_characters_to_try=50"
# )
print(f"Here is the text from the image:\n{text}")

