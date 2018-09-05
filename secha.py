from math import asin,sin
from matplotlib import pyplot as plt
from pylab import linspace
from qc import Calc



#构建点集
h = linspace(0.01, 17, 10000)

#初始化函数
a = Calc()
a.set_raw_values(u1=0, hm=17)


#计算h/hm
y = []
for i in linspace(0.01, 17, 10000):
    y.append(i/a.get_raw_values('hm'))


#计算D光
LD = []
DetalLD = []
a.set_raw_values(r1=105.1175, r2=-74.7353, r3= -215.38763374564763)
a.set_raw_values(d1=5.32, d2=2.5)
a.set_raw_values(n1=1, n1s=1.51633, n2=1.51633, n2s=1.6727, n3=1.6727, n3s=1)
a.do_update()
ld = a.get_raw_values('l')
for i in h:
    L3s = a.get_L3s(i)
    DetalLD.append(L3s-ld)
    LD.append(L3s)
print("h/hm=0.707时球差：",a.get_L3s(0.707*a.get_raw_values('hm'))-ld)
print("h/hm=1时球差：",a.get_L3s(a.get_raw_values('hm'))-ld)
#计算C光

LC = []
DetalLC = []
a.set_raw_values(n1=1, n1s=1.51385, n2=1.51385, n2s=1.66662, n3=1.66662, n3s=1)
a.do_update()
lc = a.get_raw_values('l')
for i in h:
    L3s = a.get_L3s(i)
    DetalLC.append(L3s-ld)
    LC.append(L3s)
    
L3csh = a.get_L3s(a.get_raw_values('hm'))
L3cs = a.get_L3s(0.707*a.get_raw_values('hm'))

#计算F光

LF = []
DetalLF = []
a.set_raw_values(n1=1, n1s=1.52191, n2=1.52191, n2s=1.68749, n3=1.68749, n3s=1)
a.do_update()
lf = a.get_raw_values('l')
for i in h:
    L3s = a.get_L3s(i)
    DetalLF.append(L3s-ld)
    LF.append(L3s)
L3fs = a.get_L3s(0.707*a.get_raw_values('hm'))
L3fsh = a.get_L3s(a.get_raw_values('hm'))
hmsc = L3fsh - L3csh
now_sc = L3fs - L3cs
fc = ((0.707 * a.get_raw_values('hm')) / a.get_mid_values('sinU3s')) - (17 / a.get_mid_values('u3s'))
osc = (fc - now_sc) / (17 / a.get_mid_values('u3s'))

fc2 = ((a.get_raw_values('hm')) / a.get_mid_values('sinU3s')) - (17 / a.get_mid_values('u3s'))
osc2 = (fc2 - hmsc) / (17 / a.get_mid_values('u3s'))

print(r"h/hm = 0.707时色差：",now_sc)
print(r"h/hm = 0.707时正弦差：",osc)
print(r"h/hm = 0.1时色差：",hmsc)
print(r"h/hm = 0.1时正弦差：",osc2)

#计算色差
SC = []
for i in range(len(h)):
    SC.append(LF[i] - LC[i])


fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
axes.plot(DetalLD,y,'y')
axes.plot(DetalLC,y,'r')
axes.plot(DetalLF,y,'b')

#坐标轴
x2 = linspace(0,0,1000)
y2 = linspace(-0.1,1.2,1000)
plt.plot(x2,y2 ,color='black',linewidth=0.7)
axes.set_xlabel('δL^‘ (mm)')
axes.set_ylabel('  h/hm  (mm)')

fig2 = plt.figure()
axes2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes2.plot(SC,y,'b')
plt.plot(x2,y2 ,color='black',linewidth=0.7)
axes.set_xlabel('δL^‘ (mm)')
axes.set_ylabel('  h/hm  (mm)')

plt.show()

    


