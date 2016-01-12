#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     19/10/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def setUpCanvas(root):
    root.title("Practice Tk/Python Graphics Program")
    canvas= Canvas(root,width=1270,height=780, bg='GREY30')
    canvas.pack(expand=YES, fill=BOTH)
    return canvas
def disk(x,y,r,kolor):
    return canvas.create_oval(x-r,y-r,x+r,y+r)
def leftBtn(evnt):
    canvas.create_text(evnt.x,evnt.y,text="Hold and move", fill='green',font='times')
def rightBtn(evnt):
    canvas.create_text(200,200,text="Goodbye",fil='cyan',font='times')
def runExampleGraphicsCode():
    obj1=canvas.create_line(100,100,200,200,width=2, fill='GREEN')
    canvas.update()
    obj2=canvas.create_oval(100,100,200,200,width=3,fill='BLUE')
    obj3=disk(300,300,50,'RED')
    obj4=canvas.create_rectangle(500,500,900,600, width=4,fill='YELLOW')
    obj5=canvas.create_rectangle(700,200,703,203,width=1,fill='WHITE')
    obj6a=canvas.create_text(259,280,text="Hello",fill='GREEN',font='times')
    obj6b=canvas.itemconfigure(obj6a,text='Hey!',font='Courier 48')
    obj7=canvas.create_polygon(300,300,400,400,300,400,fill='green',outline='black',width=5,tag='Tag1')
   # photo=PhotoImage(file='thing.gif')
   # print("w=",photo.width(),"c=", photo.height())
    #obj8=canvas.create_image(500,0,image=photo,anchor=NW)
    canvas.update()
    for n in range(100):
        canvas.move(obj7,2,2)
        canvas.update()
        sleep(0.01)
    sleep(0.5)
    canvas.delete('all')
    canvas.create_rectangle(0,0,1270,780,fill='BLACK')

    root.bind('<Button-1>',leftBtn)
    root.bind('<Button-3>',rightBtn)
    root.bind('<B1-Motion>',leftBtn)
    canvas.create_rectangle(100,100,700,600,width=4,fill='GRAY')
    ball1=disk(300,300,10, 'BROWN')
    xInc=2;yInc=2
    for n in range(100):
        canvas.move(ball1,xInc,yInc)
        canvas.update()
        sleep(0.01)
from tkinter import*
from time import clock,sleep
root=Tk()
canvas=setUpCanvas(root)

def main():
    runExampleGraphicsCode()
    print('\n---TOTAL run time=',round(clock()-startTime,2),'seconds.')
    root.mainloop()

if __name__ == '__main__': startTime=clock(); main();
