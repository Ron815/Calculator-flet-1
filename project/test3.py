import flet as ft

def main(page: ft.Page):
    user_input = ft.TextField(label="請輸入內容", width=300)
    display_text = ft.Text(value="這裡會顯示你輸入的內容", size=20)

    def button_clicked(e):
        display_text.value = f"你輸入了：{user_input.value}"
        page.update()

    
    submit_btn = ft.Button(content="送出", on_click=button_clicked)

    page.add(
        user_input,
        submit_btn,
        display_text
    )

# 最新版 Flet 建議用 ft.run(main) 取代 ft.app(target=main) 以避免 Warning
ft.run(main)