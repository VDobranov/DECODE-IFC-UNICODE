import re
import flet as ft


def decode_ifc_text(text) -> str:
    matches = re.findall(r'\\X2\\([0-9A-Z]*)\\X0\\', text)
    for match in matches:
        hex_chars = [match[i:i+4] for i in range(0, len(match), 4)]
        decoded_str = ''.join([chr(int(h, 16)) for h in hex_chars])
        text = text.replace(f'\\X2\\{match}\\X0\\', decoded_str)
    return text


def main(page: ft.Page):

    # \X2\041F043504400435043A0440044B044204380435\X0\: 50,00 \X2\043C043C\X0\
    # #1671=IFCDOOR('3Xy9QMLb95gPwSyhpv2mM0',$,'\X2\0414043204350440044C\X0\ - \X2\041E0434043D043E043F043E043B044C043D0430044F\X0\ \X2\044004300441043F04300448043D0430044F\X0\ (\X2\0433043B04430445043E0435\X0\ \X2\04420435043C043D043E0435\X0\): 600,00 \X2\043C043C\X0\ x 2\X2\00A0\X0\100,00 \X2\043C043C\X0\',$,$,#1672,#1681,$,2100.,600.,$,$,$);

    def textbox_changed(e):
        tb2.value = decode_ifc_text(e.control.value)
        page.update()

    tb1 = ft.TextField(label="Введите текст для конвертации",
                       value="\X2\\041F04400438043C04350440\X0\\",
                       autofocus=True,
                       on_change=textbox_changed,
                       on_focus=textbox_changed,
                       multiline=True,
                    #    text_align=ft.TextAlign.CENTER,
                    #    prefix_text="\X2\\",
                    #    suffix_text="\X0\\"
                       )
    tb2 = ft.TextField(label="Результат",
                       multiline=True,
                       read_only=True,
                       border=ft.InputBorder.NONE,
                       filled=True)
    
    info = ft.Text("ⓘ Вставьте текст вида «\X2\…\X0\» в верхнее поле", selectable=True, theme_style=ft.TextThemeStyle.LABEL_MEDIUM)

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column(
                    controls=[
                        tb1,
                        tb2,
                        info],
                    width=800,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center),
            expand=True,
        )
    )


ft.app(main)
