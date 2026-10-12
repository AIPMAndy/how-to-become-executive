from pathlib import Path
P=Path(__file__).resolve().parents[1]
b=P/'build.py';s=b.read_text(encoding='utf-8')
needle="    resources=''.join("
assert needle in s
block='''    evidence_ids=['EV01','EV02','EV05','EV06','EV07','EV11']
    evidence_byid={e['id']:e for e in data['evidence']}
    source_byid={s['id']:s for s in data['sources']}
    cards=[]
    for eid in evidence_ids:
        e=evidence_byid[eid]
        source=source_byid[e['source_id']]
        cards.append('<article class="evidence-card"><div class="ev-meta">'+html.escape(e['id'])+' · '+html.escape(e['type'])+'</div><div class="ev-number">'+html.escape(e['number'])+'</div><h3>'+html.escape(e['headline'])+'</h3><p>'+html.escape(e['what'])+'</p><p class="ev-limits"><strong>不能这样推：</strong>'+html.escape(e['limits'])+'</p><a target="_blank" rel="noopener noreferrer" href="'+html.escape(source['url'],quote=True)+'">查原始研究 ↗</a> · <a href="evidence/RESEARCH_ATLAS.html#'+eid.lower()+'">看证据边界</a></article>')
    evidence_section='<section class="evidence-section" id="evidence"><div class="section-title"><h2>先看硬证据，再跟着做</h2></div><p class="sub">企业原始披露、研究数据、元分析。数字只支持对应的结论，不表示个人升职概率。</p><div class="evidence-cards">'+''.join(cards)+'</div><div class="evidence-images"><figure><img src="evidence/manager-engagement-2022-2025.svg" loading="lazy" alt="2022至2025全球经理与非经理敬业度对比，Gallup 2026数据二次绘图"><figcaption>根据Gallup2026公开数据重绘；敬业度不能代替管理能力或晋升概率。</figcaption></figure><figure><img src="evidence/internal-mobility-leadership.svg" loading="lazy" alt="内部流动率高的企业晋升次数相对对比，低组100、高组179"><figcaption>根据LinkedIn2024企业观察重绘；相关性不证明内部流动导致晋升。</figcaption></figure></div><p><a class="btn primary" href="evidence/RESEARCH_ATLAS.html">查看14张完整证据卡及原始链接 →</a> <a class="btn" href="evidence/CASE_STUDIES.html">3个真实企业案例</a> <a class="btn" href="audit/EVIDENCE_AUDIT.html">对抗审查报告</a></p></section>'
'''
s=s.replace(needle,block+needle)
s=s.replace('<a href="#tools">免费工具</a><a href="#references">参考来源</a>', '<a href="#tools">免费工具</a><a href="#evidence">原始证据</a><a href="#references">参考来源</a>')
s=s.replace('<section class="layout" id="actions">','{evidence_section}<section class="layout" id="actions">')
s=s.replace("files=[*ROOT.glob('guides/*.md')", "files=[*ROOT.glob('evidence/*.md'),*ROOT.glob('guides/*.md')")
b.write_text(s,encoding='utf-8')
css=P/'assets/style.css';s=css.read_text(encoding='utf-8');s+='''\n/* Credible-source panel: original numbers and clear exclusions */\n.evidence-section{margin:28px 0 35px}.evidence-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:20px 0}.evidence-card{border:1px solid var(--stroke);background:#fff;border-radius:15px;padding:19px}.ev-meta{font-size:11px;color:var(--muted)}.ev-number{font-weight:900;font-size:35px;color:var(--blue);line-height:1.3;margin-top:6px}.evidence-card h3{font-size:16px;line-height:1.4;margin:4px 0 8px}.evidence-card p{font-size:13px;line-height:1.65;color:#475569}.evidence-card .ev-limits{font-size:12px;background:#fff6eb;padding:9px;border-radius:8px;color:#67481b}.evidence-card a{font-size:12px;font-weight:700}.evidence-images{display:grid;grid-template-columns:1fr 1fr;gap:14px}.evidence-images figure{padding:10px;margin:0;border:1px solid var(--stroke);border-radius:15px;background:#fff}.evidence-images img{display:block;width:100%;height:auto}.evidence-images figcaption{font-size:12px;color:var(--muted);padding:9px 10px}@media(max-width:900px){.evidence-cards{grid-template-columns:repeat(2,1fr)}}@media(max-width:640px){.evidence-cards,.evidence-images{grid-template-columns:1fr}}\n''';css.write_text(s,encoding='utf-8')
js=P/'assets/app.js';s=js.read_text(encoding='utf-8')
s=s.replace("num:'56'", "num:String(d.tasks.length)")
s=s.replace("if(t.sources.length){details.appendChild(TEXT('div','研究与官方来源','label'))", "if(t.sources.length){details.appendChild(TEXT('div','外部证据/政策（适用范围请核对）','label'))")
s=s.replace("}card.appendChild(details);cards.appendChild(card)","}else{details.appendChild(TEXT('div','证据提示','label'));details.appendChild(TEXT('p','这是项目作者设计的实务练习，目前没有直接实证证据支持该任务可预测晋升。'))}card.appendChild(details);cards.appendChild(card)")
js.write_text(s,encoding='utf-8')
print('Patched build, CSS and task source presentation')
