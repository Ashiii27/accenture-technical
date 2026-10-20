/* ===== App — routing, playground, assessment ===== */
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const toast = msg => { const t=$('#toast'); t.textContent=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),2200); };

// ---- Routing ----
function showView(name){
  $$('.view').forEach(v=>v.classList.remove('active'));
  $(`#view-${name}`).classList.add('active');
  $$('.nav-link').forEach(l=>l.classList.toggle('active', l.dataset.view===name));
  window.scrollTo(0,0);
}
$$('.nav-link,.plat-card,.logo,[data-view]').forEach(el=>{
  el.addEventListener('click',()=>{
    const v=el.dataset.view; if(v) showView(v);
  });
});
$('#hamburger').addEventListener('click',()=>$('.nav-links').classList.toggle('open'));

// ---- Playground ----
const TEMPLATES = {
  blank:{h:'<h1>Hello, Accenture!</h1>\n<p>Edit me — see live preview.</p>',c:'body{\n  font-family: system-ui;\n  padding: 24px;\n  color: #1a1730;\n}\nh1{ color: #6c4cff; }',j:'// JavaScript here\ndocument.querySelector(\"h1\").addEventListener(\"click\", ()=>{\n  alert(\"Clicked!\");\n});'},
  counter:{h:'<div class=\"card\">\n  <h2 id=\"count\">0</h2>\n  <div class=\"row\">\n    <button id=\"dec\">−</button>\n    <button id=\"inc\">+</button>\n    <button id=\"reset\">Reset</button>\n  </div>\n</div>',c:`.card{\n  max-width:320px;margin:40px auto;\n  border:1px solid #e8e6f3;border-radius:14px;\n  padding:24px;text-align:center;\n  background:#fff;font-family:system-ui;\n}\n#count{font-size:48px;margin:0 0 12px}\n.row{display:flex;gap:8px;justify-content:center}\nbutton{padding:8px 16px;border-radius:8px;border:1px solid #ddd;cursor:pointer}\n#inc{background:#6c4cff;color:#fff;border-color:#6c4cff}`,j:'let n=0;\nconst el=document.getElementById(\"count\");\nconst render=()=> el.textContent=n;\ndocument.getElementById(\"inc\").onclick=()=>{ n++; render(); };\ndocument.getElementById(\"dec\").onclick=()=>{ n--; render(); };\ndocument.getElementById(\"reset\").onclick=()=>{ n=0; render(); };'},
  boxes:{h:'<h3>Click a box to toggle it</h3>\n<div class=\"grid\">\n  <div class=\"box\" data-c=\"1\"></div>\n  <div class=\"box\" data-c=\"2\"></div>\n  <div class=\"box\" data-c=\"3\"></div>\n  <div class=\"box\" data-c=\"4\"></div>\n  <div class=\"box\" data-c=\"5\"></div>\n  <div class=\"box\" data-c=\"6\"></div>\n</div>',c:`h3{font-family:system-ui;text-align:center}\n.grid{\n  display:grid;grid-template-columns:repeat(3,100px);\n  gap:12px;justify-content:center;margin-top:16px;\n}\n.box{\n  width:100px;height:100px;border-radius:12px;\n  background:#ede9ff;border:2px solid #c4b5fd;\n  cursor:pointer;transition:.2s;\n}\n.box.on{ background:#6c4cff;border-color:#6c4cff;transform:scale(.96)}\n`,j:`document.querySelectorAll(".box").forEach(b=>{\n  b.addEventListener("click",()=> b.classList.toggle("on"));\n});`},
  tipcalc:{h:'<div class=\"tip\">\n  <h2>Tip Calculator</h2>\n  <label>Bill: <input id=\"bill\" type=\"number\" value=\"100\"></label>\n  <label>Tip %: <input id=\"pct\" type=\"number\" value=\"15\"></label>\n  <button id=\"calc\">Calculate</button>\n  <p id=\"out\"></p>\n</div>',c:`.tip{\n  max-width:360px;margin:30px auto;\n  border:1px solid #e8e6f3;border-radius:14px;\n  padding:20px;font-family:system-ui;background:#fff;\n}\n.tip label{display:flex;justify-content:space-between;margin:8px 0}\n.tip input{width:120px;padding:6px;border:1px solid #ddd;border-radius:6px}\n#calc{width:100%;margin-top:10px;padding:10px;background:#6c4cff;color:#fff;border:none;border-radius:8px;cursor:pointer}\n#out{margin-top:12px;font-weight:700;text-align:center}`,j:`document.getElementById("calc").addEventListener("click",()=>{\n  const bill=parseFloat(document.getElementById("bill").value)||0;\n  const pct=parseFloat(document.getElementById("pct").value)||0;\n  const tip=bill*pct/100;\n  document.getElementById("out").textContent=\n    "Tip: $"+tip.toFixed(2)+" · Total: $"+(bill+tip).toFixed(2);\n});`},
  todo:{h:'<div class=\"todo\">\n  <h2>To-Do</h2>\n  <div class=\"row\">\n    <input id=\"inp\" placeholder=\"Add a task…\">\n    <button id=\"add\">Add</button>\n  </div>\n  <ul id=\"list\"></ul>\n</div>',c:`.todo{max-width:380px;margin:30px auto;font-family:system-ui;background:#fff;border:1px solid #e8e6f3;border-radius:14px;padding:20px}\n.row{display:flex;gap:8px}\n#inp{flex:1;padding:8px;border:1px solid #ddd;border-radius:8px}\n#add{padding:8px 14px;background:#6c4cff;color:#fff;border:none;border-radius:8px;cursor:pointer}\n#list{list-style:none;margin-top:12px}\n#list li{padding:8px;border-bottom:1px solid #f1efff;display:flex;justify-content:space-between}\n#list li.done{opacity:.5;text-decoration:line-through}\n`,j:`const inp=document.getElementById("inp"), list=document.getElementById("list");\nfunction addTask(){\n  const t=inp.value.trim(); if(!t) return;\n  const li=document.createElement("li");\n  li.textContent=t;\n  li.addEventListener("click",()=> li.classList.toggle("done"));\n  const del=document.createElement("button");\n  del.textContent="✕"; del.style.cssText="background:none;border:none;cursor:pointer";\n  del.onclick=e=>{ e.stopPropagation(); li.remove(); };\n  li.appendChild(del);\n  list.appendChild(li); inp.value="";\n}\ndocument.getElementById("add").onclick=addTask;\ninp.addEventListener("keydown",e=>{ if(e.key==="Enter") addTask(); });`},
};

