# -*- coding: utf-8 -*-
import os, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from data import PROJECTS, MORE_COMMERCIAL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = json.load(open(os.path.join(ROOT, 'build', 'meta.json')))
SITE = 'https://cozyburo.ru'
TG = 'https://t.me/Lena_Drumlevich'
IG = 'https://www.instagram.com/cozyburo/'

CSS = r"""
:root{--bg:#0f0d0b;--bg2:#15120f;--ink:#f1ece4;--mute:rgba(241,236,228,.56);--line:rgba(241,236,228,.16);--serif:'Cormorant Garamond',Georgia,serif;--sans:'Montserrat',system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-weight:400;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{display:block;max-width:100%}
.wrap{width:min(1360px,100% - clamp(32px,6vw,96px));margin:0 auto}
/* nav */
.nav{position:fixed;inset:0 0 auto 0;z-index:20;display:flex;align-items:center;justify-content:space-between;padding:22px clamp(16px,3vw,48px);transition:background .5s,padding .5s;mix-blend-mode:normal}
.nav.solid{background:rgba(15,13,11,.82);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);padding:14px clamp(16px,3vw,48px)}
.nav .brand{font:500 12px/1 var(--sans);letter-spacing:.42em;text-indent:.42em;text-transform:uppercase}
.nav .brand span{opacity:.6}
.nav ul{display:flex;gap:clamp(18px,3vw,40px);list-style:none}
.nav ul a{font:400 11px/1 var(--sans);letter-spacing:.22em;text-transform:uppercase;opacity:.8;transition:opacity .3s;padding:6px 0;position:relative}
.nav ul a:after{content:'';position:absolute;left:0;right:100%;bottom:0;height:1px;background:var(--ink);transition:right .4s}
.nav ul a:hover{opacity:1}.nav ul a:hover:after{right:0}
@media(max-width:640px){.nav ul{gap:16px}.nav ul a{font-size:10px;letter-spacing:.16em}}
/* hero */
.hero{position:relative;height:100svh;min-height:560px;overflow:hidden;background:#0a0908}
.slide{position:absolute;inset:-4%;background-size:cover;background-position:center;opacity:0;transition:opacity 2.2s ease;will-change:opacity,transform}
.slide.on{opacity:1;animation:drift 26s ease-in-out infinite alternate}
@keyframes drift{from{transform:scale(1) translate(0,0)}to{transform:scale(1.06) translate(-1%,.6%)}}
.veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,9,8,.42) 0%,rgba(10,9,8,.10) 35%,rgba(10,9,8,.14) 65%,rgba(15,13,11,.92) 100%)}
.grain{position:absolute;inset:0;opacity:.09;pointer-events:none;mix-blend-mode:overlay}
.hero .center{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;text-align:center;border:1px solid rgba(241,236,228,.5);background:rgba(14,11,9,.14);backdrop-filter:blur(2.5px);-webkit-backdrop-filter:blur(2.5px);padding:clamp(22px,3vw,36px) clamp(22px,3.4vw,44px);max-width:calc(100% - 40px)}
.hero .center:after{content:'';position:absolute;inset:6px;border:1px solid rgba(241,236,228,.18);pointer-events:none}
.mark{font:400 clamp(28px,4.6vw,56px)/1 var(--sans);letter-spacing:.42em;text-indent:.42em;text-transform:uppercase}
.mark b{font-weight:500}
.mark small{display:block;font-size:.5em;letter-spacing:.9em;text-indent:.9em;opacity:.8;margin-top:.55em}
.line{font:italic 400 clamp(19px,2.2vw,27px)/1.3 var(--serif);margin-top:20px;opacity:.92}
.hero .foot{position:absolute;left:0;right:0;bottom:28px;display:flex;justify-content:space-between;align-items:flex-end;padding:0 clamp(16px,3vw,48px);font:400 10px/1 var(--sans);letter-spacing:.22em;text-transform:uppercase;opacity:.7}
.hero .foot .cap{font-family:var(--serif);font-style:italic;font-size:15px;letter-spacing:0;text-transform:none;opacity:.95;transition:opacity .6s}
.scroll{position:absolute;left:50%;bottom:70px;width:1px;height:48px;background:linear-gradient(var(--ink),transparent);opacity:.6;animation:pulse 2.4s ease-in-out infinite}
@keyframes pulse{0%,100%{transform:scaleY(.4);transform-origin:top;opacity:.2}50%{transform:scaleY(1);opacity:.7}}
.fade{opacity:0;animation:in 1.6s .4s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes in{to{opacity:1}}
/* sections */
section.block{padding:clamp(72px,10vw,140px) 0 0}
.head{display:flex;align-items:baseline;gap:22px;margin-bottom:clamp(28px,4vw,54px);padding-bottom:18px;border-bottom:1px solid var(--line)}
.head .n{font:italic 400 15px/1 var(--serif);opacity:.5}
.head h2{font:300 clamp(28px,3.6vw,46px)/1.1 var(--serif);letter-spacing:.01em}
.head .cnt{margin-left:auto;font:400 10px/1 var(--sans);letter-spacing:.22em;text-transform:uppercase;opacity:.5}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(28px,4vw,56px) clamp(20px,3vw,40px)}
.grid.one{grid-template-columns:1fr}
@media(max-width:720px){.grid{grid-template-columns:1fr}}
.card{display:block}
.card .ph{position:relative;overflow:hidden;aspect-ratio:4/3;background:#1a1613}
.grid.one .card .ph{aspect-ratio:21/9}
@media(max-width:720px){.grid.one .card .ph{aspect-ratio:4/3}}
.card img{width:100%;height:100%;object-fit:cover;transform:scale(1.001);transition:transform 1.4s cubic-bezier(.2,.7,.2,1),opacity .8s;opacity:0}
.card img.ld{opacity:1}
.card:hover img{transform:scale(1.045)}
.card .t{display:flex;justify-content:space-between;align-items:baseline;gap:16px;margin-top:16px}
.card h3{font:400 clamp(22px,2.2vw,28px)/1.15 var(--serif)}
.card h3 i{font-style:italic;opacity:.75}
.card .y{font:400 11px/1 var(--sans);letter-spacing:.2em;opacity:.55}
.card .m{font:400 11px/1.6 var(--sans);letter-spacing:.14em;text-transform:uppercase;opacity:.55;margin-top:6px}
.more{margin-top:clamp(28px,4vw,48px);border-top:1px solid var(--line)}
.more div{display:flex;justify-content:space-between;gap:16px;padding:16px 0;border-bottom:1px solid var(--line);font:400 11px/1.6 var(--sans);letter-spacing:.14em;text-transform:uppercase;opacity:.6}
.more div span:last-child{text-align:right}
/* buro */
.buro{display:grid;grid-template-columns:5fr 6fr;gap:clamp(28px,5vw,80px);align-items:center}
@media(max-width:820px){.buro{grid-template-columns:1fr}}
.buro .ph{aspect-ratio:4/5;overflow:hidden;background:#1a1613}
.buro .ph img{width:100%;height:100%;object-fit:cover}
.buro h2{font:300 clamp(30px,3.6vw,48px)/1.12 var(--serif);margin-bottom:22px}
.buro h2 i{font-style:italic}
.buro p{font:400 clamp(15px,1.25vw,17px)/1.75 var(--sans);font-weight:300;opacity:.86;max-width:52ch}
.buro p+p{margin-top:14px}
.buro .sig{margin-top:30px;font:italic 400 22px/1.2 var(--serif)}
.buro .sig small{display:block;font:400 10px/1.8 var(--sans);letter-spacing:.22em;text-transform:uppercase;opacity:.55;margin-top:6px}
/* contacts / footer */
.contacts{text-align:center;padding:clamp(72px,10vw,140px) 0 clamp(40px,6vw,80px)}
.contacts h2{font:300 clamp(30px,4vw,54px)/1.1 var(--serif)}
.contacts h2 i{font-style:italic}
.contacts p{margin-top:16px;font-weight:300;opacity:.7;max-width:44ch;margin-inline:auto}
.contacts .links{display:flex;justify-content:center;flex-wrap:wrap;gap:14px 36px;margin-top:34px}
.contacts .links a{font:400 11px/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;padding:14px 0;border-bottom:1px solid var(--line);transition:border-color .4s}
.contacts .links a:hover{border-color:var(--ink)}
footer{border-top:1px solid var(--line);padding:24px 0 34px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font:400 10px/1.6 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.45}
/* project page */
.phead{padding:clamp(120px,16vw,190px) 0 clamp(28px,4vw,48px)}
.phead .back{font:400 10px/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.55;transition:opacity .3s}
.phead .back:hover{opacity:1}
.phead h1{font:300 clamp(40px,6.4vw,92px)/1.02 var(--serif);margin-top:26px;letter-spacing:-.005em}
.phead .logo{margin-top:34px;height:clamp(72px,11vw,150px);width:auto;max-width:min(520px,80vw);object-fit:contain;object-position:left}
.phead .logo+h1{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.phead{position:relative}
.phead .sub{font:italic 300 clamp(26px,3.4vw,44px)/1.1 var(--serif);margin-top:18px;opacity:.85}
.phead h1 i{font-style:italic;opacity:.8}
.phead .meta{display:flex;flex-wrap:wrap;gap:8px 28px;margin-top:22px;font:400 11px/1.6 var(--sans);letter-spacing:.18em;text-transform:uppercase;opacity:.6}
.phead .desc{margin-top:30px;max-width:62ch;font-weight:300;font-size:clamp(15px,1.25vw,17px);line-height:1.75;opacity:.86}
.lead{aspect-ratio:16/9;overflow:hidden;background:#1a1613}
.lead img{width:100%;height:100%;object-fit:cover}
.gal{columns:2;column-gap:clamp(16px,2.4vw,32px);margin-top:clamp(16px,2.4vw,32px)}
@media(max-width:720px){.gal{columns:1}}
.gal a{display:block;break-inside:avoid;margin-bottom:clamp(16px,2.4vw,32px);overflow:hidden;background:#1a1613;cursor:zoom-in}
.gal img{width:100%;height:auto;transition:transform 1.4s cubic-bezier(.2,.7,.2,1),opacity .8s;opacity:0}
.gal img.ld{opacity:1}
.gal a:hover img{transform:scale(1.03)}
.pn{display:flex;justify-content:space-between;gap:24px;margin-top:clamp(56px,8vw,110px);padding-top:28px;border-top:1px solid var(--line)}
.pn a{max-width:48%}
.pn a small{display:block;font:400 10px/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.5;margin-bottom:10px}
.pn a span{font:400 clamp(20px,2.4vw,30px)/1.15 var(--serif)}
.pn a.next{text-align:right;margin-left:auto}
/* lightbox */
.lb{position:fixed;inset:0;z-index:50;background:rgba(10,9,8,.96);display:none;align-items:center;justify-content:center}
.lb.on{display:flex}
.lb img{max-width:min(96vw,1800px);max-height:92vh;object-fit:contain;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.lb button{position:absolute;background:none;border:0;color:var(--ink);cursor:pointer;font:300 40px/1 var(--serif);padding:20px;opacity:.6;transition:opacity .3s}
.lb button:hover{opacity:1}
.lb .x{top:10px;right:14px;font-size:30px}.lb .p{left:6px;top:50%;transform:translateY(-50%)}.lb .nx{right:6px;top:50%;transform:translateY(-50%)}
.lb .c{position:absolute;bottom:16px;left:0;right:0;text-align:center;font:400 10px/1 var(--sans);letter-spacing:.24em;opacity:.5}
@media(prefers-reduced-motion:reduce){.slide.on{animation:none}.fade{animation:none;opacity:1}.scroll{animation:none}}
"""

