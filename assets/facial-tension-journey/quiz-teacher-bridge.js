'use strict';
(() => {
  const stage = document.getElementById('stage');
  if (!stage) return;
  const addTeacherBridge = () => {
    const grid = stage.querySelector('.result-grid');
    const next = stage.querySelector('.lesson-next');
    if (!grid || !next || stage.querySelector('.teacher-proof')) return;
    const proof = document.createElement('section');
    proof.className = 'teacher-proof';
    proof.innerHTML = `
      <img src="assets/facial-tension-journey/m1-start-captioned.jpg" alt="Lan Yu-Ting teaching an eye-area Bojin lesson" width="1280" height="720">
      <div>
        <p class="eyebrow">MEET YOUR TEACHER</p>
        <h3>Learn with Lan Yu-Ting.</h3>
        <p>Lan Yu-Ting is the founder of He-He Ya-Chu SPA and an international Bojin teacher. She has taught for more than a decade and has guided more than 1,000 learners, including complete beginners.</p>
        <p>Her teaching is built around clear goals, step-by-step practice, and details you can return to as you learn.</p>
        <p class="teacher-links"><a class="text-button" href="https://bojin-expert.com/" target="_blank" rel="noopener">Read her story on the official site →</a><a class="text-button" href="https://www.youtube.com/@Bojin-Expert" target="_blank" rel="noopener">See her teaching on YouTube →</a></p>
      </div>`;
    grid.after(proof);
    const nextTitle = next.querySelector('h3');
    if (nextTitle) nextTitle.textContent = 'Now put your small win in context.';
    const nextCopy = next.querySelector('.eyebrow')?.parentElement?.querySelector('p:not(.eyebrow)');
    if (nextCopy) nextCopy.textContent = 'The full 2 min 44 sec demonstration shows how this small detail fits into the wider practice, with Lan Yu-Ting explaining what to notice as you watch.';
    const unlock = next.querySelector('#unlock');
    if (unlock) unlock.textContent = 'Continue to the full demonstration →';
  };
  new MutationObserver(addTeacherBridge).observe(stage, {childList:true,subtree:true});
  addTeacherBridge();
})();
