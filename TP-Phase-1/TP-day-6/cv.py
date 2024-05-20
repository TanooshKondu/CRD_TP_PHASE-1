import cv2
img=cv2.imread('color.jpg')
# print (img)  image pixels

gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
color=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# print(gry)   new greyish pic image pixels

cv2.imwrite('grey.jpg',gry)
cv2.imwrite('color.jpg',color)