const codeEls={html:$('#code-html'),css:$('#code-css'),js:$('#code-js')};
let activeEd='html';
$$('.ed-tab').forEach(t=>{
  t.addEventListener('click',()=>{
    $$('.ed-tab').forEach(x=>x.classList.remove('active'));
    $$('.ed-pane').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');
    $(`#ed-${t.dataset.ed}`).classList.add('active');
    activeEd=t.dataset.ed;
  });
});

function loadTemplate(k){
  const tpl=TEMPLATES[k]||TEMPLATES.blank;
  codeEls.html.value=tpl.h; codeEls.css.value=tpl.c; codeEls.js.value=tpl.j;
  runPreview();
}
$('#templateSelect').addEventListener('change',e=>loadTemplate(e.target.value));
$('#resetBtn').addEventListener('click',()=>{ loadTemplate($('#templateSelect').value); toast('Reset'); });
$('#runBtn').addEventListener('click',runPreview);

let runTimer=null;
Object.values(codeEls).forEach(el=> el.addEventListener('input',()=>{
  clearTimeout(runTimer); runTimer=setTimeout(runPreview,400);
}));

function runPreview(){
  const h=codeEls.html.value, c=codeEls.css.value, j=codeEls.js.value;
  const src=`<!DOCTYPE html><html><head><style>${c}<\/style><\/head><body>${h}<script>
try{${j}}catch(e){
  parent.postMessage({type:'jserr',msg:e.message},'*');
}
<\/script><\/body><\/html>`;
  const fr=$('#preview');
  fr.srcdoc=src;
  $('#consoleBody').innerHTML='';
}
window.addEventListener('message',e=>{
  if(e.data && e.data.type==='jserr'){
    const d=document.createElement('div'); d.className='err'; d.textContent='✕ '+e.data.msg;
    $('#consoleBody').appendChild(d);
  }
});
$('#clearConsole').addEventListener('click',()=> $('#consoleBody').innerHTML='');

// console capture for in-frame logs
(function hookConsole(){
  const orig=console.log;
  // no need — errors come via postMessage
})();

loadTemplate('counter');

