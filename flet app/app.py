import flet as ft

current_value = 0



def main (page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.title = "My Counter"
    page.window.width = 400
    page.window.height = 300

    text_update = ft.Text("0", size=40, weight=ft.FontWeight.BOLD)
    text_debug = ft.Text("")

    def reset_counter (e):
        global current_value 
        current_value = 0
        text_update.value = current_value
        text_debug.value = "Debug : RESET"
        print("Debug : RESET")
        
    def plus1 (e):
        global current_value
        current_value += 1
        text_update.value = current_value
        text_debug.value = "Debug : Added 1"
        print("Debug: Added 1")
        # print(current_value)

    def min1 (e):
        global current_value
        if current_value > 0:
            current_value -= 1
            text_update.value = current_value
            print("Debug: Minus 1")
            text_debug.value = "Debug : Minus 1"
            # print(current_value)
        else:
            text_debug.value = "Value Too Short To Substract From"
            print("Value Too Short To Substract From")
            # print(current_value)

    page.add(
        
        ft.Text("My Counter APP", size=35, weight=ft.FontWeight.BOLD),
        ft.Text("My First Flet Python App 14-Nov-26", size=15),
        
        ft.Text("Current Count", size=30),

        text_update,
        ft.Row(
            controls=[
                
                ft.Button("-", on_click=min1, width = 100, height=60),
                ft.Button("+", on_click=plus1, width = 100, height=60),
                

            ],alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Button("RESET", on_click=reset_counter, width=200, height=50),
        ft.Text("Debug"),
        text_debug

        
    )


        
ft.run(main)