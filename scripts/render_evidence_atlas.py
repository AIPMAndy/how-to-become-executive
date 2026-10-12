from pathlib import Path
import json,html
P=Path(__file__).resolve().parents[1]
d=json.loads((P/'data/guide.json').read_text(encoding='utf-8'))
refs={v['id']:v for v in d['sources']}
P.joinpath('evidence').mkdir(exist_ok=True)
s=['# 高管成长证据图谱：从研究原文到每一步行动', '', '> 资料核验：2026-10-12。这里刻意区分“原始研究实际测量的内容”和“作者建议的行动”。证据不保证任何读者晋升；关联不是因果。每份资料都可以点开原文独立核查。', '', '[返回项目首页](../README.md) · [3个真实企业案例](CASE_STUDIES.md) · [统计图数据与方法](DATA_VISUALIZATIONS.md) · [对抗式审核](../audit/ADVERSARIAL_REVIEW.md)', '', '## 第一组：最值得先看的事实', '', '| 编号 | 研究或真实案例 | 关键数据 | 证明什么 | 不能证明什么 |', '|---|---|---|---|---|']
for e in d['evidence']:
 r=refs[e['source_id']]
 s.append(f"| [{e['id']}](#{e['id'].lower()}) | [{e['headline']}]({r['url']}) | **{e['number']}** | {e['supports']} | {e['limits']} |")
s+=['','## 逐条证据：来源、研究对象、局限和执行动作','']
for e in d['evidence']:
 r=refs[e['source_id']]
 s += [f"<a id=\"{e['id'].lower()}\"></a>",f"### {e['id']}｜{e['headline']}",'',f"**证据的原始结果：** {e['what']}",'',f"**研究类型与样本：**{e['type']}。{e['sample']}",'',f"**能支持的建议：**{e['supports']}",'',f"**不能推出什么：**{e['limits']}",'',f"**今天具体做什么：**{e['action']}",'',f"**证据评价：**{e['confidence']}",'',f"**原始来源：**[{r['org']}｜{r['title']}]({r['url']})（公开时间：{r['published']}；核验：{r['checked']}）。",'','---','']
