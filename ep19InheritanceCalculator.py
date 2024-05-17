class Calculator:
    def Add(self,a,b):
        return a+b;
    def __changeBattery(self):
        print("Time to Change Battery")
    def _chargeBattery(self):
        print("Time to Charge Battery")
        
class engineerCalculator(Calculator):
    def CalculateSurfaceArea(self):
        super()._chargeBattery() #super ใช้ class function ของพ่อ
        print("Use In Engineer Career")

class Calculator:
    def AggregateDataset(self):
        print("Use In Data Analyst Career")

eng = engineerCalculator()
eng.Add(10,20)
# eng.__changeBattery()
eng._chargeBattery();
eng.CalculateSurfaceArea()