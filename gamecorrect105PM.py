import turtle
import winsound
winsound.PlaySound("mn.wav",winsound.SND_ALIAS |winsound.SND_ASYNC)
screen = turtle.Screen()
x_max = -218
x_min = -278
y_max = 50
y_min = 23
Pen=False
#Pen Max and Min Coordinates
x_list_max = [-209, 295, -135, 459]
x_list_min = [-291, 232, -203, 418]
y_list_max = [57, -146, 75, 3]
y_list_min = [25, -211, 34, -31]



background=["vaso.gif","imagee.gif","ketrigjeli.gif","won.gif"]
i = 0
a=0


def bye():
   screen.bye()


def upp(x,y):
   global i
   global a
   if( i < len(background)):
   #for i in range(1,4):
        print(i)
        if(x_list_min[a] < x and x < x_list_max[a]):
            if(y_list_min[a]<y and y<y_list_max[a]):
                print("You found it")
                screen.bgpic(background[i])
                screen.update()
                i=i+1
                a=a+1
   else:
      bye()



screen.onclick(upp)
screen=turtle.Screen()
screen.bgpic("ok.gif")
screen.update()
screen.onkey(bye, 'q')
screen.listen()
winsound.PlaySound("mn.wav",winsound.SND_ALIAS |winsound.SND_ASYNC)
turtle.done()

