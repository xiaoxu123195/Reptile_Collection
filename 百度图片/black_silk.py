import requests

headers = {
    'Host': 'image.baidu.com',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsMSw0LDUsOCw3LDYsOQ%3D%3D&word=%E9%BB%91%E4%B8%9D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Cookie': 'BDqhfp=%E9%BB%91%E4%B8%9D%26%26NaN-1undefined%26%26472%26%262; BIDUPSID=61C3471D78389B62142B97E33BB03A7D; PSTM=1635821083; __yjs_duid=1_b1269b7b3bc307374be0c886f3b6f6a41635909726812; indexPageSugList=%5B%22%E4%BA%94%E4%B8%AA%E4%BA%BA%E6%90%9E%E7%AC%91%E5%90%88%E7%85%A7%E9%AB%98%E6%B8%85%E5%9B%BE%E7%89%87%22%2C%22%E4%BA%94%E4%B8%AA%E4%BA%BA%E5%90%88%E7%85%A7%E9%AB%98%E6%B8%85%E5%9B%BE%E7%89%87%22%2C%22%E9%AB%98%E6%B8%85%E9%9B%AA%E5%B1%B1%E5%9B%BE%E7%89%87%22%2C%22%E9%AB%98%E6%B8%85%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87%22%2C%22%E9%AB%98%E6%B8%85%E7%94%B5%E8%84%91%E4%BB%A3%E7%A0%81%E5%9B%BE%E7%89%87%22%2C%22%E9%AB%98%E6%B8%85%E4%BB%A3%E7%A0%81%E5%9B%BE%E7%89%87%22%2C%22%E9%AB%98%E6%B8%85%E9%9B%AA%E5%B1%B1%22%2C%22%E9%AB%98%E6%B8%85%E5%A4%A7%E5%9B%BE%22%2C%22%E9%AB%98%E6%B8%85%E5%9B%BE%E7%89%87%22%5D; BAIDUID=91645807A1A38D332C41BA52547D6AD3:SL=0:NR=10:FG=1; MCITY=-%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDUSS=VZdURJZFZSNzZVenNKdzJhVEdrbHlQcnExRG1KTlRGSFZBbWk1ckw2ZmFiZTlpSVFBQUFBJCQAAAAAAAAAAAEAAAA0im5z06PC5OnkuttvTwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANrgx2La4MdiZU; BDUSS_BFESS=VZdURJZFZSNzZVenNKdzJhVEdrbHlQcnExRG1KTlRGSFZBbWk1ckw2ZmFiZTlpSVFBQUFBJCQAAAAAAAAAAAEAAAA0im5z06PC5OnkuttvTwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANrgx2La4MdiZU; BA_HECTOR=2120al0g0l0k8h8h8k0ho1rs1hcljrj16; ZFY=DWE94331gsJcGLo2R16zztrtcen8McghJ06ekjg4Xk0:C; BAIDUID_BFESS=C6AF49D4A006048FE0B9854B93EFC9C3:FG=1; BDRCVFR[n9IS1zhFc9f]=Ae1_MfEv1LYmLPbUB48ugf; delPer=0; PSINO=2; H_PS_PSSID=31253_26350; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MTljMDg4OTE2MDUwMjMyYTEzMzA5MjBiMWY1MGY1ODUyYzYwNTliYTQ4ODY5YTZlYzJmNjRhMzE0MWZmNTg2OGIzNzc4NDIzMjgzZjcxMTI3OWQ1NWZiMzhkN2Y1Y2VhNmFiYWEyNjRlNmY0YjcwZGE3YzU3MjExZDFlN2FkZDViMWQ5MzkzMDRiNDQ4NWIzNmFhNDYyNjAyZjBiZGNkOQ=='
}
number = 1
for page in range(1, 11):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8800483858498541404&ipn=rj&ct=201326592&is' \
          '=&fp=result&fr=&word=%E9%BB%91%E4%B8%9D&queryWord=%E9%BB%91%E4%B8%9D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid' \
          '=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc' \
          f'=&isAsync=&pn={page * 30}&rn=30&gsm=5a&1657542268753= '
    response = requests.get(url=url, headers=headers)
    json_data = response.json()
    # print(response.json())
    data_list = json_data['data']
    for data in data_list[:-1]:
        title = data['fromPageTitleEnc']
        middleURL = data['middleURL']
        # print(title, middleURL)
        img_data = requests.get(middleURL).content
        with open(f'img/{number}.jpg', mode='wb') as f:
            f.write(img_data)
        number += 1
