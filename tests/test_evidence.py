import unittest, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'data/guide.json').read_text(encoding='utf-8'))
class EvidenceIntegrity(unittest.TestCase):
 def test_14_distinct_cards_grounded_to_source(self):
  evs=D['evidence'];ids=[e['id'] for e in evs];src={s['id']:s for s in D['sources']}
  self.assertEqual(len(evs),14);self.assertEqual(len(ids),len(set(ids)))
  for e in evs:
   with self.subTest(evidence=e['id']):
    self.assertIn(e['source_id'],src)
    for k in ('headline','number','what','type','sample','supports','limits','action','confidence'):
     self.assertGreaterEqual(len(e[k]),3)
    self.assertGreaterEqual(len(e['limits']),15)
    self.assertTrue(src[e['source_id']]['url'].startswith('https://'))
 def test_stage_coverage(self):
  used={e['stage'] for e in D['evidence']}
  self.assertEqual(used,{s['id'] for s in D['stages']})
  for stage in used:self.assertGreaterEqual(sum(x['stage']==stage for x in D['evidence']),1)
 def test_composition_and_original_sources(self):
  core=(ROOT/'README.md').read_text(encoding='utf-8')
  self.assertIn('75%',core)
  self.assertIn('79%',core)
  self.assertIn('335个独立样本',core)
  self.assertIn('180个Google团队',core)
  self.assertIn('观察',core)
  self.assertIn('关联',core) if '关联' in core else self.assertIn('不能推出',core)
  for rel in ('evidence/RESEARCH_ATLAS.html','evidence/CASE_STUDIES.html','evidence/DATA_VISUALIZATIONS.html','audit/EVIDENCE_AUDIT.html'):
   self.assertTrue((ROOT/rel).is_file(),rel)
  idx=(ROOT/'index.html').read_text(encoding='utf-8')
  self.assertIn('id="evidence"',idx)
  for e in D['evidence']:
   self.assertIn(e['id'],(ROOT/'evidence/RESEARCH_ATLAS.md').read_text(encoding='utf-8'))
 def test_evidence_links_in_guides(self):
  for p in list((ROOT/'guides').glob('*.md'))+list((ROOT/'playbooks').glob('*.md'))+list((ROOT/'tracks').glob('*.md')):
   with self.subTest(page=p.name):
    s=p.read_text(encoding='utf-8')
    self.assertIn('先看原始证据',s)
    self.assertIn('不能推断',s)
 def test_two_original_chart_data(self):
  a=(ROOT/'evidence/manager-engagement-2022-2025.svg').read_text()
  b=(ROOT/'evidence/internal-mobility-leadership.svg').read_text()
  for pct in ('31%','30%','27%','22%','20%','19%'):self.assertIn(pct,a)
  self.assertIn('179',b)
  self.assertIn('100',b)
 def test_critical_errors_excluded(self):
  audit=(ROOT/'audit/EVIDENCE_AUDIT.md').read_text(encoding='utf-8')
  for t in ('分母','因果','随机','沃尔玛','GitHub','效度','AI'):self.assertIn(t,audit)
if __name__=='__main__':unittest.main()
