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

# Load and preprocess the first image
image_path = Path("static/images/en_article2.jpg")
# img = preprocess_image(image_path)
img = Image.open(image_path)
# Use pytesseract to do OCR on the image with psm 3
text = pytesseract.image_to_string(img)
# text = pytesseract.image_to_string(
#     img, lang="eng", config="--psm 3 -c min_characters_to_try=50"
# )
print(f"Here is the text from first image:\n{text}")

# # Load and preprocess the second image
# image_path = Path("static/images/en_article1.png")
# img = preprocess_image(image_path)
# # Use pytesseract to do OCR on the image with psm 3
# text = pytesseract.image_to_string(img, lang="eng", config="--psm 3")
# print(f"Here is the text from second image:\n{text}")
