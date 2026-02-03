#继承的基础语法

#演示单继承
class Phone: 
    IMET = None #序列号
    producer = "ITCAST" #厂商

    def call_by_4g(self):
        print("4g通信")


class Phone2022(Phone):
    face_id = "10001"  #面部识别ID

    def call_by_5g(self):
        print("2022年新功能：5G通信")

phone = Phone2022()        
phone.call_by_4g()
phone.call_by_5g()

#多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")    


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")        

class Myphone(Phone, NFCReader, RemoteControl):
    pass

phone = Myphone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)


"""
继承中对父类成员的复写和调用
"""
#父类见上面
#定义子类，复写父类成员
class myphone(Phone):
    producer =  "hunan"

    def call_by_4g(self):
        print("开启CPU单核模式，确保通话时省电")
        """
        方式1：
        print(f"父类的厂商是{Phone.producer})
        Phone.call_by_4g(self)
        """
        print(f"父类的厂商是：{super().producer}")
        super().call_by_4g()
        print("关闭CPU单核模式，确保性能")

phone1 = myphone()
phone1.call_by_4g()
print(phone.producer)
#在子类中调用父类        