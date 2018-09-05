from math import asin,sin
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

a.set_raw_values(n1=1, n1s=1.51630, n2=1.51630, n2s=1.6727, n3=1.6727, n3s=1)

for times in range(1):
#计算D光
    LD = []
    DetalLD = []
    r32 = 0
    if not r32:
        a.set_raw_values(r1=105.1175, r2=-74.7353, r3=-219.591)
    a.set_raw_values(d1=5.32, d2=2.5)
    a.do_update()
    ld = a.get_raw_values('l')
    #for i in h:
    #    L3s = a.get_L3s(i)
    #    DetalLD.append(L3s-ld)
    #    LD.append(L3s)

    #print("边光球差：")
    L3ds = a.get_L3s(17)
    now_qc = L3ds-ld
    #print(now_qc)

    #计算C光
    LC = []
    DetalLC = []
    a.set_raw_values(n1=1, n1s=1.51385, n2=1.51385, n2s=1.66662, n3=1.66662, n3s=1)
    a.do_update()
    lc = a.get_raw_values('l')
    L3cs = a.get_L3s(0.707*a.get_raw_values('hm'))



    #计算F光
    LF = []
    DetalLF = []
    a.set_raw_values(n1=1, n1s=1.52191, n2=1.52191, n2s=1.68749, n3=1.68749, n3s=1)
    a.do_update()
    lf = a.get_raw_values('l')
    L3fs = a.get_L3s(0.707*a.get_raw_values('hm'))
    now_sc = L3fs - L3cs

    #print("带光色差：")
    #print(now_sc)

    #正弦差计算
    #print("正弦差：")
    fc = ((0.707*a.get_raw_values('hm'))/a.get_mid_values('sinU3s')) - (17/a.get_mid_values('u3s'))
    osc = (fc-now_qc)/(17/a.get_mid_values('u3s'))
    #print(osc)
    #计算r3目标值
    target_sc = 0
    nf = 1.68749
    nc = 1.66662
    r3p1 =1/a.get_raw_values('r3') + (target_sc-now_sc) / ((nf-nc)*(L3cs*L3fs))
    r32 = 1/r3p1
    print("应得r3 : ",end="")
    print(r32)


    a.set_raw_value('r3',r32)
    a.do_update()

#计算容限
