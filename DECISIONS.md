# DECISIONS.md — 重大刻意決策（The Bojin Method 美國站）

> 只記錄**已經明確做出**的重要、刻意的決策與原因。
> **假設／待確認事項不放這裡**（統一在 `PROJECT.md` 第 9 節）。
> 未來 AI 看到這些設計，不要當成 bug 想「修掉」；要改動前先看「重新檢討條件」。
> **更新日期：2026-08-08**

每則格式：**決策 / 原因 / 背景 / 不採用什麼 / 什麼情況重新檢討**

---

## D1. 定位為 Bojin，不等同 Gua Sha
- **決策**：品牌對外一律稱 Bojin／The Bojin Method，不把 Bojin 翻譯或等同成 Gua Sha。
- **原因**：這是定位策略，不是語言方便問題；等同刮痧會被市場攻擊「這不就是刮痧」，失去差異化。
- **背景**：美國消費者較熟 Gua Sha，容易想簡化理解。
- **不採用什麼**：不採用「更強的刮痧／另一種刮痧」的說法。
- **重新檢討**：若市場測試明確顯示「Bojin」一詞造成理解障礙、且有不損定位的替代說法時。

## D2. 合規語言：不用醫療／經絡／TCM
- **決策**：對外內容不描述成治療／診斷／醫療效果，不主動使用 meridian／acupoint／氣血／TCM 等語言。
- **原因**：降低合規與法律風險，避免誤導美國消費者。
- **背景**：台灣原素材大量使用中醫語言，不能直接搬。
- **不採用什麼**：不採用療效式、醫療式宣稱來衝轉換率。
- **重新檢討**：法規或品牌策略明確改變時（需使用者拍板）。

## D3. 核心切入 Facial Tension，而非抗老
- **決策**：品牌問題框架以「臉部長期張力與使用習慣」為核心，可談 aging appearance 但不簡化為「抗老療程」。
- **原因**：建立品牌自己的問題框架，比跟眾人擠「抗老」更有差異化。
- **背景**：客群 50／55+ 美國女性容易把一切歸因於年齡。
- **不採用什麼**：不把品牌定位成「抗老／除皺」產品。
- **重新檢討**：市場驗證顯示此框架無法引起共鳴時。

## D4. 現階段先驗證市場，不做大型技術架構
- **決策**：現階段刻意不做 CRM、複雜 backend、大型 automation；優先原生能力與免費設定。
- **原因**：核心目標是驗證強需求 + 可規模化付費市場，不是技術完整度；避免 overengineering。
- **背景**：過去容易從簡單商業問題一路延伸到 n8n／Database／Backend。
- **不採用什麼**：不採用「為了技術完整而先建系統」。
- **重新檢討**：市場驗證通過、需要規模化時，再評估是否建更重的系統。

## D5. 課程頁 noindex、暫不開賣
- **決策**：`course.html` 設 noindex、不放進主要銷售路徑，課程暫不開賣。
- **原因**：課程還沒到要賣的階段；先驗證市場再決定金流。
- **背景**：課程頁線上曾標示為 demo。
- **不採用什麼**：現階段不急著做課程金流。
- **重新檢討**：確定第一個要賣的正式產品、且要開賣課程時。

## D6. 見證用「教學型」，不用「成效型」
- **決策**：見證呈現成「跟 Yu-Ting 學習」的教學型見證，不偽裝成「自己用了臉變好」的成效型。
- **原因**：現有真實評價本質是「讚老師教學」；用成效型有 FTC 假證言風險。
- **背景**：見證翻自使用者 FB 真實評價（台／港／馬）。
- **不採用什麼**：不採用虛構美式名字、不採用療效式成效宣稱。
- **重新檢討**：日後取得真實「成效型」見證（本人使用前後對比）時。

## D7. Results／證據頁不進主選單
- **決策**：`results.html` 當漏斗中的信任證據頁，不放進主導覽。
- **原因**：讓 landing 保持乾淨只做「留 email」，results 專門說服理性派，分工清楚。
- **背景**：使用者策略文件顯示客群吃證據。
- **不採用什麼**：不把 results 當一般訪客必經的導覽頁。
- **重新檢討**：整體導覽策略調整時。

