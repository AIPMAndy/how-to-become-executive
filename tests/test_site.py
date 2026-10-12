import json,re,subprocess,unittest
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/guide.json').read_text(encoding='utf-8'))
class Links(HTMLParser):
    def __init__(self):super().__init__();self.items=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':self.items += [v for k,v in attrs if k=='href' and v]
class SiteTests(unittest.TestCase):
    def test_stages_tasks(self):
        self.assertEqual(len(DATA['stages']),7);self.assertEqual(len(DATA['tasks']),84);self.assertEqual(len(DATA['sources']),32)
        self.assertEqual(len({t['id'] for t in DATA['tasks']}),84)
        self.assertEqual({s['id'] for s in DATA['stages']},{t['stage'] for t in DATA['tasks']})
        self.assertTrue(all(sum(t['stage']==stage['id'] for t in DATA['tasks'])==12 for stage in DATA['stages']))
    def test_action_evidence_block(self):
        refs={s['id'] for s in DATA['sources']}
        for t in DATA['tasks']:
            with self.subTest(task=t['id']):
                self.assertGreaterEqual(len(t['action']),18)
                self.assertGreaterEqual(len(t['steps']),3)
                self.assertGreaterEqual(len(t['gate']),8)
                self.assertGreaterEqual(len(t['proof']),7)
                self.assertGreaterEqual(len(t['blocked']),10)
                self.assertTrue(set(t['sources']).issubset(refs))
    def test_policy_and_scientific_bounds(self):
        self.assertIn('第265条',(ROOT/'README.md').read_text(encoding='utf-8'))
        self.assertIn('因果',(ROOT/'audit/ADVERSARIAL_REVIEW.md').read_text(encoding='utf-8'))
        self.assertIn('不能预测',(ROOT/'REFERENCES.md').read_text(encoding='utf-8'))
        self.assertTrue(all(s['url'].startswith('https://') for s in DATA['sources']))
    def test_build_reproducibility(self):
        before=(ROOT/'index.html').read_bytes();r=subprocess.run(['python3',str(ROOT/'build.py')],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(before,(ROOT/'index.html').read_bytes())
    def test_offline_index(self):
        body=(ROOT/'index.html').read_text(encoding='utf-8')
        for expect in ('id="route"','id="cards"','id="score-rows"','id="export"','84','普通人成为高管'):
            self.assertIn(expect,body)
        self.assertNotIn('<script src=',body)
        self.assertNotIn('<link rel="stylesheet"',body)
    def test_links(self):
        pages=[ROOT/'index.html',*ROOT.glob('guides/*.html'),*ROOT.glob('templates/*.html'),*ROOT.glob('playbooks/*.html'),*ROOT.glob('tracks/*.html'),*ROOT.glob('audit/*.html'),*ROOT.glob('*.html')]
        self.assertGreaterEqual(len(pages),20)
        for page in pages:
            l=Links();l.feed(page.read_text(encoding='utf-8'))
            for href in l.items:
                if href.startswith(('https://','http://','#','mailto:')):continue
                target=(page.parent/unquote(urlsplit(href).path)).resolve()
                with self.subTest(page=page.name,href=href):self.assertTrue(target.is_file(),f'Missing target: {page}: {href}')
    def test_full_playbooks_and_tracks(self):
        self.assertEqual(len(list((ROOT/'playbooks').glob('*.md'))),10)
        self.assertEqual(len(list((ROOT/'tracks').glob('*.md'))),3)
        for f in list((ROOT/'playbooks').glob('*.md')):
            with self.subTest(playbook=f.name):
                self.assertGreaterEqual(len(f.read_text(encoding='utf-8')),450)
                self.assertTrue(f.with_suffix('.html').exists())

    def test_all_careers_have_new_material(self):
        for st in DATA['stages']:
            self.assertEqual(len([t for t in DATA['tasks'] if t['stage']==st['id']]),12)
        audit=(ROOT/'audit/ADVERSARIAL_REVIEW.md').read_text(encoding='utf-8')
        for phrase in ('公司根本没有管理岗位','关联','GMV','90天','隐私','无偿'):
            self.assertIn(phrase,audit)

    def test_workbook_is_readable_zip_and_linked(self):
        from zipfile import ZipFile
        file=ROOT/'templates/普通人成为高管_完整实操工作簿.xlsx'
        self.assertTrue(file.is_file())
        with ZipFile(file) as z:
            self.assertIsNone(z.testzip())
            self.assertIn('xl/workbook.xml',z.namelist())
        self.assertIn('普通人成为高管_完整实操工作簿.xlsx',(ROOT/'index.html').read_text(encoding='utf-8'))

    def test_templates(self):
        files=list((ROOT/'templates').glob('*.md'))+list((ROOT/'templates').glob('*.csv'))
        self.assertEqual(len(files),33)
        self.assertTrue((ROOT/'assets/social-preview.png').exists())
if __name__=='__main__':unittest.main()
