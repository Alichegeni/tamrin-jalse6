# from pyfiglet import Figlet
products = []

def show_menu():
    print("1-add qeimat")
    print("2- eddit qeimat")
    print("3- del qeimat")
    print("4- search")
    print("5- show list")
    print("6- buy")
    print("7- exit")

def serch():
    u = input("donbal chi migardi? ")
    for i in range(len(products)):
        if products[i]["name"]== u or str(products[i]["id"])==u:
            print (products[i])
        elif u not in products[i]:
            print("yaft nashod")

def tamoom():
    f = open("paniz.txt", "w")
    for i in range(len(products)):
        newdata = (str(products[i]["id"]) + ","+ products[i]["name"] +","+ str(products[i]["price"])+ ","+ str(products[i]["count"])+"\n")
        f.write(newdata)
    f.close()
    exit()

def loading():
    print("loading...")
    myfile = open("ali.txt","r")
    data = myfile.read().split("\n")
    for i in range(len(data)):
        product_info = data[i].split(",")
        dict = {}
        dict["id"] = int(product_info[0])
        dict["name"] = product_info[1]
        dict["price"] = float(product_info[2])
        dict["count"] = int(product_info[3])
        products.append(dict)
    myfile.close()
    print("welcome")

def ad():  
    i_D = int(input("code? "))
    name = input("name? ")
    pric = float(input("price? "))
    countt = int(input("teedad? "))
    products.append({"id": i_D, "name" : name,"price": pric, "count" : countt})
    print("shod")

def lete():
    iddd = int(input("shomare uni ke mikhai hazf koni bede: "))
    for i in range(len(products)):
        if products[i]["id"] == iddd:
            products.pop(i)
            print("hazf shod")
            print()
            break

def show_list():
    for i in range(len(products)):
        print(products[i]["id"], "\t",products[i]["name"],"\t",products[i]["price"],"\t",products[i]["count"] )

def buy():
    sabad = []
    while True:
        idddd = int(input("id ro bede: "))
        for i in range (len (products)):
            if products[i]["id"]==idddd:
                countt = int(input("chanta mikhai? "))
                if products[i]["count"]>=countt:
                    sabad.append({"name":products[i]["name"],
                                    "price":products[i]["price"],
                                    "count" : countt})
                    products[i]["count"]-=countt
                    print("kharide shod ")
                else:
                    print("we have", products[i]["count"], "az chizi ke mikhaid, enghad ke mikhaid nadarim")
                    print("nadarim")

        inpu = input("edame midi?" )
        if inpu == "no" or inpu== "NO":
            break
        print(sabad)
        total_price = 0
        for i in range (len(sabad)):
            total_price+=sabad[i]["price"]*sabad[i]["count"]
        print("qeimat kol is: ", total_price)

def showedditmenu():
    print("1. name?")
    print("2. price?")
    print("3. count? ")
    print("4. end eddit")

def edit():
    idd = int(input("please enter id: "))
    for i in range (len(products)):
        if products[i]["id"] == idd:
            while True:
                showedditmenu()
                chocho = int(input("yekyo begu: "))
                if chocho == 1:
                    products[i]["name"] = input("esm jadido begu: ")
                elif chocho == 2:
                    products[i]["price"] = input("qeimat jadido begu: ")
                elif chocho == 3:
                    products[i]["count"] = input("teedad jadido begu: ")
                elif chocho == 4:
                    break
                else :
                    print("nemifahamam chi migi")

# f = Figlet(font='standard')
# print (f.renderText('ali  store'))

loading()

while True:
    show_menu()
    choo = int(input("please yekyo entekhab kon: "))
    if choo ==1:
        ad()
    if choo ==2:
        edit()
    if choo ==3:
        lete()
    if choo ==4:
        serch()
    if choo ==5:
        show_list()
    if choo ==6:
        buy()
    if choo ==7:
        tamoom()