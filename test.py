bx=300
by=300
bxs=0
bys=0
ry=250
rx=250
rxs=3
rys=3
x=250
def setup():
    global bx,bx
    size(600,600)
def draw():
    global bx,by,bys,bxs,ry,rx,rxs,rys,x
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
    rect(20,ry,10,100)
    if keyPressed:
        if key == 'w' and ry>=104:
            ry-=5
        if key == 's' and ry<=396:
            ry+=5
    fill(255,254,0)
    ellipse(bx,by,15,15)
    if keyPressed:
          if key == 'p':
              bxs=-3
              bys=3
          if key == 'c':
              bxs=0
              bys=0
    bx+=bxs
    by+=bys
    if bx<=18:
        bxs=-bxs
    if by>=485:
        bys=-bys
    if by<=120:
        bys=-bys
    if bx>=600:
        bxs=-bxs
    if bx<=40 and by>=ry and by<=ry+100:
        bxs=-bxs
    if bx>=574 and by>=rx and by<=rx+100:
        bxs=-bxs
        bys=-bys
    if bx<=5:
        bxs=0
        bys=0
        bx=width/2
        by=height/2
    if bx>=595:
        bxs=0
        bys=0
        bx=width/2
        by=height/2
        

