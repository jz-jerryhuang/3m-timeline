# -*- coding: utf-8 -*-
import json
import sys

def main():
    json_path = 'timeline_data.json'
    js_path = 'timeline_data.js'

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    event_map = {e.get('date'): e for e in data['events']}

    # 1. Update 2026-06-28
    if '2026-06-28' in event_map:
        e1 = event_map['2026-06-28']
        e1['title'] = "AI Agent 應用實踐與自主代理人架構實戰"
        e1['speakers'] = ["Howard", "Vickie", "3M 全體成員"]
        e1['drive_url'] = "https://drive.google.com/drive/u/0/folders/1PFjPQ_Tp11nIssJnQ1QKzIirCXp1EEdD"
        e1['summary'] = "探討非工程師如何藉由 Lovable、OpenAI Codex 與 Claude AI 打造自主 Agent，從 NBA 冠軍預測跨足個人自動化財務分析，深度覆盤 Prompt 工程、資料管線除錯與決策輔助邊界。"
        e1['knowledge'] = {
            "exec_summary": "AI 浪潮已從單純對話式問答（ChatGPT），全面推進至端到端自主執行任務的 AI Agent 與無代碼/低代碼系統建構。本場聚會由非工程師成員現身說法，深度覆盤兩大實戰專案：運用 Lovable 與 OpenAI Codex 構建 NBA 賽事預測系統，以及利用 Claude AI 打造全自動個人財務資產儀表板。從提示詞工程、API 數據管線到架構除錯，全景探討生成式 AI 如何賦能個人由『使用者』躍升為『系統創造者』。",
            "provocations": [
                {
                    "speaker": "Howard",
                    "tag": "AI 門檻與能力邊界",
                    "quote": "大家都以為 AI Agent 是非工程師的魔法棒，但實戰後發現：自然語言建站只是表面，底層的 API 串接、資料清洗與邏輯除錯，依舊是非工程師不可逃避的高牆。",
                    "insight": "無代碼工具降低了 80% 的初期進入門檻，卻將剩餘 20% 的關鍵除錯難度成倍放大；真正的競爭力不在於會不會下 Prompt，而在於能否理解資料流與系統架構。"
                },
                {
                    "speaker": "Becky",
                    "tag": "決策外包的底層風險",
                    "quote": "當我們讓 AI 自動生成財務報告甚至投資決策建議時，最危險的不是 AI 算錯，而是我們因為『產出太快且看起來太專業』而徹底放棄了批判性審查。",
                    "insight": "自動化是效率槓桿，但不能成為思考的替代品。高階決策者的角色必須從『繁瑣操作員』升級為『AI 結論的首席質疑官（Chief Challenger）』。"
                }
            ],
            "topics": [
                {
                    "title": "非工程師的 AI Agent 實戰：Lovable vs. OpenAI Codex 構建賽事預測",
                    "speaker": "Howard",
                    "bullets": [
                        "[現況 Fact] 日常問答 ChatGPT 足以勝任，但構建自主 Agent 需打通外部 API、資料端點與自動化工作流，Prompt 精準度成為核心瓶頸。",
                        "[洞察 Insight] Lovable 擅長以自然語言極速生成視覺化前端，但即時數據驗證困難；Codex 掌控底層邏輯更強，但環境變數（.env）與終端報錯對非工程師門檻極高。",
                        "[反思 Tension] 工具層出不窮，但用 AI 提升生產力終究無法跳過工程思維與底層邏輯打磨的苦工。"
                    ],
                    "file": "現場實戰簡報：AI 工具 x NBA 總冠軍預測 (Lovable & OpenAI Codex 實戰體驗)"
                },
                {
                    "title": "低手動・高自動化：個人資產管理與 Claude AI 深度整合",
                    "speaker": "Vickie",
                    "bullets": [
                        "[現況 Fact] 傳統 Excel 記帳分散繁瑣、缺乏即時趨勢圖表，常因手動維護成本過高而難以維持長期追蹤。",
                        "[洞察 Insight] 串接 Claude 自動化財務分析模組，將記帳升級為每月自動生成的資產負債報告與消費優化洞察，讓數據轉化為具體行動建議。",
                        "[反思 Tension] 自動化雖然節省了 90% 的記錄時間，但系統對邊緣異常開銷的歸因仍需人工校準，避免演算法偏差產生錯誤財務安全感。"
                    ],
                    "file": "現場專案簡報：背景、痛點與核心產出 (打造個人資產管理與 AI 財務建議系統)"
                }
            ],
            "open_discussions": [
                {
                    "topic": "當非工程師透過 AI 具備開發能力，傳統軟體開發與組織分工的邊界何在？",
                    "thesis": "AI 大幅拉平工程能力鴻溝，業務專家能直接將領域知識（Domain Knowledge）具象化為運作軟體，繞過繁瑣的跨部門溝通，敏捷度倍增。",
                    "antithesis": "缺乏系統架構與資訊安全訓練的『平民開發』極易埋下技術債與維護災難；一旦核心人員離職或模型升級，無人能承擔除錯與營運責任。",
                    "pivot": "企業對影子 IT（Shadow IT）與平民開發系統的治理框架，以及 AI 自主自檢修復能力的演進程度。"
                }
            ],
            "predictions": [
                "未來兩年內，個人化微型 Agent 將普及至日常工作流，每位知識工作者都將擁有 3-5 個專屬自動化數位分身。",
                "無代碼建站與代碼生成工具將朝『端到端自動驗證與單元測試』進化，大幅降低非工程師除錯與部屬摩擦。"
            ],
            "materials": [
                {
                    "name": "Google 雲端硬碟原始專題資料夾",
                    "type": "drive",
                    "url": "https://drive.google.com/drive/u/0/folders/1PFjPQ_Tp11nIssJnQ1QKzIirCXp1EEdD"
                },
                {
                    "name": "LINE 聚會相簿：AI agent sharing 實戰現場",
                    "type": "image"
                }
            ]
        }
        print("Updated 2026-06-28 successfully.")

    # 2. Update 2026-07-05
    if '2026-07-05' in event_map:
        e2 = event_map['2026-07-05']
        e2['title'] = "平台和生態系競爭策略個案專題：顛覆賽局與飛輪效應"
        e2['speakers'] = ["劉耀元學長", "3M 全體成員"]
        e2['drive_url'] = "https://drive.google.com/drive/u/0/folders/1IGHOOblFs6q9BvLsnet3dq0vFEl80b0D"
        e2['summary'] = "特邀劉耀元學長深度剖析 Tesla vs. Uber、Netflix vs. 百視達、Chrome vs. IE、柯達等生態系顛覆賽局，解析雙邊平台網絡效應、生態位互依與價值共創的策略本質。"
        e2['knowledge'] = {
            "exec_summary": "在數位經濟時代，企業競爭已從單一產品或供應鏈的較量，全面升級為『生態系與平台網絡』的體系對決。本次專題特邀劉耀元學長返場分享，從學術定義與商業實戰出發，剖析平台生態系『相互依賴、命運與共、價值共創』的底層邏輯。透過 Tesla vs. Uber、Netflix vs. 百視達、Chrome vs. IE 以及柯達數位相機等經典個案，全景拆解單邊/雙邊網絡效應的臨界點、生態位鎖定策略與 incumbents（既有巨頭）面臨創新者窘境時的致命盲區。",
            "provocations": [
                {
                    "speaker": "劉耀元學長",
                    "tag": "生態系本質與價值共創",
                    "quote": "做產品是自己賺錢，做平台是讓大家幫你賺錢，但做生態系則是構建一個命運與共的共同體——如果核心平台無法讓生態夥伴活得更好，你的護城河在外部衝擊下將不堪一擊。",
                    "insight": "許多企業誤把『抽成中介』當作平台，真正的生態系競爭優勢在於能否創造『非你不可的外部正向網絡效應』，讓離開平台的轉移成本高於留在內部的協同價值。"
                },
                {
                    "speaker": "Becky",
                    "tag": "顛覆者的盲區與邊界",
                    "quote": "百視達不是輸給了技術，柯達也不是發明不出數位相機，他們都死在『現有最賺錢業務所綁架的內部生態阻力』；高階經理人最難的決策，永遠是親手掐死昨天的搖錢樹。",
                    "insight": "生態系顛覆往往不是發生在正面戰場，而是由邊緣市場以全新價值主張（如 Netflix 郵寄吃到飽轉串流、Chrome 極簡開放架構）切入，當既有巨頭驚覺威脅時，用戶心智與飛輪慣性早已不可逆轉。"
                }
            ],
            "topics": [
                {
                    "title": "生態系競爭的戰略本質：從單點產品到多方命運共同體",
                    "speaker": "劉耀元學長",
                    "bullets": [
                        "[現況 Fact] 商業生態系是由群體圍繞核心平台建立互依關係的系統，參與者各司其職且共享繁榮，但面臨平台規則制定與利益分配的長期動態博弈。",
                        "[洞察 Insight] 傳統線型供應鏈追求降本增效，平台追求雙邊規模經濟，而生態系追求跨界飛輪效應（如硬體補貼軟體、數據驅動演算法）。",
                        "[反思 Tension] 平台若過早過度抽成（Extract Value），生態夥伴將紛紛出逃或另立山頭，在『價值培育』與『變現獲利』之間存在根本張力。"
                    ],
                    "file": "講座簡報：平台和生態系競爭策略 (國立臺灣科技大學 劉耀元學長主講)"
                },
                {
                    "title": "經典商業顛覆實戰拆解：Tesla vs. Uber、Netflix vs. 百視達",
                    "speaker": "劉耀元學長",
                    "bullets": [
                        "[現況 Fact] Tesla 掌控垂直整合硬體與自駕數據，Uber 掌握全球雙邊出行調度；Netflix 從實體 DVD 租賃徹底轉型為原創串流巨擘，重擊百年百視達。",
                        "[洞察 Insight] Uber 依賴司機與乘客雙邊網絡，但缺乏資產壁壘；Tesla 試圖以 Robotaxi 與車載 OS 直接打穿出行生態，實現生產要素閉環。",
                        "[反思 Tension] 百視達高度依賴逾期罰金（Late Fees）營收，當 Netflix 推出免逾期費包月制時，百視達因無法割捨既得利益而錯失自救窗口。"
                    ],
                    "file": "講座簡報：跨產業平台博弈案例研究"
                },
                {
                    "title": "標準之爭與創新者窘境：Chrome vs. IE、柯達數位興衰",
                    "speaker": "劉耀元學長",
                    "bullets": [
                        "[現況 Fact] 微軟 IE 憑藉 Windows 綁定曾獨霸 95% 市佔，但終被 Google Chrome 憑藉極速沙盒、擴充生態與開源 Chromium 徹底逆轉；柯達雖首創數位相機，卻受制膠卷利潤走向破產。",
                        "[洞察 Insight] 平台主導權的更迭往往來自『關鍵架構創新』：Chrome 把瀏覽器重定義為雲端應用操作系統，瓦解了微軟原生桌面軟體的防線。",
                        "[反思 Tension] 柯達的管理層並非對數位化無知，而是理性地將資本投向利潤高達 70% 的膠卷事業，這種短期股東價值最大化的決策最終導致了長期毀滅。"
                    ],
                    "file": "講座簡報：技術破壞與防禦策略"
                }
            ],
            "open_discussions": [
                {
                    "topic": "企業面對潛在顛覆威脅時，應自建封閉生態閉環（如 Apple/Tesla），還是擁抱開放跨界聯盟（如 Android/Chromium）？",
                    "thesis": "閉環生態能確保終端使用者體驗極致、利潤率最高，並透過端到端垂直整合構建難以逾越的技術護城河。",
                    "antithesis": "開放生態藉由低門檻吸引全球第三方開發者與硬體夥伴共同參與，規模擴張速度呈指數級增長，往往能以群體智慧碾壓閉環系統。",
                    "pivot": "市場進入成熟期的速度：在技術爆發初期閉環體驗勝出，在產業標準化階段開放生態將依靠網絡效應佔據主導。"
                }
            ],
            "predictions": [
                "未來平台競爭的主戰場將是『AI 原生生態系』，傳統依靠用戶停留時長的雙邊平台，將被依靠 Agent 自主調度與服務撮合的新型協議取代。",
                "跨國反壟斷監管將常態化，平台巨頭必須向第三方開放數據互操作性（Interoperability），傳統圍牆花園（Walled Garden）模式將逐步瓦解。"
            ],
            "materials": [
                {
                    "name": "Google 雲端硬碟原始專題資料夾",
                    "type": "drive",
                    "url": "https://drive.google.com/drive/u/0/folders/1IGHOOblFs6q9BvLsnet3dq0vFEl80b0D"
                },
                {
                    "name": "LINE 聚會相簿：平台生態系講座紀實",
                    "type": "image"
                }
            ]
        }
        print("Updated 2026-07-05 successfully.")

    # Write back timeline_data.json
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {json_path} successfully.")

    # Write timeline_data.js
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("const timelineData = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Updated {js_path} successfully.")

if __name__ == '__main__':
    main()
