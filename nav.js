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

  function loadTrackers(){
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
  }

  /* The journal is image and content heavy. Keep its first paint clear while
     still recording visitors who interact; all other pages track immediately. */
  if(location.pathname === '/blog.html'){
    var started = false;
    function start(){
      if(started) return;
      started = true;
      loadTrackers();
    }
    document.addEventListener('pointerdown', start, {once:true, passive:true});
    document.addEventListener('keydown', start, {once:true});
    window.addEventListener('scroll', start, {once:true, passive:true});
    function queueStart(){ window.setTimeout(start, 4000); }
    if(document.readyState === 'complete') queueStart();
    else window.addEventListener('load', queueStart, {once:true});
  } else {
    loadTrackers();
  }
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

/* V8 Journal: preserve blog.html as the article archive, route Journal navigation to the dual entrance. */
(function(){document.querySelectorAll('.site-header .nav-links a').forEach(function(a){if(a.textContent.trim().toLowerCase()==='journal')a.setAttribute('href','blog.html');});})();


/* ── UX Tool 1 & Toast: Web Share API helper ────────────────────────────── */
window.bojinToast = function(msg){
  var t = document.getElementById('bojinToast');
  if(!t){
    t = document.createElement('div');
    t.id = 'bojinToast';
    t.className = 'bojin-toast';
    document.body.appendChild(t);
  }
  t.textContent = msg || 'Link copied to clipboard!';
  t.classList.add('is-shown');
  clearTimeout(t._timer);
  t._timer = setTimeout(function(){ t.classList.remove('is-shown'); }, 2600);
};

window.bojinShare = function(opts, btnEl){
  opts = opts || {};
  var shareData = {
    title: opts.title || document.title,
    text: opts.text || (document.querySelector('meta[name="description"]') ? document.querySelector('meta[name="description"]').getAttribute('content') : ''),
    url: opts.url || window.location.href
  };
  if(navigator.share){
    navigator.share(shareData).catch(function(){});
  } else if(navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(shareData.url).then(function(){
      window.bojinToast('✓ Link copied to clipboard!');
      if(btnEl){
        var old = btnEl.textContent;
        btnEl.textContent = '✓ Copied!';
        setTimeout(function(){ btnEl.textContent = old; }, 2000);
      }
    }).catch(function(){
      window.prompt('Copy link:', shareData.url);
    });
  } else {
    window.prompt('Copy link:', shareData.url);
  }
};

/* ── UX Tool 2: Golden Reading Progress Bar ─────────────────────────────── */
(function(){
  var bar = document.getElementById('readingProgress');
  if(!bar){
    bar = document.createElement('div');
    bar.id = 'readingProgress';
    bar.className = 'reading-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
  }
  var ticking = false;
  function updateProgress(){
    var scrollH = document.documentElement.scrollHeight - window.innerHeight;
    if(scrollH > 100){
      var pct = Math.min(100, Math.max(0, (window.scrollY / scrollH) * 100));
      bar.style.width = pct + '%';
    } else {
      bar.style.width = '0%';
    }
    ticking = false;
  }
  window.addEventListener('scroll', function(){
    if(!ticking){
      window.requestAnimationFrame(updateProgress);
      ticking = true;
    }
  }, {passive:true});
})();

/* ── UX Tool 3: Gentle Exit-Intent Modal ────────────────────────────────── */
(function(){
  if(location.pathname.indexOf('quiz') !== -1) return;

  function initExitIntent(){
    var shown = false;
    try { shown = !!sessionStorage.getItem('bojin-exit-shown'); } catch(e){}
    if(shown) return;

    var modal = document.createElement('div');
    modal.id = 'exitModal';
    modal.className = 'exit-modal';
    modal.setAttribute('aria-hidden', 'true');
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.innerHTML =
      '<div class="exit-modal__backdrop" id="exitModalBackdrop"></div>' +
      '<div class="exit-modal__card">' +
        '<button class="exit-modal__close" id="exitModalClose" aria-label="Close dialog">&times;</button>' +
        '<p class="exit-modal__eyebrow">Before you go</p>' +
        '<h3 class="exit-modal__title">Save the 5-Zone Face Tension Guide</h3>' +
        '<p class="exit-modal__desc">A concise, illustrated PDF reference covering brows, eyes, cheeks, jawline, and neck &mdash; plus comfortable pressure boundaries to practice safely at home.</p>' +
        '<div class="exit-modal__actions">' +
          '<a class="btn btn--lg" href="guide.html">Get the Free 5-Zone Guide &rarr;</a>' +
          '<button class="exit-modal__dismiss" id="exitModalDismiss">Maybe later</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(modal);

    function show(){
      if(shown) return;
      shown = true;
      try { sessionStorage.setItem('bojin-exit-shown', '1'); } catch(e){}
      modal.classList.add('is-visible');
      modal.setAttribute('aria-hidden', 'false');
    }

    function hide(){
      modal.classList.remove('is-visible');
      modal.setAttribute('aria-hidden', 'true');
    }

    document.getElementById('exitModalClose').addEventListener('click', hide);
    document.getElementById('exitModalBackdrop').addEventListener('click', hide);
    document.getElementById('exitModalDismiss').addEventListener('click', hide);
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') hide(); });

    // Desktop exit-intent: mouse leaves through top
    document.documentElement.addEventListener('mouseleave', function(e){
      if(e.clientY <= 0 && window.scrollY > 200){
        show();
      }
    });

    // Mobile intent: user stays > 25s, scrolled down > 300px, then rapidly scrolls up
    var lastY = window.scrollY;
    var stayTime = 0;
    var timer = setInterval(function(){ stayTime += 1; }, 1000);
    window.addEventListener('scroll', function(){
      var curY = window.scrollY;
      var diff = lastY - curY;
      if(stayTime >= 25 && curY > 300 && diff > 150){
        show();
      }
      lastY = curY;
    }, {passive:true});
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', initExitIntent);
  } else {
    initExitIntent();
  }
})();
