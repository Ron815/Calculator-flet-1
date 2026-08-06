import flet as ft
from decimal import Decimal


def main(page: ft.Page):
    
    number_type=["0","1","2","3","4","5","6","7","8","9"]
    symbol_type=["+", "-", "*", "/", "^","."]
    brackets_type=["(", ")"]
    current_number=[]  #list
    current_calculation=[]  #list
    calculation_back=[]
    calculation_back2=[]
    calculation_show=ft.Text(value="", size=15)  
    result=ft.Text(value="", size=20)
    calc_state=True


    def clicked_show(e):
        enter=e.control.content
        nonlocal current_number, current_calculation, calculation_back, calculation_show
        if calc_state==True:
            if result.value !="" and result.value != "Error":
                if enter in symbol_type:
                    current_calculation.clear()
                    current_calculation.append(str(Decimal(result.value)))
                    current_calculation.append(enter)
                    current_number.clear()
                    calculation_back.clear()
                    calculation_back.append(str(Decimal(result.value)))
                    calculation_back.append(enter)
                    result.value=""
                else:
                    return
            
            if (enter in number_type and current_calculation==[]) or (enter in number_type and  current_calculation[-1]!=")"):
                current_number.append(enter)
                current_calculation.append(enter)

            elif enter == "(" :
                if current_calculation==[] or current_calculation[-1]=="(" or current_calculation[-1] in symbol_type:
                    calculation_back.append(enter)
                    current_calculation.append(enter)

            elif enter in symbol_type :
                if current_calculation != [] :

                    if current_calculation[-1] in number_type:

                        if enter != ".":
                            calculation_back.append("".join(current_number))
                            calculation_back.append(enter)
                            current_number=[]
                            current_calculation.append(enter)

                        elif (enter =="." and "." not in current_number)  :
                            current_number.append(enter)
                            current_calculation.append(enter)

                    if current_calculation[-1]==")" and enter !=".":
                        current_calculation.append(enter)
                        calculation_back.append(enter)

            elif  (enter == ")") and (current_calculation!=[]) :
                if  (current_calculation[-1] != "(") and (current_calculation[-1] not in symbol_type):
                    if current_calculation[-1] in number_type:
                        calculation_back.append("".join(current_number))
                        calculation_back.append(enter)
                        current_number=[]
                        current_calculation.append(enter)        

                    elif current_calculation [-1] == ")":        
                        calculation_back.append(enter)
                        current_calculation.append(enter)

        calculation_show.value = "".join(current_calculation)
        page.update()


    def clicked_calc():
        nonlocal calculation_back2
        def sort(index,ans,calculation):
            calculation.pop(index)
            calculation.pop(index)
            calculation[index-1]=str(ans)

    #main
        def calc_main(calculation, start_index="", end_index=""):
            nonlocal calculation_back, calc_state

            if calc_state==True :
                while "^" in calculation:
                    for index, value in enumerate(calculation):
                        if value == "^":
                            try:
                                ans = Decimal(calculation[index-1]) ** Decimal(calculation[index+1])
                                sort(index,ans, calculation)
                            except :
                                result.value="Error"
                                calc_state=False
                                return "Error"

                while "*" in calculation or "/" in calculation : 
                    for index,value in enumerate(calculation):
                            if value == "*":
                                ans = Decimal(calculation[index-1]) * Decimal(calculation[index+1])
                                sort(index,ans,calculation)
                            elif value == "/":
                                try:
                                    ans = Decimal(calculation[index-1]) / Decimal(calculation[index+1])
                                    sort(index,ans,calculation)
                                except :
                                    result.value="Error"
                                    calc_state=False
                                    return "Error"

                while "+" in calculation or "-" in calculation : 
                    for index,value in enumerate(calculation):             
                        if value == "+":
                            ans = Decimal(calculation[index-1]) + Decimal(calculation[index+1])
                            sort(index,ans,calculation)
                        elif value == "-":
                            ans = Decimal(calculation[index-1]) - Decimal(calculation[index+1])
                            sort(index,ans,calculation)

                if start_index != "" :
                    del calculation_back[start_index+1 : end_index+1]
                    calculation_back[start_index] = "".join(calculation)

                result.value = "".join(calculation_back)

            else:
                result.value = "Error"

