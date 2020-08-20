 
class StatisticsCalculator:
    def __init__(self):
        self.totdist = 0
        self.userdist = {}
        self.citycount = {}
        
    def process(self,line):
        acct, city1, city2, dist = line.split(":")[0],line.split(":")[1],line.split(":")[2],line.split(":")[3]
        self.totdist += int(dist)
        
        if(acct not in self.userdist):
            self.userdist[acct] = int(dist)
        else:
            self.userdist[acct] += int(dist)
        
        if(city1 not in self.citycount):
            self.citycount[city1] = 1
        else:
            self.citycount[city1] += 1
        
        if(city2 not in self.citycount):
            self.citycount[city2] = 1
        else:
            self.citycount[city2] += 1
        
        
        #print(sorted(self.userdist.items(),reverse=True, key=lambda item: item[1]))
        
        maxvisits = sorted(self.citycount.items(),reverse=True, key=lambda item: item[1])[0][1]
        topcity = []
        for i in sorted(self.citycount.items(),reverse=True, key=lambda item: item[1]):
            if i[1] == maxvisits:
                topcity.append(i[0])
        topcity.sort()
        
        maxdist = sorted(self.userdist.items(),reverse=True, key=lambda item: item[1])[0][1]
        topaccts = []
        for i in sorted(self.userdist.items(),reverse=True, key=lambda item: item[1]):
            if i[1] == maxdist:
                topaccts.append(i[0])
        topaccts.sort()
       
        
        line = str(self.totdist) +":" +str(topaccts[0]) + ":" + str(topcity[0])
        return line;