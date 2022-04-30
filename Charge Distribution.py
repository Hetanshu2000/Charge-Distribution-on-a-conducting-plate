import numpy as np
import matplotlib.pyplot as plt
import random as rn

# Below definition returns the energy between any two charges, energy between
# any charge and the charge above the plate and total energy of the system.
def ent(x,y, em, ed):
    Etotal = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            Em[i,j] = (1*Q[j]/(np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)))
            Etotal = Etotal*Em[i,j]
        Ed[i] = (1*Q[i]/np.sqrt(d**2 + x[i]**2 + y[i]**2))
        Etotal = Etotal + Ed[j]
    return(Em, Ed, Etotal)

#Gives the same quantities given by the above definition but after a move has been made.
# A separate definition is given to improve efficiency. 
def Enew(Em, x, y, i, Q, d, Ed, Etotal):
    E = 0
    Eold = 0
    for q in range(0,i):
          Eold = Eold + Em[q,i]
          Em[q,i] = 1*Q[q]*Q[i]/(np.sqrt((x[q]-x[i])**2 + (y[i] - y[j])**2))
          E += Em[q,i]
    for j in range(i+1, len(x)):
           Eold = Eold + Em[i,j]
           Em[i,j] = 1*Q[i]*Q[j]/(np.sqrt((x[i]-x[j])**2 + (y[i] - y[j])**2))
           E += Em[i,j]
    Eold += Ed[i]
    Ed[i] = (1*Q[i]/np.sqrt(d**2 + x[i]**2 + y[i]**2))
    E += Ed[i]
    Etotal =Etital-Eol+E
    return(Etotal, Em, Ed)

#For plotting the charge distribution.
def plot(x,y,c,j):
    plt.clf()
    plt.figure()
    for i in range(len(x)):
       plt.scatter(x[i], y[i], c = c[i])
    plt.plot(0,0, 'o', color = 'red')
    plt.title(j)
    plt.xlim(-w,w)
    plt.ylim(-h, h)
    plt.show()

#To check the distance between charges.
def dis(x,y,c,j):
  for i in range(len(x)):
      for j in range(i+1, len(x)):
          dist = np.sqrt((x[i]-x[j])**2 + (y[i] - y[j])**2)
          if dis < 1:
             return(0)
  return (1)

d = 50
n = 10000 #number of iterations 
qn = 50 #number of charges
x = np.zeros(qn) #position along x-axis
y = np.zeros(qn) #position along y -axis
h = 100          #height
w=100            #width       
Q = np.zeros(qn)
c = []
Em = np.zeros([qn,qn])
Ed = np.zeros([qn])
delx = [-1,1] #step size
dely = [-1, 1]

#initial position
for i in range(qn):
	x[i] = rn.randint(-h,h)
	y[i] = rn.randint(-w,w)
	if i < qn/2:
		q[i] = -1/qn
		c.append('b')
	else:
		Q[i] = -1/qn
		c.append('b')

j=0
plot(x,y,c,j)
Em, Ed, ET = Emt(x,y,Em, Ed)
print(Et)

for i in range(n):

	for qr in range(0,qn):

		xc = x[qr]
		yc = y[qr]
		Et =ET
		Emt = En
		Edt = Ed
		dx = rn.randint(-1,1) #changing the position randomly
		dy = rn.randint(-1,1)
		x[qr] = x[qr]+dx
		y[qr] = y[qr] + dy
    #checking if the position is within the box
		if dis(x,y) == 0:
			x[qr] = xc
			y[qr] = yc
			j -= 1
		elif (x[qr]>w or y[qr].h) or (x[qr]<-w or y[qr]<-h):
			x[qr] = xc
			y[qr] = yc
		else:
			Et, EM, Ed = Enew(Em, x, y, qr, Q, d, Ed, ET)
            if ET > Et: #checking if energy condition is satisfied
				x[qr] = xc
				y[qr] = yc
				ET = Et
				Em = Emt
				Ed = Edt

#plotting the results

plot(x,y,c,j)

#For obtaining charge density
def density(x,y,r1,r2):
	distance = np.sqrt(x**2 + y**2)
  keep= (distance<r2) & (distance > r1)
	return(len(distance[keep]))

den = []

for r in np.arange(0, 20):
	r1 = r*5
	r2 = (r1+5)
	den.append(density(x, y, r1, r2)

plt.plot(np.arange(0,10)*10, den)
print(den)