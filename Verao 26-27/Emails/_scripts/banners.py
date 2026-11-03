# Banners com título no lado direito (texto alinhado à direita) + degradê verde leve
import os,sys,json
from playwright.sync_api import sync_playwright
B=sys.argv[1]; OUT=sys.argv[2]
W,H=1200,700
items=[
 ('banner-v1m','rede42','50% 62%','Vocês já conhecem<br>o caminho'),
 ('banner-v1','deck-serra','50% 55%','Enquanto a cidade ferve,<br>a serra refresca'),
 ('banner-v2','hidro132','95% 60%','Janeiro<br>começa aqui'),
 ('banner-v3','cafe355','20% 45%','Quem vem,<br>conta'),
 ('banner-v4','drone','15% 50%','Qual chalé<br>é o de vocês?'),
 ('banner-v5','quarto162','10% 60%','Março é o<br>segredo da serra'),
 ('banner-v6','deck-serra','30% 90%','O verão está<br>acabando'),
 ('banner-a3','lavanda','15% 55%','Ainda pensando<br>nas datas?'),
]
css=f"""@font-face{{font-family:'Romansa';src:url('fonts/romansa.otf')}}
@font-face{{font-family:'Jost';src:url('fonts/Jost.ttf');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:'Jost'}}
.f{{position:absolute;inset:0;background-size:cover}}
.g{{position:absolute;inset:0;background:linear-gradient(270deg,rgba(54,66,48,.6) 0%,rgba(54,66,48,.42) 32%,rgba(54,66,48,.14) 58%,rgba(54,66,48,0) 75%)}}
.g2{{position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(31,38,27,.32),rgba(31,38,27,0))}}
.logo{{position:absolute;top:44px;left:56px;width:380px}}
.t{{position:absolute;right:64px;top:0;bottom:0;width:740px;display:flex;flex-direction:column;justify-content:center;align-items:flex-end;text-align:right;color:#fff}}
/*selo*/.selo{{border:2px solid #C98939;border-radius:60px;padding:12px 28px;font-size:22px;font-weight:600;letter-spacing:.3em;color:#fff;background:rgba(31,38,27,.18)}}
h1{{font-family:'Romansa';font-weight:normal;font-size:76px;line-height:1.06;margin-top:26px;text-shadow:0 2px 6px rgba(0,0,0,.28),0 4px 26px rgba(0,0,0,.4)}}
.l{{width:80px;height:3px;background:#C98939;margin-top:28px}}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':W,'height':H})
    for name,img,pos,t in items:
        h=f"""<html><head><meta charset=utf-8><style>{css}</style></head><body><div class=f style="background-image:url('img/{img}.jpg');background-position:{pos}"></div><div class=g></div><div class=g2></div>
<img class=logo src="img/logo-claro.png"><div class=t><span class=selo>VERÃO 26/27</span><h1 style="font-size:{66 if t.count("<br>")==1 and len(t)>36 else 76}px">{t}</h1><div class=l></div></div></body></html>"""
        f=os.path.join(B,name+'.html'); open(f,'w').write(h)
        pg.goto('file://'+f); pg.wait_for_timeout(400); pg.screenshot(path=os.path.join(OUT,name+'.png'))
    b.close()
