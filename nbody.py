#!/usr/bin/env python3
"""N-body gravitational simulation."""
import sys, math
G=1.0
class Body:
    def __init__(self,x,y,vx,vy,m,name=''):
        self.x,self.y,self.vx,self.vy,self.m,self.name=x,y,vx,vy,m,name
def step(bodies,dt):
    for a in bodies:
        ax=ay=0
        for b in bodies:
            if a is b: continue
            dx,dy=b.x-a.x,b.y-a.y; r=math.hypot(dx,dy)+0.1
            f=G*b.m/r**2; ax+=f*dx/r; ay+=f*dy/r
        a.vx+=ax*dt; a.vy+=ay*dt
    for b in bodies: b.x+=b.vx*dt; b.y+=b.vy*dt
bodies=[Body(0,0,0,0,100,'Sun'),Body(10,0,0,3,1,'Planet'),Body(15,0,0,2.5,0.5,'Moon')]
for t in range(100):
    step(bodies,0.01)
    if t%20==0:
        print(f"t={t*0.01:.2f}")
        for b in bodies: print(f"  {b.name}: ({b.x:.2f},{b.y:.2f})")
