import PIL.Image
import sys

# ASCII CHARS REPRESENTING DENSITY OF A PIXEL (FROM HIGH TO LOW)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# RESIZE IMAGE
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width) * 0.55
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# CONVERT IMAGE TO GRAYSCALE
def convert_image_to_grayscale(image):
    return image.convert("L")


# MAP EVERY PIXELS TO ASCII CHAR
def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


# MAIN FUNCTION THAT CONVERT IMAGE TO ASCII ART
def convert_image_to_ascii_art(path, new_width=100):
    try:
        image = PIL.Image.open(path)

    except:
        print(f"{path} is not valid")
        return

    image = resize_image(image, new_width=new_width)

    image = convert_image_to_grayscale(image)

    ascii_str = map_pixels_to_ascii(image)

    img_width = image.width

    ascii_image = "\n".join(
        [ascii_str[i : i + img_width] for i in range(0, len(ascii_str), img_width)]
    )

    # print(ascii_image)
    print("ASCII art generated.")

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


if __name__ == "__main__":
    """
    1. RESIZE IMAGE
    2. CONVERT IMAGE INTO GRAYSCALE
    3. MAP EVERY PIXEL TO ASCII CHARACTER ACCORDING TO DENSITY
    4. RETURN ASCII ART
    """

    if len(sys.argv) != 2:
        print("Usage: python ascii_image.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    convert_image_to_ascii_art(path=path, new_width=100)
