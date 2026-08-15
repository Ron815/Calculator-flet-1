import flet as ft
from decimal import Decimal


def main(page: ft.Page):
    
    number_type=["0","1","2","3","4","5","6","7","8","9"]
    symbol_type=["+", "-", "*", "/", "^","."]
    brackets_type=["(", ")"]
    current_number=[]  #list
    current_calculation=[]  #list
    calculation_back=[]
    calculation_back_copy=[]
    calculation_show=ft.Text(value="", size=15)  
    result=ft.Text(value="", size=20)
    calc_state=True

    def change_list(action_type, list1, list2=[""], value=""):
        if action_type =="append":
            list1.append(value)
            list2.append(value)
        elif action_type =="pop":
            list1.pop()
            list2.pop()
        elif action_type == "clear":
            list1.clear()
            list2.clear()
        else:
            return

    def clicked_show(e):
        enter=e.control.content
        nonlocal current_number, current_calculation, calculation_back, calculation_show, calculation_back_copy, number_type
        if calc_state==True:
            if result.value !="" and result.value != "Error":    

                if enter in symbol_type:
                    change_list("clear", current_calculation, calculation_back)

                    if Decimal(result.value) < Decimal("0"):
                        change_list("append", current_calculation, calculation_back, "(")
                        for value in list(str(float(result.value))):
                            change_list("append", current_calculation, current_number, str(value))
                        calculation_back.append("".join(current_number))
                        current_number.clear()

                    else:
                        change_list("append", str(Decimal(result.value)))

                    change_list("append",current_calculation, calculation_back, enter)
                    current_number.clear()
                    calculation_back_copy.clear()
                    result.value=""

                    calculation_show.value = "".join(current_calculation)
                    page.update()

                elif enter in number_type:
                    change_list("clear", current_calculation, calculation_back)
                    change_list("append", current_calculation, current_number)            
        #number
            if (enter in number_type and current_calculation==[]) or (enter in number_type and  current_calculation[-1] != ")"):
                change_list("append", current_calculation, current_number, enter)

        #left bracket
            elif enter == "(" :
                if current_calculation==[] or current_calculation[-1] == "("   or  (current_calculation[-1] in symbol_type) :
                    if current_calculation != []: 
                        if current_calculation[-1] != ".":
                            change_list("append",current_calculation, calculation_back, enter)
                    else:
                        change_list("append", current_calculation, calculation_back, enter)

        #symbol
            elif enter in symbol_type :
                if current_calculation != [] :

                    if current_calculation[-1] in number_type:

                        if enter != ".":
                            calculation_back.append("".join(current_number))
                            if "-" in current_number:
                                change_list("append", current_calculation, calculation_back, ")")

                            change_list("append",current_calculation, calculation_back, enter)
                            current_number=[]
                            
                        elif (enter =="." and "." not in current_number)  :
                            change_list("append", current_calculation, current_number, enter)

                    elif current_calculation[-1]==")" and enter !=".":
                        change_list("append",current_calculation,calculation_back, enter)

                    elif ((current_calculation[-1] in symbol_type) or (current_calculation[-1] == "(" )) and (enter == "-") and (current_calculation[-1] != ".") :
                        if current_calculation[-1] in symbol_type:
                            change_list("append", current_calculation, calculation_back, "(")
                            change_list("append", current_calculation, current_number, enter)
                        elif current_calculation[-1] == "(":
                            change_list("append", current_calculation, current_number, enter)

                elif enter == "-":
                    change_list("append", current_calculation, calculation_back, "(")
                    change_list("append", current_calculation, current_number, enter)


        #right bracket 
            elif  (enter == ")") and (current_calculation!=[]) :
                if  (current_calculation[-1] != "(") and (current_calculation[-1] not in symbol_type):
                    if current_calculation[-1] in number_type:
                        calculation_back.append("".join(current_number))
                        current_number=[]
                        change_list("append", current_calculation, calculation_back, enter)

                    elif current_calculation [-1] == ")":        
                        change_list("append", current_calculation, calculation_back ,enter)


        calculation_show.value = "".join(current_calculation)
        page.update()


    def clicked_calc():
        nonlocal calculation_back_copy                        

    #main
        def calc_main(calculation, start_index="", end_index=""):
            nonlocal calculation_back, calc_state

            if calc_state==True :
                while "^" in calculation:
                    for index, value in enumerate(calculation):
                        if value == "^" and "^" not in calculation[index+1:] :
                            calculation[index-1:index+2] = [str(Decimal(calculation[index-1])**Decimal(calculation[index+1]))]

                while "*" in calculation or "/" in calculation : 
                    for index,value in enumerate(calculation):
                            if value == "*":
                                calculation[index-1:index+2] = [str(Decimal(calculation[index-1]) * Decimal(calculation[index+1]))]
                                
                            elif value == "/":
                                try:
                                    calculation[index-1:index+2] = [str(Decimal(calculation[index-1]) / Decimal(calculation[index+1]))]
                                    
                                except :
                                    result.value="Error"
                                    calc_state=False
                                    return "Error"

                while "+" in calculation or "-" in calculation : 
                    for index,value in enumerate(calculation):             
                        if value == "+":
                            calculation[index-1:index+2] = [str(Decimal(calculation[index-1]) + Decimal(calculation[index+1]))]
                            
                        elif value == "-":
                            calculation[index-1:index+2] = [str(Decimal(calculation[index-1]) - Decimal(calculation[index+1]))]
                            

                if start_index != "" :
                    del calculation_back[start_index+1 : end_index+1]
                    calculation_back[start_index] = "".join(calculation)

                result.value = "".join(calculation_back)

            else:
                result.value = "Error"

#action
        if current_calculation!=[] and any("".join(list(x)) in current_calculation for x in number_type):
            if current_number!=[]:
                calculation_back.append(str(Decimal("".join(current_number))))
                current_number.clear()

            while (calculation_back[-1])[-1] in symbol_type or calculation_back[-1] in brackets_type:
                change_list("pop", current_calculation, calculation_back)

            while calculation_back.count("(") > calculation_back.count(")"):
                change_list("append", current_calculation, calculation_back, ")")

            while calculation_back.count("(") < calculation_back.count(")"):
                calculation_back.insert(0,"(")
                current_calculation.insert(0,"(")

            for index, value in enumerate(calculation_back):
                if value == "(":
                    while ")" not in calculation_back[index:]:
                        change_list("append",")")
                
            while calculation_back.count("(") < calculation_back.count(")"):
                calculation_back.insert(0,"(")
                current_calculation.insert(0,"(")

            while calculation_back.count("(") > calculation_back.count(")"):
                change_list("append", current_calculation, calculation_back, ")")

            calculation_back_copy = calculation_back.copy()

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
        nonlocal current_number, current_calculation, calculation_back, result, calculation_show, calc_state, calculation_back_copy
        current_number.clear()
        current_calculation.clear()
        calculation_back.clear()
        calculation_back_copy.clear()
        result.value=""
        calc_state=True

        calculation_show.value = "".join(current_calculation)
        page.update()
    
    def back(): 
        nonlocal current_number, current_calculation, calculation_back, result, calculation_show, calc_state, brackets_type, calculation_back_copy
        if result.value!="":
            calculation_back = calculation_back_copy.copy()
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