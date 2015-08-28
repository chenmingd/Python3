#! /usr/bin/env python3
#-*- coding:utf-8 -*-
'系统默认自带的常用的模块'

from datetime import datetime
now=datetime.now()
print(now,type(now))

datetime=datetime(2015,4,8,12,33,33)
print(datetime,datetime.timestamp())

from collections import namedtuple
Point=namedtuple("Point",['x','y'])
p=Point(1,2)
print(p)

import hashlib
md5=hashlib.md5()
md5.update("chenmd and helan an 小胡吧".encode("utf-8"))
print(md5.hexdigest())

md5=hashlib.md5()
md5.update("chenmd and".encode("utf-8"))
md5.update(" helan an 小胡吧".encode("utf-8"))
print(md5.hexdigest())

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
im=Image.open("d:/data/1.jpg")
# 获得图像尺寸:
w,h=im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save("D:/data/thumbnail.jpg","jpeg")

#生成验证码
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf",36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('D:/data/code.jpg', 'jpeg')

