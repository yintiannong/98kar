import json
import requests
from lxml import etree
def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data


header='''Cookie: UM_distinctid=167cf84267730f-068a64127e7935-5701732-1fa400-167cf84267a602; _dg_check.fead5c35a26d8f7d.b634=-1; _dg_playback.fead5c35a26d8f7d.b634=1; LiveWSMNG38236045=95149363ad4041019fafae40909b0fd9; LiveWSMNG38236045sessionid=95149363ad4041019fafae40909b0fd9; NMNG38236045fistvisitetime=1545374808661; NMNG38236045lastvisitetime=1545374808661; NMNG38236045visitecounts=1; NMNG38236045visitepages=1; NMNG38236045IP=%7C1.202.251.26%7C; NMNG38236045LR_mimiwin=95149363ad4041019fafae40909b0fd9; NMNG38236045LR_lastchat=1; NMNG38236045lastinvite=1545374823975; _dg_id.fead5c35a26d8f7d.b634=6004dc11e63d92a3%7C%7C%7C1545374808%7C%7C%7C1%7C%7C%7C1545374825%7C%7C%7C1545374821%7C%7C%7C%7C%7C%7Cb197e0106dd7a485%7C%7C%7Chttps%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E7%2599%25BE%25E5%2590%2588%25E7%25BD%2591%26oq%3D%2525E5%2525BE%2525AE%2525E5%25258D%25259A%26rsv_pq%3Dfa9378a20007e523%26rsv_t%3Dd73dIRO00Gkc5qjXNqt1g%252BVTMMGt4xoqI1FrGkQVke%252BS5bqm%252BCJjmzsOVqM%26rqlang%3Dcn%26rsv_enter%3D1%26inputT%3D1622%26rsv_sug3%3D11%26bs%3D%25E5%25BE%25AE%25E5%258D%259A%7C%7C%7Chttps%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E7%2599%25BE%25E5%2590%2588%25E7%25BD%2591%26oq%3D%2525E5%2525BE%2525AE%2525E5%25258D%25259A%26rsv_pq%3Dfa9378a20007e523%26rsv_t%3Dd73dIRO00Gkc5qjXNqt1g%252BVTMMGt4xoqI1FrGkQVke%252BS5bqm%252BCJjmzsOVqM%26rqlang%3Dcn%26rsv_enter%3D1%26inputT%3D1622%26rsv_sug3%3D11%26bs%3D%25E5%25BE%25AE%25E5%258D%259A%7C%7C%7C1%7C%7C%7Cundefined; accessID=20181221144738509466; lastLoginDate=Fri%20Dec%2021%202018%2014%3A47%3A38%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29; tempID=0311734984; orderSource=10130301; accessToken=BH1545374868140115923; NTKF_T2D_CLIENTID=guest7D68ECB9-1B5A-1C47-48EF-CF8526373877; Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d=1545374876; AuthCookie=4BFFD62B611D896EC104333FD04597F91B7A4433F902AAEC29337560B4D6F56AC094CA543E0BA97099A623C400A34B150B5A44BC19B908B79BF608CB30C4F468740A0A3FA06C2099A60B62B81CE4DB63125D1D1510136056; AuthMsgCookie=E0793AD56D3A3B1425C22A12225D1E16D2563DD39AB230CE32D30CBAEC77504D6AB1055864A8F60591838E09D94CFA26932E313B73534022E991B252E3754E4D4D334DDD4A3E469EB9BA59038B4142CED75CD2081F27EC21; GCUserID=162677201; OnceLoginWEB=162677201; LoginEmail=13488601496%40mobile.baihe.com; userID=162677201; spmUserID=162677201; AuthCheckStatusCookie=3C95820095DC72A04D7345514D20204314D1D3015978705726A127B203C4931405E9D878DCC812E7; nTalk_CACHE_DATA={uid:kf_9847_ISME9754_162677201,tid:1545374869047183}; _fmdata=7Wwe0mO03oLADt12LXMXC1nUXBj0wqMr%2FB0TQqHpFQxPMWL4jmhKT3JbDAUs5PSEG6rjfsM6Tb8oCTbdA9Hv9O0IAbl9ym2xMeR7z6wvaXY%3D; Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d=1545375452; noticeEvent_162677201=21
Host: profile1.baihe.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'''
oppID=500
header=get_data_from_params(header)
while 1 :
    print(oppID)
    try:
        url = 'http://profile1.baihe.com/?oppID=' + str(oppID)
        text = requests.get(url=url, headers=header).text
        html = etree.HTML(text)
        username = html.xpath('//div[@class="name"]//text()')[3]
        ages = html.xpath('//div[@class="inter"]/p//text()')
        age = ages[0]
        high = ages[2]
        education = ages[4]
        adreess = ages[6]
        labe = ' '.join(html.xpath('//div[@class="inter label"]/span/text()'))
        # c = html.xpath('//div[@class="data"]/dl/dd/text()')
        # house = c[0]
        # car = c[1]
        # belong = c[2]
        # hometown = c[3].strip('\n')
        # price = c[4]
        # job = c[5]

        print( username, age, education, adreess, labe)
        oppID += 1
    except:
        oppID += 1