HEAD = """<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#0f0d0b">
<meta property="og:type" content="website"><meta property="og:site_name" content="Cozy Buro"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{og}"><meta property="og:url" content="{url}"><meta property="og:locale" content="ru_RU">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%230f0d0b'/%3E%3Ctext x='32' y='42' font-family='Georgia,serif' font-size='30' fill='%23f1ece4' text-anchor='middle'%3ECB%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,400&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
<style>{css}</style>
{ld}</head><body>"""

NAV = """<nav class="nav{solid}" id="nav"><a class="brand" href="{base}">Cozy <span>Buro</span></a>
<ul><li><a href="{base}#projects">Проекты</a></li><li><a href="{base}#buro">Бюро</a></li><li><a href="{base}#contacts">Контакты</a></li></ul></nav>"""

CONTACTS = """<section class="contacts wrap" id="contacts">
<h2>Поговорим <i>о&nbsp;вашем</i> пространстве</h2>
<p>Рестораны, бары, кафе и&nbsp;частные интерьеры. Напишите в&nbsp;Telegram&nbsp;— ответим в&nbsp;течение дня.</p>
<div class="links"><a href="%s" target="_blank" rel="noopener">Telegram · @Lena_Drumlevich</a><a href="%s" target="_blank" rel="noopener">Instagram · @cozyburo</a></div>
</section>
<footer class="wrap"><span>© Cozy Buro · Елена Друмлевич</span><span>Restaurant &amp; Interior Design · Moscow</span></footer>""" % (TG, IG)

