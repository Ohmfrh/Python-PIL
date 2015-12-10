import Image


def main():
    filename_one = 'img/img.jpg'
    filename_two = 'img/img4.jpg'

    image_one = Image.open(filename_one)
    image_two = Image.open(filename_two)

    Image.composite(image_one, image_two, image_two).show()

    del image_one, image_two

if __name__ == "__main__":
    main()
