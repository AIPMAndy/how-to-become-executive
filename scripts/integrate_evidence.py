from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
d=json.loads((P/'data/guide.json').read_text(encoding='utf-8'))
refs={s['id']:s for s in d['sources']}
evs={e['id']:e for e in d['evidence']}
# Stage chapter citation: fact, actual scope, implementation and what it doesn't establish
stagefiles={
 'guides/00-start.md':['EV01','EV02','EV05'],
 'guides/01-position.md':['EV01','EV03'],
 'guides/02-expert.md':['EV05','EV12'],
 'guides/03-owner.md':['EV06','EV04'],
 'guides/04-manager.md':['EV04','EV07','EV08','EV10'],
 'guides/05-business.md':['EV11','EV14'],
 'guides/06-promotion.md':['EV02','EV09','EV12'],
 'guides/07-onboard.md':['EV11','EV13'],
 'playbooks/01-first-week.md':['EV01','EV09'],
 'playbooks/02-impact-evidence.md':['EV12','EV05'],
 'playbooks/03-owner-authority.md':['EV06'],
 'playbooks/04-manager-first-30.md':['EV04','EV08','EV10'],
 'playbooks/05-financial-literacy.md':['EV11'],
 'playbooks/06-promotion-sponsor.md':['EV02','EV09','EV12'],
 'playbooks/07-new-role-180.md':['EV11','EV07'],
 'playbooks/08-career-stuck.md':['EV03','EV02'],
 'playbooks/09-governance-ethics.md':['EV13'],
 'playbooks/10-executive-interview.md':['EV12','EV11'],
 'tracks/ai-product.md':['EV14'],
 'tracks/product-operations.md':['EV06','EV11'],
 'tracks/finance-hr-technology.md':['EV13','EV09'],
}
for rel,ids in stagefiles.items():
 p=P/rel
 if not p.exists():print('MISSING',rel);continue
 s=p.read_text(encoding='utf-8')
 if '<!-- EVIDENCE START -->' in s:continue
 sentences=['<!-- EVIDENCE START -->','', '## 先看原始证据，再决定怎么做', '']
 for id in ids:
  e=evs[id];r=refs[e['source_id']]
  sentences += [f"**[{id}｜{e['number']}]({r['url']})** {e['what']}", '', f"**因此可以做：**{e['action']} **但不能推断：**{e['limits']}", '']
 sentences+=['> 提醒：这些来源包括企业披露、平台观察数据、实务综述和研究样本；相关性不是因果。下方动作由本项目设计，不是研究保证的晋升步骤。详情见 [完整证据图谱](../evidence/RESEARCH_ATLAS.md)。','','<!-- EVIDENCE END -->','']
 # add after top title and intro before other headings
 ls=s.splitlines(keepends=True)
 idx=next((i+1 for i,line in enumerate(ls) if line.startswith('# ')),0)
 ls.insert(idx,'\n'+'\n'.join(sentences)+'\n')
 p.write_text(''.join(ls),encoding='utf-8')
# README frontload evidential arguments rather than merely bibliography.
p=P/'README.md';s=p.read_text(encoding='utf-8')
if '## 这份指南终于有硬证据' not in s:
 start=s.index('## 第一次看，照着做这6步')
 evidence='''## 这份指南终于有硬证据：原始研究、真实企业、反例

> 数据均取自发布者公开原文。**每个数字对应特定统计对象**，并非“完成本项目就能升职”的预测。全部14张证据卡见 [研究原文与反例图谱](evidence/RESEARCH_ATLAS.html)。

| 核验过的结论 | 出处与对象 | 可以得出的行动 | 不能推出的结论 |
|---|---|---|---|
| **75%** 的沃尔玛受薪经理从小时工起步 | [沃尔玛2026年官方文章](https://corporate.walmart.com/news/2026/06/29/bringing-new-career-paths-into-focus) | 查内部晋升机制、学历与技能路线 | “基层员工有75%概率当经理” |
| 内部流动最高企业的**人均领导晋升次数高79%** | [LinkedIn 2024企业观察](https://www.linkedin.com/business/talent/blog/talent-acquisition/how-internal-mobility-benefits-employers) | 查轮岗、内部竞聘、管理岗位机会 | “个人横向跳岗晋升率提升79%” |
| **335个独立样本**支持领导力培训总体有效 | [Lacerenza等2017年元分析](https://pubmed.ncbi.nlm.nih.gov/28749153/) | 做真实项目、反馈、间隔练习 | “参加课程即可升高管” |
| **近300名初任管理者、12类挑战** | [CCL2024研究](https://www.ccl.org/articles/leading-effectively-articles/first-time-managers-must-conquer-these-challenges/) | 补授权、反馈、团队协作 | “每名经理都会遭遇这12项” |
| **180个Google团队**识别五项相关因素 | [Google re:Work原始说明](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness) | 建立清晰决策权、可靠协作 | “单靠心理安全可提升固定百分比绩效” |
| 2025年全球经理敬业度**22%** | [Gallup 2026全球职场报告](https://www.gallup.com/workplace/349484/leadership.aspx) | 升经理前评估资源、压力和组织环境 | “经理只有22%有能力”或“经理晋升率22%” |
| 研究覆盖**7800位CEO的历史数据库** | [McKinsey2019原始研究](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-mindsets-and-practices-of-excellent-ceos) | 学习方向、资源、团队、治理取舍 | “基层员工需要成为小CEO” |

![按Gallup2026公开数字重绘的管理者敬业度图](evidence/manager-engagement-2022-2025.svg)

<small>本图为依据Gallup公开数据绘制的二次图表，并非官方原图，指标为全球从业者自评的敬业度，不是晋升成功率。</small>

[研究证据总览](evidence/RESEARCH_ATLAS.html) · [3个真实企业案例](evidence/CASE_STUDIES.html) · [图表数字与口径](evidence/DATA_VISUALIZATIONS.html) · [证据纠错规则](audit/EVIDENCE_AUDIT.html)

'''
 s=s[:start]+evidence+s[start:]
s=s.replace('**7个阶段 · 84项具体任务 · 10份专题SOP · 33份文本/CSV模板 + 1份Excel工作簿 · 18条研究与法规来源**','**7个阶段 · 84项具体任务 · 10份专题SOP · 33份文本/CSV模板 + 1份Excel工作簿 · 14张原始证据卡（32条研究与法规线索）**')
s=s.replace('全部来源、发布年与适用限制见 [REFERENCES](REFERENCES.html)。','逐条论证、样本、数字来源与不能外推的边界，见 [14张证据卡](evidence/RESEARCH_ATLAS.html)；补充参考文献见 [REFERENCES](REFERENCES.html)。')
p.write_text(s,encoding='utf-8')
# Source references summary points to empirical atlas first
p=P/'REFERENCES.md';s=p.read_text(encoding='utf-8')
s=s.replace('# 研究来源与适用边界（核验：2026-10-12）','# 研究来源与适用边界（核验：2026-10-12）\n\n**原来这页主要是参考文献目录，缺少研究内容。现在已新增 [14张逐条证据卡](evidence/RESEARCH_ATLAS.md)、[3个企业案例](evidence/CASE_STUDIES.md) 和 [有原始数据口径的证据图](evidence/DATA_VISUALIZATIONS.md)。下方既有旧版资料链接，也有背景阅读链接；请优先参考逐条核验的证据卡。**')
p.write_text(s,encoding='utf-8')
print('Updated',len(stagefiles),'stage/SOP/track files plus README and references')