s+=['## 哪些建议仍只有实务逻辑，缺少晋升结果验证？','','以下属于本项目的原创教学设计，不应归因于Gallup、Google、McKinsey或CIPD的研究：','','- **“7阶段成长路线、84项任务”**：教学组织方法；没有任何研究证明完成即升职。','- **“找3份JD、做3张案例卡、90天计划”**：便于读者实践的练习量；不是论文验证的最佳阈值。','- **“8维自评0—3分”**：作者整理的自查清单；没有心理测量效度、个案预测效度。','- **“有Sponsor会晋升”**：可能是现实职场现象，但本文没有直接使用能够证明特定概率的对照研究，所以不写百分比。','- **“某企业宣称75%经理从基层来”**：历史已任职管理者的构成，不能倒推出员工晋升概率，存在存活者偏差。','', '## 读者如何反查一条结论？','','打开链接 → 确认页面发布者、发布时间 → 核对原始数据的统计对象和分母 → 判断描述/相关/因果 → 列出不适用的人和公司 → 再把行动写成可验证的交付物。','','如发现数字、措辞或来源变化，欢迎提交 GitHub Issue：请附官方原文、变更日期、建议修订、你的质疑。不要上传个人工资、公司数据或客户信息。','']
(P/'evidence/RESEARCH_ATLAS.md').write_text('\n'.join(s),encoding='utf-8')
case='''# 三个真实企业案例：这才叫原始证据

> 这三例全部使用企业或研究发布者自己的公开材料，不虚构“某学员从0到VP”故事。它们说明组织里某些路径确实存在，但**不承诺对每个普通人有效**。

## 案例一：沃尔玛，基层岗位真的有人走向管理岗位

沃尔玛2026年6月29日公司高管公开文章指出：**75%的受薪经理曾从小时工岗位起步**。这是一条相当具体的组织内部人才流动事实。沃尔玛同时披露培训项目和岗位发展计划。2025年文章还描述了其员工技能训练及AI面试辅导尝试。

- **直接证据：**[2026年沃尔玛公司文章，首席人力官署名](https://corporate.walmart.com/news/2026/06/29/bringing-new-career-paths-into-focus)。
- **辅助资料：**[2025年沃尔玛面试教练与技能培训新闻](https://corporate.walmart.com/news/2025/06/05/walmart-pilots-ai-interview-coach-and-accelerates-associate-to-technician-program-to-fuel-careers)。
- **可以迁移的动作：**不要只问“我在当前岗位干多久才能升”，要核实企业是否有内部竞聘、培训、跨岗历练和正式上升通道。
- **不能这么推断：**“每个基层员工75%概率成为经理”。该75%是**已成为经理的人过去从哪起步**，不是所有基层员工最终能升职的比例，分母不同；也不保证中国企业相同。

**普通读者实操：**联系主管/HR问这3件事：过去一年本部门真实晋升了哪些岗位（无需索取他人隐私）；晋升人选通常要拥有哪类可核验成果；下一次内部选拔/试任是什么时间。把答复写进 [岗位对照表](../templates/role-gap.md)。

## 案例二：谷歌，180个团队的管理研究

Google re:Work公开Project Aristotle：**180个团队，含115个工程项目组、65个销售小组**，综合主管、负责人、团队成员等评价与销售目标，识别了心理安全、可靠性、结构清晰、意义和影响等团队动态因素。

- **直接证据：**[Google re:Work 原始研究说明](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness)。
- **可以迁移的动作：**项目负责人至少写清目标与完成条件、每个关键依赖的负责人、出现分歧谁有最后决策权、团队怎样安全地上报坏消息。
- **不能这么推断：**任何团队只要开会讨论心理安全，绩效就会提升某个固定百分比。Google研究以本企业组织为主，不是跨中国企业的随机实验。

**普通读者实操：**任选一个已授权项目，组织15分钟风险回顾；把最影响目标的三项阻碍写进 [项目章程](../templates/project-charter.md) 和 [风险登记表](../templates/risk-register.csv)，与Sponsor确认升级人。

## 案例三：亚马逊，高级岗位面试要说具体行为和结果

亚马逊官方招聘指导说明，它会结合公司的Leadership Principles，让候选人讲过去如何围绕客户问题作选择、承担责任、持续交付。官网举的案例展示**故事如何组织**，这些数字只是官方示范话术，不是独立审计过的真实业绩。

- **直接证据：**[Amazon官方：领导力原则与面试](https://www.aboutamazon.com/news/workplace/amazon-leadership-principles-interview)。
- **可以迁移的动作：**准备能被追问的项目故事：目标、当时的信息缺口、你做出的决定、其他人的贡献、实际结果、如果重做会怎么改变。
- **不能这么推断：**亚马逊以外所有企业都有同样的面试流程，更不能把它的示例数字复制成个人简历成果。

**普通读者实操：**按 [成果证据卡](../templates/impact-evidence.md) 完成3个真实案例，预演“结果真由你带来吗”“如何排除行情变化”“当时谁拍板”三项追问。

## 三个案例共同能说明什么？

**路径存在，需要组织机制；能力要体现在团队和业务行动；成果要经得起检验。** 但目前没有一个可信研究支持“照此操作X个月后，普通人成为VP的概率是Y%”。项目因此明确不提供保证。
'''
(P/'evidence/CASE_STUDIES.md').write_text(case,encoding='utf-8')
fig='''# 两张数据图：核对口径后再解读

图像由本项目依据出处提供的**数字重新绘制**，没有伪装成Gallup、LinkedIn的官方截图。这里给出每个值的原始出处与计算规则。

## 图一：全球管理者敬业度从2022到2025的变化

![按Gallup 2026公开数据重绘：2022–2025全球经理与非经理敬业度](manager-engagement-2022-2025.svg)

| 年份 | 全球经理敬业度 | 全球非经理敬业度 |
|---|---:|---:|
| 2022 | 31% | 20% |
| 2023 | 30% | 18% |
| 2024 | 27% | 18% |
| 2025 | 22% | 19% |

原始来源：[Gallup 2026全球职场报告](https://www.gallup.com/workplace/349484/leadership.aspx)，统计的是从业者报告的**engaged**比例。**这不是升职概率**；说明管理岗位所受的环境压力需要被认真考虑。

## 图二：内部流动率不同的企业管理晋升差异

![按LinkedIn 2024分析重绘：低流动组指数100 vs 高流动组179](internal-mobility-leadership.svg)

LinkedIn 2024年企业数据分析报告：内部流动率最高十分位企业，**每位员工获得管理岗位晋升次数**比最低十分位高79%。图中将低流动组设为“100”，高组为“179”，属于**相对指标重绘**，不是原文公布的绝对概率，也不是个体晋升成功率。

原始来源：[LinkedIn Talent Solutions 2024](https://www.linkedin.com/business/talent/blog/talent-acquisition/how-internal-mobility-benefits-employers)，主要限制为观察性平台数据、非随机比较；无法判定内部流动本身带来了多少晋升。
'''
(P/'evidence/DATA_VISUALIZATIONS.md').write_text(fig,encoding='utf-8')
# Unpretentious self-made chart SVG with accurate data
labels=[2022,2023,2024,2025];manager=[31,30,27,22];nonmanager=[20,18,18,19]
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="570" viewBox="0 0 1100 570" role="img">', '<rect width="1100" height="570" rx="20" fill="#f8fafc"/>','<text x="50" y="68" fill="#0f172a" font-size="32" font-family="Noto Sans CJK SC,sans-serif" font-weight="bold">全球管理者敬业度持续下降</text>','<text x="50" y="109" fill="#475569" font-size="19" font-family="Noto Sans CJK SC,sans-serif">2022—2025 · 按 Gallup 2026 公开百分比重绘 · 单位：%</text>']
for i,(year,m,n) in enumerate(zip(labels,manager,nonmanager)):
 y=148+i*85
 svg.extend([f'<text x="55" y="{y+38}" fill="#334155" font-size="22">{year}</text>',f'<rect x="150" y="{y+4}" width="{m*19}" height="30" rx="5" fill="#2563eb"/>',f'<text x="{158+m*19}" y="{y+27}" font-size="19" fill="#1e3a8a">{m}% 经理</text>',f'<rect x="150" y="{y+41}" width="{n*19}" height="25" rx="5" fill="#94a3b8"/>',f'<text x="{158+n*19}" y="{y+60}" font-size="17" fill="#475569">{n}% 非经理</text>'])