JS_COMMON = r"""
<script>
(function(){
var nav=document.getElementById('nav');var hero=document.querySelector('.hero');
function onS(){var y=scrollY;nav.classList.toggle('solid',hero?y>innerHeight*0.7:y>40);}
addEventListener('scroll',onS,{passive:true});onS();
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var im=e.target;im.src=im.dataset.src;im.onload=function(){im.classList.add('ld')};io.unobserve(im);}})},{rootMargin:'400px'}):null;
document.querySelectorAll('img[data-src]').forEach(function(im){if(io)io.observe(im);else{im.src=im.dataset.src;im.classList.add('ld');}});
})();
</script>"""

def esc(s): return html.escape(s, quote=True)

def title_html(p, tag='h3'):
    if p.get('sub'):
        return '<%s>%s <i>%s</i></%s>' % (tag, esc(p['name']), esc(p['sub']), tag)
    return '<%s>%s</%s>' % (tag, esc(p['name']), tag)

def full_name(p):
    return p['name'] + (' · ' + p['sub'] if p.get('sub') else '')

def card(p):
    meta = ' · '.join(x for x in [p['kind'], p['address']] if x)
    return ('<a class="card" href="p/%s.html"><div class="ph"><img data-src="img/%s/cover-m.jpg" alt="%s" width="960" height="640"></div>'
            '<div class="t">%s<span class="y">%s</span></div><div class="m">%s</div></a>') % (
        p['slug'], p['slug'], esc(full_name(p)), title_html(p), esc(p['year']), esc(meta))

