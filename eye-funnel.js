/* Part 03 card only. Existing opt-in URLs and workflows are preserved. */
(function () {
  'use strict';
  // Keep this page's reviewed label without publishing pending shared-nav changes.
  function labelDemo(){
    var link=document.querySelector('.bojin-sticky-bar .bsb-primary');
    if(link && link.href.indexOf('/landing.html')!==-1)link.textContent='Free 1:18 Demo →';
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',labelDemo);else labelDemo();
  var watched=0, shown=false, last=new WeakMap();
  var selector='#compare-player,#dual-circle';
  function reset(e){if(e.target.matches && e.target.matches(selector))last.delete(e.target);}
  ['seeking','pause','ended'].forEach(function(type){document.addEventListener(type,reset,true);});
  document.addEventListener('visibilitychange',function(){last=new WeakMap();});
  document.addEventListener('timeupdate',function(e){
    var video=e.target;
    if(!video.matches || !video.matches(selector))return;
    var now=performance.now(), previous=last.get(video);
    last.set(video,now);
    if(shown || document.hidden || video.paused || video.seeking || video.readyState<2 || previous===undefined)return;
    var seconds=(now-previous)/1000;
    if(seconds>0 && seconds<=1.5)watched+=seconds;
    if(watched<8)return;
    shown=true;
    var card=document.createElement('aside');card.className='eye-intent-toast';
    card.setAttribute('aria-label','Continue with the full demonstration');
    card.innerHTML='<button type="button" class="eye-toast-close" aria-label="Dismiss demonstration suggestion">×</button>'+
      '<p><strong>Want to see the complete movement?</strong></p><div class="eye-toast-actions">'+
      '<a class="btn" href="https://go.bojinfacetension.com/facial-tension-check">Get the free 1:18 demo</a>'+
      '<a class="btn btn--ghost" href="https://go.bojinfacetension.com/bojin-eye-method">Full Course ($79)</a></div>';
    card.querySelector('.eye-toast-close').onclick=function(){card.remove();};
    document.body.appendChild(card);
  },true);
})();
