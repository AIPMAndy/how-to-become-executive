from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
D=P/'data/guide.json'
d=json.loads(D.read_text(encoding='utf-8'))
new_sources=[
('e-walmart','沃尔玛2026官方：75%受薪经理从小时工岗位起步','https://corporate.walmart.com/news/2026/06/29/bringing-new-career-paths-into-focus','Walmart Corporate','2026-06-29'),
('e-linkedin-leaders','LinkedIn2024：内部流动与领导晋升的企业数据','https://www.linkedin.com/business/talent/blog/talent-acquisition/how-internal-mobility-benefits-employers','LinkedIn Talent Solutions','2024-06-24'),
('e-linkedin-mobility','LinkedIn2024：2021–2023企业内部流动比例','https://www.linkedin.com/business/talent/blog/talent-management/internal-mobility-is-booming-but-not-for-everybody','LinkedIn Talent Solutions','2024-02-22'),
('e-ccl-12','CCL2024：近300名新兴领导者的12类挑战','https://www.ccl.org/articles/leading-effectively-articles/first-time-managers-must-conquer-these-challenges/','Center for Creative Leadership','2024-10-25'),
('e-meta-training','Lacerenza等2017：领导力培训335独立样本元分析','https://pubmed.ncbi.nlm.nih.gov/28749153/','Journal of Applied Psychology / PubMed','2017'),
('e-google-180','Google re:Work：Aristotle 180团队研究','https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness','Google re:Work','公开研究（页面持续更新）'),
('e-gallup-2026','Gallup2026：2025管理者敬业度22%','https://www.gallup.com/workplace/349484/leadership.aspx','Gallup','2026-04'),
('e-gallup-70','Gallup2015：管理者解释团队敬业度评分的显著差异','https://www.gallup.com/workplace/236570/managers-account-percent-variance-employee-engagement.aspx','Gallup','2015-04-08'),
('e-cipd-succ','CIPD2025：继任计划侧重关键岗位与真实工作历练','https://www.cipd.org/en/knowledge/factsheets/succession-planning-factsheet/','CIPD','2025-12-05'),
('e-cipd-feedback','CIPD2022：绩效反馈证据综述','https://www.cipd.org/uk/knowledge/evidence-reviews/performance-feedback/','CIPD','2022-09-20'),
('e-mck-7800','McKinsey2019：基于7800名CEO数据库的六项职责框架','https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-mindsets-and-practices-of-excellent-ceos','McKinsey & Company','2019-10-25'),
('e-amazon-hiring','亚马逊2025：领导力原则如何用于面试案例','https://www.aboutamazon.com/news/workplace/amazon-leadership-principles-interview','Amazon官方','2025'),
('e-company-law','市场监管总局：《中华人民共和国公司法》','https://www.samr.gov.cn/xyjgs/flfg/art/2024/art_d4e84936a8a744f8928ac7aec7594345.html','国家市场监督管理总局','2024-07-01'),
('e-gallup-ai','Gallup2026：经理支持AI与团队使用率的调查关联','https://www.gallup.com/workplace/349484/leadership.aspx','Gallup','2026-04'),
]
known={s['id'] for s in d['sources']}
for id,title,url,org,published in new_sources:
 if id not in known:d['sources'].append({'id':id,'title':title,'url':url,'org':org,'published':published,'checked':'2026-10-12'})
