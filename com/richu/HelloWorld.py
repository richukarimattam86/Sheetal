print ("Hello World")

#!/bin/python3
import turtle
import math
import time
import urllib.request
import PIL
from PIL import Image
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

#loading screen
def loadScreen():
    loadWindow = turtle.Screen()
    image = r"C:\Users\richu\IdeaProjects\Python\com\richu\rr.gif"
    loadWindow.addshape(image)
    turtle.shape(image)
    turtle.mainloop()
    # Finally made this work

    # loadWindow.setup(500,400,0,0)
    # loadWindow.bgcolor("red")
    # loadWindow.bgpic('rr.gif)

# def loadScreen():
#     loadWindow = turtle.Screen()
#     loadWindow.setup(500,400,0,0)
#     loadWindow.bgcolor("red")
#     # loadWindow.bgpic("rr.gif")
#
#
loadScreen()
#
# def askEmail():
#     value = input('Enter your email id:')
#     print("The Email ID %s was entered " % (value))
#     print("The Email ID " + value + " was entered")
#
# askEmail()

print("Sheetal is trying merge conflict")

#Reading input value
def askEmail():
    value = input('Enter your email id:')
    print("The Email ID %s was entered " %(value))
    print("The Email ID " + value + " was entered")


# print("Sheetal is trying merge conflict 2222")
#askEmail()

#Using {} for passing params
# first_name = "Sheetal"
# last_name = "Hemrom"
# para = "Hey {1} , My parents named me  {0} {1} . the story of my last name {1} is that it means {1} is  ".format(first_name , last_name)
# # print(para)


# printing fibonacci 0,1,1,2,3,5,8,13......
# prevNum = 1
# fib = 0

# print("I want those changes")

# for x in range(10):
#    print(fib)
#    temp = fib
#    fib = prevNum + fib
#    prevNum = temp


# nested loop

# for x in range (10):
#     for y in range (10):
        # print("{0} {1}".format(x,y))

# def printFibonacci(num):
#     print(num)
#     num = prevNum + printFibonacci(num)



#loadWindow.bgpic("roof.jpg")
#loadWindow.bgcolor("#E1AAE1")
#loadWindow.bgpic(urllib.request.urlopen)
#getImage()

# taylor = turtle.Turtle()
# taylor.shape('square')
# taylor.color('#FF33FC')
# taylor.speed(0)
#
# print(math.sqrt(2))
#
# print ("Hello World")
#
# colors = ['#ffc412','#f5b426','#eca33a','#e2934d',
#           '#d88361','#cf7275','#c56288','#bb529c',
#           '#b241b0','#a831c4','#9e21d7','#9510eb',
#           '#8b00ff']
#
# taylor.penup()
# #taylor.goto(50, -30)
# taylor.pendown()
#
# for x in range(40):
#     taylor.shape('circle')
#     taylor.pensize(10)
#     taylor.pencolor(colors[x % 6])
#     #taylor.pencolor(choice(colors))
#     taylor.width(x / 90 + 1)
#     taylor.back(x/2)
#     taylor.circle(x*5)
#
#     taylor.left(15)
# #taylor.circle(x)
#
#
#
# taylor.penup
# taylor.goto(0, 0) # this is x y position in frame
# taylor.right(190)
# taylor.speed(4)
# taylor.forward(10)
# taylor.write("Hiya!!", align="left", font=("Arial", 14, "bold"))
# time.sleep(1)
# taylor.color('#c56288')
# taylor.write("Hiya!!", align="left", font=("Arial", 14, "bold"))
# taylor.color('#74c161')
# #taylor.write("I'm Sheetal", align="left", font=("Arial", 14, "bold"))
# #taylor.back(20)
# taylor.setheading(90)

# print ("\nPython is awesome" *5)

# # print (
#     "Mary had a little lamb,",
#     "Little Lamb,",
#     "Little Lamb,",
#     "Its fleece was white as snow."
# )

# x = "Mary had a little lamb"
# y = "\nLittle Lamb" *2 # \n is called escape sequence
# z = "\nIts fleece was white as %s." % "snow"
# # print (x + y + z)

# print ("""
# There is something going on here.
# With the three double quotes.
# We will be able to type as much as we want.
# Even 4 lines, or 5 or 6. """
# )

# age = input("How old are you: ")
# height = input("How tall are you: ")
# weight = input("How much do you weigh: ")
# print(" You are {0} old, {1} in height, and {2} in weight.".format(age, height, weight))
# print(" You are %r old, %r in height, and %r in weight." %(age, height, weight))

print("#############")

print("#############")
# Download an image and copy to a specific folder
import requests
def getsaveImage():
    image_url = "https://cdn4.littlethings.com/app/uploads/2017/05/cute-dog-husky-smiling-600x600.jpg"
    file_path = r'c:\Users\richu\Desktop\Resume\richu\cutedog'
    # resource = urllib.urlretriece(src, 'location/on/my/system/foo.png')
    resource = requests.get(image_url, stream=True)
    with open(file_path, 'wb') as cutedog:
        for chunk in r.iter_content(chunk_size=1024):
            length = cutedog.write(chunk)

#Open a particular image
from PIL import Image
image = Image.open('cutedog.jpg')
image.show()

#Image Properties
print(image.format)
print(image.mode)
print(image.size)

print("Good Morning Sheetal")

# def getImage():
#     url = "https://cdn4.littlethings.com/app/uploads/2017/05/cute-dog-husky-smiling-600x600.jpg"
#     resource = urllib.request.urlopen(url)
#     output = open("cutedog.jpg","wb")
#     output.write(resource.read())
#     output.close()
#     # urlretrieve(url, "cutedog.jpg")
#     # loadWindow.bgpic("cutedog")
#     turtle.shape(url)
#     turtle.mainloop()
#
# getImage()