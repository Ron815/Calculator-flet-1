import flet as ft
from decimal import Decimal

def main(page: ft.Page):
    number_type=["0","1","2","3","4","5","6","7","8","9","."]
    symbol_type=["+", "-", "*", "/", "^"]
    number1=[]  #list
    number2=[]  #list
    symbol=""
    calculation=ft.Text(value="", size=15)  
    result=ft.Text(value="", size=20)

    def convert(a):
        if a=="":
             return "0"
        return Decimal("".join(a))

    def clicked(e):
        enter=e.control.content
        nonlocal symbol, number1, number2, calculation, result
        if enter in symbol_type:
                symbol=enter 
        
        elif enter in number_type:
            if symbol=="":
                if enter==".":
                    if number1 !=[] and number1.count(".")==0:
                        number1.append(enter)
                else:
                    number1.append(enter)


            else:
                if enter==".":
                    if number2 !=[] and number2.count(".")==0:
                        number2.append(enter)
                else:
                    number2.append(enter)
               
        a="".join(number1)
        b="".join(number2)
        calculation.value = a + symbol + b
        page.update()

    def calc(): 
        nonlocal symbol, number1, number2, calculation, result
        if number1!=[] and number2 !=[] and symbol!="":
            if symbol == "+":
                result.value = str(f"={convert(number1) + convert(number2)}")
            elif symbol == "-":
                result.value = str(f"={convert(number1) - convert(number2)}")
            elif symbol == "*":
                result.value = str(f"={convert(number1) * convert(number2)}")
            elif symbol == "/":
                if str(convert(number2))=="0":
                    result.value="Error"
                else:
                    result.value = str(f"={convert(number1) / convert(number2)}")
            elif symbol == "^":
                result.value = str(f"={convert(number1) ** convert(number2)}")

        elif number1!=[] and symbol=="":
            result.value=str(convert(number1))

        else:
            result.value="Error"

    def clear():
        nonlocal symbol, number1, number2, calculation, result 
        number1.clear()
        number2.clear()
        symbol=""
        calculation.value=""
        result.value=""
    
    def back():
        nonlocal symbol, number1, number2, calculation, result
        if number2!=[]:
            number2.pop()
            a="".join(number1)
            b="".join(number2)
            result.value=""
            calculation.value = a + symbol + b
            page.update()
            
        elif symbol != "":
            symbol=""
            a="".join(number1)
            b="".join(number2)
            calculation.value = a + symbol + b
            page.update()
            
        elif number1 !=[]:
            number1.pop()
            a="".join(number1)
            b="".join(number2)
            calculation.value = a + symbol + b
            page.update()
    

    page.add(
        calculation,
        result,
        ft.Row(
            controls=[
            ft.Button(content="1", on_click=clicked),
            ft.Button(content="2", on_click=clicked),
            ft.Button(content="3", on_click=clicked),
            ft.Button(content="4", on_click=clicked),
        ]
            ),
            
    ft.Row(
            controls=[            
            ft.Button(content="5", on_click=clicked),
            ft.Button(content="6", on_click=clicked),
            ft.Button(content="7", on_click=clicked),
            ft.Button(content="8", on_click=clicked),
        ]
            ),
    ft.Row(
            controls=[            
            ft.Button(content="9", on_click=clicked),
            ft.Button(content="0", on_click=clicked),
            ft.Button(content=".", on_click=clicked),
            ft.Button(content="+", on_click=clicked),
        ]
            ),
    ft.Row(
            controls=[
            ft.Button(content="-", on_click=clicked),
            ft.Button(content="*", on_click=clicked),
            ft.Button(content="/", on_click=clicked),
            ft.Button(content="^", on_click=clicked),
        ]
            ),
    ft.Row(
            controls=[
            ft.Button(content="=", on_click=calc),
            ft.Button(content="AC", on_click=clear),
            ft.Button(content="←", on_click= back)
        ]
            ))
    

if __name__ == "__main__" :
    ft.run(main)