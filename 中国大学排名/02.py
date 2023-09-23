import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            hdfd = tds[0].find('div')
            tt = hdfd.string.split()
            ff = "".join(tt)
            attr = tds[1].find('a')
            hh = tds[4].string.split()
            hg = "".join(hh)
            shf = tds[2].text.split()
            shfn = "".join(shf)
            ulist.append([ff, attr.string, shfn, hg])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "省份", "总分", chr(12288)))
    with open('save.txt', 'w+', encoding='utf-8') as f:
        f.write(tplt.format("排名", "学校名称", "省份", "总分", chr(12288)))
        f.write('\n')
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
        with open('save.txt', 'a', encoding='utf-8') as f:
            f.write(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
            f.write('\n')


def main():
    with open('save.txt', 'w+', encoding='utf-8') as f:
        f.write("排名,学校,省份,总分\n")
        f.close()
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 30)


main()
