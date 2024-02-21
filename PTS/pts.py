import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from alg1 import plaka_konum_don
from plakatanima import plakaTani

veriler = os.listdir("veriseti")

isim = veriler[0]


print("veriseti/"+isim)


img = cv2.imread("veriseti/"+isim)


img = cv2.resize(img,(500,500))


plaka = plaka_konum_don(img)

plakaImg,plakaKarakter = plakaTani(img,plaka)

print("arabanin plakasi  :",plakaKarakter)

plt.imshow(plakaImg)
plt.show()


