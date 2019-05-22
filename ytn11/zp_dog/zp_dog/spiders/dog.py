#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: dog.py
@time: 2019/1/2 21:37
@desc:
'''
import json
import time
import requests

def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

import scrapy
class Dog(scrapy.Spider):
    formdata = '''lientNo: 
userToken: 84DA14F87C3A99FECE624DA6F466C6B0
clientType: 2'''
    formdata=get_data_from_params(formdata)
    name = 'dog'
    def start_requests(self):
        cookies={'zhaopingou_select_city':1}
        url='http://qiye.zhaopingou.com/zhaopingou_interface/find_resumeHtmlResidence?timestamp=1546517982572'
        yield scrapy.FormRequest(url=url,formdata=self.formdata,cookies=cookies)
    def parse(self, response):
        for i in range(1,374):
            cookies={'zhaopingou_select_city':str(i)}
            time.sleep(1)
            times=str(int(time.time()))+str(123)
            yield scrapy.FormRequest(url='http://qiye.zhaopingou.com/zhaopingou_interface/find_resumeHtmlResidence?timestamp='+times,cookies=cookies,formdata=self.formdata,callback=self.parse1)
    def parse1(self,response):
        list1=json.loads(response.text)['resumeHtmlResidenceList']
        key_word = {'预结算员': 471, '信托服务': 432, '机械研发工程师': 1015, '电气工程师': 1018, '烧烤师': 884, '药品市场推广经理/主管': 793,
                    '储备经理人': 199, '文案策划': 581, '美容整形师': 864, '网络推广经理/主管': 136, '葡萄牙语翻译': 505, '数据分析师': 414,
                    '预定部主管': 842, '供应商/采购质量管理': 700, '房地产客服': 437, '彩妆培训师': 867, '会务经理/主管': 276, '工程资料管理': 456,
                    '作家/编剧/撰稿人': 551, '药品研发': 792, '驾驶教练': 623, '电脑操作/打字/录入员': 363, '地勤人员': 622, '导演/编导': 573,
                    '销售业务跟单': 196, '家政保洁': 825, 'Android工程师': 29, '电信网络工程师': 76, '飞机维修机械师': 1008, '针灸、推拿': 818,
                    '汽车销售/经纪人': 232, '服装领班': 729, '广告创意/设计经理/广告创意/设计师': 265, '变压器与磁电工程师': 94, '后勤人员': 364, '园艺师': 942,
                    '韩语/朝鲜语翻译': 507, '电信交换工程师': 73, '数控编程': 766, '区域销售总监': 180, '前厅接待/礼仪/迎宾': 895, '记者/采编': 550,
                    '生产项目经理/主管': 673, '理科教师': 526, '潜水员': 873, '业务分析专员/助理': 224, '钢筋工 ': 480, '电路工程师/技术员': 108,
                    '招商主管': 237, '企业策划人员': 275, '统计员': 358, '中医科医生': 807, '大学/大专应届毕业生': 965, '用户运营': 135, '化妆师': 861,
                    '银行大堂经理': 206, '洗车工': 647, '外语教师': 524, '特效设计师': 1017, '项目总监': 693, 'CAD设计/制图': 151, 'SPA 技师': 911,
                    '数据库工程师/管理员': 1029, '电子商务经理/主管': 318, 'JAVA工程师': 1030, '保险契约管理': 406, '汽车定损/车险理赔': 257,
                    '汽车设计工程师': 746, '部门/事业部管理': 340, '算法工程师': 1038, '图书管理员   文档/资料管理': 975, '电镀工': 638, '机场代表': 852,
                    '油漆工': 481, '证券/投资项目管理': 412, '融资经理/主管': 425, '校对/录入': 560, '质量管理/测试经理': 694, '公司业务客户经理': 210,
                    '文科教师': 527, '店面/展览/展示/陈列设计': 155, '临床研究员': 785, '整经工': 723, '美容整形科医生': 805, '物流专员/助理': 604,
                    '兽医': 812, 'DJ': 589, '兼职': 960, '人事信息系统(HRIS)管': 376, '会籍顾问': 193, '临床协调员': 780, '涂料研发工程师': 733,
                    '货运代理': 600, '演员/模特': 584, '系统集成工程师': 32, '生鲜食品加工/处理': 930, '冲压工': 664, '硬装设计师': 167,
                    '证券/投资客户主管': 419, '促销经理': 308, '救生员': 918, '板房/楦头/底格出格师': 725, '市场分析/调研人员': 305, '副总裁/副总经理': 332,
                    '空调工/电梯工/锅炉工': 640, '意大利语翻译': 503, '银行客户代表': 1043, '质量检验员/测试员': 695, '酒店前台': 848, '宠物护理和美容': 834,
                    '院校教务管理人员': 517, '证券/投资客户总监': 415, '仪表工': 643, '美容店长': 860, '工业设计': 153, '无线电工程师': 91,
                    '给排水/暖通/空调工程': 451, '网站运营总监/经理': 122, '化工技术应用/化工工程师': 731, '销售行政专员/助理': 220, '固定资产会计': 348,
                    '广告创意总监': 267, '营运经理': 675, '瑜伽老师': 915, '心理医生': 819, '转播工程师': 586, '泰语翻译': 508, '网络推广总监': 128,
                    '化验师': 683, '食品加工/处理': 931, '税务专员/助理': 350, '通信技术工程师': 70, '信贷管理/资信评估/分析': 395, '视觉设计师': 1019,
                    '信息技术经理/主管': 53, '咨询员': 542, '媒介专员/助理  公关专员/助理': 288, '猎头/人才中介': 378, '注塑工程师/技师': 987,
                    '保险业务管理': 403, '产品总监': 1059, '特教(特殊教育)': 529, '列车设计与制造': 762, '首席技术执行官CTO/首席信息官CIO': 86,
                    '产品工艺/制程工程师': 978, '专业顾问': 539, '镗工': 666, '厨师/面点师': 891, '洗碗工': 880, '销售运营专员/助理': 226,
                    '版图设计工程师': 95, '采购经理/主管': 1045, '助理/秘书/文员': 361, '奢侈品销售': 926, '店长/经理': 841, '西班牙语翻译': 504,
                    '嵌入式硬件开发': 34, '投资/基金项目经理               ': 423, '游戏产品/策划': 1062, '金融产品经理': 421, '医药化学分析': 783,
                    '防损员/内保': 929, '调墨技师': 564, '银行客户服务': 251, '银行会计/柜员': 401, '化妆师/造型师/服装/道具': 582,
                    '网络管理(Helpdesk)': 47, '岩土工程': 450, '安防主管': 934, '电子技术研发工程师': 89, '产品/品牌专员': 299,
                    '轨道交通工程师/技术员': 1005, '集成电路IC设计/应用工程': 100, 'IT技术支持/维护经理': 46, '汽车零配件销售': 233, 'VIP专员': 241,
                    '呼叫中心客服': 252, '品牌策划': 311, '培训经理/主管': 372, '汽车售后服务/客户服务': 258, '物业机电工程师': 495, '质量管理/测试主管': 704,
                    '美发/发型师': 876, '建筑工程测绘/测量': 461, '物料主管/专员': 617, '软件测试': 61, '航空乘务': 629, '印染工': 717, '硬件工程师': 31,
                    '审计经理/主管': 325, 'Flash设计/开发': 1024, '工艺品/珠宝设计': 148, '楼面经理': 840, 'Python': 1028, 'IT文档工程师': 45,
                    '经销商': 192, '陈列员': 936, '架线和管道工程技术': 462, '区域销售经理/主管': 182, '证券总监/部门经理': 417, '安全员': 473,
                    '酒店管理': 868, '电子／电器/制程工程师': 90, '生产经理/车间主任': 678, '导购员': 935, '淘宝/微信运营专员/主管': 133, '前台/总机/接待': 362,
                    '客服主管': 240, '系统工程师': 56, '包装设计': 154, '压痕工': 559, '酒店试睡员': 870, '车工': 654, '促销主管/督导': 302,
                    '商务经理/主管/专员/助理': 230, '电子工程师/技术员': 87, '市场通路专员': 300, '船舶驾驶/操作     船长': 628, '大学教师': 525,
                    '报关员': 1053, '烫金工': 561, '网店运营': 143, '计算机硬件维护工程师': 36, '平面设计总监': 159, '保险精算师': 201, '传菜主管': 886,
                    '汽车电工': 757, '兼职教师': 518, '互联网产品专员/助理': 1061, '汽车零部件设计师': 756, '中餐厨师': 898, '成本会计': 355,
                    '政府事务管理': 292, '发行管理': 585, '游泳教练': 916, '电工': 641, '控制保护研发工程师': 776, '客房服务员/楼面服务员': 837,
                    '三维/3D设计/制作   多媒体/动画设计': 168, '清洁工': 830, '道路/桥梁/隧道工程技术': 454, '木工': 483, '宾客服务经理': 849,
                    '石油天然气技术人员': 994, '产品运营': 125, '能源/矿产项目管理': 773, '建筑设计师': 448, '设备主管': 682, '空调工程/设计': 114,
                    '促销员/导购': 309, '医疗器械研发': 782, '客服经理': 242, '汽车项目管理': 749, '进出口/信用证结算': 400, '电子/电器维修/保养': 105,
                    '室内装潢设计': 165, '助理业务跟单': 1052, '项目管理': 979, '兼职店员': 937, '保险培训师': 404, 'C＋＋': 1035, '铆工': 658,
                    '采购总监': 1044, '财会助理/文员': 357, '面料辅料开发/采购': 708, '市场/营销/拓展主管': 295, '工程/机械绘图员': 1011, '总监/部门经理': 344,
                    '外籍教师 ': 523, '动物育种/养殖': 948, '切割技工': 668, '电子/电器项目管理': 92, '投资银行业务': 203, '二手车评估师': 260,
                    '钟点工': 828, '网站推广': 312, '餐厅领班': 888, '产品规划工程师': 996, '房地产项目/开发/策划主管/专员': 442, '培训讲师': 534,
                    '招聘经理/主管': 370, '安防系统工程师': 98, '财务分析员': 349, '预定员': 847, '技术研发经理/主管': 977, '护士/护理人员': 822,
                    '质量管理': 938, '印刷排版/制版': 562, '活动执行': 290, '金融服务经理': 204, '婚礼/庆典策划服务': 833, '党工团干事': 971,
                    '俄语翻译': 502, '物流/仓储调度': 612, '会展策划/设计': 279, '保安人员': 491, '供应商开发': 1046, '模拟电路设计/应用工程师': 40,
                    '银行柜员': 393, '金融/经济研究员': 420, '厨工': 881, '无损检测工程师': 767, '机修工': 770, '出纳员': 347, '抹灰工': 477,
                    '儿科医生': 808, '金融租赁': 429, '薪酬福利专员/助理': 382, '入殓师': 1063, '汽车电子工程师': 747, '音乐/美术教师': 520,
                    '公共卫生/疾病控制': 821, 'html5': 1026, '艺术/设计总监': 572, 'COCOS2D-X': 1025, '模特': 592, '配色技术员': 734,
                    '公司业务部门经理/主管': 212, '仿真应用工程师': 38, '临时': 961, '证券/投资客户代表': 416, '销售代表': 185, '促销主管/销售': 932,
                    '生产跟单': 692, '房地产评估': 434, '资产/资金管理': 352, '汽车装饰美容': 758, '珠宝/收藏品鉴定': 433, '销售经理': 174,
                    '房地产店长/经理': 435, '贸易跟单': 1048, '西点师': 900, '校长': 511, '销售运营经理/主管': 229, '供应链总监': 597, '律师助理': 384,
                    '监控维护': 497, '品类管理': 925, '核力/火力工程师': 772, '刨工': 656, '办事处首席代表': 337, '理货/分拣/打包': 611,
                    '大客户销售代表': 184, '公务员/事业单位人员': 974, '保险项目经理/主管': 407, '综合门诊/全科医生': 813, '废气处理工程师': 955, '物流总监': 595,
                    'IT质量管理工程师': 65, '销售培训师/讲师': 227, '公关经理/主管': 285, '化学/化工技术总监': 744, '矿产勘探/地质勘测工程师': 1007,
                    '电商客服': 253, '门卫': 939, '电子元器件工程师': 112, '铲车/叉车工': 632, '仪器/仪表/计量工程师': 99, '选址拓展/新店开发': 303,
                    '绿化工': 496, '行程管理/计调': 851, '系统管理员/网络管理员': 58, '环境/健康/安全经理/主管': 701, '业务跟单经理': 1050, '.NET': 1034,
                    '人力资源总监': 366, '幕墙工程师': 458, '施工队长': 457, '工程造价/预结算': 452, '放映员': 567, '医药项目招投标管理': 795, '吹膜工': 670,
                    '健身房服务': 844, '土木/土建/结构工程师     水利/港口工程技术': 449, '故障分析工程师': 697, '基金项目经理': 422, '汽车安全性能工程师': 751,
                    '核保理赔': 255, '电子商务总监': 319, '服装/纺织设计总监': 156, '砌筑工': 475, '经纪人/星探': 576, '采购材料/设备管理': 707,
                    '导游/票务/旅游顾问': 1056, '员工关系/企业文化/工会  ': 374, '包装工': 633, '会务/会展经理': 281, '网站维护工程师': 50,
                    '管家部经理/主管': 845, '会务/会展专员': 283, '海关事务管理': 601, '铣工': 655, '分公司/代表处负责人': 341, '自动化工程师': 110,
                    '拖压工': 637, '法务经理': 385, '证券/期货/外汇经纪人': 408, 'iOS工程师': 28, 'C': 1032, '卖场经理/店长': 920, '美发培训师': 879,
                    '数据挖掘': 1036, '人力资源专员/助理': 380, '医药销售经理/主管': 801, '养殖部主管': 949, '汽车维修/保养': 259, 'PHP工程师': 1031,
                    '售前/售后技术支持工程师': 51, '业务拓展专员/助理': 222, '平面设计经理/主管': 160, '组装工': 635, '物业专员/助理': 486, '客户代表': 246,
                    '手机维修': 856, '艺术指导/舞美设计': 577, '4S店经理/维修站经理': 231, '销售工程师': 188, '打稿机操作员': 565, '生物工程/生物制药': 777,
                    '瘦身顾问': 910, '混凝土工': 476, '产品/品牌经理': 298, '裱胶工': 569, '项目经理/主管': 607, '浮法操作工(玻璃技术)': 768,
                    'ERP实施顾问': 49, '建筑施工现场管理': 466, '广告文案策划': 270, '生产项目工程师': 674, '夹具工程师/技师': 988, '安全管理': 705,
                    '配菜/打荷': 887, '橱柜设计师': 465, '专柜彩妆顾问(BA)': 865, '食品/饮料检验': 883, '广告美术指导': 269, '供应链管理': 594,
                    '细纱工': 716, '音效师': 578, '高级建筑工程师/总工': 447, '标准化工程师': 67, '发动机/总装工程师': 748, '储备干部': 966,
                    '订单处理员': 608, '供应链经理/主管': 598, '餐饮服务员': 897, '销售主管': 175, '市场主管': 316, '客房管理': 869,
                    '电声/音响工程师/技术员': 104, '设计管理人员': 152, '城市规划与设计': 171, '新媒体运营': 124, '汽车底盘/总装工程师': 754, '产品/品牌主管': 306,
                    '法语翻译': 501, '建筑制图': 173, '健身/美体/舞蹈教练': 914, '无线/射频通信工程师': 72, '手缝工': 727, '房地产销售经理/主管': 217,
                    '网络运营管理': 127, '环境/健康/安全工程师': 699, '品酒师': 885, '安检员': 616, '资产评估': 411, '工装工程师': 771, '总编/副总编': 552,
                    '策略发展总监': 334, '演员/群众演员': 593, '企业培训师/讲师': 379, '保镖': 970, '产品管理': 685, '网站编辑': 137, '内容运营': 126,
                    '西餐厨师': 890, '银行经理/主任': 391, '运输经理/主管': 599, '学徒工': 645, '机动车司机/驾驶': 626, '药品生产/质量管理': 787,
                    '旅游计划调度': 871, '化学操作': 740, '配音员': 579, '生产设备管理': 689, '用户界面（UI）设计': 147, '医疗器械销售': 797, '喷塑工': 644,
                    '美容助理': 862, '钳工': 665, '化妆品研发': 735, '市场/营销/拓展总监': 294, '环境评价工程师': 956, '法务主管/专员  法务助理': 386,
                    '销售助理': 195, '工厂厂长/副厂长': 671, '咨询经理': 541, '舞蹈演员': 591, '旅游产品/线路策划': 872, '用户体验（UE/UX）设计师': 146,
                    '硬件测试': 62, 'Hadoop': 1037, '影视策划/制作人员': 571, '美术编辑/美术设计': 545, '电池/电源开发': 96, '麻醉医生': 816,
                    '贸易/外贸经理/主管/专业/助理': 1049, '促销员': 923, '林业技术人员': 941, '数码直印/菲林输出': 556, '综合业务专员': 397, '饲料销售': 950,
                    'IT技术支持/维护工程师': 44, '移动通信工程师': 75, '媒介经理/主管': 287, '测试/可靠性工程师': 106, '总工程师/副总工程师': 672,
                    '店员/营业员/导购员': 922, '市场企划经理/主管': 307, '大学教授': 512, '保洁': 492, '人力资源主管': 368, '机械工程师': 982,
                    '数据运营': 131, '配置管理工程师': 68, '化验/检验科医师': 810, '宠物护理/美容': 835, '理货员': 927, '志愿者/义工/社会工作者': 963,
                    '其他语种翻译': 510, '样衣工': 718, '成本经理/成本主管': 324, 'IT项目总监': 83, '人力资源经理': 367, '行政专员/助理': 360,
                    'IC验证工程师': 101, '音效设计师': 1020, '有线传输工程师': 71, '医疗器械注册': 788, '船舶工程师': 992, '家用电器/数码产品研发': 102,
                    '高级业务跟单': 1051, '海外游计调': 874, '院长': 824, '工业工程师': 983, '发型助理/学徒': 878, '证券/投资客户经理': 418,
                    '酒店/宾馆销售': 846, '寻呼员/话务员': 247, '个人业务部门经理/主管': 214, '工艺/制程工程师': 687, '后期制作': 575, '网络维修': 857,
                    '财务经理': 321, '制造工程师': 686, '技术研发工程师': 995, '安全消防': 702, '中学教师': 513, '外语培训师': 516, '排版设计': 549,
                    '外汇交易': 396, '预订员': 901, '税务经理/主管': 326, '绩效考核经理/主管': 369, 'IT技术文员/助理': 48, '生产运营管理': 684,
                    '市政工程师': 460, '通信项目管理': 81, '汽车检验/检测': 261, '保安经理': 490, '高尔夫教练': 917, '医药招商': 794, '机械设计师': 1014,
                    '渠道/分销经理/主管': 178, '生产总监': 677, '客户经理/主管': 179, '活动策划': 291, '驻唱/歌手': 590, '网络与信息安全工程师': 59,
                    '半导体技术': 103, '临床推广经理': 799, '医疗器械维修/保养': 790, '维修经理/主管': 985, '电脑放码员': 719, '测试员': 63,
                    '培训专员/助理    ': 375, '机械维修/保养': 761, '复卷工': 570, '工程/设备工程师': 981, '材料工程师': 999, '咨询热线/呼叫中心服务人员': 243,
                    '水运/陆运/空运销售': 614, '万能工': 648, '医疗器械生产/质量管理': 789, '内勤人员': 365, '单证员': 606, '光伏系统工程师': 991,
                    '汽车机械工程师': 755, '销售行政经理/主管': 219, '电子/电器工程师   ': 88, '中国方言翻译': 509, '钳工/机修工/钣金工': 653,
                    '药房管理/药剂师': 820, '成本管理员': 354, '放映管理': 580, '鞋子设计': 158, '文字编辑/组稿': 546, '媒介销售': 289,
                    '中专/职转生': 1057, '视频主播': 587, '工程/设备经理': 980, '证券分析/金融研究': 409, '瓦工': 482, '市场企划专员': 301,
                    '药品市场推广主管/专员/助理': 798, '环保技术工程师': 951, '地铁轨道设计': 769, '普工/操作工': 631, '电子软件开发(ARM/MCU...)': 35,
                    '融资专员/助理': 426, 'IT项目经理/主管': 82, '农艺师': 940, '语音/视频/图形开发': 37, '化工实验室研究员/技术员': 732, '签证业务办理': 1055,
                    '飞行器设计与制造': 1009, '裁床': 714, '服装/纺织/皮革工艺师': 157, '系统分析师': 1042, '会务专员/助理': 278, '缝纫工': 711,
                    '合伙人': 333, '市场/营销/拓展经理': 296, '临床数据分析员': 786, '美容培训师/导师': 863, '客服总监': 238, '合同管理': 390,
                    '服装打样/制版': 710, '电气线路设计': 117, '物流经理/主管': 596, '专业培训师': 532, '客户服务/续期管理': 256, '系统测试': 60,
                    '培训督导': 533, '投资银行财务分析': 424, '银行卡/电子银行业务推广': 208, '运营主管/专员': 123, '医疗管理人员': 802, '舞蹈老师': 528,
                    '保险内勤': 405, '理疗师': 817, '招聘专员/助理': 381, '网络/在线客服': 244, '造纸研发': 736, '信用卡销售': 207, '插花设计师': 943,
                    '水质检测员': 958, '仓库/物料管理员': 618, '买手': 1058, '需求工程师': 1039, '维修工程师': 1012, '化工项目管理': 742, '网店推广': 145,
                    '收银主管': 928, '驯兽师': 836, '浆纱工': 722, '软装设计师': 166, '美体师': 912, '保险核安': 254, '广告制作执行': 268,
                    '服装/纺织设计': 721, '施工员': 464, '营养师': 809, '焊接工程师/技师': 1002, '吊车司机/卡车司机': 646, '财务总监': 327,
                    '售前/售后技术支持管理': 52, '广告客户主管/专员': 264, '纺织工/针织工': 712, '高级软件工程师': 976, '主笔设计师': 544,
                    '保险代理/经纪人/客户经理': 198, '培训助理': 538, '首席运营官COO': 331, 'SEO/SEM': 314, '市场运营': 134, '实习生': 968,
                    '加油站工作员': 969, '招商专员': 194, '洗衣工': 831, '电分操作员': 557, '保险电销': 197, '小学教师': 514, '生产文员': 681,
                    '模具工程师': 984, '科研人员': 973, '主持人/司仪': 583, '宴会管理': 843, '广告客户总监/副总监': 262, '折弯工': 662,
                    '水利/水电工程师': 993, '审计专员/助理': 353, '生产主管/督导/组长': 679, '模具工': 652, '监察人员': 439, '财务主管/总帐主管': 322,
                    '代驾': 624, '化工研发工程师': 738, '服装/纺织/皮革跟单': 235, '信审核查': 398, '橡胶工程师': 743, '烫工': 726,
                    '网络运营专员/助理': 130, '国外求职': 962, '信息技术标准化工程师': 66, 'IT项目执行/协调人员': 84, '装配工程师/技师': 986, '玩具设计': 150,
                    '销售总监': 1021, '汽车机构工程师': 745, '护理主任/护士长': 811, '送餐员': 903, '炼胶工': 669, '仓库经理/主管': 605,
                    '固废处理工程师': 954, '水族馆表演演员': 875, '调色员': 553, '培训策划': 535, '团购业务员': 191, '电话销售': 189, '培训/课程顾问': 537,
                    '科研管理人员': 972, '灯光师': 566, '房地产中介/置业顾问/销售': 218, '职业技术教师': 522, '光源与照明工程': 1013, '企业/业务发展经理': 274,
                    'IT质量管理经理/主管': 69, 'web前端': 1022, '高级硬件工程师': 30, '信息技术专员': 55, '猎头顾问/助理': 377, '服装/纺织品/皮革质量管理': 728,
                    '医药学术推广': 779, '生态治理/规划': 952, '冲压工程师/技师': 989, '综合业务经理/主管': 213, '空调维修': 854, '数据通信工程师': 74,
                    '行政经理/主管/办公室主任': 359, '集装箱业务': 609, '调酒师/茶艺师/咖啡师/吧台员/侍酒师': 893, '广告/会展业务拓展': 272, '编辑出版': 548,
                    '网页设计/制作/美工': 162, '船舶维修/保养': 764, '物业招商/租赁/租售': 489, '市场助理': 297, '保险产品开发/项目策划': 402,
                    '工程/设备主管': 998, '运营总监': 343, '行政主厨': 889, '美发店长': 877, 'CNC工程师': 1003, '电脑维修': 855, '环境监测工程师': 957,
                    '银行客户总监': 215, '会务/会展主管': 282, '网站策划': 138, '工程监理/质量管理': 453, '研究生': 964, '渠道/分销专员': 186,
                    '体育教师': 521, '电器项目管理': 115, '行李员': 838, '车床/磨床/铣床/冲床工': 651, '电器研发工程师': 109, '广告客户代表': 271,
                    '化学分析': 739, '纸样师/车板师': 709, '资金专员': 351, '智能大厦/布线/弱电/安防': 463, '风险控制': 399, '高级客户经理/客户经理': 211,
                    '磨工': 663, '律师/企业律师/法律顾问': 383, '工程总监': 455, '银行客户经理': 250, '送水工': 832, '培训生': 967, '列车维修/保养': 763,
                    '包装工程师': 691, '药品注册': 781, '理财顾问/财务规划师': 200, '财务分析经理/主管': 323, '裁剪工': 713, '风险管理/控制/稽查': 427,
                    '护工': 829, '搬运工': 603, '清算人员': 394, '医药技术研发人员': 784, '挡车工': 715, '物料经理': 619, '绩效考核专员/助理': 373,
                    '场长(农/林/牧/渔业)': 944, '网店模特': 588, '行政总监': 346, '业务分析经理/主管': 221, '营运主管': 676, '医药技术研发管理人员': 778,
                    '美容顾问': 858, '建筑工程师': 459, '大堂经理/领班': 896, '首席财务官CFO': 320, '校长/副校长': 342, '客服专员/助理': 248,
                    '房地产资产管理': 440, '原画师': 169, '网络/在线销售': 190, '客户关系/投诉协调人员': 245, '现场应用工程师（FAE）': 107, '大客户销售经理': 181,
                    '印刷机械机长': 563, '销售数据分析': 228, '英语翻译': 498, '眼科医生/验光师  ': 823, '电气设计': 116, '脚本开发工程师': 1027,
                    '首席执行官CEO/总裁/总经理': 330, '电话采编': 547, '房地产项目招投标': 438, '娱乐服务员': 905, '水处理工程师': 953, '合规主管/专员': 389,
                    '物业维修员  物业机电维修工': 487, '气动工程师': 760, '建筑工程验收': 468, '摄影师/摄像师': 574, '汽车质量管理': 752, '家教': 519,
                    '广告/会展项目管理': 273, '融资总监': 428, '商务专员/助理': 223, '钢筋工': 649, '开发报建': 470, '电力工程师/技术员': 990,
                    '汽车动力系统工程师': 753, '化验/检验': 706, '施工开料工': 479, '渠道/分销总监': 177, '媒介策划/管理': 293, '旅游产品销售': 1054,
                    '团购经理/主管': 183, '采购专员/助理': 1047, '网店管理员': 144, '投资者关系': 336, '游戏测试': 64, '高级物业顾问/物业顾问': 488,
                    '水工/木工/油漆工': 639, '列车乘务    公交/地铁乘务   列车乘务   ': 625, '医疗器械推广': 796, '互联网产品经理/主管': 1060,
                    '飞机驾驶/操作': 620, '环境管理/园林景区保护': 959, '水运/空运/陆运操作': 613, '客户关系经理/主管': 239, '房地产内勤': 436,
                    '股票/期货操盘手': 410, '停车管理员': 494, '技工': 642, '外科医生': 814, '美容师/美甲师': 859, '日式厨师': 899, '游戏界面设计师': 170,
                    '前台迎宾': 906, '切纸机操作工': 558, '空调/热能工程师': 1006, '汽车装配工艺工程师': 750, '汽车/摩托车工程师': 759,
                    '认证/体系工程师/审核员': 698, '锅炉工程师/技师': 1004, '钻工': 657, '公关总监': 284, '机电工程师': 1010, '游戏开发/设计': 1023,
                    '通信电源工程师': 77, '按摩/足疗': 913, '户外/游戏教练': 919, '结构工程师': 1000, '通信研发工程师': 79, '广告客户经理': 263,
                    '电焊工/铆焊工': 634, '架构师': 85, '医药项目管理': 791, '厨师助理/学徒': 892, '通信标准化工程师': 80, '建筑安装施工员': 474,
                    '投资/理财服务': 431, '财务顾问': 328, '建筑机电工程师': 467, '金融产品销售': 202, '牙科医生': 815, '建筑项目助理': 472,
                    '公关专员/助理': 286, '电子商务专员/助理': 317, '增值产品开发工程师': 78, '列车驾驶/操作': 621, '配色工': 724, '收货员': 933,
                    '企业秘书/董事会秘书': 335, '面点师': 924, '办事处/分公司/分支机构经理': 345, '学术推广': 310, '德语翻译': 500, '情报信息分析人员': 413,
                    '收银员': 839, '医药代表': 800, '清洁服务人员': 850, '咨询项目管理': 530, '电力线路工': 636, '畜牧师': 946, '医学影像/放射科医师': 806,
                    '培训产品开发': 536, '微信推广': 132, '钣金工': 667, '服装/纺织品/皮革销售': 234, '印刷操作': 568, '市场/营销/拓展专员': 304,
                    '抛光工': 659, '化学制剂研发': 741, '装订工': 554, '激光/光电子技术': 119, '技术文档工程师': 690, '音频/视频工程师/技术员': 41,
                    '房地产投资分析': 444, '总裁助理/总经理助理': 338, '漂染工': 720, '上门沐浴': 1064, '船务/空运陆运操作': 610, '射频工程师': 93,
                    '拍卖/担保/典当业务': 430, '家具设计 | 家居用品设计': 149, '楼宇自动化': 469, '生产计划/物料管理(PMC)': 680, '品牌/连锁招商管理': 921,
                    '咨询总监': 540, '交通管理员': 630, '商务经理/主管   商务专员/助理': 225, '其他': 650, '硫化工': 660, '会计经理/会计主管': 329,
                    '月嫂': 827, '银行客户主管': 249, '招商经理': 236, '平面设计': 161, '物流销售': 615, '电梯工': 484, '数控操作': 765,
                    '注塑工': 661, '幼教': 515, '业务拓展经理/主管': 176, '调研员': 543, '浇注工': 478, 'IT技术总监/经理/主管': 54, '娱乐领班': 904,
                    '食品/饮料研发': 882, '嵌入式软件工程师': 43, '塑料工程师': 737, '可靠度工程师': 696, '阿拉伯语翻译': 506, '家电维修': 853, '传菜员': 902,
                    '物业经理/主管': 485, '网店店长': 142, '光源/照明工程师': 113, '专科医生': 804, '快递员/速递员': 602, 'ERP技术/开发应用': 42,
                    '美容师': 866, '质量管理/测试工程师': 703, '合规经理': 387, '家政服务/保姆/育婴师/保育员': 826, '市场通路经理/主管': 315,
                    '服装/纺织/皮革项目管理': 730, '晒版员': 555, '日语翻译': 499, '铸造/锻造工程师/技师': 1001, '个人业务客户经理': 216,
                    '薪酬福利经理/主管': 371, '网络工程师': 57, '线路结构设计': 118, '行长/副行长': 392, '电力电子研发工程师': 775, '知识产权/专利/商标': 388,
                    '房地产项目/开发/策划经理': 441, '船员/水手': 627, '园林/景观设计': 945, '杂工': 894, '网店美工': 164, '物业设施管理人员': 493,
                    '动物营养/饲料研发': 947, '绘画': 163, '市场文案策划': 313, '内科医生': 803, '会计/会计师': 356, '房产项目配套工程师': 443,
                    '实验室负责人/工程师': 997, '网络推广专员': 129, '咨询师': 531, '房地产项目管理': 445, '电力系统研发工程师': 774}
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
        for j in key_word:
            for i in list1:
                time.sleep(1)
                times = str(int(time.time())) + str(123)
                formdata='''pageSize: 0
    pageNo: 25
    keyStr: 
    companyName: 
    schoolName: 
    postionStr: 
    startDegrees: -1
    endDegress: -1
    startAge: 0
    endAge: 0
    gender: -1
    keyStrPostion: 341
    region: 
    timeType: -1
    startWorkYear: -1
    endWorkYear: -1
    beginTime: 
    endTime: 
    isMember: -1
    hopeAdressStr: 
    cityId: 1
    updateTime: 
    tradeId: 
    startDegreesName: 
    endDegreesName: 
    tradeNameStr: 
    regionName: 
    isC: 1
    is211_985_school: 0
    clientNo: 
    userToken: 84DA14F87C3A99FECE624DA6F466C6B0
    clientType: 2'''
                formdata=get_data_from_params(formdata)
                url3='http://qiye.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new?timestamp='+times
                formdata['cityId']=str(i['city']['id'])
                formdata['postionStr']='web前端'
                formdata['keyStrPostion']='1031'
                formdata['region']=i['residenceName']
                # print(formdata)
                yield scrapy.FormRequest(url=url3,formdata=formdata,callback=self.parse2,headers=headers)

    def parse2(self,response):
        print(response.text)
        # dict1=json.loads(response.text)
        # print(dict1)
        # for i in dict1['warehouseList']:
        #     pass

           # print(i)
    #  def start_requests(self):
    #     for i in range(4,19):
    #         self.formdata['parentId'] = str(i)
    #
    #         yield scrapy.FormRequest(url=url,formdata=self.formdata)
    # def parse(self, response):
    #     dict1=json.loads(response.text)
    #     a=dict1['listFenLeiData']
    #     list1=[]
    #     for i in a:
    #         list1.append(i['positionName'])
    #     print(list1)


        #
        # for cityid in range(1,374)
        #     for i in a:
