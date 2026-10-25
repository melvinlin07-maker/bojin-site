/* Shared language preference for the public-language V8 previews. */
(() => {
  const key = 'bojin-public-language-v2';
  const pages = [
    'blog.html',
    'eye-area-guides.html',
    'brow-guide.html'
  ];
  let memory = 'en';
  function get() {
    try {
      const v = localStorage.getItem(key);
      if (v === 'es') return 'es';
      if (v === 'en') return 'en';
      return 'en';
    }
    catch (_) { return memory; }
  }
  function remember(lang) {
    memory = lang === 'es' ? 'es' : 'en';
    try { localStorage.setItem(key, memory); } catch (_) {}
  }
  function choose(lang) {
    remember(lang);
    const url = new URL(location.href);
    url.searchParams.set('lang', memory);
    history.replaceState(null, '', url);
  }
  function sync(es) {
    const lang = es ? 'es' : 'en';
    document.documentElement.lang = es ? 'es' : 'en';
    const button = document.querySelector('#lang-btn, #v3-lang');
    if (button) {
      button.textContent = es ? '🌐 English' : '🌐 Español';
      button.setAttribute('aria-label', es ? 'Switch to English' : 'Cambiar a Español');
      button.setAttribute('title', es ? 'English' : 'Español');
      button.setAttribute('lang', es ? 'en' : 'es');
    }
    document.querySelectorAll('a[href]').forEach(a => {
      try {
        const url = new URL(a.getAttribute('href'), location.href);
        if (url.origin === location.origin && pages.some(page => decodeURIComponent(url.pathname).endsWith('/' + page))) {
          url.searchParams.set('lang', lang);
          a.href = url.href;
        }
      } catch (_) {}
    });
  }
  window.BojinLanguage = {get, remember, choose, sync};
})();