// Tasks
const TASKS=[
  {title:'Counter with step',desc:'Add a <select> for step (1, 5, 10) so +/− uses it.',tpl:'counter'},
  {title:'Colour palette',desc:'6 boxes — click to cycle white → purple → green. Bonus: “Reset all” button.',tpl:'boxes'},
  {title:'Tip calculator + split',desc:'Add “Split among N people” — show per-person total.',tpl:'tipcalc'},
  {title:'To-Do: filter',desc:'Add All / Active / Done filter buttons above the list.',tpl:'todo'},
  {title:'Live search',desc:'Input filters a list of 20 names in real time (case-insensitive).',tpl:'blank'},
  {title:'Form validation',desc:'Email + password form: show inline errors, disable submit until valid.',tpl:'blank'},
];
const grid=$('#taskGrid');
TASKS.forEach(t=>{
  const d=document.createElement('div'); d.className='task';
  d.innerHTML=`<h4>${t.title}</h4><p>${t.desc}</p><code>Template: ${t.tpl}</code>`;
  d.addEventListener('click',()=>{
    $('#templateSelect').value=t.tpl; loadTemplate(t.tpl);
    document.querySelector('.play-layout').scrollIntoView({behavior:'smooth'});
    toast('Loaded: '+t.title);
  });
  grid.appendChild(d);
});

