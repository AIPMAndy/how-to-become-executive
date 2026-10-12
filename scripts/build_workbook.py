#!/usr/bin/env python3
"""Optional authoring source for editable workbook; requires artifact_tool.
User data remains in the local workbook; filled example values are teaching examples.
"""
from pathlib import Path
from artifact_tool import Workbook, SpreadsheetFile
ROOT=Path(__file__).resolve().parents[1]
w=Workbook.create()
header={'fill':'#152C43','font':{'bold':True,'color':'#FFFFFF'},'row_height':27,'horizontal_alignment':'center','vertical_alignment':'center'}

def tab(name,columns,n=12,notes=None):
 s=w.worksheets.add(name)
 L=len(columns);s.get_range_by_indexes(0,0,1,L).values=[columns]
 s.get_range_by_indexes(0,0,1,L).format=header
 s.get_range_by_indexes(0,0,n,L).format.row_height=25
 s.get_range_by_indexes(1,0,n-1,L).format.wrap_text=True
 s.get_range_by_indexes(0,0,n,L).format.column_width=18
 s.get_range_by_indexes(0,0,n,1).format.column_width=22
 s.freeze_panes.freeze_rows(1)
 return s
s=tab('使用说明',['请先读这里','规则','什么时候完成','风险提醒'],8)
s.get_range('A2:D7').values=[
 ['1 岗位对照','只填真实JD与经授权信息','比较3个岗位','不知道的项写未知，不按Title猜测'],
 ['2 成果证据','基线、本人动作、团队贡献、结果分开','至少3项真实案例','不得填公司机密和编造增长率'],
 ['3 项目授权','先确认Sponsor和权限','章程与停止条件有人确认','不越权承诺预算或人事安排'],
 ['4 经营测算','仅做概念性算术训练','向有权财务人员核对口径','教学数字非财务报表'],
 ['5 晋升材料','岗位要求逐条匹配证据','审核人给出具体反馈','空缺与能力分开判断'],
 ['6 90天计划','阶段任务、依赖、验收、风险','30/60/90天滚动复盘','90天不是法定晋升时间表']]
s=tab('岗位对照',['组织/公司','岗位名称','直接团队','业务/职能范围','预算/人事权','考核指标','汇报对象','证据/链接','最大差距'],14)
s.get_range('A2:A4').values=[['目标岗位1'],['目标岗位2'],['目标岗位3']]
s=tab('成果证据',['项目与时间','业务问题','指标与基线','我的授权/角色','关键动作','团队贡献','结果与时间窗','混杂因素/代价','合法证据','审核反馈'],16)
s=tab('项目授权',['试点名称','授权人/Sponsor','目标与验收','范围及不做项','预算与权限上限','风险触发信号','截止/检查日期','验收与复盘'],14)
s=tab('经营测算',['指标（虚构演示）','人民币金额','口径/解释'],15)
s.get_range('A2:C11').values=[
 ['确认收入（教学）',1000000,'用户填写，非GMV/合同额'],
 ['直接成本（教学）',600000,'计入直接交付相关成本'],
 ['毛利（教学）',None,'公式=确认收入-直接成本'],
 ['毛利率（教学）',None,'仅除法演示，收入为0则显示0'],
 ['期间费用（教学）',300000,'具体费用按财务确认'],
 ['简化利润（教学）',None,'不含税费与其他收支'],
 ['当期实际收款（教学）',500000,'收款时点独立于收入确认'],
 ['当期实际现金支出（教学）',900000,'用于简单现金变化估算'],
 ['简化净现金变化（教学）',None,'不等于标准现金流量表'],
 ['风险说明',None,'本表是虚构教学示例，不应对外作为业绩']]
s.get_range('B4').formulas=[['=B2-B3']]
s.get_range('B5').formulas=[['=IF(B2=0,0,B4/B2)']]
s.get_range('B7').formulas=[['=B4-B6']]
s.get_range('B10').formulas=[['=B8-B9']]
s.get_range('B2:B11').format.column_width=20
s.get_range('C1:C11').format.column_width=42
s.get_range('B5').format.number_format='0.0%'
s.get_range('A12:C12').values=[['注意','不要把订单金额、收入、利润、现金混用','公司真实数字只在获批的内部系统处理']]
s=tab('晋升材料',['目标岗位要求','已达到的事实','真实结果与时间窗','本人权限','证据材料','还缺的能力','组织有无岗位','审核反馈','下一次复盘'],16)
s=tab('90天计划',['阶段','责任目标','具体动作','授权人与协作人','资源与停止条件','需要的证据','完成状态','复盘日期'],14)
s.get_range('A2:A5').values=[['第1—15天'],['第16—30天'],['第31—60天'],['第61—90天']]
s.get_range('G2:G5').values=[['未开始'],['未开始'],['未开始'],['未开始']]
s.get_range('G2:G14').data_validation={'rule':{'type':'list','values':['未开始','进行中','已完成','受阻','停止']}}
out=ROOT/'templates/普通人成为高管_完整实操工作簿.xlsx'
SpreadsheetFile.export_xlsx(w).save(str(out))
print(out, out.stat().st_size)
try:
 print('SHEETS',w.inspect({'kind':'sheet','include':'id,name'}).ndjson[:1200])
 print('KEYS',w.inspect({'kind':'table','range':'经营测算!A1:C11','include':'values,formulas','table_max_rows':11,'table_max_cols':3}).ndjson[:2600])
except Exception as e:print('Nonfatal inspect:',str(e)[:250])
