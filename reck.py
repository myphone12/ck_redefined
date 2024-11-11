import random as r
import json

class DataLoading:

    def __init__(self, set = 'default'):
        with open('.\\database.json', 'r', encoding='utf-8') as file:
            self.data = json.loads(file)
        if not isinstance(set,list):
            if set in self.data:
                self.data = self.data[set]
            else:
                self.data = self.data['default']

        self.dt=[0,0,0,0,0]

class Ck(DataLoading):

    '''
    This is a class which can get a random result from the
    database with a confirmed probability,and it could also 
    set a confirmed result after some gets.
    '''

    def __init__(self, set='default'):
        super().__init__()
    
    def __getitem__(self, num):
        return self.ResultData[num]
    
    def __len__(self):
        return self.dt[0]
    
    def __eq__(self, other):
        if self.set == other.set:
            return True
        return False
    
    def __repr__(self):
        return f"{self.ResultData}"
    
    def getRandomResult(self,data):
        tmp = r.random()
        if tmp <= data:
            return 1
        else:
            return 0

    def Chouka(self):
        if self.getRandomResult(self.Gold):
            return r.choice([3,4])
        elif self.getRandomResult(self.Purple):
            return r.choice([1,2])
        else:
            return 0
    
    def Baodi(self):
        if self.dt[4] >= self.GoldDabaodi and self.GoldBaodi:
            return 4
        elif self.dt[3] >= self.GoldBaodi and self.GoldBaodi:
            return 3
        elif self.dt[2] >= self.PurpleDabaodi and self.PurpleBaodi:
            return 2
        elif self.dt[1] >= self.PurpleBaodi and self.PurpleBaodi:
            return 1
        else:
            return 0
    
    def getItemLevel(self):
        Level = 0
        for i in range(len(self.dt)):
            self.dt[i] += 1
        Level = self.Baodi()
        if Level == 0:
            Level = self.Chouka()
        if Level > 0:
            if Level == 4:
                self.dt[3] = 0; self.dt[4] = 0
            elif Level == 2:
                self.dt[2] = 0; self.dt[1] = 0
            else:
                self.dt[Level] = 0
        return Level
    
    def ck(self, cishu = 1, ReturnLevel = 0):
        result = []
        a = []
        if cishu <= 0:
            return None
        for i in range(cishu):
            a.append(self.getItemLevel())
            if a[i] == 0:
                result.append(r.choice(self.data['Blue']))
            if a[i] == 1:
                result.append(r.choice(self.data['Purple']))
            if a[i] == 2:
                result.append(r.choice(self.data['UPpurple']))
            if a[i] == 3:
                result.append(r.choice(self.data['Gold']))
            if a[i] == 4:
                result.append(r.choice(self.data['UPGold']))
        self.ResultData.append(result)
        if ReturnLevel:
            return (result,a)
        return result
