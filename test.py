bx=300 
by=300 
bxs=0 
bys=0 
r=580 
n=280 
def setup(): 
size(600,600) 
def draw(): 
global bxs,bys,bx,by,r,n 
rect(10,10,580,590) 
rect(n,r,70,10) 
ellipse(bx,by,10,10) 
bx-=bxs 
by+=bys 
if by>=574 and bx>=n and bx<=n+70: 
bys=-bys 
if keyPressed: 
if key == 'p': 
bxs=+3 
bys=-3 
if key == 'w' and n>=15: 
n-=5 
if key == 's' and n<=515: 
n+=5 

if bx<=580: 
bxs=-bxs 
if by>=16: 
bys=-bys 
if by<=590: 
bys=-bys 
if bx>=16: 
bxs=-bxs

