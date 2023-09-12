import os
import shutil
import cv2

if __name__ == '__main__':
    xml_dirs = 'Annotations/'
    test_image = 'JPEGImages/'
    # print(data[0].split(';', 6))
    for image in os.listdir(test_image):
        print(image)
        filename = os.path.splitext(os.path.split(image)[1])[0]
        if not os.path.exists(xml_dirs + filename + '.xml'):
            print('delete:',image)
            os.remove(test_image + image)
    print('over')
