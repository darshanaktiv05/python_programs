shelf_1 = {'pro_1': {'jan_cost': [10, 30, 45, 50], 'fab_cost': {'60', '64', '68'}},
           'pro_2': {'jan_cost': {'66', '67', '81', '75'}, 'fab_cost': {'78', '81', '85'}},
           'pro_3': {'jan_cost': {'18', '20'}, 'fab_cost': {'21', '22'}, 'mar_cost': {'22', '23', '24'}},

           }
shelf_2 = {
    'pro_1': {'jan_cost': {'206', '220', '225'}, 'mar_cost': {'180', '170', '165'},
              'apr_cost': {'160', '150', '136'}},
    'pro_4': {'jan_cost': '300', 'fab_cost': {'280', '300', '385'}, 'mar_cost': {'280', '300', '385'},
              'apr_cost': {'360', '376'}},
}
shelf_3 = {'pro_2': {'mar_cost': {'55', '59', '61'}, 'apr_cost': {'53', '64', '55'}}}

class super_store:
    def update_sale_price(self):
        pr_1 = list(shelf_1['pro_1']['jan_cost'])
        for i in pr_1:
            convert = int(i)
            sp = ((convert * 20) / 100) + convert
            print("sales price for product 1 in january: ", sp)
        print("\n")

        pr_1 = list(shelf_1['pro_1']['fab_cost'])
        for i in pr_1:
            convert = int(i)
            sp = ((convert * 30) / 100) + convert
            print("sales price for product 2 in february: ", sp)
        print("\n")

        pr_2 = list(shelf_1['pro_2']['jan_cost'])
        for i in pr_2:
            convert = int(i)
            sp = ((convert * 20) / 100) + convert
            print("sales price for product 1 in january: ", sp)
        print("\n")

        pr_2 = list(shelf_1['pro_2']['fab_cost'])
        for i in pr_2:
            convert = int(i)
            sp = ((convert * 30) / 100) + convert
            print("sales price for product 2 in february: ", sp)
        print("\n")

        pr_3 = list(shelf_1['pro_3']['jan_cost'])
        for i in pr_3:
            convert = int(i)
            sp = ((convert * 20) / 100) + convert
            print("sales price for product 3 in january: ", sp)
        print("\n")

        pr_3 = list(shelf_1['pro_3']['fab_cost'])
        for i in pr_3:
            convert = int(i)
            sp = ((convert * 20) / 100) + convert
            print("sales price for product 3 in february: ", sp)
        print("\n")

        pr_3 = list(shelf_1['pro_3']['mar_cost'])
        for i in pr_3:
            convert = int(i)
            sp = ((convert * 20) / 100) + convert
            print("sales price for product 3 in march: ", sp)

    def create_shelf(self):
        enter_dict = int(input("how many keys you want to add in dictionary: "))
        shelf_4 = {}

        for i in range(enter_dict):
            pro_1 = input("Enter product's name: ")
            month_cost = input("Enter month name's : ")

            shelf_4[pro_1] = month_cost

        print(shelf_4)

    def reset_cost_price(self):
        choose = int(input("enter which shelf you want to make zero cost: "))
        if choose == 1:
            # make_zero = shelf_1
            make_zero = 0
            print("cost of shelf 1 and product and month is now: ", make_zero)
        elif choose == 2:
            # make_zero = shelf_2['pro_1']['jan_cost']
            make_zero = 0
            print("cost of shelf 2 and product and month is now: ", make_zero)
        elif choose == 3:
            # make_zero = shelf_3['pro_1']['jan_cost']
            make_zero = 0
            print("cost of shelf 3 and product and month is now: ", make_zero)
        else:
            print("choose between 1 to 3 numbers.")

    def display_max_min(self):

        p_1_j = list(shelf_1['pro_1']['jan_cost'])
        p_1_f = list(shelf_1['pro_1']['fab_cost'])
        p_2_j = list(shelf_1['pro_2']['jan_cost'])
        p_2_f = list(shelf_1['pro_2']['fab_cost'])
        p_3_j = list(shelf_1['pro_3']['jan_cost'])
        p_3_f = list(shelf_1['pro_3']['fab_cost'])
        p_3_m = list(shelf_1['pro_3']['mar_cost'])
        # maximum
        print("this is maximum of shelf 1")
        print("the maximum of shelf 1 of product 1 in january is: ", max(p_1_j))
        print("the maximum of shelf 1 of product 1 in february is: ", max(p_1_f))
        print("the maximum of shelf 1 of product 2 in january is: ", max(p_2_j))
        print("the maximum of shelf 1 of product 2 in february is: ", max(p_2_f))
        print("the maximum of shelf 1 of product 3 in january is: ", max(p_3_j))
        print("the maximum of shelf 1 of product 3 in february is: ", max(p_3_f))
        print("the maximum of shelf 1 of product 3 in march is: ", max(p_3_m))
        # minimum
        print("\n\nthis is minimum of shelf 1")
        print("the minimum of shelf 1 of product 1 in january is: ", min(p_1_j))
        print("the minimum of shelf 1 of product 1 in february is: ", min(p_1_f))
        print("the minimum of shelf 1 of product 2 in january is: ", min(p_2_j))
        print("the minimum of shelf 1 of product 2 in february is: ", min(p_2_f))
        print("the minimum of shelf 1 of product 3 in january is: ", min(p_3_j))
        print("the minimum of shelf 1 of product 3 in february is: ", min(p_3_f))
        print("the minimum of shelf 1 of product 3 in march is: ", min(p_3_m))

    def avg_cost_sale_shelf(self):
        pr_1 = list(shelf_1['pro_1']['jan_cost'])
        print("the cost of product is: ", pr_1)
        s = 0
        for i in pr_1:
            convert = int(i)
            s = s + convert
        print("total of shelf 1 of month january is: ", s)
        print("average of total cost is: ", s / 4)

        pr_2 = list(shelf_1['pro_2']['jan_cost'])
        print("the cost of product is: ", pr_2)
        s = 0
        for i in pr_2:
            convert = int(i)
            s = s + convert
        print("total of shelf 1 of month january is: ", s)
        print("average of total cost is: ", s / 4)

        pr_3 = list(shelf_1['pro_3']['jan_cost'])
        print("the cost of product is: ", pr_3)
        s = 0
        for i in pr_3:
            convert = int(i)
            s = s + convert
        print("total of shelf 1 of month january is: ", s)
        print("average of total cost is: ", s / 2)


obj = super_store()

# obj.update_sale_price()
obj.create_shelf()
# obj.reset_cost_price()
# obj.display_max_min()
# obj.avg_cost_sale_shelf()
