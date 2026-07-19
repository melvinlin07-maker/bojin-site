/* Meta Pixel — Bojin Funnel Pixel-US (751313064707787).
   Loaded site-wide via nav.js so it survives page rewrites / new articles.
   Fires PageView on every page. (Lead/Purchase get added at their action points later.) */
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '751313064707787');
fbq('track', 'PageView');

/* Google Analytics 4 — property for bojinfacetension.com (G-2VFEVY9Q1F).
   Loaded site-wide via nav.js so it survives page rewrites / new articles. */
(function(){
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-2VFEVY9Q1F';
  document.head.appendChild(s);
})();
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-2VFEVY9Q1F');

/* Shared mobile navigation — hamburger toggle for the top nav.
   Included on every page via <script src="nav.js"></script>.
   Works off the existing .site-header / .nav-links markup. */
(function(){
  var toggle = document.querySelector('[data-nav-toggle]');
  var header = document.querySelector('.site-header');
  if(!toggle || !header) return;

  function close(){ header.classList.remove('nav-open'); toggle.setAttribute('aria-expanded','false'); toggle.setAttribute('aria-label','Open menu'); }
  function open(){ header.classList.add('nav-open'); toggle.setAttribute('aria-expanded','true'); toggle.setAttribute('aria-label','Close menu'); }

  toggle.addEventListener('click', function(e){
    e.stopPropagation();
    if(header.classList.contains('nav-open')) close(); else open();
  });

  /* close after tapping a menu link */
  header.querySelectorAll('.nav-links a').forEach(function(a){ a.addEventListener('click', close); });

  /* close when tapping outside, or on Escape */
  document.addEventListener('click', function(e){ if(header.classList.contains('nav-open') && !header.contains(e.target)) close(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') close(); });
})();

/* Auto-append legal links (Privacy · Terms) to the footer on every page,
   so all pages carry them without editing each file individually. */
(function(){
  var footer = document.querySelector('.site-footer');
  if(!footer || footer.querySelector('.legal-links')) return;
  var bar = document.createElement('div');
  bar.className = 'wrap';
  bar.style.cssText = 'margin-top:.2rem';
  var links = document.createElement('div');
  links.className = 'legal-links foot-note';
  links.style.cssText = 'display:flex;gap:1.4rem;flex-wrap:wrap;border-top:1px solid var(--edge, rgba(120,90,60,.14));padding-top:1rem;margin-top:.6rem;width:100%';
  links.innerHTML = '<a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a>';
  bar.appendChild(links);
  footer.appendChild(bar);
})();

/* On article pages, upgrade the plain author line (.post-bio) into an
   author card with avatar + a link to About — builds trust and E-E-A-T.
   Only runs where .post-bio exists (i.e. blog articles), so other pages skip it. */
(function(){
  var bio = document.querySelector('.post-bio');
  if(!bio || bio.getAttribute('data-authorcard')) return;
  var card = document.createElement('div');
  card.className = 'author-card';
  card.setAttribute('data-authorcard','1');
  card.style.cssText = 'display:flex;gap:1rem;align-items:flex-start;margin-top:1.8rem;padding-top:1.4rem;border-top:1px solid var(--edge, rgba(120,90,60,.16))';
  var img = document.createElement('img');
  img.src = 'assets/yu-ting-lan-bojin-instructor.webp';
  img.alt = 'Yu-Ting Lan, bojin instructor';
  img.loading = 'lazy';
  img.style.cssText = 'width:66px;height:66px;border-radius:50%;object-fit:cover;object-position:50% 18%;flex:none;background:#F1EADB';
  var col = document.createElement('div');
  var p = document.createElement('p');
  p.className = 'foot-note';
  p.style.cssText = 'margin:0;font-size:.92rem;line-height:1.6';
  p.innerHTML = bio.innerHTML;
  var a = document.createElement('a');
  a.href = 'about.html';
  a.innerHTML = 'Read Yu-Ting&rsquo;s story &rarr;';
  a.style.cssText = 'display:inline-block;margin-top:.55rem;font-size:.9rem;font-weight:600';
  col.appendChild(p);
  col.appendChild(a);
  card.appendChild(img);
  card.appendChild(col);
  bio.parentNode.replaceChild(card, bio);
})();

/* On article pages, insert a compact "free guide" opt-in CTA before the
   Keep-reading / related block. Low-friction email capture for the blog
   lead magnet (the 5-zone face-tension PDF). Auto-covers all current and
   future articles; only runs where .post-bio exists (blog articles). */
(function(){
  if(document.querySelector('.guide-cta')) return;
  /* .post-bio is replaced by .author-card above, so anchor on either
     (or the related block). Only article pages have these, so this
     doubles as the "is this an article" guard. */
  var anchor = document.querySelector('.related') || document.querySelector('.author-card') || document.querySelector('.post-bio');
  if(!anchor) return;
  var box = document.createElement('div');
  box.className = 'guide-cta reveal in';
  box.style.cssText = 'display:flex;flex-wrap:wrap;gap:1rem;align-items:center;justify-content:space-between;margin:1.8rem 0;padding:1.1rem 1.3rem;background:var(--paper-2,#FDF8F2);border:1px solid var(--edge, rgba(120,90,60,.16));border-left:3px solid var(--jade);border-radius:14px';
  var txt = document.createElement('div');
  txt.style.cssText = 'flex:1 1 16rem;font-size:.98rem;line-height:1.5;color:var(--ink)';
  txt.innerHTML = '<strong>Not sure where your tension is?</strong> Take the free 2-minute 5-zone face check &mdash; find where your face holds tension, and feel it for yourself.';
  var a = document.createElement('a');
  a.className = 'btn';
  a.href = 'guide.html';
  a.style.cssText = 'flex:none';
  a.innerHTML = 'Get the free guide &rarr;';
  box.appendChild(txt);
  box.appendChild(a);
  anchor.parentNode.insertBefore(box, anchor);
})();
