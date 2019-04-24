import cv2
import numpy as np
img = cv2.imread('noise.jpg',0)
img = (img/255)    # range between 0 - 1
img = np.pad(img,[(1,),(1,)],mode = 'constant',constant_values = np.nan)
SE = np.ones((3,3))  # structure element

# for y in range(0,len(img)):
#    for x in range(0,len(img[y])):
#        print(img[y][x],end = " ")
#    print(" ")

def dilation(image):
    img = image.copy()
    result = np.zeros((image.shape[0],image.shape[1]))
    for y in range(1,len(img)-1):
        for x in range(1,len(img[y])-1):
            center = img[y][x]
            matrix = np.array([[img[y-1][x-1],img[y-1][x],img[y-1][x+1]],[img[y][x-1],center,img[y][x+1]],[img[y+1][x-1],img[y+1][x],img[y+1][x+1]]])
            if SE.all() == matrix.any():
                result[y][x] = 1
    return result

def erosion(image):
    img = image.copy()
    result = np.zeros((image.shape[0],image.shape[1]))
    for y in range(1,len(img)-1):
        for x in range(1,len(img[y])-1):
            center = img[y][x]
            matrix = np.array([[img[y-1][x-1],img[y-1][x],img[y-1][x+1]],[img[y][x-1],center,img[y][x+1]],[img[y+1][x-1],img[y+1][x],img[y+1][x+1]]])
            if SE.all() == matrix.all():
                result[y][x] = 1
    return result



def closingboundaryExtraction(setA,setB):
    boundary = np.zeros((setB.shape[0],setB.shape[1]))
    for y in range(0,len(setB)):
        for x in range(0,len(setB[y])):
            boundary[y][x] =  setA[y][x] - setB[y][x]       #  Boundary(setA) = setA  - (setA ! setB )
    return boundary

def openingboundaryExtraction(setA,setB):
    boundary = np.zeros((setB.shape[0],setB.shape[1]))
    for y in range(0,len(setB)):
        for x in range(0,len(setB[y])):
            boundary[y][x] =  setB[y][x] - setA[y][x]       #  Boundary(setA) = setA  - (setA ! setB )
    return boundary

################################################
# dilation = dilation(img)
# erosion1 = erosion(dilation)
# erosion2 = erosion(erosion1)
# cv2.imshow("res_noise1",erosion2)
# cv2.waitKey(0)
# boundary1 = closingboundaryExtraction(img,erosion2)
# for y in range(0,len(boundary1)):
#     for x in range(0,len(boundary1[y])):
#         boundary1[y][x] = boundary1[y][x]*255
# cv2.imwrite("res_bound1.jpg",boundary1)
# cv2.imshow("res_bound1",boundary1)
# cv2.waitKey(0)
################################################
erosion = erosion(img)
dilation1 = dilation(erosion)
dilation2 = dilation(dilation1)
# cv2.imshow("res_noise2",dilation2)
# cv2.waitKey(0)
boundary2 = openingboundaryExtraction(img,dilation2)
for y in range(0,len(boundary2)):
    for x in range(0,len(boundary2[y])):
        boundary2[y][x] = boundary2[y][x]*255

cv2.imwrite("res_bound2.jpg",boundary2)
# cv2.imshow("res_bound2",boundary)
cv2.waitKey(0)
