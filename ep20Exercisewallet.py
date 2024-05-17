import datetime # สิ่งที่อยู่หลัง Import เรียกว่า Module เทียบได้กับชั้นหนังสือ
#now = datetime.datetime.now()
#nowwithformat = datetime.datetime \
#                .now().strftime('%Y-%m-%d %H:%M:%S')
#print(now)
#print(nowwithformat)

class Wallet:
    __amount = 0 #เป็น Class attribute เพราะ รู้อยู่แล้วว่าเปิดกระเป๋าตังค์มา
                # เป็น 0 อยู่แล้ว เช่นเดียวกับการเปิดบัญชี กำหนดเป็น private เพราะไม่ต้องการให้ assign โดยตรง
                # ให้ไปผ่านที่ process
    def __init__(self,owner):
        self.owner = owner
    def checkBalance(self): #เป็นเงินบาทเท่านั้น , function ใน class ต้องมี self เสมอ เพราะต้องถูกเรียกใช้โดย Instance
        return self.__amount
    def deposit(self,currency,depamount):
        if currency == "TH":
            self.__amount = self.__amount + depamount
        elif currency == "USD":
             self.__amount = self.__amount + (depamount * 35)
        else:
            print("Invalid Currency")
            return
        self.recordTransaction("DEP",depamount)
        return self.checkBalance()
    def withdraw(self,currency,wdamount):
        w_amountTH = 0
        if currency == "TH":
            w_amountTH = wdamount
        elif currency == "USD":
            w_amountTH = (wdamount * 35)
        else:
            print("Invalid Currency")
            self.recordTransaction("ERR1",0)
            return
        if self.__amount >= w_amountTH:
            self.__amount = self.__amount - w_amountTH
        else:
            print("Insufficience Amount")
            self.recordTransaction("ERR2",0)
            return
        self.recordTransaction("WDM",w_amountTH)
        return self.checkBalance() #ต้อง return เพื่อรับค่า
    #def GetAmount(self):
    #   print(self.__amount)
    #    print(self.__class__.__amount)
    def recordTransaction(self,tranType,amount):
        now = datetime.datetime \
                .now().strftime('%Y-%m-%d %H:%M:%S')
        writer = open("transaction.txt","a")
        msg = "{} Transaction Type : {} Amount : {} Balance : {} \n" \
                .format(now,tranType,amount,self.__amount)
        writer.write(msg)
        writer.close() #ทำการเขียน file ต้อง close เสมอ
        
myWallet = Wallet("Phakkhaphon") #ประกาศตัวแปร รับ instance
#myWallet.GetAmount()
balance = myWallet.deposit("TH",10000)
print("Your Balance is {}".format(balance)) 
#balance = myWallet.deposit("USD",10000)
#print("Your Balance is {}".format(balance))
#balance = myWallet.withdraw("TH",10000)
#print("Your Balance is {}".format(balance))