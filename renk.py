import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
#hsv uzayı
dusuk = np.array([90,50,50])
yuksek = np.array([130,255,255])

while True:
    ret,goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

    #hsv uzayındaki değerleri alabilmek
    mask = cv2.inRange(hsv,dusuk,yuksek)
    #gerçek rengi ile görmek
    son_resim = cv2.bitwise_and(goruntu,goruntu,mask=mask)

    #yumuşatma
    kernel = np.ones((15,15),dtype=np.float32)/225
    smoothed = cv2.filter2D(son_resim,-1,kernel)

    #blur
    blur = cv2.GaussianBlur(son_resim,(15,15),0)

    #median
    median = cv2.medianBlur(son_resim,15)

    #bilatarel
    

    cv2.imshow("medianBlur",median)
    cv2.imshow("BGR(BLUE,GREEN,RED) uzayı,ana goruntu",goruntu)
    cv2.imshow("blur",blur)
    cv2.imshow("renk algılama",son_resim)
    cv2.imshow("yumusatma",smoothed)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
print(kernel)
kamera.release()
cv2.destroyAllWindows()
