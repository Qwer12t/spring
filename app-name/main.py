import flet as ft


def main(page: ft.Page):
    print("a")
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)
