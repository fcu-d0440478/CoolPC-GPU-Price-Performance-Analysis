## **Phase 5 - 數據分析報告**

題目主題：結構型資料的分析案例
專案脈絡：詳見"分析文件撰寫.docx"
主要技術或工具：Python、selenium、sqlite、pandas、sklearn、matplotlib、seaborn

### 📘 一、引言

本次專案以原價屋顯示卡銷售資料為基礎，分析其價格、效能（分數）、以及性價比（CP 值）等指標，探索市場趨勢與產品定位。分析目標包括：

- 探索價格與效能的關聯性
- 發現高性價比顯卡
- 藉由視覺化與描述統計洞察市場動態
- 是否推薦現在購買顯示卡

---

### 🧹 二、數據清理

在資料前處理階段，我們完成以下清理流程：

- **gpus.db 前處理**：去除重複的 GPU 名稱，保留最高分數的記錄（134 個型號）
- **vga.db 處理**（不修改原始資料庫）：
  - 使用 AI 生成的對照表（`3 gpu_mapping_checklist.json`）建立 `pure_chipset` 欄位
  - 從 `gpus.db` 匹配效能分數 `score`（整數型態）
  - 計算 `CP` 欄位（score / price），用以衡量性價比
- **過濾無效資料**：
  - 移除配件、轉接盒、專業繪圖卡等非消費級顯卡
  - 過濾促銷活動產品（贈品、合購、紅包等）
  - 移除 `pure_chipset` 或 `score` 為空值的資料
- **產出乾淨資料庫**：`filtered_df.db`（保持 `vga.db` 原始資料不變）

✅ 最終清理後，共保留 **72,217 筆有效顯卡紀錄**。

---

### 📊 三、探索性數據分析（EDA）

#### 1️⃣ 描述性統計分析：

| 指標  | 平均值  | 中位數  | 標準差  | 最小值 | 最大值   |
| ----- | ------- | ------- | ------- | ------ | -------- |
| 價格  | $20,406 | $14,888 | $16,229 | $2,790 | $128,888 |
| 分數  | 2,913   | 2,405   | 2,266   | 120    | 14,469   |
| CP 值 | 0.146   | 0.149   | 0.052   | 0.003  | 0.854    |

📌 **觀察摘要：**

- 價格分布極度右偏，有部分顯卡極高價
- 分數集中於 1,000 ～ 4,000，CP 值集中於 0.09 ～ 0.18

---

#### 2️⃣ 數據視覺化圖表與分析

![最新Top 10 CP](Image/Top10CP.png)
![跨日顯卡市場趨勢分析：價格與效能](Image/跨日顯卡市場趨勢分析：價格與效能.png)
![時間序列CP值分布圖](Image/時間序列CP值分布圖.png)
![顯卡價格vs分數分布熱點圖](Image/顯卡價格vs分數分布熱點圖.png)
![顯卡價格與分數的KMeans聚類分析](Image/顯卡價格與分數的KMeans聚類分析.png)

---

#### 3️⃣ 時間序列趨勢分析

- 平均價格與平均 CP 值都有上升的趨勢，所以即便顯示卡價格變貴仍有購買的價值

---

### 🔎 四、初步發現與結論

1. **價格與效能關聯性**：顯卡價格與效能具高度正相關（透過散點圖與聚類分析驗證），但部分高階產品存在品牌溢價現象。

2. **高性價比區段**：最佳 CP 值產品集中在 $8,000 ～ $17,000 價格帶，提供效能與價格的最佳平衡點。

3. **Top 10 CP 值顯卡（2025-11-18 最新資料）**：

   - **AMD Radeon RX 9060 XT**：CP 值高達 0.418，價格僅 $8,888，為目前市場最佳選擇
   - **AMD Radeon RX 9070**：CP 值 0.370，價格 $16,990，中高階最佳性價比
   - **Intel Arc B580**：CP 值 0.361，價格 $8,490，Intel 陣營唯一入榜
   - Top 10 中 AMD 佔 9 張，Intel 佔 1 張，NVIDIA 未入榜

