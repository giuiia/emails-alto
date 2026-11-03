# Otimização de peso: banners <= ~85 KB, cards <= ~28 KB, logo 2x (380px) com paleta reduzida
import sys,os,io
from PIL import Image
D=sys.argv[1]
def jpg(f,limit,qmax=82,qmin=60):
    im=Image.open(f).convert('RGB'); best=None
    for q in range(qmax,qmin-1,-2):
        b=io.BytesIO(); im.save(b,'JPEG',quality=q,optimize=True,progressive=True,subsampling='4:2:0')
        best=(q,b.getvalue())
        if len(best[1])<=limit: break
    open(f,'wb').write(best[1]); return best[0],len(best[1])//1024
for n in sorted(os.listdir(D)):
    f=os.path.join(D,n); before=os.path.getsize(f)//1024
    if n.startswith('banner'): q,kb=jpg(f,95*1024)
    elif n.endswith('.jpg'): q,kb=jpg(f,28*1024)
    elif n=='logo-header.png':
        im=Image.open(f).convert('RGBA'); w=380; im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
        im.quantize(colors=128,method=Image.Quantize.FASTOCTREE).save(f,optimize=True); q,kb='png8',os.path.getsize(f)//1024
        print('logo size',im.size)
    print(n,before,'KB ->',kb,'KB',q)
