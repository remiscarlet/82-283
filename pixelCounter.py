from PIL import Image
import numpy as np
import os
import time

black = np.array([0,0,0,255])
white = np.array([255,255,255,255])
def notTransparent(pixel):
  return pixel[3] > 0

def isBlack(pixel):
  return sum(black==pixel) == 4
def isWhite(pixel):
  return sum(white==pixel) == 4

def remTransparent(arr):
  ret = []
  for row in arr:
    tmp = filter(lambda pixel: pixel[3] == 255, row)
    ret.append(tmp)
  return np.asarray(ret)

images = os.listdir("img")
images = filter(lambda name: name.find("copy") > -1 and 
                             name.find("png") > -1, images)

for image in images:
  im = Image.open(image)
  start = time.time()
  arr = remTransparent(np.asarray(im))

  counter = lambda p: 1 if isBlack(p) else 0
  counter2 = lambda p: 1 if isWhite(p) else 0
  numBlack = sum(map(lambda row: sum(map(counter, row)), arr))
  numWhite = sum(map(lambda row: sum(map(counter2, row)), arr))

  totalPixels = im.size[0] * im.size[1] - numWhite

  print "--------------"
  print image
  print "Total pixels:", totalPixels
  print "Total text pixels:", numBlack
  print "Percent of page covered in text: %.4g%%" % (float(numBlack)/totalPixels*100)

