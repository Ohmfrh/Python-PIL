import Image


def main():
    filename_one = 'img/img.jpg'
    filename_two = 'img/img4.jpg'

    image_one = Image.open(filename_one)
    image_two = Image.open(filename_two)

    image_blended = Image.blend(image_one, image_two, 0.2)

    # image_one.show()
    # image_two.show()
    image_blended.show()

    del image_one, image_two

if __name__ == "__main__":
    main()
