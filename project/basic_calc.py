import flet as ft
from decimal import Decimal

def main(page: ft.Page):
    number_type=["0","1","2","3","4","5","6","7","8","9","."]
    symbol_type=["+", "-", "*", "/", "^"]
    number1=[]  #list
    n=[]  #list
    s=[]
    symbol=""
    calculation=ft.Text(value="", size=15)  
    result=ft.Text(value="", size=20)

    def convert(a):
        if a=="":
             return "0"
        return Decimal("".join(a))

    def clicked(e):
        enter=e.control.content
        nonlocal symbol, number1, n, calculation, result, s
        if enter in symbol_type and len(s)== len(number1) -1:
                s.append(enter) 
        
        elif enter in number_type:
            if symbol=="":
                if enter==".":
                    if number1 !=[] and number1.count(".")==0:
                        number1.append(enter)
                else:
                    number1.append(enter)


            else:
                if enter==".":
                    if n !=[] and n.count(".")==0:
                        n.append(enter)
                else:
                    n.append(enter)
               
        a="".join(number1)
        b="".join(n)
        calculation.value = a + symbol + b
        page.update()

    def calc(): 
        nonlocal symbol, number1, n, calculation, result
        if number1!=[] and n !=[] and symbol!="":
            if symbol == "+":
                result.value = str(f"={convert(number1) + convert(n)}")
            elif symbol == "-":
                result.value = str(f"={convert(number1) - convert(n)}")
            elif symbol == "*":
                result.value = str(f"={convert(number1) * convert(n)}")
            elif symbol == "/":
                if str(convert(n))=="0":
                    result.value="Error"
                else:
                    result.value = str(f"={convert(number1) / convert(n)}")
            elif symbol == "^":
                result.value = str(f"={convert(number1) ** convert(n)}")

        elif number1!=[] and symbol=="":
            result.value=str(convert(number1))

        else:
            result.value="Error"

    def clear():
        nonlocal symbol, number1, n, calculation, result 
        number1.clear()
        n.clear()
        symbol=""
        calculation.value=""
        result.value=""
    
    def back():
        nonlocal symbol, number1, n, calculation, result
        if n!=[]:
            n.pop()
            a="".join(number1)
            b="".join(n)
            result.value=""
            calculation.value = a + symbol + b
            page.update()
            
        elif symbol != "":
            symbol=""
            a="".join(number1)
            b="".join(n)
            calculation.value = a + symbol + b
            page.update()
            
        elif number1 !=[]:
            number1.pop()
            a="".join(number1)
            b="".join(n)
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