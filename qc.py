from math import asin,sin

class Calc(object):
    ##这是一个计算L3'的类
    def __str__(self):
        return "Version:0.1"

#定义参数
    def __init__(self):
        self.raw_data = {
            "r1":62.5,
            "r2":-43.65,
            "r3":-124.35,
            "d1":4.0,
            "d2":2.5,
            "n1":1,
            "n1s":1.51633,
            "n2" : 1.51633,
            "n2s":1.67270,
            "n3" : 1.67270,
            "n3s": 1,
            "u1": 0,
            "hm": 17,
        }
        self.mid_data = {}


    def do_update(self):
        pass
        self.mid_data = self.raw_data

        # 第一曲面
        self.mid_data['i1'] = self.mid_data['hm'] / self.mid_data['r1']
        self.mid_data['i1s'] = self.mid_data['i1'] * self.mid_data['n1'] / self.mid_data['n1s']
        self.mid_data['u1s'] = self.mid_data['i1'] - self.mid_data['i1s']
        self.mid_data['l1s'] = self.mid_data['r1'] + self.mid_data['r1'] * self.mid_data['i1s'] / self.mid_data['u1s']
        self.mid_data['l1'] = self.mid_data['l1s'] - self.mid_data['d1']

        # 第二曲面
        self.mid_data['l2'] = self.mid_data['l1s'] - self.mid_data['d1']
        self.mid_data['u2'] = self.mid_data['u1s']
        self.mid_data['i2'] = self.mid_data['u2'] * (self.mid_data['l2'] - self.mid_data['r2']) / self.mid_data['r2']
        self.mid_data['i2s'] = self.mid_data['n2'] / self.mid_data['n2s'] * self.mid_data['i2']
        self.mid_data['u2s'] = self.mid_data['u2'] + self.mid_data['i2'] - self.mid_data['i2s']
        self.mid_data['l2s'] = self.mid_data['r2'] + self.mid_data['r2'] * self.mid_data['i2s'] / self.mid_data['u2s']

        # 第三曲面
        self.mid_data['l3'] = self.mid_data['l2s'] - self.mid_data['d2']
        self.mid_data['u3'] = self.mid_data['u2s']
        self.mid_data['i3'] = self.mid_data['u3'] * (self.mid_data['l3'] - self.mid_data['r3']) / self.mid_data['r3']
        self.mid_data['i3s'] = self.mid_data['n3'] / self.mid_data['n3s'] * self.mid_data['i3']
        self.mid_data['u3s'] = self.mid_data['u3'] + self.mid_data['i3'] - self.mid_data['i3s']
        self.mid_data['l3s'] = self.mid_data['r3'] + self.mid_data['r3'] * self.mid_data['i3s'] / self.mid_data['u3s']

        self.mid_data['l'] = self.mid_data['l3s']


    def set_raw_values(self,**kwargs):
        if kwargs:
            for j in kwargs:
                self.raw_data[j] = kwargs[j]

    def set_raw_value(self,item,value):
        if item and value:
            try:
                self.raw_data[item] = value
                return item + str(self.raw_data[item])
            except:
                return "更新失败或未找到对应参数"
        else:
            return "参数不全"

    def get_raw_values(self,item):
        return self.raw_data[item]

    def get_mid_values(self,item):
        return self.mid_data[item]

    def get_L3s(self,h):
        # 第一曲面
        U1 = 0
        sinI1 = h / self.mid_data['r1']
        self.mid_data['h1'] = h
        sinI1s = self.mid_data['n1'] / self.mid_data['n1s'] * sinI1
        I1 = asin(sinI1)
        I1s = asin(sinI1s)

        ### U + I = Us + Is
        U1s = U1 + I1 - I1s
        sinU1s = sin(U1s)
        L1s = self.mid_data['r1'] + self.mid_data['r1'] * sinI1s / sinU1s
        L1 = L1s - self.mid_data['d1']

        # 第二曲面
        U2 = U1s
        h2 = (L1 - self.mid_data['r2']) * sin(U1s)
        self.mid_data['h2'] = h2
        sinI2 = h2 / self.mid_data['r2']
        sinI2s = self.mid_data['n2'] / self.mid_data['n2s'] * sinI2
        I2 = asin(sinI2)
        I2s = asin(sinI2s)
        U2s = U2 + I2 - I2s
        sinU2s = sin(U2s)
        L2s = self.mid_data['r2'] + self.mid_data['r2'] * sinI2s / sinU2s
        L2 = L2s - self.mid_data['d2']

        # 第三曲面
        U3 = U2s
        h3 = (L2 - self.mid_data['r3']) * sin(U2s)
        self.mid_data['h3'] = h3
        sinI3 = h3 / self.mid_data['r3']
        sinI3s = self.mid_data['n3'] / self.mid_data['n3s'] * sinI3
        I3 = asin(sinI3)
        I3s = asin(sinI3s)
        U3s = U3 + I3 - I3s
        sinU3s = sin(U3s)
        self.mid_data['sinU3s'] = sinU3s
        L3s = self.mid_data['r3'] + self.mid_data['r3'] * sinI3s / sinU3s
        return L3s
