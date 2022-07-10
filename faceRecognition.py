import cv2, editsFuncs as ef
face_cascade = cv2.CascadeClassifier('faces.xml')

img_name = 'seleccion.jpeg'
img_src = img_name
img = cv2.imread(img_src)
#graey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img, 1.1, 5) #objetivamente optimo
print(faces)
img_edt = img_src
for (x, y, w, h) in faces:
    img_src = img_name
    img_edt = ef.rectangle(img_src, x,y,w,h,21,0,0)
    cv2.imwrite('result.jpg', img_edt)
cv2.imwrite('result.jpg', img_edt)