## D8. 網站走 GitHub Pages 靜態站
- **決策**：網站以純靜態 HTML + GitHub Pages 部署。
- **原因**：免費、簡單、可版控、符合「先輕後重」原則。
- **背景**：repo `melvinlin07-maker/bojin-site`，網域 bojinfacetension.com。
- **不採用什麼**：現階段不採用需要伺服器／後端的動態站。
- **重新檢討**：功能需求超出靜態站能力時（例如需要伺服器端金流／會員）。

## D9. 追蹤碼集中在 nav.js（單一來源）
- **決策**：Meta Pixel、GA4、Lead 事件全部放共用 `nav.js`，不逐頁 inline。
- **原因**：避免其他 Session 重寫 HTML 蓋掉、且新頁自動涵蓋；單一來源好維護。
- **背景**：曾因逐頁 inline 被平行 Session 覆蓋。
- **不採用什麼**：不採用逐頁 inline 追蹤碼。
- **重新檢討**：改用 GTM 或伺服器端追蹤（CAPI）時。

## D10. 英文為絕對預設第一語言，西語採主動點擊切換（且手機端按鈕置於三條橫槓正下方）
- **決策**：全站第一語言永遠為英文（English），預設載入純英文；提供 `🌐 Español` 按鈕供美國西語裔客群主動點擊才切換西語（`es-US` / `es-419`）。手機版語言切換鍵不放進深紫色頂欄（避免擠壓 Logo），統一置於米色畫布區眉標右側（即漢堡選單三條橫槓正下方）。
- **原因**：確保美國主流英語客群進站體驗純粹，同時無縫服務 6,200 萬西語裔市場；手機端頂欄保持極簡高雅。
- **背景**：2026-10-26 全面翻新眼周指南西語字典與手機端排版。
- **不採用什麼**：不採用西語預設、不將語言鈕塞入擁擠的手機深紫頂欄、不使用歐洲本土西語（`vosotros`）或生硬機翻（輔助手一律譯為 `la mano de apoyo`）。
- **重新檢討**：未來獨立拆分西語子網域時。

## D11. 嚴格禁用「觸診／palpation」等醫療診斷詞彙，並啟動 AI 常態主動加碼協議
- **決策**：
  1. 法規紅線：中英西三語絕對禁用「觸診／触诊／palpation／diagnose」，一律使用「10秒自我觀察／輕觸感受／10-Second Touch Check／observación táctil」。
  2. 協作協議：AI 助理在每次回答或執行任務完畢後，必須主動附上 **💡【偵察報告：您沒想到的 1～2 個升級大招】**，主動挖掘高 ROI 盲點與黑科技，打破「不問就不說」的死循環。
- **原因**：遵守台灣衛福部與美國 FTC 非醫療自我保養法規；發揮高階模型最大戰略價值。
- **背景**：2026-10-26 使用者明確拍板定案。

## D12. Systeme.io 名單標籤精細分流架構（廣告名單 vs 自然指南 vs 付費買家）
- **決策**：全站名單採取精細分流（Option A），清楚切割廣告受眾與自然內容讀者，並建立買家與挽回閉環：
  1. **廣告測試名單（Paid Ads Lead）**：標籤 `Eye Reset`。專門承接 Meta/FB 付費廣告落地頁（`facial-tension-check`），累積廣告驗證數據。
  2. **自然內容指南名單（Organic Content Lead）**：標籤 `Guide - Eye Area`。專門承接官網長文、眼周三區教學（`eye-area-guides.html`）、指南頁（`guide.html`）等自然流量留名單表單（`embedded/42586344` 與 `46448045`）。
  3. **付費尊榮學員（Customers）**：標籤 `Customer - Eye Course`。凡在結帳頁（`https://go.bojinfacetension.com/order`）完成 US$79 購買（含 US$29 錄影反饋加購）者，系統自動貼標。
  4. **未結帳挽回流程（Abandoned Cart Workflow）**：進入結帳頁填寫 Email 但 1 小時內未購者自動觸發追蹤挽回信（精準排除已擁有 `Customer - Eye Course` 者）。
