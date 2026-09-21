'use strict';
(() => {
  const root = 'assets/facial-tension-journey/';
  const stage = document.getElementById('stage');
  const experience = document.getElementById('experience');
  const welcome = document.getElementById('welcome');
  const back = document.getElementById('back');
  const answers = [null, null, null, null];
  let current = 0;
  const pictures = [
    '<rect x="32" y="12" width="57" height="68" rx="28"/><path d="M60 80v13M43 94h35M47 39q13-12 26 0M50 53q10 7 20 0M48 24l-7 9M74 21l-6 7"/>',
    '<path d="M20 26h61a10 10 0 0 1 10 10v24a10 10 0 0 1-10 10H48L31 85V70H20a10 10 0 0 1-10-10V36a10 10 0 0 1 10-10Z"/><path d="M38 41q1-11 12-9 14 4 0 15v7M50 60v1M83 80h12l12 9V75"/>',
    '<rect x="18" y="30" width="86" height="55" rx="8"/><path d="M37 30l7-11h29l8 11M28 41h12"/><circle cx="65" cy="57" r="18"/><circle cx="65" cy="57" r="11"/><path d="M91 13v11M86 18h11"/>'
  ];
  const questions = [
    {label:'A MOMENT THAT FEELS FAMILIAR', title:'When do you notice it most?', hint:'Choose the moment that sounds most like you.', options:[
      {title:'In the mirror', desc:'My eyes don’t reflect how I feel inside.', response:'That gap between how you feel and what you see can be frustrating.'},
      {title:'When someone asks', desc:'“Are you tired?” Even when I feel fine.', response:'It can feel strange when someone reads your expression differently from how you feel.'},
      {title:'In a photo', desc:'I look more tired than I remember feeling.', response:'A single photo doesn’t capture all the energy you brought to that moment.'}
    ]},
    {label:'YOUR EXPERIENCE SO FAR', title:'What have you tried for your eye area?', hint:'There’s no right answer. This helps us choose how much context to give you.', options:[
      {title:'Mostly skincare', desc:'Creams or serums. Hands-on care is new to me.', response:'We’ll introduce the method without assuming you know the tools or terms.'},
      {title:'A few demonstrations', desc:'I’ve watched massage or facial-care videos.', response:'We’ll focus on the teaching details you can look for in a demonstration.'},
      {title:'Hands-on practice', desc:'I’ve tried a facial tool or a self-care routine.', response:'We’ll give you a detail to notice, without assuming every method works the same way.'}
    ]},
    {label:'WHAT WOULD HELP YOU MOST?', title:'Let’s make your first step useful.', hint:'Pick what you’d like help with today.', options:[
      {title:'Help me understand', desc:'Show me what this method involves.', response:'Your short lesson will introduce the practice and its tool.'},
      {title:'Help me feel less unsure', desc:'I’m curious, but I don’t know what to pay attention to.', response:'We’ll start by spotting the hand that isn’t holding the tool.'},
      {title:'Break it down for me', desc:'Give me one small thing to focus on.', response:'Your short lesson will focus on the position of the guiding hand.'}
    ]},
    {label:'YOUR PACE, YOUR CHOICE', title:'How would you like to begin?', hint:'Either way, your result and short lesson are free.', options:[
      {title:'Let me watch first', desc:'Give me one thing to look for in the clip.', response:'We’ll pair your clip with a simple observation prompt.'},
      {title:'Give me a small activity', desc:'Help me check what I’ve just learned.', response:'We’ll pair your clip with a small learning activity. No tool needed.'}
    ]}
  ];
  const routes = [
    {name:'Recognize the method',title:'First, see what this practice involves.',video:'m1-start-captioned',caption:'Meet the method',watch:'Watch the introduction. Notice that this is a tool-assisted eye-area routine.',activity:'Watch the introduction, then pick the description that matches what you saw.',button:'Check what I noticed',takeaway:'You can now recognize this as a tool-assisted eye-area self-care routine. That is your first piece of understanding before learning its movements.',goal:'Recognize what the method involves.',why:'you want to understand the method first',next:'Now see how the tool and guiding hand work together in a longer demonstration.',check:'What kind of practice does Lan Yu-Ting introduce?',choices:['A tool-assisted eye-area routine','A routine for applying eye cream'],correct:0,retry:'Look again at the tool in the introduction. This lesson introduces a hands-on routine.'},
    {name:'Spot the guiding hand',title:'First, know where to look.',video:'guiding-hand-teaser-hd',caption:'Spot the hand without the tool',watch:'Find the hand without the tool. Look at the shape made by its fingers.',activity:'Watch the hand without the tool, then choose the shape you notice. You can leave your own hands relaxed.',button:'Check what I noticed',takeaway:'You identified the vertical V made by the guiding hand. You now have a specific detail to look for instead of trying to follow everything at once.',goal:'Identify one visible detail in the demonstration.',why:'you want to feel less unsure about what to look for',next:'See where that hand position fits into the longer demonstration, at your own pace.',check:'Which shape does the guiding hand make in this clip?',choices:['A closed fist','A vertical V'],correct:1,retry:'Look at the two separated fingers in the poster or replay the clip. They form a vertical V.'},
    {name:'Rehearse the hand shape',title:'First, try one small preparation.',video:'guiding-hand-teaser-hd',caption:'The guiding hand, up close',watch:'Notice the vertical V made by the guiding hand. You can learn the shape just by watching.',activity:'After watching, hold your hand comfortably in front of you, away from your face. Make a V with two fingers, then relax your hand. No tool or eye-area pressure needed.',button:'I’ve tried the hand shape',takeaway:'You’ve rehearsed one hand shape away from your face. The full demonstration adds its placement and movement; the shape alone is not the complete technique.',goal:'Rehearse a hand shape away from your face.',why:'you want the teaching broken into one small step',next:'Next, watch how the hand shape connects with placement and movement in the longer demonstration.'}
  ];
  const background = ['you mainly use skincare products', 'you’ve watched a few demonstrations', 'you’ve tried hands-on care'];
  const experienceCopy = [
    'Because hands-on care is new to you: Bojin here means a tool-assisted self-care practice. This short clip is a first look, not a complete routine.',
    'Because you’ve watched demonstrations before: use this clip to notice how the teacher explains a detail, not just where the tool moves.',
    'Because you’ve tried hands-on care: treat this as an introduction to this particular method. Familiarity with another tool does not replace its instructions.'
  ];
  const feelings = ['You told us your reflection doesn’t always match how you feel.', 'You told us people sometimes read your expression as tired, even when you feel fine.', 'You told us photos sometimes look more tired than the moment felt.'];
  function pauseMedia(){stage.querySelectorAll('video').forEach(v=>v.pause());}
  function focusStage(){const h=stage.querySelector('h2');if(h){h.tabIndex=-1;h.focus({preventScroll:true});}experience.scrollIntoView({behavior:'instant',block:'start'});}
  function progress(label, count){document.getElementById('step-label').textContent=label;document.getElementById('progress-fill').style.width=`${count*25}%`;document.querySelector('.progress').setAttribute('aria-valuenow',count);}
  function renderQuestion(index){
    pauseMedia();current=index;const q=questions[index];progress(`Question ${index+1} of 4`,index);back.textContent='← Back';
    stage.innerHTML=`<section class="question"><div class="question-head"><p class="eyebrow">${q.label}</p><h2 id="question-title">${q.title}</h2><p>${q.hint}</p></div><fieldset class="choices ${q.options.length===2?'two':''}" aria-labelledby="question-title"><legend class="sr-only">Choose one answer</legend>${q.options.map((o,i)=>`<label class="choice"><input type="radio" name="answer" value="${i}" ${answers[index]===i?'checked':''}><span class="sr-only">${o.title}</span>${index===0?`<span class="choice-art" aria-hidden="true"><svg viewBox="0 0 120 110">${pictures[i]}</svg></span>`:''}<span class="choice-content"><span class="small-symbol" aria-hidden="true">${['01','02','03'][i]}</span><span class="choice-title" aria-hidden="true">${o.title}</span><span class="choice-desc">${o.desc}</span></span></label>`).join('')}</fieldset><p class="answer-feedback" aria-live="polite">${answers[index]===null?'':q.options[answers[index]].response}</p><div class="question-actions"><p>${index===3?'Your short lesson is next.':'Choose one. You can change it.'}</p><button class="primary" id="next" ${answers[index]===null?'disabled':''}>${index===3?'See my starting point':'Continue'} <span aria-hidden="true">→</span></button></div></section>`;
    stage.querySelectorAll('input[name=answer]').forEach(input=>input.addEventListener('change',()=>{answers[index]=Number(input.value);stage.querySelector('.answer-feedback').textContent=q.options[answers[index]].response;document.getElementById('next').disabled=false;}));
    document.getElementById('next').addEventListener('click',()=>{if(answers[index]===null)return;if(index===1)renderInsight();else if(index===3)renderResult();else renderQuestion(index+1);});focusStage();
  }
  function renderInsight(){pauseMedia();current='insight';progress('A small discovery · 2 of 4 answered',2);stage.innerHTML=`<section class="insight"><div><p class="eyebrow">A LITTLE SOMETHING TO TAKE WITH YOU</p><h2>The other hand<br><em>has a job, too.</em></h2><p class="lead">It’s easy to follow the tool and miss what the other hand is doing.</p><p>${answers[1]===0?'In this Bojin demonstration, one hand holds the tool while the other is deliberately positioned. There is more to watch than the tool alone.':answers[1]===1?'The next time you watch a demonstration, follow the hand without the tool first. It gives you another detail to look for.':'A tool may look familiar while the supporting-hand position differs. Notice how this teacher positions both hands before assuming the movement is the same.'}</p><button class="primary" id="insight-next">Continue to question 3 <span aria-hidden="true">→</span></button><p class="fine">Two questions left. Then your short lesson.</p></div><div class="insight-picture"><img src="${root}guiding-hand-teaser-hd.jpg" alt="The lesson shows a vertical V made by the guiding hand" width="1920" height="1080"><div class="annotation"><strong>Your first observation</strong>Find the V-shaped fingers in the teaching image. That is the detail to notice—not a cue to apply pressure.</div></div></section>`;document.getElementById('insight-next').addEventListener('click',()=>renderQuestion(2));focusStage();}
  function renderResult(){
    if(answers.some(a=>a===null)){renderQuestion(answers.indexOf(null));return;}pauseMedia();current='result';progress('Your starting point · 4 of 4 answered',4);back.textContent='← Change my last answer';const r=routes[answers[2]], active=answers[3]===1;
    stage.innerHTML=`<section class="result"><div class="result-heading"><span class="result-tag">YOUR FIRST SMALL STEP</span><h2>${r.title}</h2><p>${feelings[answers[0]]}</p><div class="recommendation"><strong>Why we picked this for you</strong><p>You told us ${background[answers[1]]}, and ${r.why}. So we’ll start here: ${active?r.goal:r.watch} ${active?'You chose a small activity, so there’s something to try below.':'You chose to watch first, so there’s no need to follow along.'}</p></div></div><div class="result-grid"><div><div class="video-box"><video id="lesson-video" controls playsinline preload="none" poster="${root+r.video}.jpg" aria-label="${r.caption}"><source src="${root+r.video}.mp4" type="video/mp4"></video><div class="video-caption"><strong>${r.caption}</strong><p>Real course excerpt · English audio &amp; on-screen subtitles</p></div><div class="watch-tools"><span>Press play for sound.</span><button class="text-button" id="replay">Replay clip ↺</button></div><p id="video-error" class="fine" hidden>Video could not load. <a href="${root+r.video}.mp4">Open the clip directly</a>.</p></div><p class="fine">${experienceCopy[answers[1]]}</p></div><aside class="task-card"><p class="eyebrow">${active?'YOUR SMALL ACTIVITY':'ONE THING TO LOOK FOR'}</p><h3>${r.name}</h3><p class="learning-goal">Your small win: ${active?r.goal:(answers[2]===2?'Recognize the V-shaped guiding hand.':r.goal)}</p><p>${active?r.activity:r.watch}</p><button class="primary" id="takeaway">${active?r.button:'Show me the takeaway'} <span aria-hidden="true">↓</span></button><div id="micro-check" hidden></div><div class="learning-note" id="learning-note" hidden role="status" tabindex="-1" aria-live="polite"><p>${active?r.takeaway:(answers[2]===2?'The guiding hand makes a vertical V in this excerpt. You now have a specific detail to watch for when you see the full demonstration.':r.takeaway)}</p></div></aside></div><section class="lesson-next"><div><p class="eyebrow">WHEN YOU’RE READY FOR A LITTLE MORE</p><h3>Ready to connect the next piece?</h3><p>${r.next} The free demonstration is 2 min 44 sec.</p></div><div><button class="primary" id="unlock">Unlock the full free demonstration <span aria-hidden="true">→</span></button><p class="fine">Your result above is already yours. No signup needed to replay it.</p><form id="email-panel" hidden><label class="email-label" for="quiz-email">Email address</label><input id="quiz-email" type="email" autocomplete="email" placeholder="you@example.com" required aria-describedby="email-note"><p id="email-note" class="fine">預覽模式：請填測試信箱。不儲存、不寄信。</p><button class="primary" type="submit">Preview my free lesson →</button></form><div id="email-success" hidden role="status"><p class="fine">示範完成，沒有寄送 Email。</p><a class="primary" href="facial-tension-journey.html">Watch the free demonstration →</a></div></div></section><div class="result-links"><button class="text-button" id="restart">Try different answers</button><a class="text-button" href="eye-method-course-preview.html">Explore the US$79 course</a></div></section>`;
    const video=document.getElementById('lesson-video');video.addEventListener('error',()=>document.getElementById('video-error').hidden=false);video.querySelector('source').addEventListener('error',()=>document.getElementById('video-error').hidden=false);
    document.getElementById('replay').addEventListener('click',()=>{video.currentTime=0;video.play().catch(()=>{document.getElementById('video-error').hidden=false;});});
    document.getElementById('takeaway').addEventListener('click',()=>{
      const note=document.getElementById('learning-note');
      document.getElementById('takeaway').hidden=true;
      if(active && r.check){
        const check=document.getElementById('micro-check');check.hidden=false;
        check.innerHTML=`<fieldset class="micro-options"><legend>${r.check}</legend>${r.choices.map((text,i)=>`<button type="button" data-answer="${i}" aria-pressed="false">${text}</button>`).join('')}</fieldset><p id="check-feedback" role="status"></p>`;
        check.querySelectorAll('button').forEach(button=>button.addEventListener('click',()=>{
          check.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed','false'));button.setAttribute('aria-pressed','true');
          const right=Number(button.dataset.answer)===r.correct;
          document.getElementById('check-feedback').textContent=right?'Yes—that’s the detail.':r.retry;
          note.hidden=!right;
        }));
        check.querySelector('button').focus();
      }else{note.hidden=false;note.focus();}
    });
    document.getElementById('unlock').addEventListener('click',()=>{document.getElementById('email-panel').hidden=false;document.getElementById('unlock').hidden=true;document.getElementById('quiz-email').focus();});
    document.getElementById('email-panel').addEventListener('submit',event=>{event.preventDefault();const form=event.currentTarget;if(!form.reportValidity())return;form.reset();form.hidden=true;document.getElementById('email-success').hidden=false;document.querySelector('#email-success a').focus();});
    document.getElementById('restart').addEventListener('click',()=>{answers.fill(null);renderQuestion(0);});focusStage();
  }
  document.getElementById('start').addEventListener('click',()=>{welcome.hidden=true;experience.hidden=false;renderQuestion(0);});
  back.addEventListener('click',()=>{if(current==='result')renderQuestion(3);else if(current==='insight')renderQuestion(1);else if(current===2)renderInsight();else if(current>0)renderQuestion(current-1);else{pauseMedia();experience.hidden=true;welcome.hidden=false;document.getElementById('start').focus();}});
})();
