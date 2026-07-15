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
