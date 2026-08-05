from decimal import Decimal


def clicked_calc(calculation_back):

        def sort(index,ans):
            nonlocal calculation_back
            calculation_back.pop(index)
            calculation_back.pop(index)
            calculation_back[index-1]=str(ans)

        while "^" in calculation_back:
            for index, value in enumerate(calculation_back):
                if value == "^":
                    ans = Decimal(calculation_back[index-1]) ** Decimal(calculation_back[index+1])
                    sort(index,ans)


        while "*" in calculation_back or "/" in calculation_back : 
            for index,value in enumerate(calculation_back):
                if value in ["*", "/", "^"]:
                    if value == "*":
                        ans = Decimal(calculation_back[index-1]) * Decimal(calculation_back[index+1])
                        sort(index,ans)
                    elif value == "/":
                        ans = Decimal(calculation_back[index-1]) / Decimal(calculation_back[index+1])
                        sort(index,ans)
        

        while "+" in calculation_back or "-" in calculation_back : 
            for index,value in enumerate(calculation_back):             
                if value in ["+", "-"]:
                    if value == "+":
                        ans = Decimal(calculation_back[index-1]) + Decimal(calculation_back[index+1])
                        sort(index,ans)
                    elif value == "-":
                        ans = Decimal(calculation_back[index-1]) - Decimal(calculation_back[index+1])
                        sort(index,ans)

        print(calculation_back)

calculation_back=["2", "^", "3","+", "4", "/", "2"]

clicked_calc(calculation_back)