4. **市場趨勢洞察**：

   - 平均價格與平均 CP 值都呈現上升趨勢，顯示技術進步帶來更好的性價比
   - 即便顯卡平均價格持續上升，但 CP 值同步提升，**現在是購買顯卡的好時機**
   - 唯一 CP 值快速下降的時間點為 2021 年顯卡礦災時期（挖礦熱潮導致價格暴漲）

5. **品牌競爭格局**：

   - **AMD** 在性價比市場佔據絕對優勢，RX 9060 XT 和 RX 9070 系列表現突出
   - **Intel Arc** 系列（B580）以極具競爭力的價格切入市場，具有潛力
   - **NVIDIA** 高階卡效能領先但價格偏高，CP 值相對較低

6. **購買建議**：
   - **預算 $8,000-$10,000**：優先選擇 AMD RX 9060 XT 或 Intel Arc B580
   - **預算 $15,000-$20,000**：推薦 AMD RX 9070，中高階最佳性價比
   - **追求極致效能**：NVIDIA RTX 5090 系列，但需接受較低的 CP 值

---

### 🚀 五、下一步計畫

- ➕ 進行特賣時間以及比特幣幣值是否會影響顯示卡市場
- 🧠 建立推薦模型：依照預算推薦最佳 CP 值顯卡
- 📈 發展時間序列預測模型（顯卡價格趨勢預測）

---

### 六、專案流程總覽（6 檔案依序執行）

本專案的目標是：**從原價屋（Wayback）歷史頁面取得顯卡商品與價格 ➜ 從 UL Benchmarks 取得顯卡效能分數 ➜ 透過對照表把兩邊資料對齊 ➜ 計算 CP 值（Score / Price）➜ 進一步清理、分析**。以下為檔案執行順序與作用說明：

## 1) `1 wayback_vga_tracker.py`

**用途：**  
批次抓取 WebArchive（Wayback Machine）上原價屋 `evaluate.php` 的每日快照，解析「顯示卡 VGA」欄位，寫入 SQLite `vga.db`。

**重點：**

- 初始化 `vga` 資料表（欄位：`date, chipset, product, price`；以 `(date, chipset, product)` 做唯一約束避免重複）。
- 先查資料庫已有日期，爬取時直接**跳過已存在日期**，避免重覆抓取。
- Selenium（可切成 headless）開頁、定位 `顯示卡VGA` 的 `<optgroup>` 與 `<option>`，解析商品與價格後寫入 DB。

**先跑它，得到：** `vga.db`

**執行範例：**

```bash
python "1 wayback_vga_tracker.py"
```

---

## 2) `2 gpu_scraper_ul.py`

**用途：**  
從 UL Benchmarks「Best GPUs」頁面抓取**顯卡型號與分數**，寫入 SQLite `gpus.db`。

**重點：**

- 初始化 `gpus` 資料表（`id, name, score`）。
- Selenium（可切 headless）抓表格每列的 GPU 名稱與分數後寫入 DB。

**第二步執行，得到：** `gpus.db`

**執行範例：**

```bash
python "2 gpu_scraper_ul.py"
```

---

## 3) `3 gpu_mapping_checklist.json` 與產生工具

**用途：**  
**名稱對照表**（多對一）：把原價屋頁面的「chipset」字串（如：`NVIDIA RTX3060-12G`）對應到 UL 分數表裡的**標準顯卡名稱**（如：`NVIDIA GeForce RTX 3060`）。

**產生方式：**

1. **`3.1 generate_chatgpt_prompt.py`**：產生可直接貼到 ChatGPT 的 prompt 檔案

   ```bash
   python "3.1 generate_chatgpt_prompt.py"
   # 產出 3.1 chatgpt_prompt.txt，複製內容貼到 ChatGPT
   ```

**匹配統計：**

- 總共 124 個 chipset
- 成功匹配約 73 個（59%）
- 未匹配的主要為周邊配件、專業繪圖卡或資料庫中沒有的型號

對不上或不需要的條目設為 `null`（會在後續過濾掉）。

**不用執行，是供下一步程式讀取的設定檔。**

---

## 4) `4 pre_process_data.ipynb`

**用途（資料前處理，建議在 Jupyter 內執行）：**

**重要：此流程不修改 `vga.db` 原始資料，所有處理都在記憶體中完成，最後產出新的 `filtered_df.db`**

