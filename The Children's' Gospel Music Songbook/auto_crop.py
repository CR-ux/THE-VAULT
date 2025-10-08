from PIL import Image

def auto_crop_image(path):
    img = Image.open(path).convert("L")  # Convert to grayscale
    img.load()

    # Apply a simple threshold to isolate foreground
    thresh = 240
    fn = lambda x : 255 if x > thresh else 0
    binary = img.point(fn, mode='1')

    # Get bounding box of non-white content
    bbox = binary.getbbox()

    if bbox:
        original = Image.open(path)
        cropped = original.crop(bbox)
        cropped.save("aria_cropped.jpg")
        print("Cropped and saved as aria_cropped.jpg")
    else:
        print("No significant content found to crop.")

auto_crop_image("aria.jpg")
