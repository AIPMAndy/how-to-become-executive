# 如何发布到 GitHub（不覆盖任何现有项目）

建议独立仓库：`AIPMAndy/how-to-become-executive`。只有仓库主人实际创建并提交后，此链接才存在。

## 创建新公开仓库

1. 打开 https://github.com/new 。
2. Owner选择 `AIPMAndy`，Repository name填写 `how-to-become-executive`，Visibility为Public。
3. 不勾选初始化README、License、.gitignore，本项目已提供。
4. 创建仓库。解压本项目ZIP，在解压目录内执行：

```bash
git init -b main
git add .
git commit -m "feat: launch executive career handbook"
git remote add origin https://github.com/AIPMAndy/how-to-become-executive.git
git push -u origin main
```

需要本地git用户身份与有效GitHub登录；不要把任何访问令牌写进仓库。使用`gh`也可以创建：`gh repo create AIPMAndy/how-to-become-executive --public --source=. --remote=origin --push`。

## 启用 GitHub Pages

仓库 Settings → Pages → Deploy from a branch → `main` / `/(root)` → Save。

**预计而未验证的地址：**`https://aipmandy.github.io/how-to-become-executive/`。待仓库创建并成功部署后再分享，不能先声称网站已经上线。

## 社交预览、About和Topics

- About：`普通人成为高管保姆级指南｜7阶段84项行动，从业务骨干到项目Owner、团队经理与业务负责人，附实操模板与免费互动工具。`
- Topics：`career-growth`, `leadership`, `management`, `career-guide`, `job-promotion`, `executive`, `open-source`, `chinese`。
- Social preview：上传已生成的 `assets/social-preview.png`（1200×630），与 README 首屏封面一致。
- 成功启用Pages后，将真正网站链接放入仓库About。

## 验收

```bash
python3 -m pip install -r requirements-dev.txt
python3 build.py
python3 -m unittest discover -s tests -v
node tests/math.test.js
```

用手机和Mac分别打开首页，检查七阶段切换、搜索、展开、勾选、刷新保存、8维自评、导出90天计划、模板下载，以及文档链接。主页面完全单文件、无外部CDN；正式浏览器交互需上线后再验收。


## v2发布前检查（2026-10-12）

- 官网首页与 README 均应显示“84项任务、18条研究及法规来源”，并链接10份 `playbooks/` 操作SOP与3条 `tracks/` 行业路线。
- `templates/普通人成为高管_完整实操工作簿.xlsx` 必须包含7个工作表、教学演示数据和可计算的经营模型。
- 执行 `python3 -m pip install -r requirements-dev.txt
python3 build.py`、`python3 -m unittest discover -s tests -v` 和 `node tests/math.test.js`；如有 Playwright/Chromium 可运行 `python3 tests/browser_smoke.py`。
- 进行人工检验：手机打开网站能搜到任务，资料页链接正确，XLSX与CSV可下载，导出计划可读。
- 本项目示例数字与案例均为教学或真实用户合法信息；不要用造假的高管故事当宣传证据。
- 设定 GitHub Pages 的地址只有仓库实际创建、部署成功后才成立。
