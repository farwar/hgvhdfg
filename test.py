bx=300
by=300
bxs=0
bys=0
ry=250
rx=250
rxs=3
rys=3
x=250
lr1=10
lr2=10
lr3=10
lr4=10
lr5=10
lr6=10
jr1=10
jr2=10
jr3=10
jr4=10
jr5=10
jr6=10
be1=10
be2=10
be3=10
be4=10
be5=10
be6=10
m=0
def setup():
    global bx,bx
    size(600,600)
def draw():
    global bx,by,bys,bxs,ry,rx,rxs,rys,x,lr1,lr2,lr3,jr1,jr2,jr3,be1,jr4,jr5,jr6,lr4,lr5,lr6,be6,be5,be4,be3,be2,m
    fill(0,0,0)
    rect(0,0,800,800)
    fill(0,255,0)
    rect(5,100,590,400)
    line(300,100,300,500)
    line(5,300,595,300)
    triangle(275,100,325,100,300,125)
    triangle(275,500,325,500,300,475)
    fill(0,0,255)
    rect(580,rx,10,100)
    if keyPressed:
        if key == 'o' and rx>=104:
            rx-=5
        if key == 'l' and rx<=396:
            rx+=5
    fill(255,0,0)
    rect(10,ry,10,100)
    if keyPressed:
        if key == 'w' and ry>=104:
            ry-=5
        if key == 's' and ry<=396:
            ry+=5
    fill(255,254,0)
    ellipse(bx,by,15,15)
    if keyPressed:
          if key == 'p' and bx>width/2:
              bxs=-3
              bys=3
          if key == 'i' and bx>width/2:
              bxs=-3
              bys=-3
          if key == 'q' and bx<width/2:               
              bxs=3
              bys=3
          if key == 'e' and bx<width/2 :
              bxs=3
              bys=-3
          if key == 'c':
              bxs=0
              bys=0
          if key == 'g':
              bxs=-3
              bys=3
    bx+=bxs
    by+=bys
    if bx<=2:
        bxs=-bxs
    if by>=485:
        bys=-bys
    if by<=120:
        bys=-bys
    if bx>=600:
        bxs=-bxs
    if bx<=30 and by>=ry and by<=ry+100:
        bxs=-bxs
    if bx>=574 and by>=rx and by<=rx+100:
        bxs=-bxs
    if bx<=12:
        bxs=0
        bys=0
        bx=50
        by=300
    if bx>=588:
        bxs=0
        bys=0
        bx=550
        by=300
    rect(10,be1,lr1,jr1)
    rect(22,be2,lr2,jr2)
    rect(34,be3,lr3,jr3)
    rect(580,be4,lr4,jr4)
    rect(568,be5,lr5,jr5)
    rect(556,be6,lr6,jr6)
    if bx<=15:
        m+=1
    if m == 1:
        be1=-10
    if m == 2:
        be2=-10
    if bx>=583:
        m+=1
    if m == 3:
        be3=-10
    if m == 4:
        be4=-10
    if m == 5:
        be5=-10
