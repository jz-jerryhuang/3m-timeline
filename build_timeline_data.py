import json, os, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(".")
PHOTO_DIR = BASE_DIR / "3M 聚會照片"

EVENTS = [
    {
        "id": "2015-10-18",
        "date": "2015-10-18",
        "year": "2015",
        "title": "3M 讀書會創立：啟程",
        "category": "週年里程碑",
        "speakers": ["3M 創始成員"],
        "summary": "2015 年 10 月 18 日，3M (Mission Marvel) 讀書會正式啟航！凝聚跨界夥伴，開啟長達十一載的思辨、科技研討與終身學習之旅。",
        "photo_folders": ["FWD_2015"]
    },
    {
        "id": "2016-04-20",
        "date": "2016-04-20",
        "year": "2016",
        "title": "FB Training（Facebook 廣告投放與社群實戰）",
        "category": "數位行銷",
        "speakers": ["3M 全員"],
        "summary": "深入探討 Facebook 廣告投放邏輯、精準受眾標籤、流量轉換漏斗與社群實務操作技巧，記錄初創時期的熱血交流。",
        "photo_folders": ["FB training_2016-04-20"]
    },
    {
        "id": "2018-04-28",
        "date": "2018-04-28",
        "year": "2018",
        "title": "3M 春酒聚餐：春日重聚",
        "category": "聚會紀實",
        "speakers": ["3M 全員"],
        "summary": "春暖花開之際的線下聚餐，分享各自年度目標與生活近況，歡聲笑語定格最真摯的夥伴情誼。",
        "photo_folders": ["3M 春酒_2018-04-28"]
    },
    {
        "id": "2018-05-26",
        "date": "2018-05-26",
        "year": "2018",
        "title": "新零售（零售 4.0 與顧客旅程體驗）",
        "category": "商業零售",
        "speakers": ["Jerry", "Vickie", "Aegon"],
        "summary": "探討線上與線下接觸點、五感體驗與消費者五階段旅程（發現、了解、購買、使用、分享），洞察全通路新零售演進。",
        "photo_folders": ["New retail_2018-5-26"]
    },
    {
        "id": "2018-06-23",
        "date": "2018-06-23",
        "year": "2018",
        "title": "人工智慧 (AI) 浪潮與商業應用",
        "category": "科技趨勢",
        "speakers": ["Jerry", "Aegon", "Vickie"],
        "summary": "剖析機器學習演算法、電腦視覺與商業落地挑戰，早在 2018 便精準前瞻 AI 對產業結構的重塑。",
        "photo_folders": ["AI_2018-6-23"]
    },
    {
        "id": "2018-07-28",
        "date": "2018-07-28",
        "year": "2018",
        "title": "區塊鏈與海耶克的貨幣非國家化",
        "category": "Web3 / 金融",
        "speakers": ["Jerry"],
        "summary": "分散式帳本技術、加密貨幣哲學與自由金融體系探討，重溫奧地利學派海耶克的經典思想。",
        "photo_folders": ["Blockchain_2018-7-28"]
    },
    {
        "id": "2018-12-15",
        "date": "2018-12-15",
        "year": "2018",
        "title": "量子運算與量子力學入門",
        "category": "前瞻科技",
        "speakers": ["Jerry"],
        "summary": "量子疊加、量子糾纏與量子霸權對現代密碼學的衝擊，跨越物理與資訊科學邊界的硬核探究。",
        "photo_folders": ["Quantum Computing_2018-12-15"]
    },
    {
        "id": "2019-07-27",
        "date": "2019-07-27",
        "year": "2019",
        "title": "無條件基本收入 (UBI, Universal Basic Income)",
        "category": "社會經濟",
        "speakers": ["Vickie"],
        "summary": "面對自動化與 AI 時代的社會保障創新，探討全球各國 UBI 經濟實驗與公平分配的深層社會契約。",
        "photo_folders": ["UBI_2019-07-27"]
    },
    {
        "id": "2020-04-26",
        "date": "2020-04-26",
        "year": "2020",
        "title": "COVID-19 疫情衝擊下的全球新常態",
        "category": "全球趨勢",
        "speakers": ["Jerry", "Jay", "Una", "Vickie", "Howard", "Paul"],
        "summary": "全方位剖析新飲食型態、供應鏈重組、遠距工作催化、社群經營與旅遊健康趨勢，記錄人類歷史分水嶺。",
        "photo_folders": [],
        "extra_image_dirs": ["4-26-2020 (COVID-19)/新冠肺炎下的新飲食型態 (Jerry)  04-26-2020"]
    },
    {
        "id": "2020-05-23",
        "date": "2020-05-23",
        "year": "2020",
        "title": "國際情勢與新冠疫苗開發進展",
        "category": "生醫與總經",
        "speakers": ["Jerry"],
        "summary": "mRNA 疫苗機制、臨床試驗速度競賽與後疫情地緣政治佈局深度研討。",
        "photo_folders": [],
        "extra_image_dirs": ["國際情勢-新冠疫苗開發 (Jerry) 5-23-2020 v2"]
    },
    {
        "id": "2021-07-31",
        "date": "2021-07-31",
        "year": "2021",
        "title": "小樹屋實體聚會：久違的溫度",
        "category": "聚會紀實",
        "speakers": ["3M 全員"],
        "summary": "疫情漸緩後的線下深度交流重聚，記錄在小樹屋裡熱烈分享的珍貴身影。",
        "photo_folders": ["小樹屋聚會_2021-7-31"]
    },
    {
        "id": "2022-05-08",
        "date": "2022-05-08",
        "year": "2022",
        "title": "小樹屋春季交流",
        "category": "聚會紀實",
        "speakers": ["3M 全員"],
        "summary": "年度主題討論與線下近況交流，持續維繫多年溫暖的知性情誼。",
        "photo_folders": ["小樹屋聚會_2022-5-8"]
    },
    {
        "id": "2023-04-23",
        "date": "2023-04-23",
        "year": "2023",
        "title": "ChatGPT 與生成式 AI 實踐",
        "category": "科技趨勢",
        "speakers": ["彥伶"],
        "summary": "Prompt Engineering、大語言模型工作流改造與生成式 AI 工具實戰應用分享。",
        "photo_folders": ["彥伶 ChatGPT 交流_2023-4-23"]
    },
    {
        "id": "2024-10-19",
        "date": "2024-10-19",
        "year": "2024",
        "title": "個人與家庭財務規劃",
        "category": "資產配置",
        "speakers": ["劉耀元學長"],
        "summary": "資產配置策略、抗通膨現金流規劃與長期財富藍圖，跨世代財務智囊深度對話。",
        "photo_folders": ["財務規劃 feat.劉耀元學長_2024-10-19"]
    },
    {
        "id": "2025-08-16",
        "date": "2025-08-16",
        "year": "2025",
        "title": "川普新關稅政策對全球與金融支付的影響",
        "category": "全球趨勢",
        "speakers": ["Jerry"],
        "summary": "關稅重啟對全球供應鏈重構、跨境支付結算系統與美元霸權秩序的深層衝擊分析。",
        "photo_folders": ["川普關稅對全球影響_2025-08-16"]
    },
    {
        "id": "2026-06-28",
        "date": "2026-06-28",
        "year": "2026",
        "title": "AI Agent 應用實踐與自主代理人架構分享",
        "category": "科技趨勢",
        "speakers": ["Jerry"],
        "summary": "探討自主 AI Agent 工作流、多代理人協作機制與大語言模型落地實務，引領最新前瞻應用體驗。",
        "photo_folders": ["2026-06-28_AI agent sharing"]
    },
    {
        "id": "2026-07-05",
        "date": "2026-07-05",
        "year": "2026",
        "title": "平台和生態系競爭策略個案專題",
        "category": "策略管理",
        "speakers": ["劉耀元學長", "Jerry"],
        "summary": "深度剖析 Tesla vs. Uber、Netflix vs. 百視達、Chrome vs. IE、柯達等生態系顛覆賽局與平台飛輪效應。",
        "photo_folders": ["2026-07-05_平台生態系講座"]
    },
    {
        "id": "2026-10-18",
        "date": "2026-10-18",
        "year": "2026",
        "title": "3M 讀書會 11 週年慶：十一載思辨，敬未來",
        "category": "週年盛典",
        "speakers": ["3M 全體成員"],
        "summary": "2015-2026 十一周年里程碑！回顧思維演進，珍藏每一刻同行的記憶，展望下一個十年！",
        "photo_folders": []
    }
]

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

