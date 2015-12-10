import Image


def main():
    box = (0, 0, 750, 500)
    filename = "img/img.jpg"

    image = Image.open(filename)
    image_crop = image.crop(box)

    image_crop.show()

    del image, image_crop


if __name__ == "__main__":
    main()
