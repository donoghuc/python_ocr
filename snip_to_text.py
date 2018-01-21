from PIL import Image
import pytesseract
import argparse
import cv2
import os
import codecs


def parse_args():
    ''' define CLI params'''
    parser = argparse.ArgumentParser(description='Optical Character Recogonition')
    parser.add_argument('-i','--image', help='imput image file (png)', required=True)
    parser.add_argument('-o','--output', help='output text file', required=True)
    return vars(parser.parse_args())


def get_text(image_file):
    ''' do minimal pre-processing and then get the text'''
   
    image = cv2.imread(image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_file = "temp_file.png"
    cv2.imwrite(temp_file, gray)
    text = pytesseract.image_to_string(Image.open(temp_file))
    os.remove(temp_file)
    return text


def main():
    args = parse_args()

    text = get_text(args['image'])
    print(text)
    with open(args['output'], "w") as fo:
        fo.write(text)


if __name__ == '__main__':
    main()