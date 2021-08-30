from PIL import Image
"""
Pic: picture a modificar
X,Y: punto de inicio
W,H: width, height
R: 
"""
def mosaic(pic, x, y, w, h,r):
  bw = pic.load()
  for i in range(x, x+w): 
    for j in range(y, y+h):
        a= 0,0,0
        valid = 0
        for n1 in range(-r,r+1):
            for n2 in range(-r,r+1):
                try:
                  a = (a[0]+bw[i+n1, j+n2][0] ,a[1]+bw[i+n1, j+n2][1] ,a[2]+bw[i+n1, j+n2][2])
                  valid+=1
                except:
                    pass
                 
        bw[i,j]=int(a[0]/valid),int(a[1]/valid),int(a[2]/valid)
  return pic 
                                                            
img = Image.open('Test Images/motorway.jpg')
r=int(input())
img = mosaic(img, 100, 100, 100, 100,r)
img.load()[100, 100] = img.load()[200, 200]=(255,0,0)

img.show()
