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
  try { localStorage.setItem('bojin-guide-requested', '1'); } catch(e) {}
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

/* Guide forms use the existing, verified guide-delivery webhook. Confirm the
   service acknowledgement before showing the download page; never infer success
   from a hidden iframe load. The response acknowledges a request, not inbox delivery. */
window.bojinWireOptin = function(form, source){
  if(!form || form.getAttribute('data-optin-wired')) return;
  form.setAttribute('data-optin-wired','1');
  var status = form.parentElement && form.parentElement.querySelector('.form-status');
  var button = form.querySelector('button[type="submit"]');
  var pending = false;
  function showStatus(message){
    if(!status) return;
    status.textContent = message || '';
    status.hidden = !message;
  }
  form.addEventListener('submit', async function(event){
    event.preventDefault();
    if(pending) return;
    var email=form.querySelector('input[type="email"]');
    if(!email || !form.reportValidity()) return;
    pending=true;
    if(button) button.disabled=true;
    form.setAttribute('aria-busy','true');
    showStatus('Sending your request…');
    var controller=new AbortController();
    var timeout=window.setTimeout(function(){ controller.abort(); },20000);
    try{
      var response=await fetch('https://melvinlin07-n8n.zeabur.app/webhook/quiz-optin',{
        method:'POST',
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        body:new URLSearchParams({email:email.value.trim(),source:source || 'guide'}),
        signal:controller.signal
      });
      if(!response.ok || (await response.text()).trim() !== 'OK') throw new Error('Unconfirmed signup');
      if(window.bojinLead) window.bojinLead(source);
      window.location.assign('guide-ready.html');
    }catch(error){
      showStatus('We could not confirm your request. Your email is still here; please try again.');
    }finally{
      window.clearTimeout(timeout); pending=false;
      form.removeAttribute('aria-busy');
      if(button) button.disabled=false;
    }
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

/* Journal pages use class-based theme buttons; preserve the same preference
   as core pages without adding a second listener to their existing controls. */
(function(){
  var buttons=document.querySelectorAll('.theme-toggle:not([data-theme-toggle])');
  if(!buttons.length) return;
  var root=document.documentElement;
  try{var saved=localStorage.getItem('bojin-theme');if(saved==='light'||saved==='dark')root.setAttribute('data-theme',saved);}catch(e){}
  buttons.forEach(function(button){
    button.setAttribute('data-theme-toggle','');
    button.addEventListener('click',function(){
      var next=root.getAttribute('data-theme')==='dark'?'light':'dark';root.setAttribute('data-theme',next);
      try{localStorage.setItem('bojin-theme',next);}catch(e){}
    });
  });
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
  function promptCopy(){ window.prompt('Copy link:', shareData.url); }
  function copyLink(){
    if(navigator.clipboard && navigator.clipboard.writeText){
      return navigator.clipboard.writeText(shareData.url).then(function(){
        window.bojinToast('✓ Link copied to clipboard!');
        if(btnEl){
          var old = btnEl.textContent;
          btnEl.textContent = '✓ Copied!';
          setTimeout(function(){ btnEl.textContent = old; }, 2000);
        }
      }).catch(promptCopy);
    }
    promptCopy();
    return Promise.resolve();
  }
  if(navigator.share){
    try{
      return Promise.resolve(navigator.share(shareData)).catch(function(error){
        if(error && error.name === 'AbortError') return;
        return copyLink();
      });
    }catch(error){
      if(error && error.name === 'AbortError') return Promise.resolve();
      return copyLink();
    }
  }
  return copyLink();
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

/* Gentle reminder: native dialog; no history interception or extra trackers. */
(function () {
  var path = location.pathname.split('/').pop() || 'index.html';
  if (!/^(index|blog|blog-.+|about|method|safety|faq|eye-area-guides|brow-guide)\.html$/.test(path)) return;
  var script = document.currentScript;
  var cssURL = new URL('exit-reminder.css?v=20261023-cover-1', script ? script.src : location.href).href;
  function init() {
    var shown = false, ready = false, engaged = false, lastInput = 0;
    var dialog, previousFocus, previousOverflow, css;
    var untilKey = 'bojin-reminder-until';
    function suppressed() {
      try {
        return !!localStorage.getItem('bojin-guide-requested') ||
          Number(localStorage.getItem(untilKey)) > Date.now() ||
          !!sessionStorage.getItem('bojin-exit-shown');
      } catch (e) { return false; }
    }
    if (suppressed() || typeof HTMLDialogElement === 'undefined') return;
    function busy() {
      var active = document.activeElement;
      return document.hidden || Date.now() - lastInput < 8000 ||
        (active && (active.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(active.tagName))) ||
        !!document.querySelector('dialog[open], [aria-modal="true"][aria-hidden="false"]') ||
        Array.prototype.some.call(document.querySelectorAll('video,audio'), function (v) { return !v.paused && !v.ended; });
    }
    function cooldown() {
      try { localStorage.setItem(untilKey, String(Date.now() + 7 * 86400000)); } catch (e) {}
    }
    function dismiss() { cooldown(); if (dialog.open) dialog.close(); }
    function build() {
      dialog = document.createElement('dialog');
      dialog.id = 'bojinExitReminder';
      dialog.setAttribute('aria-labelledby', 'bojinReminderTitle');
      dialog.setAttribute('aria-describedby', 'bojinReminderDescription');
      dialog.innerHTML = '<button type="button" class="ber-close" aria-label="Close reminder" autofocus>&times;</button>' +
        '<p class="ber-eyebrow">A little something before you go</p>' +
        '<div class="ber-cover" aria-hidden="true"><img src="/assets/guide-5-zone-cover.svg?v=20261023-cover-1" width="640" height="280" alt="" decoding="async"></div>' +
        '<h2 id="bojinReminderTitle">Does your face feel tense\u2014even when you\u2019re trying to relax?</h2>' +
        '<p id="bojinReminderDescription">Start with our free <em>5-Zone Face Tension Self-Check</em> guide to facial tension and gentle Bojin self-care. Learn what to notice, where to begin, and when to pause.</p>' +
        '<a class="ber-primary" href="/guide.html">Send Me the Free Guide <span aria-hidden="true">&rarr;</span></a>' +
        '<p class="ber-note">Enter your email on the next page to receive the PDF.</p>' +
        '<a class="ber-secondary" href="/blog.html">I\u2019ll Explore the Articles First</a>' +
        '<button type="button" class="ber-dismiss">No thanks, I\u2019m just browsing.</button>';
      document.body.appendChild(dialog);
      dialog.querySelector('.ber-close').addEventListener('click', dismiss);
      dialog.querySelector('.ber-dismiss').addEventListener('click', dismiss);
      dialog.addEventListener('cancel', function () { cooldown(); });
      dialog.addEventListener('click', function (event) { if (event.target === dialog) {
        var rect = dialog.getBoundingClientRect();
        if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dismiss();
      }});
      dialog.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', cooldown); });
      dialog.addEventListener('close', function () {
        document.body.style.overflow = previousOverflow;
        if (previousFocus && previousFocus.isConnected) previousFocus.focus({preventScroll:true});
      });
    }
    function show() {
      if (shown || !ready || !engaged || suppressed() || busy()) return;
      if (!css) {
        css = document.createElement('link'); css.rel = 'stylesheet'; css.href = cssURL;
        css.onload = show; document.head.appendChild(css); return;
      }
      if (!css.sheet) return;
      if (!dialog) build();
      shown = true;
      try { sessionStorage.setItem('bojin-exit-shown', '1'); } catch (e) {}
      previousFocus = document.activeElement; previousOverflow = document.body.style.overflow;
      dialog.showModal(); document.body.style.overflow = 'hidden';
      window.removeEventListener('scroll', onScroll);
      document.documentElement.removeEventListener('mouseleave', onLeave);
    }
    function mobile() { return matchMedia('(hover: none), (pointer: coarse), (max-width: 767px)').matches; }
    function onScroll() {
      var max = document.documentElement.scrollHeight - innerHeight;
      if (max > 200 && scrollY / max >= 0.45) engaged = true;
      if (mobile()) show();
    }
    function onLeave(event) { if (!mobile() && event.clientY <= 0) show(); }
    document.addEventListener('input', function () { lastInput = Date.now(); }, {passive:true});
    document.addEventListener('pointerdown', function () { lastInput = Date.now(); }, {passive:true});
    document.addEventListener('keydown', function () { lastInput = Date.now(); });
    document.documentElement.addEventListener('mouseleave', onLeave);
    window.addEventListener('scroll', onScroll, {passive:true});
    // Mobile uses reading engagement, not a claim to detect an actual exit.
    setTimeout(function () { ready = true; onScroll(); }, 25000);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, {once:true});
  else init();
})();