def build_index():
    com = [p for p in PROJECTS if p['section'] == 'commercial']
    prv = [p for p in PROJECTS if p['section'] == 'private']
    hero_photos = ['img/%s/cover' % p['slug'] for p in com] + ['img/bar', 'img/lounge']
    caps = [full_name(p) for p in com] + ['Riesling Boyz', 'Русалочка Азия']
    ld = json.dumps({"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Cozy Buro",
                     "founder": {"@type": "Person", "name": "Елена Друмлевич"}, "url": SITE, "image": SITE + "/img/rusalochka-asia/cover.jpg",
                     "address": {"@type": "PostalAddress", "addressLocality": "Москва", "addressCountry": "RU"},
                     "sameAs": [IG, TG], "description": "Бюро дизайна интерьеров ресторанов, баров и частных пространств"}, ensure_ascii=False)
    h = HEAD.format(title='Cozy Buro — интерьеры с характером', desc='Бюро Елены Друмлевич: интерьеры ресторанов, баров и частных пространств в Москве. Тебураси, Riesling Boyz, Русалочка, Пельменная, Шашлычная.',
                    url=SITE + '/', og=SITE + '/img/rusalochka-asia/cover.jpg', css=CSS, ld='<script type="application/ld+json">%s</script>' % ld)
    h += NAV.format(solid='', base='')
    h += """<header class="hero"><div class="slide" id="s0"></div><div class="slide" id="s1"></div><div class="veil"></div><canvas class="grain" id="g"></canvas>
<div class="center fade"><h1 class="mark"><b>Cozy</b> Buro<small>Interiors</small></h1><p class="line">Интерьеры с характером</p></div>
<div class="scroll"></div>
<div class="foot"><span class="cap" id="cap"></span><span>Moscow · since 2020</span></div></header>
<main>
<section class="block wrap" id="projects"><div class="head"><span class="n">01</span><h2>Коммерческие пространства</h2><span class="cnt">%d объектов</span></div>
<div class="grid">%s</div>
<div class="more">%s</div></section>
<section class="block wrap"><div class="head"><span class="n">02</span><h2>Частные пространства</h2></div>
<div class="grid one">%s</div></section>
<section class="block wrap" id="buro"><div class="buro"><div class="ph"><img data-src="img/buro/elena.jpg" alt="Елена Друмлевич"></div>
<div><h2>Бюро <i>Елены Друмлевич</i></h2>
<p>Cozy Buro делает интерьеры, у&nbsp;которых есть характер: рестораны, бары и&nbsp;кафе, в&nbsp;которые хочется возвращаться, и&nbsp;дома, в&nbsp;которых хочется жить.</p>
<p>Мы ведём проект от&nbsp;идеи до&nbsp;открытия&nbsp;— концепция, планировка, свет, материалы, мебель и&nbsp;авторский надзор. С&nbsp;2020 года открыли десять ресторанов в&nbsp;Москве.</p>
<div class="sig">Елена Друмлевич<small>Основатель и&nbsp;ведущий дизайнер</small></div></div></div></section>
%s</main>
""" % (len(com) + len(MORE_COMMERCIAL), ''.join(card(p) for p in com),
       ''.join('<div><span>%s</span><span>%s · %s</span></div>' % (esc(m['name']), esc(m['address']), esc(m['year'])) for m in MORE_COMMERCIAL),
       ''.join(card(p) for p in prv), CONTACTS)
    h += JS_COMMON + """<script>
(function(){
var photos=%s,caps=%s;
var mobile=Math.min(innerWidth,innerHeight)<700;function url(p){return p+(mobile?'-m':'')+'.jpg';}
var s=[document.getElementById('s0'),document.getElementById('s1')],cap=document.getElementById('cap'),cur=0,i=Math.floor(Math.random()*photos.length),loaded={},cache={};
function load(n,cb){if(loaded[n]!==undefined){cb&&cb();return;}var im=new Image(),src=url(photos[n]);im.onload=function(){loaded[n]=true;cache[n]=src;cb&&cb();};im.onerror=function(){loaded[n]=false;cb&&cb();};im.src=src;}
function paint(n){var nx=(cur+1)%%2;s[nx].style.backgroundImage='url('+cache[n]+')';s[nx].classList.add('on');s[cur].classList.remove('on');cur=nx;i=n;cap.style.opacity=0;setTimeout(function(){cap.textContent=caps[n];cap.style.opacity=1},600);}
function adv(){var n=i,t=0;do{n=(n+1)%%photos.length;t++;}while(loaded[n]!==true&&t<photos.length);if(loaded[n]===true)paint(n);}
load(i,function(){if(loaded[i])paint(i);for(var k=0;k<photos.length;k++)if(k!==i)load(k);setInterval(adv,11000);});
var c=document.getElementById('g'),x=c.getContext('2d');function gr(){c.width=innerWidth/2;c.height=innerHeight/2;var d=x.createImageData(c.width,c.height),b=d.data;for(var k=0;k<b.length;k+=4){var v=Math.random()*255|0;b[k]=b[k+1]=b[k+2]=v;b[k+3]=255;}x.putImageData(d,0,0);}gr();addEventListener('resize',gr);
})();
</script></body></html>""" % (json.dumps(hero_photos), json.dumps(caps, ensure_ascii=False))
    open(os.path.join(ROOT, 'index.html'), 'w').write(h)

