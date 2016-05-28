bx=300
by=300
bxs=0
bys=0
ry=250
rx=250
rxs=3
rys=3
x=250
be1=10
be2=10
be3=10
be4=10
be5=10
be6=10
m=0
z=0
def setup():
    global bx,bx
    size(600,600)
def draw():
    global bx,by,bys,bxs,ry,rx,rxs,rys,x,be6,be5,be4,be3,be2,be1,m,z
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
        m+=1
    if bx>=588:
        bxs=0
        bys=0
        bx=550
        by=300
        z+=1
    rect(10,be1,10,10)
    rect(22,be2,10,10)
    rect(34,be3,10,10)
    rect(580,be4,10,10)
    rect(568,be5,10,10)
    rect(556,be6,10,10)
    if m == 1:
        be1=-10
    if m == 2:
        be2=-10
    if m == 3:
        be3=-10
    if z == 1:
        be4=-10
    if z == 2:
        be5=-10
    if z == 3:
        be6=-10
    if z == 3 or m == 3:
        fill(0,0,0)
        rect(0,0,600,600)
        fill(255,0,0)
        rect(50,50,70,10)
        rect(50,60,10,150)
        rect(50,200,100,10)
        rect(140,140,10,60)
        rect(110,140,30,10)
        rect(300,50,10,170)
        rect(210,50,90,10)
        rect(200,50,10,170)
        rect(210,150,90,10)
        rect(330,50,10,170)
        rect(380,50,10,170)
        rect(430,50,10,170)
        rect(330,50,110,10)
        rect(500,50,10,170)
        rect(500,50,60,10)
        rect(500,135,60,10)
        rect(500,210,60,10)
        rect(50,300,10,170)
        rect(120,300,10,170)
        rect(50,300,80,10)
        rect(50,460,80,10)
        rect(170,300,10,85)
        rect(175,385,10,60)
        rect(190,460,30,10)
        rect(230,300,10,85)
        rect(225,385,10,60)
        rect(220,445,10,25)
        rect(180,445,10,25)
        rect(270,300,10,170)
        rect(270,300,60,10)
        rect(270,385,60,10)
        rect(270,460,60,10)
        rect(370,300,60,10)
        rect(430,310,10,70)
        rect(370,300,10,170)
        rect(380,380,50,10)
        rect(380,390,20,10)
        rect(400,400,10,30)
        rect(410,430,20,10)
        rect(430,440,10,30)
            
        
        