#action
        if current_calculation!=[] and any(x in current_calculation for x in number_type):
            if current_number!=[]:
                calculation_back.append(str(Decimal("".join(current_number))))
                current_number.clear()

            while calculation_back[-1] in symbol_type or calculation_back[-1] in brackets_type:
                calculation_back.pop()
                current_calculation.pop()

            while calculation_back.count("(") > calculation_back.count(")"):
                    calculation_back.append(")")
                    current_calculation.append(")")

            while ("".join(calculation_back)).find("(") > ("".join(calculation_back).find(")")) :
                calculation_back.insert(0,"(")
                current_calculation.insert(0,"(")
                
            while calculation_back.count("(") < calculation_back.count(")"):
                calculation_back.insert(0,"(")
                current_calculation.insert(0,"(")

            while calculation_back.count("(") > calculation_back.count(")"):
                calculation_back.append(")")
                current_calculation.append(")")

            calculation_back2 = calculation_back.copy()

            while "(" in calculation_back and calc_state==True :
                for index, value in enumerate(calculation_back):
                    if value == "(":
                        start_index=index
                    elif value == ")":
                        end_index=index
                        break

                in_bracket = calculation_back[start_index+1 : end_index]
                calc_main(in_bracket, start_index, end_index)

            
            calc_main(calculation_back)

            calculation_show.value = "".join(current_calculation)
            page.update()



    def clear(): 
        nonlocal current_number, current_calculation, calculation_back, result, calculation_show, calc_state
        current_number.clear()
        current_calculation.clear()
        calculation_back.clear()
        result.value=""
        calc_state=True

        calculation_show.value = "".join(current_calculation)
        page.update()
    
    def back(): 
        nonlocal current_number, current_calculation, calculation_back, result, calculation_show, calc_state, brackets_type, calculation_back2
        if result.value!="":
            calculation_back = calculation_back2.copy()
        result.value=""
        calc_state=True
        if current_calculation != []:
            if current_number != []:
                current_number.pop()

            elif calculation_back != []:
                if list(calculation_back[-1])[-1] in number_type or list(calculation_back[-1])[-1] ==".":
                    current_number=list(calculation_back[-1])
                    current_number.pop()
                    calculation_back.pop()

                elif (calculation_back[-1] in symbol_type) or (calculation_back[-1] in brackets_type):
                    calculation_back.pop()
                    if len(calculation_back) > 0 :
                        if list(calculation_back[-1])[-1] in number_type or list(calculation_back[-1])[-1] =="." :
                            current_number=list(calculation_back[-1])
                            calculation_back.pop()
                            

            current_calculation.pop()
            calculation_show.value = "".join(current_calculation)
            page.update()


    page.add(
        calculation_show,
        result,
        ft.Row(
            controls=[
            ft.Button(content="1", on_click=clicked_show),
            ft.Button(content="2", on_click=clicked_show),
            ft.Button(content="3", on_click=clicked_show),
            ft.Button(content="4", on_click=clicked_show),
        ]
            ),
            
    ft.Row(
            controls=[            
            ft.Button(content="5", on_click=clicked_show),
            ft.Button(content="6", on_click=clicked_show),
            ft.Button(content="7", on_click=clicked_show),
            ft.Button(content="8", on_click=clicked_show),
        ]
            ),
    ft.Row(
            controls=[            
            ft.Button(content="9", on_click=clicked_show),
            ft.Button(content="0", on_click=clicked_show),
            ft.Button(content=".", on_click=clicked_show),
        ]
            ),
    ft.Row(
            controls=[
            ft.Button(content="+", on_click=clicked_show),
            ft.Button(content="-", on_click=clicked_show),
            ft.Button(content="*", on_click=clicked_show),
            ft.Button(content="/", on_click=clicked_show),
        ]
            ),
    ft.Row(
            controls=[
            ft.Button(content="^", on_click=clicked_show),
            ft.Button(content="(", on_click=clicked_show),
            ft.Button(content=")", on_click=clicked_show),     
            ft.Button(content="=", on_click=clicked_calc), 
        ]
            ),
    ft.Row(
        controls=[
                     
            ft.Button(content="←", on_click=back),     
            ft.Button(content="AC", on_click=clear),
        ]
            )
                )
    

if __name__ == "__main__" :
    ft.run(main)