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

    # Update basic metadata
    target_event['title'] = "川普新關稅衝擊、金融支付變局與科技狹窄通道"
    target_event['speakers'] = ["Jerry", "Becky", "Johnny", "3M 全體成員"]
    target_event['drive_url'] = "https://drive.google.com/drive/u/0/folders/1quy-IPrEC5D-QHhSWAbUqLINlVycyQ5x"
    target_event['summary'] = "全方位剖析川普新關稅的多維衝擊：從 Jerry 拆解美債危機與鏈上美元穩定幣霸權重構，到 Becky 引入《自由的窄廊》框架剖析科技治理與主權再定義，結合 Johnny 及全體成員對實體供應鏈二次遷徙的實戰思辨。"

    # Multi-member Executive Knowledge Structure
    target_event['knowledge'] = {
        "exec_summary": "川普重啟高關稅政策引發全球地緣經濟震盪。本場研討跳脫單一維度，從金融、科技治理與實體產業三大視角深度覆盤：首先由 Jerry 剖析 37 兆美債危機、Ray Dalio 百年大週期與穩定幣（USDT/USDC/JPM Coin）如何重構跨境支付與美元霸權；接著由 Becky 借鑑《自由的窄廊》（The Narrow Corridor）經典模型，探討面對極權監控與失控混亂，國家主權如何被科技巨頭與開源協議『再定義』；最後由 Johnny 與全體成員針對製造業二次出海、產能分散與避險成本展開熱烈思辨，全景展現 3M 讀書會跨領域的實戰決策智慧。",
        "provocations": [
            {
                "speaker": "Jerry",
                "tag": "貨幣大週期與鏈上霸權",
                "quote": "美國是歷史上唯一能用自己印出來的貨幣買全球實體資源的國家；當美債不再被視為無風險資產、去美元化加速時，穩定幣是美國衰退下的救命稻草，還是美元霸權在數位戰場的二次重生？",
                "insight": "若傳統美元受制於債務惡性循環與關稅孤立主義，由私部門 100% 美債儲備支撐的『鏈上數位美元』將繞過主權邊界深入非美元國家，實質把全球金融流動性再度鎖死在美元體系內。"
            },
            {
                "speaker": "Becky",
                "tag": "科技狹窄通道與主權再定義",
                "quote": "未來的主權不再只是掌握在民族國家政府手上，而可能實質轉移到科技巨頭、平台公司甚至開源社群；面對科技上的狹窄通道，如何在制度規範與創新自由間尋找平衡，是決定文明走向的核心關鍵。",
                "insight": "極權監控（國家壟斷技術）與失控混亂（技術濫用崩解）是狹窄通道的兩側懸崖。高管必須意識到：關稅只能築起物理邊界，但跨國科技資本與演算法早已穿透國界，重新定義了商業與權力的遊戲規則。"
            },
            {
                "speaker": "Johnny",
                "tag": "供應鏈遷徙與實體反思",
                "quote": "大家都在談供應鏈 China+1 或奔赴東南亞與墨西哥，但若核心零組件智財權與跨境金融結算仍高度受制於強權博弈，實體工廠的物理搬遷不過是把地緣風險換了個包裝。",
                "insight": "單純產能轉移無法真正避險，未來的供應鏈競爭已由單點製造成本，升級為『在地化供應鏈韌性、跨國法規合規與多幣種清算結算』的多維立體防禦戰。"
            }
        ],
        "topics": [
            {
                "title": "川普新關稅政策與金融支付變局：美元霸權的鏈上重構",
                "speaker": "Jerry",
                "bullets": [
                    "[現況 Fact] 美國國債規模已跨越 37 兆美元，十年期殖利率維持在 4.9% 高檔，巨額利息支出迫使政府陷入舉新還舊的債務螺旋，促使金磚國家加速推展 BRICS Pay 去美元化機制。",
                    "[洞察 Insight] 美國透過《GENIUS Act》與《Anti-CBDC Act》以退為進，阻擋政府壟斷型零售 CBDC，轉而賦予私部門銀行與機構發行合規穩定幣（USDT/USDC），以 100% 美債儲備擴大全球美債買盤。",
                    "[反思 Tension] JPM Coin、Visa、SWIFT 跨鏈整合將跨境支付由 2-5 天縮短至秒級、手續費降至 1/10，大幅提升商業效率的同時，也加深了非美經濟體在數位時代的美元路徑依賴。"
                ],
                "file": "川普新關稅政策影響之金融支付的改變_v2.pptx (Jerry 主講)"
            },
            {
                "title": "科技治理的狹窄通道：從技術霸權到權力再定義 (The Narrow Corridor)",
                "speaker": "Becky",
                "bullets": [
                    "[現況 Fact] 引入 Acemoglu & Robinson《自由的窄廊》架構：科技演進正面臨兩極風險——國家壟斷技術導致失去自由的『極權監控』，與任何人濫用技術導致社會解體的『失控混亂』。",
                    "[洞察 Insight] 走出科技窄廊需要三支支柱：『審查科技資本的制度防線』、『共同制定治理標準的跨國協作』與『公民企業共同負責的自我節制』；主權概念正在深刻再定義（Redefinition of Sovereignty）。",
                    "[反思 Tension] 物理世界的關稅壁壘越築越高，但科技巨頭掌控的算力、數據與金融協議卻跨越主權，企業若缺乏跨國科技治理自覺，終將在國家干預與科技壟斷的夾縫中窒息。"
                ],
                "file": "現場專題研討：面對科技上的狹窄通道與主權再定義 (Becky 引言與思辨實錄)"
            },
            {
                "title": "實體製造二次遷徙與產業跨界避險實務",
                "speaker": "Johnny / 3M 全體成員",
                "bullets": [
                    "[現況 Fact] 川普關稅大棒重擊跨國代工與電子硬體供應鏈，原產地認定（Rules of Origin）日益嚴格，轉口貿易與洗產地套利空間被全面封堵。",
                    "[洞察 Insight] 3M 成員結合各自行業實戰深入探討：製造業出海必須從『假性設廠』升級為『真在地化營運』，建立在地生態系與多幣種資金池以抵禦關稅衝擊。",
                    "[反思 Tension] 搬遷物理工廠容易，重建高良率供應鏈聚落極其昂貴；在關稅摩擦常態化下，缺乏規模資本的中小企業將面臨殘酷的出清危機。"
                ],
                "file": "現場跨界思辨研討：供應鏈地緣風險與出海因應對策"
            }
        ],
        "open_discussions": [
            {
                "topic": "關稅壁壘時代的權力歸屬：主權國家能否透過物理關稅，重新奪回被科技與金融資本侵蝕的統治力？",
                "thesis": "立場 A（民族國家主權回歸論）：關稅、出入境與邊境管制是主權國家的終極實體武器。透過在地化就業要求、反壟斷調查與技術出口管制，國家能有效迫使跨國科技與金融資本屈服。",
                "antithesis": "立場 B（科技與鏈上資本超越論）：無形資本與演算法永遠比海關政策跑得快。跨國巨頭掌控算力基礎設施，穩定幣繞過傳統外匯管制，實質權力已不可逆地轉移至全球平台與開源協議手中。",
                "pivot": "各國政府對跨國數據與加密清算協議的實質執法穿透力，以及全球科技巨頭是否會因反壟斷分拆而削弱整體生態影響力。"
            }
        ],
        "predictions": [
            "關稅摩擦與供應鏈脫鉤將走向制度化與長期化，逼迫跨國企業普遍建立『產能多地備援』與『本幣/穩定幣雙軌結算系統』以對沖主權風險。",
            "全球科技巨頭在 AI 與金融清算基礎設施的主導地位，將引發新一輪跨國反技術壟斷立法潮，科技治理的『狹窄通道』成為各國競爭關鍵。",
            "非美經濟體將在維護貨幣主權資本管制與享受數位穩定幣高效便利之間劇烈擺盪，離岸金融中心（如香港、新加坡）的制度創新將迎來爆發機遇。"
        ],
        "materials": [
            {
                "name": "川普新關稅政策影響之金融支付的改變_v2.pptx (Jerry 主講簡報)",
                "type": "pptx",
                "url": "https://drive.google.com/drive/u/0/folders/1quy-IPrEC5D-QHhSWAbUqLINlVycyQ5x"
            },
            {
                "name": "現場研討實錄：科技狹窄通道與主權再定義 (Becky 專題剖析)",
                "type": "docx",
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
