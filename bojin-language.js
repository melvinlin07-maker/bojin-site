/* Shared language preference for the three public-language V8 previews. */
(() => {
  const key = 'bojin-public-language-v1';
  const pages = [
    'blog.html',
    'eye-area-guides.html',
    'brow-guide.html'
  ];
  let memory = 'en';
  function get() {
    try { return localStorage.getItem(key) === 'zh' ? 'zh' : 'en'; }
    catch (_) { return memory; }
  }
  function remember(lang) {
    memory = lang === 'zh' ? 'zh' : 'en';
    try { localStorage.setItem(key, memory); } catch (_) {}
  }
  function choose(lang) {
    remember(lang);
    const url = new URL(location.href);
    url.searchParams.set('lang', memory);
    history.replaceState(null, '', url);
  }
  function sync(zh) {
    const lang = zh ? 'zh' : 'en';
    document.documentElement.lang = zh ? 'zh-Hant' : 'en';
    const button = document.querySelector('#lang-btn, #v3-lang');
    if (button) {
      button.textContent = zh ? 'English' : '繁體中文';
      button.setAttribute('aria-label', zh ? '切換至英文' : 'Switch to Traditional Chinese');
      button.setAttribute('title', zh ? 'English' : '繁體中文');
      button.setAttribute('lang', zh ? 'en' : 'zh-Hant');
    }
    document.querySelectorAll('a[href]').forEach(a => {
      const url = new URL(a.getAttribute('href'), location.href);
      if (url.origin === location.origin && pages.some(page => decodeURIComponent(url.pathname).endsWith('/' + page))) {
        url.searchParams.set('lang', lang);
        a.href = url.href;
      }
    });
  }
  window.BojinLanguage = {get, remember, choose, sync};
})();