- **原因**：徹底解決過去免費版因標籤上限導致自然指南名單漏接問題；清楚區分廣告受眾與自然內容讀者之轉換率差異。
- **背景**：2026-11-09 使用者拍板採精細分流（方案 A）。
- **不採用什麼**：不採用單一標籤混雜廣告與自然讀者；不對付費學員誤寄未付款挽回信。
- **重新檢討**：未來推出第 2 門全新部位課程（如臉部/肩頸）需要新增產品線買家標籤時。


## D13. Systeme.io 完整閉環行銷與售後體驗（A5多幣別、24小時最後通牒挽回、購後14天關懷B1-B7、網域DKIM簽章）
- **決策**：
  1. **A5 培育信多幣別提示**：在 Email A5 (What's inside the  course) 加入海外非美金自動換算小貼士 (Orders outside the US: Your bank or PayPal will automatically convert from CAD, GBP, EUR, or AUD at live daily rates with zero added markup.)，消除加拿大、英國、歐洲與澳洲潛在客群的幣別心理門檻。
  2. **第 2 封 24 小時挽回信**：在購物車挽回工作流程（Workflow 572343）第 1 封信後加入 23 小時延遲與購買判斷節點（條件：標籤 Customer - Eye Course），對未結帳者自動寄出第 2 封 2 小時急迫感最後通牒信（Final notice: Your  founder access expires in 2 hours），若已結帳則自動終止。
  3. **購後 14 天學員陪跑序列（B1-B7）**：建立專屬序列 Eye Method - Post-Purchase Journey (B1-B7)（Campaign ID 1230295），包含 B1～B7 共 7 封精心撰寫之學員啟動、手法避坑、頻率建議與拍照對比關懷信，並在結帳漏斗步驟（Order Form）綁定 New sale 自動訂閱此序列（同時自動退訂 A1-A7 培育序列）。
  4. **網域 DKIM/SPF 官方簽章核驗**：系統檢查確認 ojinfacetension.com 官方 DKIM/DMARC 金鑰已於 Systeme.io 完成全面驗證（狀態：Verified，包含 inbound.systeme.io、key1.systeme.io、key2.systeme.io），確保發信到達率最高維持在 98% 頂級水準。
- **理由**：實現 100% 完整無縫的客戶生命週期閉環（獲客名單 -> 7天信任培育 -> 購物車放棄挽回 -> 結帳後14天高黏著度學員陪跑與防退款關懷），最大化轉換率與學員滿意度。
- **日期**：2026-11-10 完成全流程部署與線上核驗。

## D14. 售後轉介推薦碼（B7 Email）與課程內部補票升級通道（Lesson 1）
- **決策**：
  1. **購後第 7 天推薦轉介閉環（B7 Referral Loop）**：在學員序列第 7 封拍照對比信 Email B7（Take your second photo this week）結尾加入私密 VIP 推薦碼引導 👉 [Gift a Friend: Private  Off Access](https://go.bojinfacetension.com/bojin-eye-method)，讓對比有感的學員轉發給姊妹或親友，零廣告費實現口碑裂變。
  2. **學員後台  個人影片點評補票通道（Portal Review Pass）**：在學員課程第一課 Module 1（page/44901658）影片正上方放置香檳金虛線邊框的升級卡片 🎥 Didn't add Master Lan's Personal Video Review at checkout? Unlock Video Review () →，直接承接結帳未加購但實操產生不確定感的學員，創造持續的高毛利二次變現。
- **理由**：利用學員照鏡子有感與實操遇到問題的黃金時刻，以零廣告成本實現自然客帶客與二次加購升級。
- **日期**：2026-11-10 部署並完成即時線上截圖驗證。

## D15. 推薦優惠券 GIFT20 正式生效與結帳頁即時折抵  驗證
- **決策**：
  1. 在 Systeme.io 優惠券後台（dashboard/coupons）正式建立固定折抵  USD 的官方優惠代碼 GIFT20（名稱：GIFT20 -  Off Student Referral Gift，無限次使用、無過期日）。
  2. 將 GIFT20 正式關聯至結帳漏斗步驟（EYE-SALES -> Order Form）。
  3. 線上實地測試：於 https://go.bojinfacetension.com/order 之 #coupon-67362d0c 輸入 GIFT20 點擊 Apply，系統即時扣減 ，實付金額由 .00 降為 .00 USD，並顯示綠色成功提示。
  4. 同步更新 Email B7 文案，明示優惠代碼：Use private code: GIFT20 at checkout for  off (brings lifetime access to ).
- **理由**：確保學員推薦好友時，好友能真正於結帳頁輸入代碼享受  實質折抵，落實轉介承諾，杜絕代碼失效或客訴風險。
- **日期**：2026-11-10 部署並完成線上結帳實測截圖。

## D16. 全流程漏洞修復、Module 9履約指引、B8轉介延期與全臉大課定價定案
- **決策**：
  1. **結帳頁回歸原生乾淨計算**：移除結帳頁（order）的手寫動態總價框與 15 分鐘倒數計時器，避免與優惠券折抵邏輯衝突；經實測原生購物車套用 GIFT20 正確折抵 -.00，實付 .00 USD，版面零衝突。
  2. **課程第一課純粹化與 Module 9 履約補齊**：
     - 移除第一課（Module 1）頂部連回結帳頁之按鈕（避免已購老學員點擊後被迫重新勾選  主商品）。
     - 於 Module 9 完整配置影片上傳指引：拍 60 秒影片、信中告知最卡步驟（1~5步）、寄至 hello@bojinfacetension.com 於 3 工作天內回覆；未加購者亦可寫信單獨獲取  專屬補票通道。
  3. **購物車挽回信真誠關懷化**：修改工作流程 572343 第 2 封挽回信，剔除「最後 2 小時名額釋出」之假稀缺，改為真誠的技術/支付問題客服關懷。
  4. **A1 信件雙向兼容與團隊署名**：第一封信同時提供 1:18 影片與 PDF 自測清單下載（雙向餵飽廣告與長文兩種名單），移除 Day 0 推銷，統一署名 The Bojin Method。
  5. **轉介優惠碼延至過退款期發送（新增 B8 信件）**：B7 恢復純粹的第 7 天拍照與退款保障提醒；新增第 18 天（B7 後 11 天）信件 B8（A private gift for a sister or friend）發送 GIFT20 親友轉介碼，徹底杜絕 14 天退款期內退差價之風險。
  6. **全臉主力大課定價與分期原則定案**：
     - 主力大課（全臉＋頭部＋側肩頸）定價為 ** USD**；已購眼周之老學員享  完整抵扣＋ 尊榮津貼，專屬一口價 ** USD**（擊穿  心理門檻）。
     - 不在系統自建 3 期分期（防範看完影片後續期款倒帳），改由結帳頁全面借力 **PayPal 原生 Pay in 4**（買家分 4 期免息輕鬆付，PayPal 於成交首日將 100% 全額撥款予賣家，由 PayPal 自負催收與呆帳風險）。
- **理由**：清除所有體驗斷點與矛盾、杜絕退款套利、守護品牌誠信與大師專業形象，建立高轉化、零呆帳之健康長青商業系統。
- **日期**：2026-11-10 部署並完成線上即時截圖驗證。

## D17. 結帳頁跨國刷卡安心提示與 Email B8 雙向互惠推薦（Give $20, Get $20）
- **決策**：
  1. **結帳頁跨國銀行匯率放心提示**：在結帳頁（`go.bojinfacetension.com/order`）PayPal／付款按鍵正下方（`.bojin-after`），加入優雅極簡的安心提示：`🔒 Most major US and international cards process seamlessly at live daily interbank rates.`，打消加拿大、英國、澳洲、歐盟等海外客戶對匯率與手續費的心理卡點。
  2. **Email B8 升級「雙向互惠轉介」（Give $20, Get $20）**：在購後第 18 天發送的 Email B8 中，將原先單向「送朋友 $20 折扣」升級為雙向互惠：「當朋友使用 `GIFT20` 成功購課後，回信告知朋友名字，老學員帳戶立即存入 $20 美金忠誠折抵金，可直接用於未來購買《全臉與頭部旗艦大課》」。
- **理由**：以零現金補貼方式實現高轉化口碑裂變，並把推薦人牢牢鎖定在未來大課升級軌道。
- **日期**：2026-11-10 部署並完成線上實機截圖驗證。

## D18. Gmail 客服回信三大彩色標籤與自動分流過濾器（大招二上線）
- **決策**：在接收 `hello@bojinfacetension.com` 回信的主信箱（`melvinlin07@gmail.com`）建立 3 組專屬彩色標籤與對應自動篩選規則，且全面強制勾選「永不移至垃圾郵件」：
  1. **Video Review 審片（橘色）**：過濾寄至 `hello@bojinfacetension.com` 且包含 `"Video Review" OR "Add Video Review" OR "review my clip"` 之來信（並標示為重要）。
  2. **GIFT20 推薦登記（綠色）**：過濾寄至 `hello@bojinfacetension.com` 且包含 `GIFT20 OR "A private gift for a sister or friend" OR "loyalty credit"` 之來信。
  3. **Refund / 售後（紅色）**：過濾寄至 `hello@bojinfacetension.com` 且包含 `refund OR cancel OR dispute OR "money-back" OR "not the right fit" OR "Take your second photo" OR "course login"` 之來信。
- **理由**：A1～A7、B6、B8 與 Module 9 皆大量引導學員回信互動，建立自動化分流後可一秒識別審片、推薦折抵與退款售後優先序，確保零漏信。
- **日期**：2026-11-10 部署並完成 Gmail 後台截圖驗證。

## D19. 真實手機實測抓錯修復：1:18 觀看頁手機排版鎖定與 A1 真實 PDF 網址修正
- **決策**：依據使用者以 `lanyingmin0209@gmail.com` 真實手機測試發現之三項問題，立即完成全域修復：
  1. **1:18 觀看頁（`page/41476930` / `thank-you-6a5874551795c`）**：刪除舊版過時且撐寬手機畫面的亮藍按鈕（`YES — I'd Like Early Access`、`I Have Questions First`）與不合規舊免責文字；換上與品牌一致的深酒紅＋香檳金雙軌按鈕、頂部呼吸留白、去促銷匣提詞卡，並在手機 390×844 實測驗證 `scrollWidth === innerWidth`（零左右溢出晃動）。
  2. **修復 A1 與觀看頁 PDF 死鏈（404 -> 200）**：將錯誤的 `-checklist.pdf` 連結全數修正為網站實存之英文正式 PDF 網址 `https://bojinfacetension.com/downloads/is-it-aging-or-tension-en.pdf`（HTTP 200, 423,945 bytes）。
  3. **改善 A1 進主要收件匣機率**：拿掉 A1 中容易觸發 Gmail 促銷濾鏡的全大寫與手指 emoji 按鈕文字，改為自然口吻超連結，並在觀看頁直接引導學員將信件從「促銷內容」拖進「主要」。
- **日期**：2026-11-10 部署並完成手機實機與後台截圖驗證。

## D20. 銷售頁（bojin-eye-method v5）手機版超框修復與 PayPal 結帳說明誠實對齊
- **決策**：依據手機真實瀏覽測試發現之排版與金流文字細節，將銷售頁（`page/45013727`）升級部署至 `perfect_full_rawhtml_v5.html`：
  1. **長 Email 與手機寬度鎖定**：加入全域 `overflow-wrap: anywhere` 與 `overflow-x: hidden`，確保 14 天保證卡片內的 `hello@bojinfacetension.com` 乖乖折行於白色卡片內（`297.60 <= 352.80`），390px 手機達成 `390/390` 零水平捲動。
  2. **黃金懸浮 CTA 適配手機**：修正 `#sticky-course-cta` 與 `#sticky-btn-link` 在 `<=520px` 手機螢幕下的寬度與圓角邊距，兩端不再貼邊被裁切。
  3. **誠實對齊 PayPal 實際結帳行為**：將第 2 步說明由 `(No PayPal required)` 改為 `Pay via PayPal or eligible Debit/Credit Card`，同時確認 PayPal 商業設定後台之「非 PayPal 用戶結帳（PayPal Account Optional）」已為開啟狀態。
- **日期**：2026-11-10 部署並完成 390×844 實機渲染截圖驗證。

## D21. 全站 17 封自動化信件（A1-A7、B1-B8、WF1-WF2）個人化變數總體檢與統一修復
- **決策**：經完整稽核全站 17 封發信內容後，徹底消除 `{{contact.first_name}}` 無效變數與免填姓名表單造成之空白問候（`Hi ,`）：
  1. **A1～A7（Campaign 1230273）與購物車挽回信 WF1～WF2（Workflow 572343）**：因免費領取頁（`facial-tension-check`）與棄車訪客未必已填寫姓名，9 封信開頭全面改為自然親切的 **`Hi there,`**，並確保所有連結與 `is-it-aging-or-tension-en.pdf` 保持有效。
  2. **B1～B8（Campaign 1230295）**：修正 B7 與 B8 誤植的 `{{contact.first_name}}` 為 Systeme.io 正確單括號語法 **`Hi {first_name},`**（結帳頁有收集 `First name`），並順手修正 B1 之文法筆誤 `an rounded stick` -> `a rounded stick`（保留 Amazon 官方短網址 `link.amazon/B04ssby3t`）。
  3. **PayPal 台灣境內實測結論**：經實機驗證「非 PayPal 用戶結帳（PayPal Account Optional）」已於 PayPal 商業設定（`於 / On`）正常生效並可彈出直接刷卡欄；台灣買家受限於 PayPal 台灣雙邊交易限制無法付予台灣商家，但美國與跨國買家完全暢通。
- **日期**：2026-11-10 全數修復並經 API 全量重檢通過。

## D22. Email A1 瘦身降促銷分數、結帳姓名必填查核與一次性 $0 測試碼（TESTFREE1）就位
- **決策**：
  1. **Email A1 瘦身去敏優化**：將主旨更新為更像私人來信之 **`Here is your 1:18 Above-the-Brow clip`**，移除信內容易觸發 Gmail 促銷匣之 `free`、`PDF`、`Promotions`、`Spam` 字眼，只保留 1 條乾淨的觀看頁超連結（PDF 指南與拖進主要分頁提醒已置於觀看頁 `thank-you-6a5874551795c`），並同步更新觀看頁引用之信件主旨。
  2. **結帳頁 First name 必填核驗**：查證 `page/44335672` 結帳表單之 `First name` 欄位在 Systeme.io 編輯器與即時 SSR 結構中已設為 `"optional": false`（即必填），確保 B1～B8 學員稱呼 `{first_name}` 正常顯示名字，並同時將 `Last name` 改為 `"optional": true`（選填），減少手機打字摩擦力。
  3. **建立一次性 $0 全流程測試券 `TESTFREE1`**：移除 `TESTUSD1`，改建 `Percentage: 100%`（實付 `USD $0.00`）、限用 `1` 次之 `TESTFREE1` 並掛載於結帳步驟，讓台灣端測試可直接繞過台灣 PayPal 境內限制，完整驗收開課與退訂流程（驗收後刪除）。
- **日期**：2026-11-10 部署並完成實機截圖驗證。

## D23. 端到端完整閉環實戰驗收通過（`lanyingmin0209+test3@gmail.com`）與正式封關
- **決策**：完成免費領取 ➔ 觀看頁 ➔ 銷售頁 ➔ 結帳購買（`TESTFREE1`）➔ 自動開課 ➔ 標籤/序列切換之全鏈路真人實測驗收，並清除一次性測試碼：
  1. **Email A1 雙連結恢復**：確認移除 PDF 連結並不影響 Gmail 促銷分類，故將確定可用之 `https://bojinfacetension.com/downloads/is-it-aging-or-tension-en.pdf` 補回 Email A1（搭配 `Here is your 1:18 Above-the-Brow clip` 與 `Hi there,`）。
  2. **完整自動交付實測通過（Contact ID `452937676`）**：
     - 免費報名即貼標 `Eye Reset` 並寄出 A1；
     - 結帳購買後即自動跳轉感謝頁 `go.bojinfacetension.com/85f43e55`；
     - 自動補貼 `Customer - Eye Course`、開通 `The Bojin Eye Method`（Active / Full access）、**自動退訂 `A1-A7`**、**自動訂閱並寄出 `B1`**（正確顯示 `Hi lan,`）；
     - 系統開課密碼信（`Important: Your access to training`）100% 穩穩抵達 Gmail **主要（Primary）收件匣**。
  3. **正式封關清理**：確認 `TESTFREE1` 使用次數達 `1/1` 後即刻自後台刪除，線上僅保留 `GIFT20`（$20 推薦折抵）與歷史已用盡之 `BOJIN-QA-ZERO-7F42C9`。
- **日期**：2026-11-10 全閉環實測通過並完成封關。

## D24. 購後 B1 延遲 30 分鐘寄出（錯開密碼信）與常駐學員測試帳號紀錄
- **決策**：
  1. **Email B1（`You're in. Two things to do first`）延遲 30 分鐘寄出**：依據真人實測經驗，將 Campaign `1230295` 步驟 1（`6272927`）由 `0 minutes` 調整為 **`30 minutes`**（全時段、全星期不限制寄送），讓新學員在買完課的前 30 分鐘只收到唯一一封「設定密碼開課信」（`Important: Your access to training`），徹底消除與 `B1` 同時到達造成誤點鎖頭畫面的混淆；B2～B8 維持原定間隔不變且全數 Active。
  2. **常駐學員端體驗與客服排查專用帳號紀錄**：
     - 學員教室入口：`https://melvinlin07.systeme.io/school/course/the-bojin-eye-method`
     - 測試學員信箱：`lanyingmin0209+test3@gmail.com`（具備 `The Bojin Eye Method` Full access 永久看課權限，所有通知信寄達 `lanyingmin0209@gmail.com`；依 `CLAUDE.md` 資安規則，密碼由使用者私人備忘錄保管、不寫入 Git 公開 MD 檔，忘記隨時可用登入頁 Forgot password 重設）。
- **日期**：2026-11-10 部署並完成後台截圖驗證。

## D25. B1 信件補入「學員後台書籤 P.P.S.」＋主官網 `nav.js` 頁尾 `Student Login` 就位
- **決策**：
  1. **Systeme.io Email B1（`6272927`）加上書籤備忘 P.P.S.**：於原 `P.S.`（回信提問）下方新增一行 `P.P.S. Coming back for Lesson 2 in a few days? Bookmark your Student Portal for easy 1-click access anytime: Open Student Portal`，超連結直達 `https://melvinlin07.systeme.io/school/course/the-bojin-eye-method`；已存檔並重整實測確認維持 `Active` 與 `30 minutes` 延遲。
  2. **主官網 `nav.js` 頁尾自動補入學員登入連結**：於 `nav.js`（第 187–209 行）新增腳本，於所有載入 `nav.js` 的靜態頁頁尾 `.foot-legal` 自動附加 `Student Login`（8 個西語 `-es.html` 頁面自動切換為 `Acceso alumnos`）連往 `https://melvinlin07.systeme.io/school/course/the-bojin-eye-method`；已透過無頭 Chrome 實測英文頁與全數 8 個西語頁成功渲染（目前留存本機待使用者確認 `git push` 上線）。
- **日期**：2026-11-10 完成雲端 B1 存檔實測與本機 `nav.js` 渲染驗證。