// ===== Assessment =====
(function(){
  if(typeof QUESTION_BANK==='undefined'){ console.warn('QUESTION_BANK not loaded'); return; }

  // Topic list derived from bank
  const TOPICS=[...new Set(QUESTION_BANK.map(q=>q.topic))].sort();
  const checksEl=$('#topicChecks'), bankInfo=$('#bankInfo');
  let selCount=20, selMode='exam', selOrder='shuffle';

  function renderChecks(){
    checksEl.innerHTML='';
    TOPICS.forEach(tp=>{
      const n=QUESTION_BANK.filter(q=>q.topic===tp).length;
      const lab=document.createElement('label'); lab.className='check';
      lab.innerHTML=`<input type="checkbox" checked data-topic="${tp}"> ${tp} <span class="count">${n}</span>`;
      checksEl.appendChild(lab);
    });
    checksEl.addEventListener('change',updateBankInfo);
    $('#checkAll').addEventListener('change',e=>{
      $$('#topicChecks input').forEach(cb=> cb.checked=e.target.checked);
      updateBankInfo();
    });
    updateBankInfo();
  }
  function selectedTopics(){
    return $$('#topicChecks input:checked').map(cb=>cb.dataset.topic);
  }
  function filteredBank(){
    const sel=new Set(selectedTopics());
    return QUESTION_BANK.filter(q=> sel.has(q.topic));
  }
  function updateBankInfo(){
    const nb=filteredBank().length;
    bankInfo.textContent=nb?`${nb} questions available in selected topics.`:`No questions — select at least one topic.`;
    const maxBtn=$$('#countGroup .pill').find(b=> +b.dataset.count<=nb);
    $$('#countGroup .pill').forEach(b=> b.disabled = +b.dataset.count>nb);
    // auto-adjust count if too high
    if(+$$('#countGroup .pill.active')?.dataset.count > nb){
      $$('#countGroup .pill').forEach(b=>b.classList.remove('active'));
      if(maxBtn) maxBtn.classList.add('active'); selCount = maxBtn?+maxBtn.dataset.count:10;
    }
  }
  $$('#countGroup .pill').forEach(b=> b.addEventListener('click',()=>{
    $$('#countGroup .pill').forEach(x=>x.classList.remove('active')); b.classList.add('active'); selCount=+b.dataset.count;
  }));
  $$('#modeGroup .pill').forEach(b=> b.addEventListener('click',()=>{
    $$('#modeGroup .pill').forEach(x=>x.classList.remove('active')); b.classList.add('active'); selMode=b.dataset.mode;
  }));
  $$('#orderGroup .pill').forEach(b=> b.addEventListener('click',()=>{
    $$('#orderGroup .pill').forEach(x=>x.classList.remove('active')); b.classList.add('active'); selOrder=b.dataset.order;
  }));
  renderChecks();

  // Live state
  let bank=[], ans=[], marked=[], cur=0, timerId=null, secsLeft=0, startTime=0, bankSnapshot=[];

  function shuffle(a){ const b=[...a]; for(let i=b.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [b[i],b[j]]=[b[j],b[i]];} return b;}

  $('#startBtn').addEventListener('click',()=>{
    const pool=filteredBank();
    if(!pool.length){ toast('Select at least one topic'); return; }
    let n=Math.min(selCount, pool.length);
    let picked = selOrder==='shuffle' ? shuffle(pool).slice(0,n) : pool.slice(0,n);
    bank=picked; ans=Array(n).fill(null); marked=Array(n).fill(false); cur=0;
    bankSnapshot=[...picked];
    secsLeft = selMode==='exam' ? 45*60 : 0;
    startTime=Date.now();
    $('#assess-setup').classList.add('hidden');
    $('#assess-result').classList.add('hidden');
    $('#assess-live').classList.remove('hidden');
    $('#reviewList').innerHTML='';
    renderAll();
    startTimer();
  });

  function startTimer(){
    clearInterval(timerId);
    if(selMode!=='exam'){ $('#timer').textContent='Practice'; return; }
    tick();
    timerId=setInterval(tick,1000);
  }
  function tick(){
    if(selMode!=='exam') return;
    const m=Math.floor(secsLeft/60), s=secsLeft%60;
    const el=$('#timer');
    el.textContent=`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
    el.classList.toggle('warn', secsLeft<=300 && secsLeft>60);
    el.classList.toggle('danger', secsLeft<=60 && secsLeft>0);
    if(secsLeft<=0){ clearInterval(timerId); submit(); }
    secsLeft--;
  }

  function renderAll(){ renderQ(); renderPalette(); updateMeta(); }

  function renderQ(){
    const q=bank[cur]; if(!q) return;
    const letters=['A','B','C','D'];
    const opts=q.options.map((o,i)=>{
      const sel=ans[cur]===String.fromCharCode(97+i);
      return `<div class="q-opt ${sel?'selected':''}" data-i="${i}"><div class="q-opt-letter">${letters[i]}</div><span>${esc(o)}</span></div>`;
    }).join('');
    $('#qCard').innerHTML=`
      <div class="q-topic">${esc(q.topic)} · Q${cur+1}</div>
      <div class="q-text">${fmt(q.q)}</div>
      <div class="q-opts">${opts}</div>
    `;
    $$('#qCard .q-opt').forEach(el=>{
      el.addEventListener('click',()=>{
        ans[cur]=String.fromCharCode(97+ (+el.dataset.i));
        renderAll();
      });
    });
  }
  function renderPalette(){
    const g=$('#paletteGrid'); g.innerHTML='';
    bank.forEach((_,i)=>{
      const b=document.createElement('button'); b.className='pal-btn';
      if(ans[i]!=null) b.classList.add('answered');
      if(marked[i]) b.classList.add('marked');
      if(i===cur) b.classList.add('current');
      b.textContent=i+1; b.addEventListener('click',()=>{ cur=i; renderAll(); });
      g.appendChild(b);
    });
    const answered=ans.filter(a=>a!=null).length;
    $('#liveQpos').textContent=`Q ${cur+1} / ${bank.length}`;
    $('#liveScore').textContent=`Answered ${answered} · Marked ${marked.filter(Boolean).length}`;
    $('#liveBar').style.width=(answered/bank.length*100)+'%';
    $('#submitHint').textContent=answered===bank.length?'All answered — ready to submit.':`${bank.length-answered} unanswered`;
    $('#markBtn').classList.toggle('active', !!marked[cur]);
    $('#markBtn').textContent=marked[cur]?'★ Marked':'☆ Mark';
    $('#prevBtn').disabled=cur===0;
    $('#nextBtn').disabled=cur===bank.length-1;
  }
  function updateMeta(){}

  $('#prevBtn').addEventListener('click',()=>{ if(cur>0){ cur--; renderAll(); }});
  $('#nextBtn').addEventListener('click',()=>{ if(cur<bank.length-1){ cur++; renderAll(); }});
  $('#clearBtn').addEventListener('click',()=>{ ans[cur]=null; renderAll(); });
  $('#markBtn').addEventListener('click',()=>{ marked[cur]=!marked[cur]; renderAll(); });
  $('#submitBtn').addEventListener('click',()=> submit());

  function esc(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function fmt(s){
    // render ```code``` blocks and `inline code`
    let h=esc(s);
    h=h.replace(/```([\s\S]*?)```/g,'<pre style="background:var(--surface-2);padding:10px;border-radius:8px;overflow:auto;font-family:var(--mono);font-size:12px;white-space:pre-wrap;margin:8px 0">$1</pre>');
    h=h.replace(/`([^`]+)`/g,'<code>$1</code>');
    return h;
  }

  function submit(){
    clearInterval(timerId);
    const total=bank.length;
    let correct=0;
    const byTopic={};
    bank.forEach((q,i)=>{
      if(!byTopic[q.topic]) byTopic[q.topic]={total:0,correct:0};
      byTopic[q.topic].total++;
      const ok = ans[i] && ans[i].toLowerCase()===q.answer.toLowerCase();
      if(ok){ correct++; byTopic[q.topic].correct++; }
    });
    const pct=Math.round(correct/total*100);
    const timeTaken = Math.round((Date.now()-startTime)/1000);
    const mm=Math.floor(timeTaken/60), ss=timeTaken%60;
    const pass = pct>=60;
    $('#assess-live').classList.add('hidden');
    $('#assess-result').classList.remove('hidden');
    $('#resultHero').className='result-hero'+(pass?' pass':'');
    $('#resultHero').innerHTML=`
      <p class="muted">Mock Assessment — Result</p>
      <div class="big">${correct} / ${total}</div>
      <p style="font-size:20px;font-weight:700">${pct}% · ${pass?'PASS ✓':'Keep practicing'}</p>
      <p class="verdict">Time: ${String(mm).padStart(2,'0')}:${String(ss).padStart(2,'0')} · 1 mark per correct, no negative marking</p>
    `;
    // breakdown
    let bh='';
    for(const [tp,v] of Object.entries(byTopic)){
      const p=v.total?Math.round(v.correct/v.total*100):0;
      const color = p>=70?'var(--green)': p>=40?'var(--amber)':'var(--red)';
      bh+=`<div class="tb-row"><div class="tb-head"><span>${esc(tp)}</span><span>${v.correct}/${v.total} · ${p}%</span></div><div class="tb-bar"><div class="tb-fill" style="width:${p}%;background:${color}"></div></div></div>`;
    }
    $('#topicBreakdown').innerHTML=bh;

    // stash for review
    window._lastResult={bank:[...bank], ans:[...ans], correct, total, pct, byTopic};
  }

  $('#reviewBtn').addEventListener('click', renderReview);
  $('#retryBtn').addEventListener('click',()=>{
    ans=Array(bank.length).fill(null); marked=Array(bank.length).fill(false); cur=0;
    secsLeft = selMode==='exam'?45*60:0; startTime=Date.now();
    $('#assess-result').classList.add('hidden'); $('#assess-live').classList.remove('hidden');
    renderAll(); startTimer();
  });
  $('#newBtn').addEventListener('click',()=>{
    $('#assess-result').classList.add('hidden'); $('#assess-live').classList.add('hidden');
    $('#assess-setup').classList.remove('hidden'); $('#reviewList').innerHTML='';
    clearInterval(timerId);
  });

  function renderReview(){
    const r=window._lastResult; if(!r) return;
    const letters=['A','B','C','D'];
    let html='';
    r.bank.forEach((q,i)=>{
      const chosen=r.ans[i];
      const ok = chosen && chosen.toLowerCase()===q.answer.toLowerCase();
      const status = !chosen ? 'Unanswered' : ok ? 'Correct' : 'Wrong';
      const badge = !chosen ? 'style="background:var(--surface-2);color:var(--muted)"' : ok ? 'style="background:var(--green-bg);color:var(--green)"' : 'style="background:var(--red-bg);color:var(--red)"';
      html+=`<div class="q-card" style="margin-bottom:10px">
        <div class="q-topic">${esc(q.topic)} · Q${i+1} <span ${badge} style="float:right;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:700">${status}</span></div>
        <div class="q-text">${fmt(q.q)}</div>
        <div class="q-opts">`;
      q.options.forEach((o,idx)=>{
        const letter=String.fromCharCode(97+idx);
        const isAns=letter===q.answer.toLowerCase();
        const isChosen=letter===chosen;
        let cls='q-opt';
        if(isAns) cls+=' correct';
        else if(isChosen) cls+=' wrong';
        html+=`<div class="${cls}"><div class="q-opt-letter">${letters[idx]}</div><span>${esc(o)}</span></div>`;
      });
      html+=`</div>`;
      if(q.explanation) html+=`<div class="q-expl"><strong>Why:</strong> ${esc(q.explanation)}</div>`;
      if(!q.explanation) html+=`<div class="q-expl muted">No explanation in source — answer is <strong>${q.answer.toUpperCase()}</strong>.</div>`;
      html+=`</div>`;
    });
    $('#reviewList').innerHTML=html;
    $('#reviewList').scrollIntoView({behavior:'smooth'});
  }
})();
