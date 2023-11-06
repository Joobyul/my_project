import cv2
import os, glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from rembg import remove

DEBUG=False

def makeImg(path, width, height):
    import cv2
    from rembg import remove

    # [1] 파일불러오기
    filename=path+'*'
    fileList=glob.glob(filename)

    # [2] 이미지 row data추출해서 파일로 생성
    # 배경제거 후 사이즈 조절
    dsize_=(width,height)

    # 빈 리스트(array담을거임)
    images=[]
    for file in fileList:
        try:
            org=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            img=cv2.resize(org, dsize_)
            output=remove(img)
            if DEBUG : 
                plt.imshow(output)
                plt.show()
            # np.array배열로 변환
            images.append(output)
        except: print('error')
        
    # np array로 반환한 이미지리스트를 npz파일로 
    # 저장할 경로
    file_path=path+f'{path.split("/")[-2]}.npz'
    np.savez(file_path, data1=np.array(images))
    print(f'{path}완료')

# 함수적용하기
# <남>
path1='./PROJECT/img/kwangsoo/'
makeImg(path1, 340, 160)
path2='./PROJECT/img/sangchul/'
makeImg(path2, 340, 160)
path3='./PROJECT/img/youngho/'
makeImg(path3, 340, 160)
path4='./PROJECT/img/youngchul/'
makeImg(path4, 340, 160)
path5='./PROJECT/img/youngsik/'
makeImg(path5, 340, 160)
path6='./PROJECT/img/youngsoo/'
makeImg(path6, 340, 160)
# <여>
path7='./PROJECT/img/hyunsook/'
makeImg(path7, 340, 160)
path8='./PROJECT/img/jungsook/'
makeImg(path8, 340, 160)
path9='./PROJECT/img/ouksoon/'
makeImg(path9, 340, 160)
path10='./PROJECT/img/soonja/'
makeImg(path10, 340, 160)
path11='./PROJECT/img/youngja/'
makeImg(path11, 340, 160)
path12='./PROJECT/img/youngsook/'
makeImg(path12, 340, 160)


def userImg(width, height):
    import cv2
    from rembg import remove

    # [1] 파일불러오기 - 경로지정
    filename='./PROJECT/img/userImg.jpg'

    # [2] 이미지 배경제거 후 사이즈 조절
    dsize_=(width,height)
    org=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(org, dsize_)
    output=remove(img)

    return output