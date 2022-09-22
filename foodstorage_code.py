import json
class food:
    def __init__(self):
        self.file = "test.json"
        # Unhide this below 3 lines code if you are running this program for the first time and again hide it when the new file is created.
        self.lst1 = [{"Food_lst": [{"id": [], "food": [], "type": [], "price": []}]}]
        with open(self.file, mode='w') as w:
            json.dump(self.lst1, w)
        with open(self.file, 'r') as re:
            data = json.load(re)
            self.data = data
            self.lst = data[0]["Food_lst"]
            self.ind_id = self.lst[0]["id"]
            self.ind_fd = self.lst[0]["food"]
            self.ind_ty = self.lst[0]["type"]
            self.ind_pr = self.lst[0]["price"]

class food1(food):
    def add(self):
        with open(self.file, mode ='w') as w:
            s = int(input("How many items you want to add: "))
            for i in range(0, s):
                self.ind_id.clear()
                self.ent_fd = input("Enter food name :")
                self.ent_ty = input("Enter food type(veg/nonveg/drink/sweet) :")
                self.ent_pr = input("Enter food price :")
                # self.ind_id.append(self.ent_id)
                self.ind_fd.append(self.ent_fd)
                self.ind_ty.append(self.ent_ty)
                self.ind_pr.append(self.ent_pr)
        # with open(self.file, mode='w') as y:
                for item in range(len(self.ind_fd)):
                    item+=1
                    self.ind_id.append(item)
            json.dump(self.data, w)
        with open(self.file, 'r') as r:
            json.load(r)
            print("\nFood List :\n")
            for i in range(len(self.ind_id)):
                print(f"{self.ind_id[i]} - {self.ind_fd[i]} - {self.ind_ty[i]} - Rs {self.ind_pr[i]}")
            print("\n")
    def update(self):
        up_lst = int(input("Which List You want to update : "))
        x = up_lst - 1
        with open(self.file, mode='w') as w1:
            self.ind_id.clear()
            self.ind_fd[x] = input("Enter food name : ")
            self.ind_ty[x] = input("Enter food type : ")
            self.ind_pr[x] = int(input("Enter food price : "))
            for item in range(len(self.ind_fd)):
                item+=1
                self.ind_id.append(item)
            json.dump(self.data, w1)
        with open(self.file, 'r') as r1:
            json.load(r1)
            print("\nFood List :\n")
            for i in range(len(self.ind_id)):
                print(f"{self.ind_id[i]} - {self.ind_fd[i]} - {self.ind_ty[i]} - Rs {self.ind_pr[i]}")
            print("\n")
    def delete(self):
        h = int(input("Which List you want to Delete : "))
        g = h-1
        with open(self.file, mode='w') as w:
            # self.ind_id.pop(g)
            self.ind_id.clear()
            self.ind_fd.pop(g)
            self.ind_ty.pop(g)
            self.ind_pr.pop(g)
            for item in range(len(self.ind_fd)):
                item+=1
                self.ind_id.append(item)
            json.dump(self.data, w)
            print("\nFood List :\n")
            for i in range(len(self.ind_id)):
                print(f"{self.ind_id[i]} - {self.ind_fd[i]} - {self.ind_ty[i]} - Rs {self.ind_pr[i]}")
            print("\n")
    def food_list(self):
        print("\nFood List :\n")
        for i in range(len(self.ind_id)):
            print(f"{self.ind_id[i]} - {self.ind_fd[i]} - {self.ind_ty[i]} - Rs {self.ind_pr[i]}")
        print("\n")
    def foodby_id(self):
        with open(self.file, 'r') as r:
            json.load(r)
            print("\nFood BY ID :\n")
            for i in range(len(self.ind_id)):
                print(f"{self.ind_id[i]}")
            print("\n")
            q = int(input("Enter the id you want to show : "))
            food_id = q -1
            print("\nFood List BY ID :\n")
            print(f"{self.ind_id[food_id]} - {self.ind_fd[food_id]} - {self.ind_ty[food_id]} - Rs {self.ind_pr[food_id]}")
            print("\n")
    def foodby_name(self):
        with open(self.file, 'r') as r2:
            json.load(r2)
            print("\nFood By Name :\n")
            for i in range(len(self.ind_fd)):
                print(f"{self.ind_fd[i]}")
            print("\n")
            x = input("Enter name of the food to get the list : ")
            in_ele = self.ind_fd.index(x)
            print("\nFood List By Name :\n")
            print(f"{self.ind_id[in_ele]} - {self.ind_fd[in_ele]} - {self.ind_ty[in_ele]} - Rs {self.ind_pr[in_ele]}")
            print("\n")
    def foodby_type(self):
        with open(self.file, 'r') as r:
            ent = input("Enter food type : ")
            ty_2 = [i for i in range(len(self.ind_ty)) if self.ind_ty[i] == ent]
            print("\nFood List By type :\n")
            for i in ty_2:
                print(f"{self.ind_id[i]} - {self.ind_fd[i]} - {self.ind_ty[i]} - Rs {self.ind_pr[i]}")
            print("\n")
    def sort_fd(self):
        with open(self.file, 'r') as r2:
            json.load(r2)
            print("\nSorting Food By Name :\n")
            for i in range(len(self.ind_fd)):
                print(f"{self.ind_fd[i]}")
            print("\n")
            x = input("Enter name of the food to get the list : ")
            in_ele = self.ind_fd.index(x)
            print("\nSorted Food List By Name :\n")
            print(f"{self.ind_id[in_ele]} - {self.ind_fd[in_ele]} - {self.ind_ty[in_ele]} - Rs {self.ind_pr[in_ele]}")
            print("\n")
    def sort_fd_pr(self):
        with open(self.file, 'r') as r:
            ent = input("Enter price of the food : ")
            ty_2 = [i for i in range(len(self.ind_pr)) if self.ind_pr[i] == ent]
            print("\nSorted Food List By Price :\n")
            for i in ty_2:
                print(f"{self.ind_id[i]} - {self.ind_fd[i]} - {self.ind_ty[i]} - Rs {self.ind_pr[i]}")
            print("\n")
    def ch(self):
        while True:
            try:
                ch = int(input("1.ADD FOOD\n2.Update FOOD\n3.Delete Food\n4.Show Food List\n5.Show Food By Id\n6.Show Food by name\n7.Show Food by Type\n8.Sort Food List by name\n9.Sort Food List by Price\nEnter your Choice: "))
            except ValueError:
                print("\nChoose only digits from the given options(1 to 9)")
                print("\nPlease Follow Our Instructions!")
                continue
            else:
                if ch == 1:
                    self.add()
                if ch == 2:
                    self.update()
                if ch == 3:
                    self.delete()
                if ch == 4:
                    self.food_list()
                if ch == 5:
                    self.foodby_id()
                if ch == 6:
                    self.foodby_name()
                if ch == 7:
                    self.foodby_type()
                if ch == 8:
                    self.sort_fd()
                if ch == 9:
                    self.sort_fd_pr()

obj=food1()
obj.ch()
                    

