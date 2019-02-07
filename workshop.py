import cv2
#c = cv2.VideoCapture(0)
#x , y = c.read()
#print(x)
#c.release()
#cv2.imwrite("my.png",y)

#c = cv2.VideoCapture(0)
#x , y = c.read()
#cv2.imshow("hi",y)
#cv2.waitKey()
#cv2.destroyAllWindows()
#c.release()

#c = cv2.VideoCapture(0)
#x , y = c.read()
#y[10] = [0,255,0]
#cv2.imshow("new one",y)
#cv2.waitKey()
#cv2.destroyAllWindows()
#c.release()

#c = cv2.VideoCapture(0)
#x , y = c.read()
#cv2.imshow("cropped",y[50:300 , 100:400])
#cv2.waitKey()
#cv2.destroyAllWindows()
#c.release()

#c = cv2.VideoCapture(0)
#x , y = c.read()

#while True:
#    x,y = c.read()
#    cv2.imshow("hi",y)
#    if cv2.waitKey(1)== 13:
#        break
#cv2.destroyAllWindows()
#c.release()

c = cv2.VideoCapture(0)
x , y = c.read()
face = cv2.CascadeClassifier("/root/Desktop/faceRecog/facelib.xml")
n,m = c.read()
#cv2.imshow("my face",m)
#cv2.waitKey()
#cv2.destroyAllWindows()
faceData = face.detectMultiScale(m)

cv2.imshow("face",m)
cv2.waitKey()
cv2.destroyAllWindows()
print(faceData)

c.release()