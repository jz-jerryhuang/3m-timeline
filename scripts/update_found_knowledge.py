import json

with open('timeline_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. 2018-07-28 (區塊鏈)
k_2018_07_28 = {
    'has_minutes': True,
    'minutes_meta': {
        'note_taker': 'Jerry',
        'recorder': 'Jerry',
        'file': '會議紀錄 7-28-2018.docx'
    },
    'exec_summary': '以經濟學大師海耶克《貨幣非國家化》與《通往奴役之路》為理論起點，深度剖析區塊鏈如何打破國家與金控壟斷。探討第三方支付到代幣發行的權力轉移，激辯『去中心化 vs 製造新中心』、ICO 責任邊界，以及愛沙尼亞數位國家與未來城邦聚落經濟之可能性。',
    'topics': [
        {
            'speaker': 'Jerry',
            'title': '海耶克自由經濟與貨幣非國家化思潮',
            'bullets': [
                '海耶克在《通往奴役之路》警告政府主導經濟計劃將養出怪物體系與特權金控壟斷；主張貨幣應擺脫主權國家壟斷，交由自由市場競爭。',
                '從第三方支付到代幣經濟：互聯網與區塊鏈透過流量、用戶行為與智慧合約，首次讓大眾得以繞過百年銀行體系實現資產轉移與自建信用體系。'
            ],
            'file': '海耶克(0628).docx'
        },
        {
            'speaker': 'Jerry',
            'title': '區塊鏈技術核心：分散式帳本與共識機制',
            'bullets': [
                '剖析 Metadata（Data above data）、雜湊演算法（Hash）與非對稱加密如何打破資訊不對稱，建立去中心化的無條件信任。',
                '愛沙尼亞數位公民（e-Residency）經驗：以分散式架構與國家級數位身分，展現公共治理去實體化的前瞻原型。'
            ],
            'file': '讀書會分享 - 區塊鏈 (Jerry) 7-28-2018.pptx'
        },
        {
            'speaker': 'Aegon & 3M 團隊',
            'title': '代幣經濟的盲點：進入者越多越製造出新中心化',
            'bullets': [
                '歷史規律：君王統一度量衡與貨幣以降低交易與摩擦成本；若每個生態系各自發幣，使用者頻繁兌換的痛苦將催生『中介整合型巨頭』（如 Trivago 現象），反而走向再中心化。',
                '『信任不等於責任』：區塊鏈解決了技術上防偽防篡改的信任，但虛擬代幣倒閉或被盜時由誰承擔賠償與法律責任？責任的缺失是金融巨頭防守傳統金權的護身符。'
            ],
            'file': '會議紀錄 7-28-2018.docx'
        }
    ],
    'debates': [
        {
            'topic': '去中心化 vs 割據式新中心化矛盾',
            'proposer': 'Jerry & Aegon',
            'insight': '各自發幣若缺乏互操作性，使用者將被迫在多幣種間換匯，最終只會催生更龐大的中介平台重掌流量與匯率定價權。'
        },
        {
            'topic': '技術信任 (Trust) 能否替代法律責任 (Accountability)？',
            'proposer': '3M 夥伴',
            'insight': '代幣發行本質是追求商業利益而非公共利益，無法提供中央銀行與政府所背書的最後兜底清償責任，使大眾難以在日常大額交易中全面依賴。'
        },
        {
            'topic': '城邦聚落經濟 vs 傳統民族國家',
            'proposer': 'Jerry',
            'insight': '數位社群如 Facebook 用戶超 20 億宛如超級大國，未來經濟單元可能走向具備獨特產業分工（如台中精密機械聚落）與自我信用體系的城邦型分散社群。'
        }
    ],
    'predictions': [
        'ICO 狂潮將迎來殘酷洗牌，僅靠白皮書無實質落地與責任保障的專案將被監管與市場淘汰。',
        '區塊鏈的真正破局點不在盲目發行代幣，而在解決文化內容（如 Matters）、版權音樂（Soundscape）與公信力驗證之深層信任痛點。'
    ],
    'materials': [
        {'name': '會議紀錄 7-28-2018.docx', 'type': 'docx'},
        {'name': '海耶克(0628).docx', 'type': 'docx'},
        {'name': '讀書會分享 - 區塊鏈 (Jerry) 7-28-2018.pptx', 'type': 'pptx'}
    ]
}

# 2. 2018-12-15 (量子運算)
k_2018_12_15 = {
    'has_minutes': True,
    'minutes_meta': {
        'note_taker': 'Jerry',
        'recorder': 'Jerry',
        'file': '量子筆記 12-15-2018.docx'
    },
    'exec_summary': '從普朗克常數、量子疊加與量子穿隧等物理基本原理出發，探討量子運算顛覆現有非對稱加密體系的顛覆性潛能。結合 MIT x PRO 線上課程體系與單光子量子雷達最新突破，深入思辨科學、哲學與宗教的交會邊界，並反思演算法與社群平台對人類自由意志的操控。',
    'topics': [
        {
            'speaker': 'Jerry',
            'title': '量子力學基礎原理與運算革命',
            'bullets': [
                '從普朗克常數（Planck\'s constant）到原子能階：突破傳統電腦二進位 0/1 限制，量子位元（Qubit）透過疊加態與量子穿隧實現指數量級的平行運算力。',
                '破解現有資安防線：具備粉碎當代 RSA 密碼體系能力的量子電腦，正在迫使全球密碼學界提前佈局『後量子密碼（Post-Quantum Cryptography）』。'
            ],
            'file': '量子.docx'
        },
        {
            'speaker': 'Jerry',
            'title': '量子運算前沿動態：MIT x PRO 課程與量子雷達突破',
            'bullets': [
                '麻省理工與 IBM 合作開設全套量子運算實戰課（MIT x PRO），開放 IBM Q 系統與開源套件 Qiskit，推動量子科技從實驗室走向產業應用。',
                '中國首部單光子檢測量子雷達樣機問世，實現百公里級遠程探測，展現利用量子態在複雜電子戰中反隱身戰機的軍事戰略顛覆性。'
            ],
            'file': '量子.docx'
        },
        {
            'speaker': 'Jerry & 3M 團隊',
            'title': '科學、哲學與宗教的並行思辨及演算法操控反思',
            'bullets': [
                '物質不滅定律在量子領域的極限推演：量子運算之上是否存在無盡的套疊迴圈？佛學哲學思辨與物理學在空性與觀測者效應上的深刻共鳴。',
                '演算法操控警訊：Google Discover 與社群平台正透過『預測 (Prediction) → 介入 (Intervention) → 操縱 (Manipulation)』將人類思維推向極端單一化。',
                '捍衛不可數位化的本質：人際真實關係（Relationship）、人體能量（Energy）與細膩情感（Emotion），提醒我們必須主動增加線下 (Offline) 面對面的深度連結。'
            ],
            'file': '量子筆記 12-15-2018.docx'
        }
    ],
    'debates': [
        {
            'topic': '量子運算之商業化思考：切忌以大眾消費經濟角度衡量',
            'proposer': 'Jerry',
            'insight': '量子運算本質是用來解決超高維度的極端複雜問題（新藥研發、分子化學、材料工程、密碼學），而非個人消費級文書娛樂。'
        },
        {
            'topic': '演算法認知馴化 vs 人類自由意志',
            'proposer': '3M 夥伴',
            'insight': '線上操縱成本極低且精確投餵，唯有走出同溫層並保有線下無演算法過濾的真實思辨碰撞，才能避免陷入思維單一化。'
        }
    ],
    'predictions': [
        '量子科技將在後量子資安加密、材料模擬與軍事戰略雷達領域率先迎來地緣格局突破。',
        '下期主題鋪墊：推進至『無條件基本收入 (UBI)』與組織區塊鏈化，探索後技術時代的最優資源分配架構。'
    ],
    'materials': [
        {'name': '量子筆記 12-15-2018.docx', 'type': 'docx'},
        {'name': '量子.docx', 'type': 'docx'}
    ]
}

# 3. 2019-07-27 (UBI)
k_2019_07_27 = {
    'has_minutes': True,
    'minutes_meta': {
        'note_taker': 'Jerry',
        'recorder': 'Jerry',
        'file': '會議紀錄20190728.docx'
    },
    'exec_summary': '延續對資源分配正義與後勞動時代的思辨，深入剖析無條件基本收入 (UBI) 在芬蘭等國之社會契約實驗。結合 Becky 赴日考察高齡輔具產業鏈與長照 NGO 經營現狀，深度推演共享經濟、智慧升降家具與全民保險機制如何重塑未來超高齡社會的尊嚴生活。',
    'topics': [
        {
            'speaker': 'Vickie',
            'title': 'Universal Basic Income (UBI) 理論架構與全球實驗',
            'bullets': [
                '從芬蘭兩年期 UBI 實驗看社會契約的重構：無條件發放固定生活金並未降低勞動意願，反倒顯著降低心理壓力、提升創業自主性與社會信任感。',
                'AI 與自動化浪潮下的資源重分配：面對技術性失業，傳統社會福利安全網的官僚審查成本過高，UBI 提供了一種極簡且不具汙名化的替代方案。'
            ],
            'file': '20190727 - Universal Basic Income (Vickie).pptx'
        },
        {
            'speaker': 'Becky',
            'title': '日本高齡輔具產業鏈深度考察與『預防』哲學',
            'bullets': [
                '日本輔具核心思維在於『預防失能』而非被動照護：以不同顏色三角斜坡消弭室內外高低差、玄關直立握管避免深蹲跌倒；免釘卡榫工藝確保不破壞租賃住宅結構。',
                '嚴格認證與消毒 SOP：清洗烘乾後的被單床單一律通過金屬探測器排查殘留針頭，從制度上將突發事故轉化為產業標竿 SOP。'
            ],
            'file': '會議紀錄20190728.docx'
        },
        {
            'speaker': 'Jerry & 3M 團隊',
            'title': '長照輔具誰來買單？保險創新與智慧空間收納科技',
            'bullets': [
                '買單機制三大路徑激辯：政府課稅+保險全民買單（覆蓋所有罕見症狀） vs 民間市場化（容易遺落邊緣群體） vs 保險公司新型態『輔具租賃保單』。',
                '輔具共享經濟的文化阻力：長輩對二手病床常有『觸霉頭』心理排斥，需依賴專業機構認證洗滌扭轉社會觀感。',
                '未來微型智慧空間：以 Bumblebee 天花板智慧升降家具為例，按需收納睡床與儲物櫃，將有限都會空間最大化。'
            ],
            'file': '會議紀錄20190728.docx'
        }
    ],
    'debates': [
        {
            'topic': '輔具由全民買單 vs 商業保險市場化',
            'proposer': 'Becky & 3M 夥伴',
            'insight': '純市場化必然優先考量規模經濟，導致非主流罕見病患得不到照護；唯有全民互助機制結合產業標準化才能兼顧公平與尊嚴。'
        },
        {
            'topic': '台灣長照法規限制：非 NGO 不得經營住宿型長照機構',
            'proposer': 'Becky',
            'insight': '探討法律嚴格限制營利機構進駐的利弊，分析營利企業如何透過成立公益基金會（如長庚養生村）的形式跨足長照市場。'
        }
    ],
    'predictions': [
        '高齡化海嘯將迫使保險業由單純『現金理賠』轉型為『輔具照護服務與租賃生態圈』。',
        '天花板升降等機器人家居科技將從奢侈概念逐步下沉為都會小宅的標配解決方案。'
    ],
    'materials': [
        {'name': '會議紀錄20190728.docx', 'type': 'docx'},
        {'name': '20190727 - Universal Basic Income (Vickie).pptx', 'type': 'pptx'},
        {'name': 'Universal basic income.pptx', 'type': 'pptx'}
    ]
}

# 4. 2020-04-26 (COVID-19 新常態)
k_2020_04_26 = {
    'has_minutes': True,
    'minutes_meta': {
        'note_taker': 'Jerry & Vickie',
        'recorder': 'Jerry & Vickie',
        'file': '新冠肺炎筆記 4-26-2020.docx'
    },
    'exec_summary': '在 2020 年初全球疫情大爆發之際，3M 夥伴首次全員就『後疫情新常態 (The New Normal)』展開全景研討。橫跨 WiDS 線上社群治理、外送與植物肉飲食革命、華碩 NB 全球供應鏈東南亞遷徙、遠距工作互信危機、英國封城心理健康，到海軍敦睦艦隊隱私讓位公衛與中資抄底歐洲企業的地緣戰略衝擊。',
    'topics': [
        {
            'speaker': 'Vickie',
            'title': '社群經營的新常態：WiDS Taipei 志工線上協作',
            'bullets': [
                '斯坦福大學全球倡議 Women in Data Science (WiDS)，Taipei 分會因應疫情全面轉向線上籌備與虛擬峰會，驗證去中心化志工網絡的敏捷動能。',
                '疫情不僅是衝擊，更是不可逆的數位轉型催化劑，推動跨地域遠距研討成為主流。'
            ],
            'file': '社群經營的新常態 (Vickie) 04-26-2020.pdf'
        },
        {
            'speaker': 'Jerry',
            'title': '飲食與餐飲科技新常態：外送平台進化與科技肉革命',
            'bullets': [
                '外送平台下一步：政府補助加速小微餐飲上架，平台延伸至居家水電修繕、生鮮虛擬超市（Dark Store）與跨店家聯合一站式採購。',
                '科技肉的環境溢價：植物肉（Beyond Meat / Impossible Foods）與實驗室試管肉（Memphis Meat）雖成本較高，但若計入傳統畜牧業的巨量碳排、水資源耗損等外部社會成本，科技肉具備長期生態必然性。'
            ],
            'file': '新冠肺炎下的新飲食型態 (Jerry)  04-26-2020.pptx'
        },
        {
            'speaker': 'Jay',
            'title': '供應鏈管理新常態：中美貿易戰疊加疫情下的 NB 產能大遷徙',
            'bullets': [
                '華碩等筆電供應鏈高度依賴中國，疫情封控導致陸海空物流全線中斷；後續復工取決於政府政策、招工難度與產能修復三指標。',
                '中美貿易戰與疫情雙重夾擊，加速電子業遷往東南亞；台廠資金雖回流台灣，但多屬購地投資，實質產能移轉仍需持續追蹤評估。'
            ],
            'file': '供應鏈管理的新常態 (Jay) 04-26-2020.pptx'
        },
        {
            'speaker': 'Una',
            'title': '工作的新常態：遠距辦公的三大挑戰與數位三力',
            'bullets': [
                '遠距工作三大挑戰：資安防護、企業信任文化與寬頻網路基礎建設；本質考驗勞資彼此的深層信任。',
                '數位轉型人才必備三力：高效溝通力（非同步溝通）、自我約束力（自制力）與環境敏捷適應力。'
            ],
            'file': '遠距工作催化劑 (Una) 26-04-2020.pptx'
        },
        {
            'speaker': 'Howard',
            'title': '健康生活新常態：歐洲封城經驗與 WHO 心理健康警訊',
            'bullets': [
                '分享個人在英歐封城經歷：隔離導致社會恐慌與不確定性，全球 75% 人口處於亞健康狀態，憂鬱症與身心失衡案例遽增。',
                '線上健身房自救：健身教練透過 Zoom 直播帶動學員，冥想、瑜珈與烹飪成為維持身心靈健康的新生活模式。'
            ],
            'file': '健康生活新常態 (Howard)  26-04-2020.pdf'
        },
        {
            'speaker': 'Rebecca (Becky)',
            'title': '後疫情時代宏觀推演：客觀回不去、主觀不想回去',
            'bullets': [
                '客觀回不去：活命當前個人隱私退居次位，海軍敦睦艦隊感染事件顯示公共衛生權力凌駕一切之上。',
                '主觀不想回去：組織權力結構洗牌，管理層恐藉疫情掩蓋歷年經營虧損與爛帳，將責任全數推諉給大環境。',
                '地緣總體經濟：英美義印對中提起求償訴訟；歐洲警惕中資趁企業財務危機抄底收購，緊急構築外資審查壁壘。',
                '個體情感渴望：人類是需要真實肌膚接觸的物種，滿足實體觸覺與溫度臨場感的產品在後疫情具備龐大商機。'
            ],
            'file': 'The New norm post covid-19 ver1 (rc) 4-26-2020.pdf'
        },
        {
            'speaker': 'Paul',
            'title': '觀光旅遊業的至暗時刻與政府紓困方案',
            'bullets': [
                '國境封閉使跨國航空與旅遊業直接雪崩，探討各國政府產業補貼政策與旅行社轉型國旅之生存自救路徑。'
            ],
            'file': '旅遊業別來無恙 (Paul) 26-04-2020.pptx'
        }
    ],
    'debates': [
        {
            'topic': '公衛緊急權力 vs 個人隱私讓步',
            'proposer': 'Rebecca (Becky)',
            'insight': '當防疫需求使軍事行蹤與個人足跡被迫公諸於世，疫後國家監控權限是否會如同 911 愛國者法案般再也無法撤回？'
        },
        {
            'topic': '台灣超前部署 vs 疫苗研發進度滯後矛盾',
            'proposer': 'Rebecca & Jerry',
            'insight': '台灣雖守住本土零確診，但因缺乏足夠感染病例樣本數，導致自主疫苗臨床測試進度遠落後於每日進行 2 萬人篩檢的紐約等重災區。'
        }
    ],
    'predictions': [
        '遠距與實體混合辦公 (Hybrid Work) 將永久改寫全球企業運作模式。',
        '全球供應鏈由『JIT 成本最優化』轉向『JIC 韌性安全化』，東南亞多中心製造格局成形。'
    ],
    'materials': [
        {'name': '新冠肺炎筆記 4-26-2020.docx', 'type': 'docx'},
        {'name': '20200426 - sharing note.docx', 'type': 'docx'},
        {'name': '新冠肺炎下的新飲食型態 (Jerry)  04-26-2020.pptx', 'type': 'pptx'},
        {'name': 'The New norm post covid-19 ver1 (rc) 4-26-2020.pdf', 'type': 'pdf'},
        {'name': '供應鏈管理的新常態 (Jay) 04-26-2020.pptx', 'type': 'pptx'},
        {'name': '遠距工作催化劑 (Una) 26-04-2020.pptx', 'type': 'pptx'},
        {'name': '社群經營的新常態 (Vickie) 04-26-2020.pdf', 'type': 'pdf'},
        {'name': '健康生活新常態 (Howard)  26-04-2020.pdf', 'type': 'pdf'},
        {'name': '旅遊業別來無恙 (Paul) 26-04-2020.pptx', 'type': 'pptx'},
        {'name': 'COVID-19-Facts-and-Insights-March-25-v3.pdf', 'type': 'pdf'}
    ]
}

# 5. 2020-05-23 (國際情勢與疫苗開發)
k_2020_05_23 = {
    'has_minutes': True,
    'minutes_meta': {
        'note_taker': 'Jerry',
        'recorder': 'Jerry',
        'file': '讀書會筆記-國際情勢 20200524.docx'
    },
    'exec_summary': '台灣疫情本土『加零』後重返線下實體研討，深度聚焦『全球疫苗地緣政治戰』。剖析中美疫苗研發競賽如何重演美蘇冷戰太空競賽，推演川普『美國優先』國家保護主義對全球疫苗分配機制的衝擊，以及疫苗霸權如何直接扼住發展中國家的經濟復甦命脈。',
    'topics': [
        {
            'speaker': 'Jerry',
            'title': '全球疫苗爭奪戰：新冷戰太空競賽的當代重演',
            'bullets': [
                '兩人分組研討：疫苗開發、中美貿易摩擦與 2020 美國總統大選盤根錯節，無法孤立看待。',
                '掌握疫苗者掌握全球經濟命脈：誰能率先量產有效疫苗，誰就握有重啟經濟與對發展中國家（中南美洲、俄羅斯、非洲）施加地緣外交影響力的絕對籌碼。'
            ],
            'file': '國際情勢-新冠疫苗開發 (Jerry) 5-23-2020 v2.pptx'
        },
        {
            'speaker': 'Jerry & Rebecca (Becky)',
            'title': '川普『美國優先』國家保護主義與國際分配失靈',
            'bullets': [
                '對比奧巴馬時期美國扮演國際多邊峰會召集主席，川普政府展現強烈單邊主義，首批生產疫苗勢必優先全額支應美國本土需求，全球 COVAX 國際配發制度面臨嚴峻挑戰。',
                '病毒無國界 vs 國界封鎖：各國試圖以民族國家壁壘自保，但只要全球仍有重災區未受控，任何單一國家都難以獨善其身。'
            ],
            'file': '讀書會筆記-國際情勢 20200524.docx'
        }
    ],
    'debates': [
        {
            'topic': '疫苗民族主義 vs 全球公共財',
            'proposer': 'Jerry & Rebecca',
            'insight': '各大國將疫苗研發視為零和博弈戰略武器，導致專利壁壘與囤積競爭，嚴重阻礙全人類群體免疫與跨國供應鏈的同步修復。'
        }
    ],
    'predictions': [
        '疫苗研發速度將直接決定各國 2021 年經濟重啟先後順序，甚至左右 2020 年底美國大選走向。',
        '地緣政治格局將分化為『美歐 mRNA 陣營』與『中俄滅活/腺病毒陣營』的疫苗外交拉攏戰。'
    ],
    'materials': [
        {'name': '讀書會筆記-國際情勢 20200524.docx', 'type': 'docx'},
        {'name': '國際情勢-新冠疫苗開發 (Jerry) 5-23-2020 v2.pptx', 'type': 'pptx'}
    ]
}

mapping = {
    '2018-07-28': (k_2018_07_28, ['Jerry', 'Aegon', 'Vickie', 'Ben', 'Jaaziah']),
    '2018-12-15': (k_2018_12_15, ['Jerry', 'Vickie', 'Ben', 'Jaaziah']),
    '2019-07-27': (k_2019_07_27, ['Vickie', 'Becky', 'Jerry', 'Ben', 'Jaaziah']),
    '2020-04-26': (k_2020_04_26, ['Jerry', 'Vickie', 'Jay', 'Una', 'Howard', 'Paul', 'Becky', 'Lin', 'Ben']),
    '2020-05-23': (k_2020_05_23, ['Jerry', 'Becky', 'Jay', 'Vickie', 'Howard', 'Lin', 'Ben'])
}

for ev in data.get('events', []):
    eid = ev.get('id')
    if eid in mapping:
        k_obj, spk_list = mapping[eid]
        ev['knowledge'] = k_obj
        ev['speakers'] = spk_list
        print('Updated knowledge and speakers for:', eid, ev.get('title'))

with open('timeline_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('timeline_data.js', 'w', encoding='utf-8') as f:
    f.write('window.TIMELINE_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

print('All 5 events successfully updated and synced!')
