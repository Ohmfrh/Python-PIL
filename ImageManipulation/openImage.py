import Image


def main():
    filename = "img/img.jpg"

    image = Image.open(filename)

    image.show()

    del image

if __name__ == "__main__":
    main()
