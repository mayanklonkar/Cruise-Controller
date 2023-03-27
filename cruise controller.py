from matplotlib import pyplot as plt
import numpy as np

m=1000 
b=1.2
v_ref=100 #goal to reach velocity 100 kmph
#model u=ma+bv
e_list=[]
v_list=[]
v_1 = 0
t=0
v_0=0
e_0=100
error=100
k_p=500
k_d=100
k_i=0.5
dt=0.5
c=0
for i in range (0,300):
    if(v_1>=90 and c==0):
        print("***************************************")
        print(t)
        c=1
        
    error=v_ref - v_1
    e_list.append(error)
    u=k_p*error + k_d*((error-e_0)/dt)+k_i*(sum(e_list))
    a=(u-b*v_0)/m
    v_1=a*dt+v_0
    #v_1=((u*dt)+m*v_0)/(m+(b*dt))
    v_0=v_1
    e_0=error
    t=t+dt
    v_list.append(v_1)
    print(error)


plt.plot(e_list)
plt.plot(v_list)
plt.show()


