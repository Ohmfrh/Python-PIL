import Image


def main():
    # 1 B/W
    # L Grayscale
    # RGB
    # RGBA
    # CMYK
    # YCbCr
    # I
    # F Float pixels
    size = width, height = 320,240

    image = Image.new("RGB", size, "white")
    image.show()

    del image





if __name__ == "__main__":
    main()