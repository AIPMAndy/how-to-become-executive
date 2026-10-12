"""Optional browser smoke test, works even when file:// is blocked by test sandbox."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
R=Path(__file__).resolve().parents[1]
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  page=await b.new_page(viewport={'width':1280,'height':850},accept_downloads=True)
  errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
  await page.set_content((R/'index.html').read_text(encoding='utf-8'),wait_until='load')
  assert await page.locator('.task').count()==84
  await page.locator('#search').fill('预算')
  assert 0<await page.locator('.task').count()<84
  await page.locator('#search').fill('')
  await page.locator('.stage-btn').nth(2).click()
  assert await page.locator('.task').count()==12
  await page.locator('.stage-btn').first.click()
  await page.locator('.task .expand').first.click()
  assert await page.locator('.details:not([hidden])').count()==1
  assert '完成标准' in await page.locator('.details:not([hidden])').inner_text()
  await page.locator('.task input[type=checkbox]').first.check()
  assert await page.locator('#done').inner_text()=='1'
  await page.locator('#current').select_option('manager')
  assert '业务负责人' in await page.locator('#route-result').inner_text() or '经营业务' in await page.locator('#route-result').inner_text()
  await page.locator('#score-rows select').first.select_option('3')
  assert '优先补证据' in await page.locator('#score-result').inner_text()
  await page.locator('#p1').fill('获得业务项目明确授权')
  async with page.expect_download() as fut:
   await page.locator('#export').click()
  assert (await fut.value).suggested_filename=='我的管理成长90天行动.txt'
  mob=await b.new_page(viewport={'width':390,'height':844})
  await mob.set_content((R/'index.html').read_text(encoding='utf-8'),wait_until='load')
  assert await mob.locator('.task').count()==84
  await mob.screenshot(path=str(R.parent/'executive-mobile-preview.png'))
  assert not errs,errs
  print('BROWSER PASS: 84 cards, search, stage, details, check, route, scores, export, mobile, no JS errors')
  await b.close()
asyncio.run(main())
