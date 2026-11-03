import sys
from PIL import Image
F,O=sys.argv[1],sys.argv[2]
def crop(src,w,h,fx=.5,fy=.5,out=None,q=78):
    im=Image.open(f'{F}/{src}.jpg').convert('RGB'); W,H=im.size
    s=max(w/W,h/H); assert s<=1.0001,(src,s)
    nw,nh=round(W*s),round(H*s); im=im.resize((nw,nh),Image.LANCZOS)
    x=round((nw-w)*fx); y=round((nh-h)*fy); im=im.crop((x,y,x+w,y+h))
    im.save(f'{O}/{out}',quality=q,optimize=True,progressive=True); print(out,im.size)
B=(1200,560)
crop('rede42',*B,.5,.62,'banner-v1m.jpg')
crop('deck-serra',*B,.5,.55,'banner-v1.jpg')
crop('hidro132',*B,.55,.62,'banner-v2.jpg')
crop('cafe355',*B,.5,.45,'banner-v3.jpg')
crop('drone',*B,.42,.5,'banner-v4.jpg')
crop('quarto162',*B,.4,.6,'banner-v5.jpg')
crop('deck-serra',*B,.5,.85,'banner-v6.jpg')
crop('lavanda',*B,.5,.55,'banner-a3.jpg')
C=(524,350)
crop('hidro132',*C,.55,.6,'card-hidro.jpg',80); crop('quarto162',*C,.35,.6,'card-lareira.jpg',80); crop('cafe-ar-livre',*C,.5,.5,'card-cafe.jpg',80)
for k in ['margarida','azaleia','geranio','jasmin','lavanda','orquidea']: crop(k,*C,.5,.55,f'chale-{k}.jpg',80)
