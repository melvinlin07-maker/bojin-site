# PROJECT.md — The Bojin Method（美國站）

> 專案事實與商業脈絡基線。任何新的 AI／新 Session 接手前，先讀本檔 + `CLAUDE.md` + `DECISIONS.md`。
> **更新日期：2026-08-08**
> 建立方式：Phase 1 Evidence Inventory（程式碼盤點）+ Phase 2 Context Interview（訪談使用者）+ Phase 3 Capability Discovery + Phase 4 Synthesis。
>
> **標籤說明**
> - 【Fact】程式碼／系統直接確認的事實
> - 【Decision】使用者的商業脈絡／決策
> - 【Capability】平台原生能力機會（**尚未採用**）
> - 【Experiment】策略驗證實驗（**尚未驗證**）
> - 【Assumption】假設，尚未查證
> - 【To Confirm】待使用者或外部確認
>
> **原則**：已確認事實／商業決策／未驗證事項必須分清楚；本檔不寫任何 secret／token／password。

---

## 1. 專案總覽
- The Bojin Method 美國站：把台灣臉部撥筋，用美國消費者聽得懂、能接受的方式重新包裝，教 **50／55+ 美國女性**在家安全自做臉部放鬆與日常保養。【Decision】
- 核心訊息框架：臉看起來累／緊／沉，不一定只是老化，而是長期**臉部張力與使用習慣**造成。【Decision】
- 正式網站：`https://bojinfacetension.com` 【Fact】

## 2. 商業目標與現況
- **90 天核心目標：驗證「強需求 + 可規模化的付費市場」**——不是「有沒有人付一次錢」，而是持續、成批、跑順後能放大的購買訊號。名單／SEO／廣告／內容／漏斗都是手段，不是目的。【Decision】
- 階段：前端驗證已開始，商業閉環尚未完成。【Decision】
- 漏斗「通」的段：網站／內容／廣告入口／免費誘餌＋Quiz＋Guide／email 收集／systeme＋n8n 承接／已累積真實名單。【Fact】
- 漏斗「斷」的段（**最痛**）：有興趣 → 願意付錢 → 可持續成交——缺一個能收錢的正式 offer。【Decision】

## 3. 技術現況（Evidence）
- **架構**：純靜態站，HTML + 單一 `styles.css` + 單一 `nav.js`，無框架、無建置流程。共 68 個 HTML（50 篇 `blog-*.html` + 18 個功能頁）。【Fact】
- **部署**：GitHub Pages。repo=`melvinlin07-maker/bojin-site`；`CNAME`=`bojinfacetension.com`；有空 `.nojekyll`。另有 `Dockerfile`（nginx:alpine），歷史文件稱為備援部署，是否仍用【To Confirm】。【Fact】
- **追蹤**（全部集中在 `nav.js`，已 grep 確認無 HTML 內嵌）：Meta Pixel `751313064707787`、GA4 `G-2VFEVY9Q1F`、網域防護（只在 `*.bojinfacetension.com` 觸發）、`bojinLead(source)` 函式；GSC 驗證檔存在。【Fact】
- **表單／收信**：4 個表單 POST 到同一 systeme endpoint `embedded/42586344`（`blog.html`×1、`guide.html`×1、`landing-guide.html`×2）；`quiz.html` 走 n8n webhook；付費入口連 `go.bojinfacetension.com`。【Fact】
- **SEO**：`robots.txt`、`llms.txt`；`sitemap.xml` 59 筆；canonical 67／68（缺的 1 = Google 驗證檔，無害）；8 個 noindex 頁與 sitemap 一致。頁數對帳：68 − 1 Google 驗證檔 − 8 noindex = 59 = sitemap，完全對得起來。【Fact】
- **Git**：`main` 乾淨（僅 1 個未追蹤備份圖 `assets/bojin-stick-steel-white-bg-backup.jpg`）；`deslop-blogs` 為落後的舊分支（無獨有 commit）。【Fact】

## 4. 定位與紅線（Context）
- **差異化**：不跟醫美比「多快」，也不當「另一種刮痧」；賣「可自學、能在家長期做的溫和方法」，而非一次性刺激。【Decision】
- **必講**：安全溫和、在家自己做、方法可學不神秘、重點是「理解臉為什麼緊累沉」、不必一開始就侵入式高成本、持續日常自我照顧、源自台灣多年實戰但用美國人懂的方式重講。【Decision】
- **絕對不講**：醫療／治療／診斷；經絡／氣血／TCM；把 Bojin 等同 Gua Sha。【Decision】
- **術語鐵則**：Bojin ≠ Gua Sha；核心概念 = Facial Tension（比「抗老」更核心）；Bojin Stick ≠ gua sha tool；one-side test = 體驗觀察，非醫療證明；既有名稱（Eye Reset 等）不自行改名；免費誘餌／測驗／PDF／影片／付費產品**分層，不可混為一談**。看不懂的既有名詞先查現有頁面／文案／決策紀錄，不自行重命名或用近義詞替換。【Decision】

