'''
condtional statements are is to control the flow of control
we have three types control statements in python they are:
1.if
2.if-else
3.if-elif-else
'''
#if statement
movie_name="pokiri"
if (movie_name=="pokiri"):
    print("movie name is ",movie_name)
#if-else

screen_body_ratio=input("enter screen body ratio: ")
if(screen_body_ratio <= "6.5inch"):
    print("mobile device")
else:
    print("not a mobile device")
#if-elif-else
format=str(input("enter type of cricket format: "))
if (format=="test"):
    print("....It is a Test format.....")
elif (format=="odi"):
    print("....It is a one day format.....")
else:
    print("....it is shorter format....")
#video quality
quality=input("Enter video quality 360p,480p,720p,1080p,1440p")
if quality=="360p":
    print("your are watching video in 360p quality..")
elif quality=="480p":
    print("your are watching video in 480p quality..")
elif quality=="720p":
    print("your are watching video in 720p quality..")
elif quality=="1080p":
    print("your are watching video in 1080p quality..")
elif quality=="480p":
    print("your are watching video in 1440p quality..")
else:
    print("your watching either low or high quality video")
#marks
marks=int(input("enter your marks: "))
if marks>=90 and marks<100:
    print("you secured A+ grade")
elif marks>=80 and marks<90:
    print("you secured A grade")
elif marks>=70 and marks<80:
    print("you secured B+ grade")
elif marks>=60 and marks<70:
    print("you secured B grade")
elif marks>=50 and marks<40:
    print("you secured C grade")
elif marks>=40 and marks<30:
    print("you secured D grade")
else:
    print("failed")

