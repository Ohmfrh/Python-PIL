import PythonMagick
import Image


def main():
    pdf = 'pdf/1.pdf'
    p = PythonMagick.Image()
    p.density('200')
    p.read(pdf)
    p.write('img/1.jpg')

    filename = 'img/test.jpg'
    image = Image.open(filename)

    image.show()

    del p, image


if __name__ == "__main__":
    main()