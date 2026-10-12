import cairosvg, sys
BG="#0D1220"
def content(sw=26):
    s=f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    return f'''
  <path d="M 96 194 L 56 256 L 96 318" stroke="url(#gl)" {s}/>
  <path d="M 416 194 L 456 256 L 416 318" stroke="url(#gr)" {s}/>
  <g stroke="#FFFFFF" {s}>
    <path d="M 140 205 H 206 M 173 205 V 307"/>
    <path d="M 229 186 H 255 L 241 204 C 257 202 265 211 263 223 C 261 236 243 241 228 233" stroke-width="{sw*0.6:.1f}"/>
    <path d="M 280 307 L 308 205 L 336 307 M 290 272 H 326"/>
    <path d="M 372 205 V 307"/>
  </g>'''
def svg(rounded=True, scale=1.0, bg=True):
    defs='''<defs>
  <linearGradient id="gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4DA8FF"/><stop offset="1" stop-color="#2F8CF0"/></linearGradient>
  <linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22D3EE"/><stop offset="1" stop-color="#2DD4BF"/></linearGradient>
</defs>'''
    rect = f'<rect width="512" height="512" rx="{112 if rounded else 0}" fill="{BG}"/>' if bg else ''
    t=(512-512*scale)/2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
{defs}
{rect}
<g transform="translate({t} {t}) scale({scale})">{content()}</g>
</svg>'''
open('icon-rounded.svg','w').write(svg(True))
open('icon-square.svg','w').write(svg(False))
open('icon-maskable.svg','w').write(svg(False,0.78))
cairosvg.svg2png(bytestring=svg(True).encode(),write_to='preview.png',output_width=512,output_height=512)
cairosvg.svg2png(bytestring=svg(True).encode(),write_to='preview32.png',output_width=32,output_height=32)

import os, io
from PIL import Image
out='out'; os.makedirs(out,exist_ok=True)
def png(svgtxt, size, name):
    cairosvg.svg2png(bytestring=svgtxt.encode(), write_to=f'{out}/{name}', output_width=size, output_height=size)
R=svg(True); SQ=svg(False); MASK=svg(False,0.78); SMALL=svg(True,1.18)
png(R,512,'favicon.png'); png(SMALL,96,'favicon-96x96.png')
png(SQ,180,'apple-touch-icon.png')
png(MASK,192,'web-app-manifest-192x192.png'); png(MASK,512,'web-app-manifest-512x512.png')
png(MASK,500,'logo.png'); png(R,500,'splash.png'); png(R,500,'splash-dark.png')
open(f'{out}/favicon.svg','w').write(R)
buf=io.BytesIO(); cairosvg.svg2png(bytestring=SMALL.encode(),write_to=buf,output_width=256,output_height=256)
Image.open(io.BytesIO(buf.getvalue())).save(f'{out}/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
png(SMALL,32,'_small32.png')
