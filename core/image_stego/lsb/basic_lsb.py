from PIL import Image

DELIMITER = "#####"

def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def embed(image_path, secret_message, output_path):
    image = Image.open(image_path).convert("RGB")
    binary_message = text_to_bin(secret_message + DELIMITER)

    pixels = image.load()
    data_index = 0

    for y in range(image.height):
        for x in range(image.width):
            pixel = list(pixels[x, y])

            for n in range(3):
                if data_index < len(binary_message):
                    pixel[n] = pixel[n] & ~1 | int(binary_message[data_index])
                    data_index += 1

            pixels[x, y] = tuple(pixel)

    image.save(output_path)

def extract(image_path):
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()

    binary_data = ""

    for y in range(image.height):
        for x in range(image.width):
            pixel = pixels[x, y]

            for n in range(3):
                binary_data += str(pixel[n] & 1)

    decoded = ""

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]

        if len(byte) < 8:
            break

        decoded += chr(int(byte, 2))

        if decoded.endswith(DELIMITER):
            return decoded[:-len(DELIMITER)]

    return decoded