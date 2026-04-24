import csv
import qrcode
import time
import os 

#addproduct
class AddProduct:
    def __init__(self, title: str, desc: str, price: int):
        self.title = title
        self.desc = desc
        self.price = price
#income
class Income:
    def __init__(self, incom: int):  
        self.incom = incom

def main():
    print("TEST CRM ")
    print("1-add product\n2-income\n3-qr-generator\n")
    tools = input("Number: ")
    
    if tools == '1':
        title = input("Title: ")
        desc = input("Description: ")
        
        try:
            price = int(input("Price: "))
        except ValueError:
            print("Error ")
            return
        
        product = AddProduct(title, desc, price)
        print(f"Title: {product.title}\nDescription: {product.desc}\nPrice: {product.price}")
        print("saved in product.csv")
        
        with open("product.csv", 'a', newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Title", "Description", "Price"])
            writer.writerow([product.title, product.desc, product.price])
        time.sleep(2)
        os.system("clear")
        os.system("python main.py")
          
    if tools == "2": 
        inco = input("income: ")  
        try:
            incom = int(inco)  
            inw = Income(incom) 
            print("saved income.csv")
            with open("income.csv", 'a', newline="") as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(["income"])
                writer.writerow([inw.incom])
            time.sleep(2)
            os.system("clear")
            os.system("python main.py")
        except ValueError:
            print("Error")
          
    if tools == '3':
        print("QR GENERATOR")
        text = input("Text/URL/ Product: ")
        name = input("name file (without png!): ")

        qrcode.make(text).save(f"{name}.png")
        print(f" {name}.png created")
        time.sleep(2)
        os.system("clear")
        os.system("python main.py")

if __name__ == "__main__":
    main()