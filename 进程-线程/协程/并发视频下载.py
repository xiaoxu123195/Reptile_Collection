from gevent import monkey
import gevent
import urllib.request
import ssl

monkey.patch_all()
ssl._create_default_https_context = ssl._create_unverified_context


def my_downLoad(file_name, url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()


with open(file_name, "wb") as f:
    f.write(data)
print('%d bytes received from %s.' % (len(data), url))
gevent.joinall([
    gevent.spawn(my_downLoad, "1.mp4", '视频URL地址'),
    gevent.spawn(my_downLoad, "2.mp4", '视频URL地址2')
])
