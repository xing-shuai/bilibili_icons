import urllib.request as rq
import os
import json
from eprogress import LineProgress

url = "https://www.bilibili.com/index/index-icon.json"
save_dir = "bilibili_images/"

res = rq.urlopen(url)
json_str = json.loads(res.read())

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

images = json_str["fix"]
total = len(images)

progress = LineProgress(title='total ' + str(total) + ' images, downloading progress')

for index, im in enumerate(images):
    title, icon_url = im["title"], im["icon"]

    ss = rq.urlretrieve("http:" + icon_url, filename=os.path.join(save_dir, title + "." + icon_url.split('.')[-1]))

    progress.update(int((index + 1) / total * 100))
print("\ndone.")
