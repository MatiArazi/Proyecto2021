from PIL import Image

def mosaic(pic, x, y, w, h):
  bw = pic.load()
  for i in range(w): 
    for j in range(h):
        bw[x+i,y+j]=0
        a= 0,0,0
        for n1 in range(-10,10):
            for n2 in range(-10, 10):
                try:
                  a = (a[0]+bw[x+i+n1, y+j+n2][0],a[1]+bw[x+i+n1, y+j+n2][1],a[2]+bw[x+i+n1, y+j+n2][2],)
                except:
                    pass
        bw[x+i,y+j]=int(a[0]/(19*19-1)),int(a[1]/(19*19-1)),int(a[2]/(19*19-1))
  return pic #version alternativa. sirve mas.

img = Image.open('bts.jpg')

img = mosaic(img, 100, 100, 100, 100)
img.load()[100, 100] = img.load()[200, 200]=(255,0,0)

img.show()