**處理流程：**

1. **gpus.db 前處理**：

   - 將 score 轉為整數型態（Int64）
   - 去除重複的 GPU 名稱，保留最高分數的記錄
   - 更新 gpus.db（134 個型號）

2. **載入 GPU mapping**：

   - 讀取 `3 gpu_mapping_checklist.json` 對照表

3. **從 vga.db 讀取並處理**（不修改原始資料庫）：

   - 讀取所有 vga 資料到記憶體（101,558 筆）
   - 新增 `pure_chipset` 欄位（使用 mapping 對照）
   - 新增 `score` 欄位（整數型態，從 gpus.db 對應）
   - 計算 `CP` 值（score / price）

4. **過濾資料**：

   - 排除配件、轉接盒、專業繪圖卡（chipset 關鍵字過濾）
   - 排除促銷活動產品（product 關鍵字過濾：贈品、合購、紅包等）
   - 移除 `pure_chipset` 或 `score` 為空值的資料

5. **儲存到 filtered_df.db**：
   - 按 CP 值降序排序
   - 產出乾淨資料（72,217 筆）

**第四步執行，產出：** `filtered_df.db`（保持 `vga.db` 原始資料不變）

**執行範例：**

```bash
jupyter lab
# 開啟 5 pre_process_data.ipynb 並執行所有 cell
```

---

## 5) `5 data_analyze.ipynb`

**用途（探索性資料分析/視覺化）：**

從 `filtered_df.db` 讀取乾淨資料（72,217 筆），進行完整的 **EDA**：

**分析項目：**

1. **描述性統計分析**：

   - 價格、分數、CP 值的分布統計
   - 平均值、中位數、標準差等指標

2. **CP 值排名分析**：

   - 最新日期的 Top 10 高 CP 值顯卡
   - 最低 CP 值顯卡（識別離群值）
   - 輸出 `Top CP VGA data.csv`

3. **視覺化圖表**：

   - Top 10 CP 值長條圖
   - 價格 vs 分數熱點圖（含密度標註）
   - 時間序列趨勢圖（價格、分數、CP 值）
   - KMeans 聚類分析（4 群，含代表顯卡標註）

4. **時間序列分析**：
   - 跨日平均價格與效能趨勢
   - CP 值變化趨勢
   - 市場動態洞察

**第五步執行，產出：**

- 分析圖表（儲存至 `Image/` 資料夾）
- `Top CP VGA data.csv`（最新日期完整排名）

**執行範例：**

```bash
jupyter lab
# 開啟 6 data_analyze.ipynb 並執行所有 cell
```

---

## 環境需求與小提醒

- **Python 3.10+**（建議）
- **套件**：`selenium`, `requests`, `pandas`, `sqlite3`, `matplotlib`, `numpy`, `seaborn`, `sklearn`（標準庫）
  ```bash
  pip install -r requirements.txt
  ```
- **Chrome / ChromeDriver**：版本需相容；若要無頭模式，記得解除註解 `--headless`。
- **抓取間隔**：視網頁載入速度調整 `time.sleep()`；必要時可加入顯性等待（`WebDriverWait`）。

---

## 一鍵跑完（命令列示意）

```bash
# 1) 取得歷史價格資料
python "1 wayback_vga_tracker.py"

# 2) 取得效能分數
python "2 gpu_scraper_ul.py"

# 3) 產生 GPU mapping 對照表（三選一）
# 方法 A: 使用 ChatGPT
python "3.1 generate_chatgpt_prompt.py"
# 複製 3.1 chatgpt_prompt.txt 內容到 ChatGPT，將回應存為 3 gpu_mapping_checklist.json

# 4) 資料前處理（產出 filtered_df.db）
# 方法 A: 使用 Jupyter Notebook（推薦）
jupyter lab
# 開啟「4 pre_process_data.ipynb」並執行所有 cell

# 5) 探索性資料分析
jupyter lab
# 開啟「5 data_analyze.ipynb」並執行所有 cell
```

**資料庫檔案說明：**

- `vga.db`：原始價格資料（保持不變）
- `gpus.db`：GPU 效能分數（會更新去重）
- `filtered_df.db`：乾淨的分析資料（由步驟 4 產生）
