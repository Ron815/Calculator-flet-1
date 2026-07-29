import flet as ft
from decimal import Decimal

def main(page: ft.Page):
    number_type=["0","1","2","3","4","5","6","7","8","9"]
    symbol_type=["+", "-", "*", "/", "^","."]
    current_number=[]  #list
    numbers=[]  #list

    symbols=[]
    calculation_back=[]
    calculation_show=ft.Text(value="", size=15)  
    result=ft.Text(value="", size=20)

    def clicked_show(e):
        enter=e.control.content
        nonlocal symbols, current_number, numbers, calculation_back, result, calculation_show
        if enter in number_type:
            current_number.append(enter)
            calculation_back.append(enter)

        elif enter in symbol_type and current_number != [] :

            if calculation_back[-1] not in symbol_type:

                if enter != ".":
                    numbers.append("".join(current_number))
                    current_number.clear()
                    calculation_back.append(enter)

                elif enter =="." and "." not in current_number :
                    symbols.append(enter)
                    current_number.append(enter)
                    numbers.append(str(Decimal("".join(current_number))))
                    calculation_back.append(enter)

        calculation_show.value = "".join(calculation_back)
        page.update()
        
    def clicked_calc():
        result.value = eval("".join(calculation_back))
        

    def convert(a):
        if a=="":
             return "0"
        return Decimal("".join(a))


    def clear(): #test: OK
        nonlocal symbols, current_number, numbers, calculation_back, result, calculation_show
        current_number.clear()
        numbers.clear()
        symbols=[]
        calculation_back=[]
        calculation_show.value=""
        result.value=""
    
    def back(): #test: OK
        nonlocal symbols, current_number, numbers, calculation_back, result, calculation_show
        if calculation_back!=[]:
            calculation_back.pop()
            calculation_show.value = "".join(calculation_back)
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
            ft.Button(content="+", on_click=clicked_show),
        ]
            ),
    ft.Row(
            controls=[
            ft.Button(content="-", on_click=clicked_show),
            ft.Button(content="*", on_click=clicked_show),
            ft.Button(content="/", on_click=clicked_show),
            ft.Button(content="^", on_click=clicked_show),
        ]
            ),
    ft.Row(
            controls=[
            ft.Button(content="=", on_click=clicked_calc),          
            ft.Button(content="AC", on_click=clear),
            ft.Button(content="←", on_click=back),     
            ]
                )
                    )
    

if __name__ == "__main__" :
    ft.run(main)