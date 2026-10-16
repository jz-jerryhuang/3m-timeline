# -*- coding: utf-8 -*-
import json
import sys

def main():
    json_path = 'timeline_data.json'
    js_path = 'timeline_data.js'

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_event = None
    for e in data['events']:
        if e.get('date') == '2025-08-16':
            target_event = e
            break

    if not target_event:
        print("Error: Event 2025-08-16 not found!")
        sys.exit(1)

    # Update basic metadata and drive_url
    target_event['title'] = "川普新關稅政策影響：金融支付的顛覆與數位美元霸權戰"
    target_event['speakers'] = ["Jerry", "3M 全體成員"]
    target_event['drive_url'] = "https://drive.google.com/drive/u/0/folders/1quy-IPrEC5D-QHhSWAbUqLINlVycyQ5x"
    target_event['summary'] = "川普新關稅政策引發全球金融變局，從 Ray Dalio 貨幣大週期看美債危機與去美元化挑戰；美國三大數位資產法案（GENIUS Act / Anti-CBDC）扶持民間穩定幣，華爾街巨頭全面佈局跨鏈清算，探討穩定幣究竟是美元霸權的救命稻草還是特洛伊木馬。"

    # Update knowledge section
    target_event['knowledge'] = {
        "exec_summary": "川普重啟高關稅政策加速全球地緣經濟分化與美債信任危機（國債突破 37 兆美元）。本場研討深入拆解 Ray Dalio 貨幣百年大週期與去美元化挑戰（如金磚國家 BRICS Pay），並聚焦美國如何透過立法（GENIUS Act、Anti-CBDC Act）扶持民間美元穩定幣（USDT/USDC），以及華爾街巨頭（JPMorgan、Visa、PayPal、SWIFT）如何推動支付重構，探討在關稅風暴下，穩定幣是否將成為數位時代延續美元霸權與重塑跨國清算的關鍵載體。",
        "provocations": [
            {
                "speaker": "Jerry",
                "tag": "貨幣大週期與定價權",
                "quote": "美國是歷史上唯一能用自己印出來的貨幣買全球實體資源的國家；當美債不再被視為無風險資產、去美元化加速時，穩定幣是美國衰退下的救命稻草，還是美元霸權在數位戰場的二次重生？",
                "insight": "若傳統美元受制於債務惡性循環與關稅孤立主義，由私部門 100% 美債儲備支撐的『鏈上數位美元』將繞過主權邊界深入非美元國家，實質把全球金融流動性再度鎖死在美元體系內。"
            },
            {
                "speaker": "Becky",
                "tag": "地緣監管與主權博弈",
                "quote": "當跨國企業與民間全面改用美元穩定幣完成秒級結算與避險，非美各國央行的貨幣主權與資本管制將直接被穿透——面對這場無聲入侵，打不過就加入，是香港試點發行穩定幣的核心動機。",
                "insight": "穩定幣不是單純的支付技術工具，而是國家貨幣主權的數位領土戰。中國採取『香港試點、內地嚴管』模式，正是為了在保留資本管制的同時，為數位人民幣國際化預備話語權。"
            }
        ],
        "topics": [
            {
                "title": "貨幣大週期與美元霸權的三大根基鬆動",
                "speaker": "Jerry",
                "bullets": [
                    "[現況 Fact] 美國國債規模已跨越 37 兆美元，美債十年期殖利率維持在 4.9% 高檔，巨額利息支出迫使政府陷入舉新還舊的債務螺旋。",
                    "[洞察 Insight] 依據 Ray Dalio 大週期模型，1944 布雷頓森林與 1974 石油美元確立了全球 60% 貿易與 80% 外匯由美元計價；如今川普高關稅削弱政策信任，金磚國家聯盟（BRICS Pay）加速去美元化進程。",
                    "[反思 Tension] 傳統美元信用雖然衰退，但在全球尚無任何單一主權貨幣能提供等同美債深度與流動性的前提下，多極貨幣結算仍面臨嚴重的流動性碎片化痛點。"
                ],
                "file": "川普新關稅政策影響之金融支付的改變_v2.pptx (Slide 1-7)"
            },
            {
                "title": "美國三大數位資產法案與鏈上美元生態",
                "speaker": "Jerry",
                "bullets": [
                    "[現況 Fact] 美國加速推動《GENIUS Act》（天才法案）規範穩定幣 100% 儲備美債與現金，並透過《Anti-CBDC Act》禁止聯準會發行官方零售數位貨幣。",
                    "[洞察 Insight] 美國戰略是『以退為進』：放棄政府集中監控的 CBDC，轉而賦予私部門銀行與科技巨頭合法發行合規穩定幣的權利，將發行儲備直接綁定短期美債需求。",
                    "[反思 Tension] USDT（街頭零售派，1,450 億美元）與 USDC（機構合規派，500 億美元）合計壟斷 90% 以上份額，形成由私營企業代表國家向全球輸出數位美元的特殊體制。"
                ],
                "file": "川普新關稅政策影響之金融支付的改變_v2.pptx (Slide 8-12)"
            },
            {
                "title": "傳統金融基礎建設的升級：JPM Coin、Visa、PayPal 與 SWIFT",
                "speaker": "Jerry",
                "bullets": [
                    "[現況 Fact] JPM Coin 日結算破 10 億美元、累計破 3,000 億美元；Visa 與 Mastercard 將 USDC 納入清算；PayPal 推出 PYUSD 並完成企業商業支付；SWIFT 跨鏈整合測試成功。",
                    "[洞察 Insight] 傳統跨境支付（SWIFT）需耗時 2-5 天、每筆成本 20-50 美元；穩定幣實現 24/7 即時清算、成本降至 1/10，B2B 跨境效率提升 90% 以上。",
                    "[反思 Tension] 傳統金融機構不再視加密貨幣為威脅，而是透過『把區塊鏈包裹進現有牌照與帳戶體系』迅速吃下新型結算通道，鞏固既有抽成與結算主導權。"
                ],
                "file": "川普新關稅政策影響之金融支付的改變_v2.pptx (Slide 15-18)"
            },
            {
                "title": "香港試點 vs 內地嚴管：非美經濟體的貨幣防線",
                "speaker": "Jerry",
                "bullets": [
                    "[現況 Fact] 香港金管局預計 2025 年開放穩定幣牌照，要求 100% 儲備；京東、螞蟻、小米等科技巨頭積極佈局穩定幣跨境支付。",
                    "[洞察 Insight] 中國採取『香港前線試點、內地嚴加看管』策略，試圖以離岸港幣與潛在人民幣穩定幣抗衡美元穩定幣滲透，並爭奪亞太貿易計價權。",
                    "[反思 Tension] 當穩定幣在跨國供應鏈與新興市場成為事實上的計價通訊協議，各國若缺乏有競爭力的本土穩定幣，將實質喪失貨幣政策自主權。"
                ],
                "file": "川普新關稅政策影響之金融支付的改變_v2.pptx (Slide 19)"
            }
        ],
        "open_discussions": [
            {
                "topic": "穩定幣究竟是美元霸權的『救命稻草』，還是加速實體主權解體的『特洛伊木馬』？",
                "thesis": "穩定幣本質上是『美債的超級分銷商』。GENIUS Act 強制要求以美債做儲備，反而為 37 兆美元美債創造了最堅固的非自主買盤，使美元穿透外匯管制滲透全球民間。",
                "antithesis": "當全球跨國交易習慣純鏈上資產與智能合約清算，美元僅僅淪為記帳單位（Unit of Account），一旦出現由黃金、大宗商品或多國貨幣籃子支持的無國界穩定幣，美元霸權將被底層協議直接抽空。",
                "pivot": "聯準會對穩定幣利息分潤的監管放行程度，以及金磚國家本幣結算系統（BRICS Pay）在實體大宗商品貿易中的滲透速度。"
            }
        ],
        "predictions": [
            "2025-2026 年美國與香港將先後完成主要穩定幣牌照審批，全球跨境 B2B 支付將迎來一輪由穩定幣驅動的降費提速潮。",
            "傳統銀行與跨國收單機構（Visa/Mastercard/SWIFT）將全面把合規穩定幣納入標準後台，穩定幣將從『加密衍生品』正式質變為『常規金融清算管道』。",
            "非美經濟體（特別是新興市場與能源出口國）將在資本外逃防堵與穩定幣支付效率之間面臨空前監管抉擇。"
        ],
        "materials": [
            {
                "name": "川普新關稅政策影響之金融支付的改變_v2.pptx (Jerry 主講簡報)",
                "type": "pptx",
                "url": "https://drive.google.com/drive/u/0/folders/1quy-IPrEC5D-QHhSWAbUqLINlVycyQ5x"
            },
            {
                "name": "Google 雲端硬碟原始專題資料夾",
                "type": "drive",
                "url": "https://drive.google.com/drive/u/0/folders/1quy-IPrEC5D-QHhSWAbUqLINlVycyQ5x"
            }
        ]
    }

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
