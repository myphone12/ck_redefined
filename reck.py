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
        super().__init__(set)
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
        for i in self.TimesDB:
            if i == 'all':
                continue
            if self.TimesDB[i][1] >= self.probabilities[i]['BMG'] and self.probabilities[i]['BMG']:
                self.TimesDB[i] = [0,0]
                return (i,1)
            elif self.TimesDB[i][0] >= self.probabilities[i]['SMG'] and self.probabilities[i]['SMG'] and self.probabilities[i]['BMG']:
                self.TimesDB[i][0] = 0
                return (i,r.choice([0,1]))
            elif self.TimesDB[i][0] >= self.probabilities[i]['SMG'] and self.probabilities[i]['SMG'] and not self.probabilities[i]['BMG']:
                self.TimesDB[i][0] = 0
                return (i, 0)
            if not self.probabilities[i]['BMG']:
                self.TimesDB[i][1] = 0
        return 0

    def ck(self, cishu = 1, ReturnLevel = 0):
        result = []
        if cishu <= 0:
            return None
        for i in range(cishu):
            for i in self.TimesDB:
                if i == 'all':
                    self.TimesDB[i] += 1
                else:
                    for j in range(len(self.TimesDB[i])):
                        self.TimesDB[i][j] += 1
            tmp = self.Chouka()
            baodi = self.Baodi()
            if baodi:
                if baodi[1] == 1:
                    self.TimesDB[baodi[0]] = [1,1]
                    result.append(r.choice(self.database[baodi[0]]['BMG']))
                    continue
                else:
                    self.TimesDB[baodi[0]][0] = 0
                    result.append(r.choice(self.database[baodi[0]]['main']))
                    continue
            if tmp[1] == 1:
                self.TimesDB[tmp[0]] = [1,1]
                result.append(r.choice(self.database[tmp[0]]['BMG']))
                continue
            else:
                self.TimesDB[tmp[0]][0] = 0
                result.append(r.choice(self.database[tmp[0]]['main']))
                continue


        self.ResultData.append(result)
        return result