def build_project(p, prev, nxt):
    items = META[p['slug']]
    name = full_name(p)
    desc = '%s · %s · %s. Интерьер — Cozy Buro, бюро Елены Друмлевич.' % (p['kind'], p['address'], p['year']) if p['year'] else '%s · Интерьер — Cozy Buro.' % p['kind']
    h = HEAD.format(title='%s — Cozy Buro' % name, desc=desc, url='%s/p/%s.html' % (SITE, p['slug']),
                    og='%s/img/%s/cover.jpg' % (SITE, p['slug']), css=CSS, ld='')
    h += NAV.format(solid=' solid', base='../')
    meta = ''.join('<span>%s</span>' % esc(x) for x in [p['kind'], p['address'], p['year']] if x)
    gal = ''
    for it in items[1:]:
        gal += '<a href="../img/%s/%02d.jpg" data-w="%d" data-h="%d"><img data-src="../img/%s/%02d-s.jpg" width="%d" height="%d" alt="%s"></a>' % (
            p['slug'], it['i'], it['w'], it['h'], p['slug'], it['i'], it['w'], it['h'], esc(name))
    h += """<main class="wrap"><div class="phead"><a class="back" href="../#projects">← Все проекты</a>%s%s<div class="meta">%s</div><!--desc--></div>
<a class="lead" href="../img/%s/00.jpg"><img src="../img/%s/00.jpg" alt="%s"></a>
<div class="gal">%s</div>
<div class="pn">%s%s</div></main>
<div class="lb" id="lb"><button class="x" aria-label="Закрыть">×</button><button class="p" aria-label="Назад">‹</button><button class="nx" aria-label="Вперёд">›</button><img alt=""><div class="c" id="lbc"></div></div>
%s""" % ((('<img class="logo" src="../img/logo/%s.png" alt="%s">' % (p['logo'], esc(name))) + (('<div class="sub">%s</div>' % esc(p['sub'])) if p.get('sub') else '')) if p.get('logo') else '', title_html(p, 'h1'), meta, p['slug'], p['slug'], esc(name), gal,
         '<a href="%s.html"><small>Предыдущий</small><span>%s</span></a>' % (prev['slug'], esc(full_name(prev))) if prev else '',
         '<a class="next" href="%s.html"><small>Следующий</small><span>%s</span></a>' % (nxt['slug'], esc(full_name(nxt))) if nxt else '',
         CONTACTS)
    h += JS_COMMON + r"""<script>
(function(){var ls=[].slice.call(document.querySelectorAll('.lead,.gal a')),lb=document.getElementById('lb'),im=lb.querySelector('img'),c=document.getElementById('lbc'),k=0;
function show(n){k=(n+ls.length)%ls.length;im.src=ls[k].href;c.textContent=(k+1)+' / '+ls.length;lb.classList.add('on');document.body.style.overflow='hidden';}
function hide(){lb.classList.remove('on');document.body.style.overflow='';}
ls.forEach(function(a,n){a.addEventListener('click',function(e){e.preventDefault();show(n);});});
lb.querySelector('.x').onclick=hide;lb.querySelector('.p').onclick=function(){show(k-1)};lb.querySelector('.nx').onclick=function(){show(k+1)};
lb.addEventListener('click',function(e){if(e.target===lb||e.target===im)hide();});
addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;if(e.key==='Escape')hide();if(e.key==='ArrowLeft')show(k-1);if(e.key==='ArrowRight')show(k+1);});
var sx=0;lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});lb.addEventListener('touchend',function(e){var d=e.changedTouches[0].clientX-sx;if(Math.abs(d)>50)show(d<0?k+1:k-1);});
})();
</script></body></html>"""
    os.makedirs(os.path.join(ROOT, 'p'), exist_ok=True)
    open(os.path.join(ROOT, 'p', p['slug'] + '.html'), 'w').write(h)

build_index()
for n, p in enumerate(PROJECTS):
    build_project(p, PROJECTS[n - 1] if n else None, PROJECTS[n + 1] if n + 1 < len(PROJECTS) else None)
# sitemap + robots
urls = [SITE + '/'] + ['%s/p/%s.html' % (SITE, p['slug']) for p in PROJECTS]
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join('<url><loc>%s</loc></url>' % u for u in urls) + '</urlset>')
open(os.path.join(ROOT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % SITE)
print('ok', len(PROJECTS))
