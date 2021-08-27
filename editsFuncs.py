import cv2

def blur(imgFile, x, y, w, h, k):
  #read image
  img_src = cv2.imread(imgFile)
  img_edt = img_src[y:y+h, x:x+w]
  # applying a gaussian blur over this new rectangle area
  img_edt = cv2.GaussianBlur(img_edt, (k, k), 0)
  img_src[y:y+img_edt.shape[0], x:x+img_edt.shape[1]] = img_edt
  return img_src

def pixelate(imgFile, x, y, w, h, k):
  #read image
  img_src = cv2.imread(imgFile)
  img_edt = img_src[y:y+h, x:x+w]
  # Resize input to "pixelated" size
  img_edt = cv2.resize(img_edt, (k, k), interpolation=cv2.INTER_LINEAR)
  # Initialize output image
  img_edt = cv2.resize(img_edt, (w, h), interpolation=cv2.INTER_NEAREST)
  img_src[y:y+img_edt.shape[0], x:x+img_edt.shape[1]] = img_edt
  return img_src

def rectangle(imgFile, x, y, w, h, r,g,b):
  #read image
  img_src = cv2.imread(imgFile)
  cv2.rectangle(img_src,(x,y),(x+w,y+h),(r,g,b),-1)
  return img_src

