import random
from io import BytesIO
from PIL import Image


def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


class PhotoShuffle:
    def __init__(self, path='image.png'):
        self.img = Image.open(path)
        self.pixels = self.img.load()  # Indexable AccessPixel data type.
        self.pixelArray = []  # Personal pixel array, storing it's order in a counter variable used for replacing the
        # pixels.
        self.size = self.img.size
        counter = 0
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.pixelArray.append((counter, self.img.getpixel((x, y))))
                counter += 1

    def shuffle(self):
        counter = 0
        random.shuffle(self.pixelArray)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.img.putpixel((x, y), (self.pixelArray[counter][1]))
                counter += 1

    def sortPixels(self):
        list.sort(self.pixelArray)
        counter = 0
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.img.putpixel((x, y), (self.pixelArray[counter][1]))
                counter += 1
    # Returns None unless the list is already sorted.
    def sortOnce(self):
        index = 0
        # Making sure we haven't already finished replacing the pixels before checking if the current pixel is in the
        # correct position
        while len(self.pixelArray) > index == self.pixelArray[index][0]:
            index += 1
        if index >= len(self.pixelArray):
            return 1
        # Otherwise, we can swap the pixel at index with it's correct position.
        # Note that the other swapped pixel may be in the incorrect position.
        swap(self.pixelArray, index, self.pixelArray[index][0])
        # Replacing the pixels individually saves much needed time
        # rather than reading the pixelArray back onto the image.
        self.img.putpixel((int(index / self.size[1]), index % self.size[1]),
                          self.pixelArray[self.pixelArray[index][0]][1])
        self.img.putpixel((int(self.pixelArray[index][0] / self.size[1]), self.pixelArray[index][0] % self.size[1]),
                          self.pixelArray[index][1])
    # Swaps two pixels in a random location on the list.
    def shuffleOnce(self):
        l = len(self.pixelArray)
        rand1 = random.randint(0, l - 1)
        rand2 = random.randint(0, l - 1)
        swap(self.pixelArray, rand1, rand2)
        self.img.putpixel((int(rand1 / self.size[1]), rand1 % self.size[1]), self.pixelArray[rand2][1])
        self.img.putpixel((int(rand2 / self.size[1]), rand2 % self.size[1]), self.pixelArray[rand1][1])

    def showImg(self):
        self.img.show()
    # Formats the image into a language kivy can understand, formatting it as a byte array.
    def ImgAsByteArray(self):
        img_byte_arr = BytesIO()
        self.img.save(img_byte_arr, format='png')
        img_byte_arr.seek(0)  # Not sure what this does, but is necessary.
        imgData = BytesIO(img_byte_arr.read())
        return imgData
