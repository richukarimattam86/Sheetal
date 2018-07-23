print ("Hello World")

#!/bin/python3
import turtle
import math
import time
# import urllib.request
# import PIL
# from PIL import Image
#try:
#    from urllib.request import urlretrieve  # Python 3
#except ImportError:
#   from urllib import urlretrieve  # Python 2
from random import shuffle, randrange, choice

# def getImage():
#     url = "https://images.pexels.com/photos/87840/daisy-pollen-flower-nature-87840.jpeg?cs=srgb&dl=plant-flower-macro-87840.jpg&fm=jpg"
#     resource = urllib.request.urlopen(url)
#     output = open("flower.jpg","wb")
#     output.write(resource.read())
#     output.close()
#     #urlretrieve(url, "flower.jpg")
#     loadWindow.bgpic("flower.jpg")
#
# def resizeImage():
#     mywidth = 500
#     img = Image.open('someimage.jpg')
#     wpercent = (mywidth/float(img.size[0]))
#     hsize = int((float(img.size[1])*float(wpercent)))
#     img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
#     img.save('resized.jpg')


loadWindow = turtle.Screen()
loadWindow.setup(500,500)
#loadWindow.bgpic("roof.jpg")
#loadWindow.bgcolor("#E1AAE1")
#loadWindow.bgpic(urllib.request.urlopen)
#getImage()

taylor = turtle.Turtle()
taylor.shape('square')
taylor.color('#FF33FC')
taylor.speed(0)

print(math.sqrt(2))

print ("Hello World")

colors = ['#ffc412','#f5b426','#eca33a','#e2934d',
          '#d88361','#cf7275','#c56288','#bb529c',
          '#b241b0','#a831c4','#9e21d7','#9510eb',
          '#8b00ff']

taylor.penup()
#taylor.goto(50, -30)
taylor.pendown()

for x in range(40):
    taylor.shape('circle')
    taylor.pensize(10)
    taylor.pencolor(colors[x % 6])
    #taylor.pencolor(choice(colors))
    taylor.width(x / 90 + 1)
    taylor.back(x/2)
    taylor.circle(x*5)

    taylor.left(15)
#taylor.circle(x)



taylor.penup
taylor.goto(0, 0) # this is x y position in frame
taylor.right(190)
taylor.speed(4)
taylor.forward(10)
taylor.write("Hiya!!", align="left", font=("Arial", 14, "bold"))
time.sleep(1)
taylor.color('#c56288')
taylor.write("Hiya!!", align="left", font=("Arial", 14, "bold"))
taylor.color('#74c161')
#taylor.write("I'm Sheetal", align="left", font=("Arial", 14, "bold"))
#taylor.back(20)
taylor.setheading(90)





