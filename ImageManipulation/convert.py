import Image


def main():
    filename = "img/img.jpg"

    image = Image.open(filename)

    image_c = image.convert("1")

    image_c.show()

    del image, image_c


if __name__ == "__main__":
    main()
