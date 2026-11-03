import sys
from PIL import Image
B,O=sys.argv[1],sys.argv[2]
import glob,os
for f in glob.glob(B+'/../bprev/banner-*.png'):
    Image.open(f).convert('RGB').save(O+'/'+os.path.basename(f)[:-4]+'.jpg',quality=92)
def crop(src,out,fx=.5,fy=.55,w=524,h=350):
    im=Image.open(f'{B}/img/{src}.jpg').convert('RGB');W,H=im.size;s=max(w/W,h/H)
    im=im.resize((round(W*s),round(H*s)),Image.LANCZOS);x=round((im.width-w)*fx);y=round((im.height-h)*fy)
    im.crop((x,y,x+w,y+h)).save(f'{O}/{out}',quality=92)
crop('lavanda','card-quarto-lavanda.jpg'); crop('margarida','card-quarto-margarida.jpg'); crop('jasmin','card-quarto-jasmin.jpg')
crop('azaleia','card-quarto-azaleia.jpg'); crop('cafe074','card-cafe-mesa.jpg'); crop('cafe355','card-cafe-buffet.jpg',.3,.5)