d['evidence']=[
{'id':'EV01','source_id':'e-walmart','stage':'position','headline':'75% 的受薪经理从基层小时工起步','number':'75%','what':'沃尔玛于2026年6月披露：其受薪经理中有75%曾从小时工岗位起步；沃尔玛同时披露培训、学历/技能路径和岗位发展项目。','type':'企业自行披露的人才数据','sample':'沃尔玛相关受薪管理群体；原文未提供完整因果识别模型','supports':'部分大型企业有真实的内部晋升通道；应查内部选拔规则和管理者培养项目。','limits':'既不能推导一个基层员工有75%概率升经理，也不能推导中国互联网公司采用相同机制。','action':'查组织过去12个月内部晋升样例、岗位开放机制和能力标准。','confidence':'中：原始企业披露；对企业自身有说明力，无法外推'},
{'id':'EV02','source_id':'e-linkedin-leaders','stage':'promotion','headline':'企业内部流动高的一组，领导岗位晋升更多','number':'+79%','what':'LinkedIn 2024企业级观察：内部流动率最高十分位企业的人均管理岗位晋升数量，比最低十分位企业高79%。','type':'平台会员职业变动数据的观察研究','sample':'企业按内部流动率分十等分；参与企业须至少100次岗位转换且至少5次晋升，具体方法见原文','supports':'研究公司是否提供内部转岗、轮岗、公开竞聘与晋升通道，很有必要。','limits':'相关性，不代表“多参加轮岗可提升79%个人晋升概率”；可能有组织规模、人才质量等混杂变量。','action':'询问HR内部岗位公告、轮岗审批、晋升评审和经理支持机制。','confidence':'中：有披露方法；缺少随机分配与因果控制'},
{'id':'EV03','source_id':'e-linkedin-mobility','stage':'position','headline':'LinkedIn样本中的内部流动率曾上升','number':'18.7% → 24.4%','what':'2024年LinkedIn对历史样本的分析显示，符合其筛选条件企业的内部流动率由2021年18.7%升至2023年24.4%。','type':'平台职业变动数据','sample':'企业需至少75次岗位转换；采用企业内部流动率中位数，样本来自LinkedIn会员数据','supports':'职业发展可以考虑横向移动和内部跨职能，不必只等原岗位升职。','limits':'不代表2026年所有企业内部流动率，也不代表内部移动都属于晋升。','action':'优先从目标岗位实际需要的相邻职能积累责任和证据。','confidence':'中：限定平台和企业筛选条件'},
{'id':'EV04','source_id':'e-ccl-12','stage':'manager','headline':'新经理真正困难的不是写计划，而是带人','number':'近300人 / 12类挑战','what':'CCL分析近300名参加初任经理领导力项目的新兴领导者，归纳12项挑战，包括管理昔日同事、授权、绩效反馈、冲突和跨组织沟通。','type':'培训参与者的组织研究/实务归纳','sample':'近300名参加CCL特定培训项目的人员，非随机全球经理代表样本','supports':'从骨干晋升为经理需要专项训练团队与反馈技能。','limits':'不能据此证明12项挑战有统一排序，或每名经理都经历全部挑战。','action':'制定新经理30天清单：明确目标、1对1、授权边界、反馈与冲突升级。','confidence':'中：明确样本且与场景直接相关'},
{'id':'EV05','source_id':'e-meta-training','stage':'expert','headline':'领导力训练是可练习、可迁移的','number':'335个独立样本','what':'Lacerenza等发表于2017年的元分析整合335个独立样本，领导力培训在学习、迁移和结果等指标上总体有正向效应，效果随设计方式不同而变化。','type':'跨研究元分析','sample':'335个独立样本；发表在Journal of Applied Psychology','supports':'训练不应只看课程时长，应加入工作实践、反馈和间隔练习。','limits':'培训改善管理学习/绩效指标不等于能够预测高管升职；各研究设计和场景有差异。','action':'用真实项目练一个能力，安排30天复盘，检查结果是否迁移到工作。','confidence':'较高：多研究综合，但不针对中国高管晋升'},
{'id':'EV06','source_id':'e-google-180','stage':'owner','headline':'Google研究的关键是团队互动质量','number':'180个团队','what':'Google Project Aristotle分析180个团队（115个工程项目组和65个销售组），识别与团队有效性相关的五个动态因素：心理安全、可靠性、结构清晰、意义与影响。','type':'单一大型企业内部团队观察研究','sample':'Google 180个团队，团队规模3至50人，中位数9人','supports':'项目Owner要说明目标、角色、决策机制，并让成员能提出风险和问题。','limits':'相关研究，不证明照抄Google会议方式就必然提升KPI；也不等于群体成员素质不重要。','action':'在项目章程加入决策权、依赖、责任人、升级与复盘节奏。','confidence':'中：真实企业研究，有环境局限'},
{'id':'EV07','source_id':'e-gallup-2026','stage':'manager','headline':'当经理也会有压力，不能只看Title','number':'22%','what':'Gallup 2026全球职场报告显示：2025年全球经理敬业度22%，非经理为19%；经理敬业度由2022年的31%降至2025年的22%。','type':'跨国劳动力抽样调查','sample':'Gallup 2026报告：2025年全球调查141444位在职受访者（整体263810）','supports':'转管理岗位要同时评估资源、工作负荷与个人可持续性。','limits':'不是个人升职概率、管理技能等级或“中国经理不快乐的精确比例”。','action':'谈晋升时同时核实岗位目标、预算、直接下属数量和资源保障。','confidence':'较高：明确年度调查与方法，仍为主观敬业度指标'},
{'id':'EV08','source_id':'e-gallup-70','stage':'manager','headline':'经理对团队氛围的作用可以被量化观察','number':'约70%','what':'Gallup 2015年发表的美国管理研究称，经理因素可以解释团队敬业度评分的约70%方差，并强调频繁沟通、员工发展与优势使用。','type':'管理者及员工调查的统计关联','sample':'美国职场研究；包含7272名美国成年人等调查，页面另述经理行为调查','supports':'明确期望、持续反馈和成员发展应作为经理核心职责。','limits':'70%是方差解释，不等于经理控制70%的业绩，也不代表因果作用比例。','action':'每周明确优先级、对齐责任人，并按月复盘反馈质量。','confidence':'中：关联数据有样本，但易被公众误读'},
{'id':'EV09','source_id':'e-cipd-succ','stage':'promotion','headline':'组织是否有继任机制决定了机会是否存在','number':'关键岗位规划','what':'CIPD 2025年继任计划资料指出，继任规划识别未来关键岗位，通常包含与未来职责有关的实践性、定制化工作历练。','type':'专业机构证据与实务指南','sample':'专业组织知识综述，并非升职概率统计','supports':'职位机会和真实职责体验很重要；争取有授权的试任项目。','limits':'没有证明每家企业都运行正式继任计划；人才储备名单不等于升职承诺。','action':'向主管确认岗位窗口、试任职责、评估人和下一次讨论时间。','confidence':'中：专业实务指南，非量化因果研究'},
{'id':'EV10','source_id':'e-cipd-feedback','stage':'manager','headline':'反馈确有作用，也可能起反效果','number':'有正面也有风险','what':'CIPD 2022年对绩效反馈研究进行证据综述：反馈的方式会影响其效果，处理不当可对员工绩效产生不利作用。','type':'专业机构证据综述','sample':'CIPD回顾研究及实践建议，公开摘要未给单一可外推影响率','supports':'建立以具体行为、共同目标、行动支持为基础的反馈方式。','limits':'不能称一次1对1就能提升X%团队业绩，也不能用反馈取代正式绩效制度。','action':'设计“事实—影响—询问—行动—复盘”的1对1记录。','confidence':'中高：综合证据但效果依情境'},
{'id':'EV11','source_id':'e-mck-7800','stage':'business','headline':'高级管理者做的是资源和组织层面的取舍','number':'7800位CEO资料','what':'McKinsey 2019年CEO研究使用覆盖70国、24行业、约3500家上市公司和7800位CEO、25年数据的数据库，提出战略、组织、团队、董事会、外部利益相关者及个人效能六大职责。','type':'咨询机构历史CEO数据库分析与实务框架','sample':'上市公司CEO样本；偏向大型成熟组织','supports':'准备业务负责人时应学习预算、资源取舍、团队搭建与跨组织沟通。','limits':'无法直接推导一个基层员工的七步晋升公式；CEO职责不能原样套到小型团队主管。','action':'每月做一页经营复盘：机会、取舍、资源、利润与现金、风险。','confidence':'中：大样本框架，较强的岗位与行业选择偏差'},
{'id':'EV12','source_id':'e-amazon-hiring','stage':'promotion','headline':'真实企业在管理面试看可核验的行为案例','number':'官方招聘实践','what':'亚马逊官方招聘指导要求申请者结合领导力原则提供以客户、主人翁意识和长期结果为中心的具体经历，并解释自己做过什么。','type':'真实雇主公开招聘标准','sample':'亚马逊面试指导，非晋升成功率统计','supports':'高管面试应该练习真实决策案例、取舍、冲突与结果，而不是抽象自我评价。','limits':'不能认为所有公司按亚马逊面试，也不能直接套用其页面示例数字当本人经历。','action':'准备六张STAR-L案例卡，标明团队贡献和结果的核实方式。','confidence':'高：作为该企业招聘说明可信；外推程度低'},
{'id':'EV13','source_id':'e-company-law','stage':'onboard','headline':'高管Title与法定高管身份不能混淆','number':'《公司法》第265条','what':'中国现行《公司法》第265条对法定高级管理人员有明确界定，公司董事、高管还涉及忠实勤勉、利益冲突等义务。','type':'现行法律规范','sample':'适用依法设立的中国公司，任命与章程细节需要个案核实','supports':'签高管Offer前先核对章程、正式任命、权限和法律责任。','limits':'不能看到VP/总监头衔就断定法定身份；法律条文也不代表个案法律意见。','action':'让公司提供正式任命与权限边界；重大利益冲突求助合规或律师。','confidence':'高：直接法律依据，事实适用需核实'},
{'id':'EV14','source_id':'e-gallup-ai','stage':'business','headline':'经理支持AI时，员工高频使用AI的比例更高','number':'79% vs 46%','what':'Gallup 2026报告援引2026年一季度美国职场调查：在经理积极支持AI使用的群体中，高频使用率79%，缺少这种支持时为46%。','type':'美国职场横截面问卷关联','sample':'2026 Q1美国就业者调查，尤其涉及已经实施AI的组织','supports':'AI负责人除选工具，还要设计经理示范、培训、流程融合与使用反馈。','limits':'不能据此断言管理者支持AI会因果提升33个百分点，也不代表在中国公司效果相同。','action':'在小范围授权试点记录采用率、任务质量、成本与合规问题。','confidence':'中：调查直接、主要是相关性'},
]
# Link strongest appropriate sources to stage actions; retaining pre-existing refs.
mapping={'position':['e-walmart','e-linkedin-mobility'],'expert':['e-meta-training'],'owner':['e-google-180'],'manager':['e-ccl-12','e-gallup-2026','e-cipd-feedback'],'business':['e-mck-7800','e-gallup-ai'],'promotion':['e-linkedin-leaders','e-cipd-succ','e-amazon-hiring'],'onboard':['e-company-law','e-mck-7800']}
for stage,refs in mapping.items():
 candidates=[t for t in d['tasks'] if t['stage']==stage]
 for i,t in enumerate(candidates):
  if i<min(len(refs)*3,len(candidates)):
   ref=refs[i%len(refs)]
   if ref not in t['sources']:t['sources'].append(ref)
# Mark evidence object validity and direct linkage, prevent assigning generic general data as proof of task effect.
d['version']='3.0.0-evidence'
d['methodology']='实证调查/元分析/企业披露/法律/专业实务指南分级；关联不当作因果；练习数量是项目设计，不是研究预测。'
D.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Added',len(d['evidence']),'evidence cards;',len(d['sources']),'sources; tasks',len(d['tasks']))