svg.extend(['<text x="50" y="521" font-size="16" fill="#475569">来源：Gallup《State of the Global Workplace 2026》· 2025数据于2026发布</text>','<text x="50" y="545" font-size="14" fill="#64748b">本项目二次绘图，非Gallup官方原图。敬业度不是晋升概率，也不证明单一原因。</text>','</svg>'])
(P/'evidence/manager-engagement-2022-2025.svg').write_text('\n'.join(svg))
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="460" viewBox="0 0 1100 460" role="img">','<rect width="1100" height="460" rx="20" fill="#f8fafc"/>','<text x="50" y="68" font-size="30" font-weight="bold" fill="#0f172a">内部流动率高的企业，人均领导岗位晋升次数更多</text>','<text x="50" y="104" font-size="18" fill="#475569">LinkedIn 2024 企业数据分析 · 低流动组标准化为100</text>','<text x="50" y="170" font-size="20" fill="#334155">最低十分位</text>','<rect x="215" y="145" width="350" height="45" rx="6" fill="#94a3b8"/>','<text x="583" y="178" font-size="24" fill="#475569">100</text>','<text x="50" y="266" font-size="20" fill="#334155">最高十分位</text>','<rect x="215" y="240" width="626.5" height="45" rx="6" fill="#2563eb"/>','<text x="856" y="273" font-size="24" fill="#1d4ed8">179</text>','<text x="50" y="374" font-size="17" fill="#475569">原始报告：高流动组人均领导岗位晋升次数高79%（相对差异）</text>','<text x="50" y="411" font-size="15" fill="#64748b">本项目依数据重绘。非个体升职概率；属于相关性，不代表因果。</text>','</svg>']
(P/'evidence/internal-mobility-leadership.svg').write_text('\n'.join(svg))
print('Atlas, company cases, figures ready.')
