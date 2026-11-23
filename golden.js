/* =====================================================================
   golden.js — The Bojin Method "Golden Standard" interactions (v1)
   Shared by every upgraded SEO x GEO page. No dependencies.
   1) 10-second mirror self-check  -> suggests a tension type
   2) 3-second tension selector    -> dynamic CTA + tracking params
   3) Transcript timestamps        -> seek the demo video
   Tracking: GA4 (gtag) + Meta Pixel (fbq) are loaded by nav.js; both are
   stubbed off-production, so these calls are always safe.
   Links get only ?src=<page>&type=<tension_type> (no utm_* on purpose:
   utm tags on own-site links would restart the GA4 session and erase the
   real traffic source such as Google organic).
   ===================================================================== */
(function () {
  'use strict';

  function track(name, params) {
    try { if (window.gtag) window.gtag('event', name, params); } catch (e) {}
    try { if (window.fbq) window.fbq('trackCustom', name, params); } catch (e) {}
  }

  function withParams(href, src, type) {
    try {
      var u = new URL(href, window.location.href);
      u.searchParams.set('src', src);
      if (type) u.searchParams.set('type', type);
      return u.toString();
    } catch (e) { return href; }
  }

  /* ---------- 3-second selector ---------- */
  function initSelector(box) {
    var src = box.getAttribute('data-src') || 'unknown';
    var msg = box.querySelector('[data-gs-msg]');
    var p = box.querySelector('[data-gs-primary]');
    var s = box.querySelector('[data-gs-secondary]');
    var cta = box.querySelector('.gs-cta');
    var current = null;

    function apply(input, fromUser) {
      current = input.value;
      if (msg) msg.textContent = input.getAttribute('data-msg') || '';
      if (p) { p.href = input.getAttribute('data-primary-href'); p.textContent = input.getAttribute('data-primary-label'); }
      if (s) { s.href = input.getAttribute('data-secondary-href'); s.textContent = input.getAttribute('data-secondary-label'); }
      if (cta) cta.setAttribute('data-type', current);
      if (fromUser) track('tension_type_select', { tension_type: current, source_page: src });
    }

    box.querySelectorAll('input[name="gs-type"]').forEach(function (input) {
      input.addEventListener('change', function () { if (input.checked) apply(input, true); });
      if (input.checked) apply(input, false);
    });

    [p, s].forEach(function (a, i) {
      if (!a) return;
      a.addEventListener('click', function () {
        var type = current || 'none';
        a.href = withParams(a.getAttribute('href'), src, type);
        track('tension_cta_click', {
          tension_type: type,
          source_page: src,
          cta_rank: i === 0 ? 'primary' : 'secondary',
          link_url: a.href
        });
      });
    });

    box.gsSelect = function (type) {
      var input = box.querySelector('input[name="gs-type"][value="' + type + '"]');
      if (input) { input.checked = true; apply(input, true); }
    };
  }

  /* ---------- 10-second mirror self-check ---------- */
  function initMirror(box) {
    var src = box.getAttribute('data-src') || 'unknown';
    var result = box.querySelector('[data-gs-mirror-result]');
    var text = box.querySelector('[data-gs-mirror-text]');
    var go = box.querySelector('[data-gs-mirror-go]');
    var inputs = box.querySelectorAll('input[type="checkbox"]');
    var suggested = null;

    function update(changed) {
      var checked = [];
      inputs.forEach(function (i) { if (i.checked) checked.push(i); });
      if (changed) track('mirror_check', { item: changed.value, checked: changed.checked, checked_count: checked.length, source_page: src });
      if (!result) return;
      if (!checked.length) { result.hidden = true; return; }
      suggested = checked[0].getAttribute('data-type');
      var jaw = checked.some(function (i) { return i.getAttribute('data-type') === 'jaw_asymmetry'; });
      var eye = checked.some(function (i) { return i.getAttribute('data-type') === 'eye_cranial'; });
      if (jaw && !eye) suggested = 'jaw_asymmetry';
      if (eye) suggested = 'eye_cranial';
      if (text) {
        // Pages can override the wording with data-msg-one / data-msg-many ({n} = count).
        var one = box.getAttribute('data-msg-one') || 'You noticed one side-to-side difference. That is common, and it is useful information: it tells you where to start instead of working the whole face.';
        var many = box.getAttribute('data-msg-many') || 'You noticed {n} side-to-side differences. Start with one area only, and compare the two sides again after a few minutes.';
        text.textContent = (checked.length === 1 ? one : many).replace('{n}', checked.length);
      }
      result.hidden = false;
    }

    inputs.forEach(function (i) { i.addEventListener('change', function () { update(i); }); });

    if (go) go.addEventListener('click', function (e) {
      var target = document.getElementById(go.getAttribute('data-target') || 'choose');
      if (target && target.gsSelect && suggested) target.gsSelect(suggested);
      track('mirror_to_selector', { tension_type: suggested || 'none', source_page: src });
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  }

  /* ---------- transcript seek ---------- */
  function initTranscript(btn) {
    btn.addEventListener('click', function () {
      var v = document.getElementById(btn.getAttribute('data-video'));
      if (!v) return;
      v.currentTime = parseFloat(btn.getAttribute('data-seek')) || 0;
      var pr = v.play(); if (pr && pr.catch) pr.catch(function () {});
      track('video_seek', { seconds: v.currentTime, video: v.id });
    });
  }

  function init() {
    document.querySelectorAll('.gs-selector').forEach(initSelector);
    document.querySelectorAll('.gs-mirror').forEach(initMirror);
    document.querySelectorAll('[data-seek]').forEach(initTranscript);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
