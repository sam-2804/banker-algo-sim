import flet as ft



def main(active_page: ft.page):
    
    BG_COLOR = "#000000"       # Black background
    TEXT_MAIN = "#FFFFFF"      # White text
    TEXT_MUTED = "#AAAAAA"     # Light gray for matrix numbers 
    ACCENT_BORDER = "#333333"  # Dark gray for borders
    BTN_BG = "#FFFFFF"         # Button background-White
    BTN_TEXT = "#000000"       # Button text -Black
    
    active_page.bgcolor = "#000000"
    active_page.title = "Banker Algorithm Simulation-GUI"
    header = ft.Text("BANKER'S ALGORITHM", size=24, weight="bold", color=TEXT_MAIN)
    
    active_page.add(
        ft.SafeArea(
            expand = True,
            content = ft.Container(
                alignment = ft.Alignment.CENTER
            )
        )
    )

ft.run(main)