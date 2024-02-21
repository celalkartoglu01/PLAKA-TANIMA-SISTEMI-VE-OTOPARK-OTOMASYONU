import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle

dosya = "rfc_model.rfc"
rfc = pickle.load(open(dosya,"rb"))

sinifs = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
          'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
          'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30,
          'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'arkaplan': 36}

index = list(sinifs.values())
siniflar = list(sinifs.keys())

def islem(img):
    yeni_boy = img.reshape((1600,5,5))
    orts = []
    for parca in yeni_boy:
        ort = np.mean(parca)
        orts.append(ort)

    orts = np.array(orts)

    orts = orts.reshape(1600,)
    return orts




def plakaTani(img,plaka):
    x,y,w,h = plaka
    if(w>h):
        plaka_bgr = img[y:y+h,x:x+w].copy()
    else:
        plaka_bgr = img[y:y+w,x:x+h].copy()

    H,W = plaka_bgr.shape[:2]
    H,W = H*2,W*2

    plaka_bgr = cv2.resize(plaka_bgr,(W,H))

    plaka_resim = cv2.cvtColor(plaka_bgr,cv2.COLOR_BGR2GRAY)

    th_img = cv2.adaptiveThreshold(plaka_resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

    kernel = np.ones((3,3),np.uint8)
    th_img = cv2.morphologyEx(th_img,cv2.MORPH_OPEN,kernel,iterations=1)

    cnt = cv2.findContours(th_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0]

    cnt = sorted(cnt,key=cv2.contourArea,reverse=True)[:15]

    yaz = plaka_bgr.copy()
    mevcutPlaka = []

    for i,c in enumerate(cnt):
        rect = cv2.minAreaRect(c)
        (x,y),(w,h),r = rect

        kon1 = max([w,h])<W/4
        kon2 = w*h > 200

        if(kon1 and kon2):
            print("karakter ->",x,y,w,h)

            box = cv2.boxPoints(rect)
            box = np.int64(box)

            minx = np.min(box[:,0])
            miny = np.min(box[:,1])
            maxx = np.max(box[:,0])
            maxy = np.max(box[:,1])

            odak = 2
            minx = max(0,minx-odak)
            miny = max(0,miny-odak)
            maxx = min(W,maxx+odak)
            maxy = min(H,maxy+odak)

            kesim = plaka_bgr[miny:maxy,minx:maxx].copy()

            tani = cv2.cvtColor(kesim,cv2.COLOR_BGR2GRAY)
            tani = cv2.resize(tani,(200,200))
            tani = tani/255

            oznitelikler = islem(tani)
            karakter = rfc.predict([oznitelikler])[0]

            ind = index.index(karakter)

            sinif = siniflar[ind]

            if sinif == "arkaplan":
                continue

            mevcutPlaka.append([sinif,minx])
            
            cv2.putText(yaz,sinif,(minx-2,miny-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.drawContours(yaz,[box],0,(0,255,0),1)
        
    mevcutPlaka.sort(key=lambda x: x[1])
    plaka_dizgesi = ""
    sayac = 0
    for i, (sinif, minx) in enumerate(mevcutPlaka):
        if sinif.isdigit():
            plaka_dizgesi += sinif
            sayac +=1
            if sayac == 2:
                plaka_dizgesi += " "
                sayac = 0
        elif sinif.isalpha():
            plaka_dizgesi += sinif
            sayac += 1
            if sayac==2 and not mevcutPlaka[i+1][0].isalpha():
                plaka_dizgesi += " "
            elif sayac == 3 and not mevcutPlaka[i+1][0].isalpha():
                plaka_dizgesi += " "
                
                
    cv2.putText(yaz, sinif, (minx - 2, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return yaz, plaka_dizgesi