## 5. System Map（系統地圖）
| 系統 | 用途 |
|---|---|
| GitHub（melvinlin07-maker） | 網站原始碼、版本控制、GitHub Pages 部署 【Fact】 |
| systeme.io | 收 email 名單、表單、漏斗、感謝頁、部分銷售流程 【Fact】 |
| n8n（Zeabur 雲端） | Quiz opt-in、自動化流程、資料轉送 【Fact】 |
| Meta Business Manager | Facebook 廣告、Pixel、事件 【Fact】 |
| GA4 | 網站流量與事件分析 【Fact】 |
| Google Search Console | 搜尋收錄、索引、SEO 狀況 【Fact】 |
| 網域 / DNS 後台 | bojinfacetension.com 的 DNS／網域設定（供應商程式碼查不到，需要時問使用者【To Confirm】） |
| Vimeo | 部分免費／誘餌影片託管 【Fact】 |
| Gmail / Email | 名單、自動化郵件或系統通知（實際寄信可能透過 n8n／systeme）【Fact】 |

- **正式專案資料夾**：`C:\Users\user888\Documents\撥筋美國網站\`（正式碼與 Git repo）。【Fact】
- **素材庫（非 repo）**：`C:\Users\user888\Desktop\撥筋AI\美國撥筋教學\`（影片、廣告、文案素材）。【Fact】
- **憑證位置（只記位置，不記任何秘密值）**：n8n API key 在本機 `.n8n-cli/config.json`；GitHub 憑證在 Windows 認證管理員；systeme／Gmail 等正式 credential 存於 n8n credential 系統。**任何 key／密碼／token 都不寫進本檔或其他 MD。**【Assumption / 歷史紀錄】
- **決策者**：只有使用者一人拍板；目前無固定外部合作人。【Decision】

## 6. Known Risks（已知風險，只記錄不擅自修）
- `.gitignore` 原本忽略所有 `*.md`；`PROJECT.md`/`CLAUDE.md`/`DECISIONS.md` 已用最小例外納入追蹤（見本次修改），其餘 md 仍忽略。【Fact】
- 多個 AI（Claude Code／ChatGPT／Codex…）會同時碰同一套系統與 repo；動正式系統或重要檔案前，先查 git 狀態與現有改動，避免覆蓋別的 AI／Session 的工作。【Decision】
- systeme 三個主站表單共用同一表單 ID `42586344`，後台不易分辨來源（可用 UTM／隱藏欄位補，見第 8 節）。【Fact】
- 誘餌落地頁（landing-guide／landing-video）為孤島頁，無廣告就沒人到得了。【Fact】

## 7. Capability Opportunities（能力機會 — **尚未採用**）
> ⚠️ 以下為「平台原生能力」盤點，**尚未決定要做、尚未實作**。未來 AI 不要當成已定案。
- 【Capability】**systeme.io 原生收款**：內建訂單頁＋金流（Stripe／PayPal）＋一鍵加購，可直接掛付費 offer，不用自建購物車。（需查目前方案額度【To Confirm】）
- 【Capability】**GA4 Explore（漏斗／路徑）+ GSC 查詢報表**：免費看漏斗漏在哪、市場實際搜什麼；資料已在收、尚未使用。
- 【Capability】**Meta 自訂購買事件 + 銷售（Sales）廣告目標**：讓廣告能優化到買家，目前只用到 Lead。
- 【Capability】**URL 參數（UTM）+ 表單隱藏欄位**：讓每筆名單可歸因來源／價格；目前 systeme 端未設。

## 8. Strategic Experiments（策略實驗 — **尚未驗證**）
> ⚠️ 以下為「用既有能力做的驗證方法」，**尚未執行、尚未驗證**。未來 AI 不要當成已定案。
- 【Experiment】**對暖名單發一封真實 offer，測付費意願**：用既有 email 群發能力，最快測「有興趣 → 願意付錢」這一段。需搭配第 7 節的 systeme 收款能力。

## 9. Assumptions / To Confirm（假設與待確認）
- 【Assumption】systeme 免費／目前方案能收款（常識判斷，未查使用者實際方案）。
- 【Assumption】舊紀錄稱 systeme 感謝頁 404 已於 2026-07-15 修好（未重新驗證）。
- 【To Confirm】配色「玫瑰酒紅」是否定案（目前為試用版，commit `b799ac1`）。
- 【To Confirm】`Dockerfile` 是否仍用（歷史文件稱為 nginx 備援）。
- 【To Confirm】`deslop-blogs` 舊分支是否可刪。
- 【To Confirm】網域 DNS 供應商（程式碼查不到）。
- 【To Confirm】**「第一個要賣的正式產品」到底是什麼**（價位／形式）——第 2 節「最痛斷點」指向此，使用者尚未點名具體商品。
