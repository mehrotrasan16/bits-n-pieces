import math #import pi,sin,cos
class DestinationCalculator:
    def __init__(self):
        self.city = {}
        
    def degtorad(self,num):
        return (num * math.pi)/180
        
    def process(self,line):
        cmd = line.split(":")[0]
        if(cmd == "LOC"):
            name = line.split(":")[1]
            lat = float(line.split(":")[2])
            long = float(line.split(":")[3])
            self.city[name] = [lat,long]
            line = name
            
        if(cmd == "TRIP"):
            acct = line.split(":")[1]
            city1 = line.split(":")[2]
            city2 = line.split(":")[3]
            #print(city1)
            
            city1det = self.city[city1]
            city2det = self.city[city2]
            #print(city1det)
            
            city1rad = [self.degtorad(city1det[0]),self.degtorad(city1det[1])]
            city2rad = [self.degtorad(city2det[0]),self.degtorad(city2det[1])]
            #print(city1rad)
            
            abslong = abs(city1rad[1] - city2rad[1])
            #print(abslong)
            delta = math.acos(math.sin(city1rad[0]) * math.sin(city2rad[0]) + math.cos(city1rad[0]) * math.cos(city2rad[0]) * math.cos(abslong))
            res = int(delta * 3963)
            
            line = acct + ":" + city1 + ":" + city2 + ":" + str(res)
        return line;