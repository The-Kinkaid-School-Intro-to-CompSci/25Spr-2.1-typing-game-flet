import flet as ft


global sentence, start_time, input_field, page_global
sentence = "The quick brown fox jumped over the lazy dog"
start_time = None
input_field = None
page_global = None
result_text = ft.Text("", size=20)


def show_play_again():
    global sentence, start_time, input_field, page_global
    


def check_answer(event):
    global sentence, start_time, input_field, page_global
    print("checking the answer")

    # 6. Implement this function

    # 6.a. Calculate the elapsed_time using the current time and the start_time you calculated in step 3

    # 6.b. Get the value of the input_field (i.e. what the user wrote). See slides.

    # 6.c. Compare what the user wrote to the sentence. See doc for details.



def start_game(event):
    global sentence, start_time, input_field, page_global
    # 1. Link the button and the function to start the game
    page_global.controls.clear()
    page_global.update()

    # 2. Show the sentence and add it to the page

    # 3. Print the start_time

    # 4. Make a TextField input box (see input_field)

    # 5. Make check_answer the callback function for the input_field


def main(page: ft.Page):
    global sentence, start_time, input_field, page_global
    # DO NOT EDIT THESE LINES
    page_global = page
    page.title = "Typing Speed Test"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN) # Except for color, you can change the color theme
    page.bgcolor = ft.ColorScheme.background
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # 1. Create a Start Button (and add it to the page)


ft.app(main)
