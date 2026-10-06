import flet as ft



def main(active_page: ft.page):
    
    active_page.add(
        ft.SafeArea(
            expand = True,
            content = ft.Container(
                alignment = ft.Alignment.CENTER
            )
        )
    )

ft.run(main)