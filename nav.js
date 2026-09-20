/* ── Analytics + Meta Pixel, gated to the real domain ──────────────────────
   Meta Pixel (Bojin Funnel Pixel-US 751313064707787) + GA4 (G-2VFEVY9Q1F),
   loaded site-wide here so they survive page rewrites / new articles.
   GUARD: only fire on *.bojinfacetension.com (apex, www, go subdomain). On
   localhost / 127.0.0.1 / file:// / any preview we install harmless no-op
   stubs and bail, so local development never pollutes the pixel or GA4.
   (Fires PageView on every real page. Lead/Purchase get added later.) */
(function(){
  var PROD = /(^|\.)bojinfacetension\.com$/i.test(location.hostname);
  window.dataLayer = window.dataLayer || [];
  if(!PROD){
    /* keep any fbq()/gtag() calls elsewhere from throwing off-production */
    window.fbq = window.fbq || function(){};
    window.gtag = window.gtag || function(){};
    return;
  }

  /* Meta Pixel base code */
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

  /* Google Analytics 4 */
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-2VFEVY9Q1F';
  document.head.appendChild(s);
  window.gtag = function(){ dataLayer.push(arguments); };
  gtag('js', new Date());
  gtag('config', 'G-2VFEVY9Q1F');
})();

/* Fire a Lead conversion once, to Meta Pixel + GA4, after an opt-in form has
   been confirmed by the Systeme.io success redirect. Call bojinLead('<source>')
   only from that confirmed path.
   - Deduped per source per page load (double-clicks won't double-count).
   - content_name / source carries which page produced the lead, so the
     three forms that share one systeme list ID can still be told apart in
     Events Manager / GA4.
   - eventID is sent for future server-side dedup if systeme ever mirrors it.
   - Off-production this is a harmless no-op: fbq/gtag are stubbed above. */
window.bojinLead = function(source){
  try{
    source = source || 'form';
    window.__bojinLeadFired = window.__bojinLeadFired || {};
    if(window.__bojinLeadFired[source]) return;
    window.__bojinLeadFired[source] = true;
    var eid = 'lead-' + source + '-' + Date.now() + '-' + Math.round(Math.random()*1e6);
    if(window.fbq) fbq('track','Lead',{content_name:source},{eventID:eid});
    if(window.gtag) gtag('event','generate_lead',{source:source});
  }catch(e){}
};

/* Keep the native Systeme.io POST, but do not guess that it succeeded from a
   submit event or an iframe load. Lead and the guide redirect are allowed only
   after the hidden iframe reaches our same-origin success page. Cross-origin
   error responses are intentionally ignored because they cannot prove opt-in. */
window.bojinWireOptin = function(form, source){
  if(!form) return;
  var targetName = form.getAttribute('target');
  var frame = targetName ? document.querySelector('iframe[name="' + targetName + '"]') : null;
  if(!frame) return;

  var successPath = '/guide-ready.html';
  var status = form.parentElement && form.parentElement.querySelector('.form-status');
  var button = form.querySelector('button[type="submit"]');
  var pending = false;
  var timer = null;

  function showStatus(message){
    if(!status) return;
    status.textContent = message || '';
    status.hidden = !message;
  }

  function finish(success){
    pending = false;
    if(timer){ window.clearTimeout(timer); timer = null; }
    if(button) button.disabled = false;
    if(success){
      if(window.bojinLead) window.bojinLead(source);
      window.location.href = successPath;
    }else{
      showStatus('We could not confirm your signup. Please try again.');
    }
  }

  frame.addEventListener('load', function(){
    if(!pending) return;
    var href;
    try{
      href = frame.contentWindow.location.href;
    }catch(e){
      /* Still on a cross-origin Systeme.io response: no success proof yet. */
      return;
    }
    try{
      var url = new URL(href, window.location.href);
      if(url.origin === window.location.origin && url.pathname === successPath){
        finish(true);
      }
    }catch(e){}
  });

  form.addEventListener('submit', function(){
    pending = true;
    showStatus('Sending…');
    if(button) button.disabled = true;
    if(timer) window.clearTimeout(timer);
    timer = window.setTimeout(function(){ finish(false); }, 30000);
  });
};

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

/* Legal links (Privacy · Terms) now live in the static footer markup
   (.foot-legal), so no JS injection is needed. */

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
