# 下载图片
import urllib
import urllib.request as ur
image_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1585119363436&di=fb7f51e18f075aba8aa0a15bd9406ad2&imgtype=0&src=http%3A%2F%2Fimg.tupianzj.com%2Fuploads%2Fallimg%2F160803%2F9-160P3223920.jpg"

response = ur.urlopen(image_url)

# 图片只能写入本地二进制的格式
# with open('qing.jpg','wb') as fp:
#     fp.write(response.read())

# 另一个写入方式
ur.urlretrieve(image_url, 'chun.jpg')

