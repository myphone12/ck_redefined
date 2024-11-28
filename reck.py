import random as r
import json

class DataLoading:

    def __init__(self, set = 'default'):
        self.set = set
        with open('.\\database.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            if self.set in self.data:
                self.database = self.data[self.set]
            else:
                self.database = self.data['default']
            self.CurrentData = self.set

    def CreateTimeSaveDB(self):
        self.TimesDB = {'all':0}
        for i in self.database:
            if i != 'data':
                self.TimesDB[i] = [0,0]

class Ck(DataLoading):

    '''
    This is a class which can get a random result from the
    database with a confirmed probability,and it could also 
    set a confirmed result after some gets.
    '''

    def __init__(self, set='default'):
        super().__init__()
        self.ResultData = []
        self.PrepareCkLoading()
        
    
    def __getitem__(self, num):
        return self.ResultData[num]
    
    def __len__(self):
        return self.TimesDB['all']
    
    def __eq__(self, other):
        if self.set == other.set:
            return True
        return False
    
    def __repr__(self):
        return f'{self.ResultData}'
    
    def PrepareCkLoading(self):
        self.items = {}
        self.probabilitylist = []
        self.CreateTimeSaveDB()
        for i in self.database:
            if i != 'data':
                self.items[i] = self.database[i]
        self.probabilities = {}
        for i in self.database['data']:
            self.probabilities[i] = {}
            for j in self.database['data'][i]:
                if j == 'probability':
                    self.probabilities[i][j] = float(self.database['data'][i][j])
                else:
                    if self.database['data'][i][j] != '0':
                        self.probabilities[i][j] = int(self.database['data'][i][j])
                    else:
                        self.probabilities[i][j] = False
            self.probabilitylist.append(float(self.database['data'][i]['probability']))
        self.probabilitykeys = list(self.probabilities.keys())
        self.CreateProbablityPool()
    
    def CreateProbablityPool(self):
        tmp = []
        for i in self.probabilitylist:
            tmp.append(str(i))
        for i in range(len(tmp)):
            tmp[i] = len(tmp[i])
        maxlen = max(tmp) - 2
        tmp = []
        for i in self.probabilitylist:
            tmp.append(int(i*10**maxlen))
        self.weightlist = tmp

    def getRandomResult(self,data):
        tmp = r.random()
        if tmp <= data:
            return 1
        else:
            return 0

    def Chouka(self):
        tmp = r.choices(self.probabilitykeys, weights=self.weightlist, k=1)[0]
        if self.probabilities[tmp]['BMG']:
            return (tmp,r.choice([0,1]))
        else:
            return (tmp,0)
    
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