for item in EVENTS:
    media_list = []
    
    # 掃描 3M 聚會照片
    for p_sub in item.get("photo_folders", []):
        target_dir = PHOTO_DIR / p_sub
        if target_dir.exists():
            for f in sorted(target_dir.iterdir()):
                if f.suffix.lower() in IMAGE_EXTS:
                    is_gif = f.suffix.lower() == ".gif"
                    media_list.append({
                        "url": f"3M 聚會照片/{p_sub}/{f.name}",
                        "type": "gif" if is_gif else "image",
                        "name": f.name
                    })

    # 掃描額外投影片影像
    for extra_dir in item.get("extra_image_dirs", []):
        target_dir = Path(extra_dir)
        if target_dir.exists():
            for f in sorted(target_dir.iterdir()):
                if f.suffix.lower() in IMAGE_EXTS:
                    is_gif = f.suffix.lower() == ".gif"
                    media_list.append({
                        "url": f"{extra_dir}/{f.name}".replace("\\", "/"),
                        "type": "gif" if is_gif else "image",
                        "name": f.name
                    })

    item["media"] = media_list
    item["photos"] = [m["url"] for m in media_list]  # 兼容舊屬性

# 寫入 timeline_data.json
with open("timeline_data.json", "w", encoding="utf-8") as f:
    json.dump(EVENTS, f, ensure_ascii=False, indent=2)

# 寫入 timeline_data.js，供前端直接全域載入，徹底免除快取與 fetch 失敗問題
js_content = "window.TIMELINE_DATA = " + json.dumps(EVENTS, ensure_ascii=False, indent=2) + ";\n"
with open("timeline_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

total_media = sum(len(e["media"]) for e in EVENTS)
total_gifs = sum(sum(1 for m in e["media"] if m["type"] == "gif") for e in EVENTS)
print(f"✅ timeline_data.json 與 timeline_data.js 已同步生成！共 {len(EVENTS)} 個節點，{total_media} 個視覺媒體（含 {total_gifs} 個 GIF）。包含 2015、2016 年前起跑節點。")
