"""Render matching SVG and PNG stakeholder charts from the same drawing commands."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
W, H = 1600, 1120
im = Image.new('RGB', (W,H), '#f5f7fb')
d = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">', '<title id="title">XXE incident risk priorities</title><desc id="desc">Five untreated risks: one very high, three high and one moderate. Chart shows estimated likelihood of continued or repeated harm versus business impact. Action priorities and evidence limits are listed alongside.</desc>']
def box(x,y,w,h,c):
    d.rectangle((x,y,x+w,y+h),fill=c)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>')
def text(x,y,s,size=24,c='#172b46',bold=False):
    font=ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),size)
    d.text((x,y),s,font=font,fill=c)
    svg.append(f'<text x="{x}" y="{y+size*0.9}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{c}">{escape(s)}</text>')
box(0,0,W,H,'#f5f7fb')
box(0,0,W,150,'#172b46')
text(48,30,'Where should management act first?',42,'#ffffff',True)
text(48,92,'XXE Infiltration | Estimated untreated risk | Training case study',25,'#dce5f2')
text(48,177,'1 VERY HIGH',27,'#9d2434',True)
text(330,177,'3 HIGH',27,'#864310',True)
text(540,177,'1 MODERATE',27,'#725700',True)
text(1010,177,'ACTION PRIORITIES',27,bold=True)
text(48,237,'Chance of continued or repeated harm',25,bold=True)
colors=['#deeee7','#fff0b5','#ffdbb5','#f5b9c1']
def col(score):return colors[0 if score<=4 else 1 if score<=9 else 2 if score<=16 else 3]
x0,y0,cw,ch=210,295,140,104
labels={ (4,4):['R01 + R02','Files +','secrets'], (3,4):['R03','Database','exposure'], (5,4):['R04','Remote','commands'], (3,3):['R05','Evidence','gap'] }
for l in range(5,0,-1):
    yy=y0+(5-l)*ch
    text(48,yy+25,{5:'Highly likely',4:'Likely',3:'Plausible',2:'Unlikely',1:'Rare'}[l],23,bold=True)
    for impact in range(1,6):
        xx=x0+(impact-1)*cw
        box(xx,yy,cw-3,ch-3,col(l*impact))
        text(xx+10,yy+9,str(l*impact),19,'#485366')
        for j,label in enumerate(labels.get((l,impact),[])):
            text(xx+10,yy+34+j*22,label,20,bold=True)
for i,label in enumerate(['Negligible','Limited','Material','Major','Severe']):text(x0+i*cw+9,833,label,23,bold=True)
text(320,880,'Potential business impact →',26,bold=True)
for j,(label,c) in enumerate(zip(['Low 1–4','Moderate 5–9','High 10–16','Very high 17–25'],colors)):
    xx=48+j*225
    box(xx,937,20,20,c)
    text(xx+29,932,label,21)
cards=[
('R04 • VERY HIGH • 20/25','Unauthorized remote commands',['Confirmed execution as the web-service account.','Contain within 4 hours; validate trusted recovery.'],'#9d2434'),
('R01 + R02 • HIGH • 16/25','File disclosure and exposed secret',['Rotate the secret within 4 hours.','Fix XML handling before return to service.'],'#864310'),
('R03 • HIGH • 12/25','Database reachable by probing source',['Restrict access to approved systems.','Review within 1 day; test before service returns.'],'#864310'),
('R05 • MODERATE • 9/25','Database access outcome unknown',['Review server audit records within 1 day.','Encrypted traffic does not prove login success.'],'#725700')]
for j,(tag,title,lines,c) in enumerate(cards):
    yy=237+j*173
    box(990,yy,562,158,'#ffffff');box(990,yy,7,158,c)
    text(1014,yy+15,tag,21,c,True)
    text(1014,yy+48,title,25,bold=True)
    for k,line in enumerate(lines):text(1014,yy+88+k*28,line,21)
text(1010,948,'Targets are proposed from response authorization.',20)
box(0,992,W,128,'#e8edf5')
text(48,1012,'How to read this: risk score = likelihood × impact. Ratings are analyst estimates, not probabilities.',23)
text(48,1048,'No remediation performed. Remaining risk cannot be rated until fixes are implemented and verified.',23,bold=True)
text(48,1083,'R05 is an evidence gap, not proof of missing logging. Assessment: Ron Richardson | October 5, 2026',20)
svg.append('</svg>')
(HERE/'risk-heat-map.svg').write_text('\n'.join(svg),encoding='utf-8')
im.save(HERE/'risk-heat-map.png')
