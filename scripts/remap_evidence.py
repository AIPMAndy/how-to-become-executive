import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data/guide.json'
d=json.loads(p.read_text(encoding='utf-8'))
m={
'po08':['e-walmart','e-linkedin-leaders','e-cipd-succ'],'po10':['e-gallup-2026'],'po11':['e-cipd-succ'],'po12':['e-linkedin-mobility'],
'ex03':['e-meta-training'],'ex06':['e-cipd-feedback'],'ex11':['e-meta-training'],'ex12':['e-amazon-hiring'],
'ow03':['e-google-180'],'ow04':['e-google-180'],'ow10':['e-google-180'],'ow11':['e-google-180'],
'ma01':['e-ccl-12'],'ma02':['e-ccl-12','e-gallup-70'],'ma03':['e-google-180'],'ma04':['e-ccl-12'],'ma05':['e-gallup-70'],'ma06':['e-cipd-feedback'],'ma07':['e-cipd-succ'],'ma09':['e-ccl-12'],'ma10':['e-cipd-feedback'],'ma11':['e-ccl-12'],'ma12':['e-cipd-feedback'],
'bu01':['e-mck-7800'],'bu03':['e-mck-7800'],'bu04':['e-amazon-hiring'],'bu05':['e-mck-7800'],'bu07':['e-mck-7800'],'bu10':['e-mck-7800'],
'pr01':['e-linkedin-leaders','e-cipd-succ'],'pr02':['e-amazon-hiring'],'pr03':['e-mck-7800'],'pr04':['e-cipd-succ'],'pr06':['e-amazon-hiring'],'pr07':['e-linkedin-leaders'],'pr08':['e-company-law'],'pr09':['e-amazon-hiring'],'pr10':['e-cipd-succ'],'pr11':['e-mck-7800'],'pr12':['e-company-law'],
'on01':['e-mck-7800'],'on02':['e-company-law'],'on03':['e-mck-7800'],'on04':['e-mck-7800'],'on05':['e-mck-7800'],'on06':['e-cipd-succ'],'on08':['e-mck-7800'],'on11':['e-google-180'],'on12':['e-cipd-succ']
}
for t in d['tasks']:
 t['sources']=[s for s in t['sources'] if not s.startswith('e-')]+m.get(t['id'],[])
 t['evidence_note']='文献仅支持相关能力或组织机制的研究背景；本任务的步骤与完成标准是本项目设计，不能据此预测晋升。' if m.get(t['id']) else '当前任务是可操作的作者建议，不提供直接证实此任务导致晋升的研究。'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Task mapping',len(m),'of',len(d['tasks']),'semantically matched; remaining labeled as applied practice')
