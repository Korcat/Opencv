import requests
import json

url = "https://www.baidu.com/s"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.82 ',
    'Cookie': 'BIDUPSID=E4A7151C19DCFAE638D1208573D39B6F; PSTM=1680597898; '
              'BAIDUID=E4A7151C19DCFAE66A9769694F44EF6B:FG=1; BAIDUID_BFESS=E4A7151C19DCFAE66A9769694F44EF6B:FG=1; '
              'BD_UPN=12314753; '
              'BDUSS=QxaDY4SVlDSE41anN3RG95by1qVzVYQ2o1a21JeExLOEg3U3h6dUxORkw1MVZrSVFBQUFBJCQAAAAAAAAAAAEAAABn'
              '-HiRS29yTnVvcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEtaLmRLWi5kdG; '
              'BDUSS_BFESS=QxaDY4SVlDSE41anN3RG95by1qVzVYQ2o1a21JeExLOEg3U3h6dUxORkw1MVZrSVFBQUFBJCQAAAAAAAAAAAEAAABn'
              '-HiRS29yTnVvcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEtaLmRLWi5kdG; '
              '__bid_n=1875510eb6001447af24a0; sugstore=1; '
              'COOKIE_SESSION=0_1_1_1_1_0_1_0_1_0_0_0_0_0_7_2_1689774412_1689774407_1689774405%7C1%230_1_1689774405'
              '%7C1; newlogin=1; BDRCVFR[bPTzwF-RsLY]=mk3SLVN4HKm; BD_HOME=1; '
              'BA_HECTOR=ag8101ag0005a020ag05ahae1ibk0h21o; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
              'ZFY=04JEDf6kiDBzLL3ZNhDIscMtf3BDAs1pmYOX8zQS3gE:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; '
              'PSINO=7; delPer=0; '
              'H_PS_PSSID'
              '=36554_38643_38831_39027_39023_38943_38882_39114_39120_39039_26350_39042_39092_22159_39100_39044; '
              'H_PS_645EC=4302T05GwVvIG8MVrQiidxgv8ylDY2I6OONP76O%2BzAssNFHIqllAwSjfKoTfioDf7oEf; BDSVRTM=270; '
              'channel=google; baikeVisitId=01c576b4-639b-4f66-b1fb-ef8b026453b4',

}
data = {
    "wd": "IP",
}
proxies={
    'http':'60.167.20.6:1133'
}
response = requests.get(url=url, params=data, headers=headers,proxies=proxies)  # 请求参数是data
response.encoding = 'utf-8'
content = response.text  # 返回的是json数据,需要在json中编码
with open('代理.html', 'w', encoding='utf-8') as f:
    f.write(content)
