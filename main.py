import flet as ft

def main(page: ft.Page):
    page.title = "Neon Calculator"
    page.background_color = "#111116"
    page.window_width = 380
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Display Screen
    result = ft.Text(value="0", color="#00ffff", size=40, text_align=ft.TextAlign.RIGHT)
    
    # Track calculation states
    state = {"operand1": 0, "operator": "", "reset": False}

    def button_click(e):
        data = e.control.text
        
        if data == "C":
            result.value = "0"
            state["operand1"] = 0
            state["operator"] = ""
            state["reset"] = False
        
        elif data in ["+", "-", "*", "/"]:
            state["operand1"] = float(result.value)
            state["operator"] = data
            state["reset"] = True
            
        elif data == "=":
            if state["operator"]:
                operand2 = float(result.value)
                op = state["operator"]
                if op == "+": res = state["operand1"] + operand2
                elif op == "-": res = state["operand1"] - operand2
                elif op == "*": res = state["operand1"] * operand2
                elif op == "/": res = state["operand1"] / operand2 if operand2 != 0 else "Error"
                
                # Format result trailing zeros
                if isinstance(res, float) and res.is_integer():
                    res = int(res)
                result.value = str(res)
                state["operator"] = ""
        else:
            if result.value == "0" or state["reset"]:
                result.value = data
                state["reset"] = False
            else:
                result.value += data
                
        page.update()

    # UI Layout
    page.add(
        ft.Container(
            width=350,
            padding=20,
            bgcolor="#1e1e24",
            border_radius=20,
            animate=ft.animation.Animation(300, "easeOut"),
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=result,
                        alignment=ft.alignment.center_right,
                        padding=10,
                        bgcolor="#0d0d11",
                        border_radius=10
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("C", on_click=button_click, bgcolor="#ff0055", color="white", weight="bold", expand=1),
                            ft.ElevatedButton("/", on_click=button_click, bgcolor="#00ffff", color="black", weight="bold", expand=1),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("7", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("8", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("9", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("*", on_click=button_click, bgcolor="#00ffff", color="black", weight="bold", expand=1),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("4", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("5", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("6", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("-", on_click=button_click, bgcolor="#00ffff", color="black", weight="bold", expand=1),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("1", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("2", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("3", on_click=button_click, bgcolor="#2d2d35", color="white", expand=1),
                            ft.ElevatedButton("+", on_click=button_click, bgcolor="#00ffff", color="black", weight="bold", expand=1),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("0", on_click=button_click, bgcolor="#2d2d35", color="white", expand=2),
                            ft.ElevatedButton("=", on_click=button_click, bgcolor="#00ff66", color="black", weight="bold", expand=2),
                        ]
                    ),
                ]
                    )
        )
    )

ft.app(target=main)
