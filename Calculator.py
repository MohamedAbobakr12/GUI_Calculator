import customtkinter as ctk

calc = ctk.CTk()
calc.geometry("470x470")
calc.title("Calculator")
calc.iconbitmap("calculator.ico")
calc.config(bg="#5BC0EB")

expression = ""

equation = ctk.StringVar()


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def Equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def Clear():
    global expression
    expression = ""
    equation.set("")


def Brackets():
    global expression
    if (expression.count("(") == expression.count(")") + 1):
        expression += ")"
    else:
        expression += "*("
    equation.set(expression)


def Pow():
    global expression
    expression += "**"
    equation.set(expression)


Label1 = ctk.CTkLabel(calc, text="Calculator", bg_color="#5BC0EB", font=("Outfit", 40), text_color="#E63946")
Label1.pack()

Entry1 = ctk.CTkEntry(calc, height=35, width=250, bg_color="#5BC0EB", state="readonly", textvariable=equation,
                      font=("Outfit", 28), text_color="#E63946")
Entry1.place(x=105, y=75)

Buttonpn = ctk.CTkButton(calc, text="x²", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                         command=lambda: Pow())
Buttonpn.place(x=10, y=400)

Button0 = ctk.CTkButton(calc, text="0", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(0))
Button0.place(x=125, y=400)

Buttond = ctk.CTkButton(calc, text=".", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press("."))
Buttond.place(x=240, y=400)

Button1 = ctk.CTkButton(calc, text="1", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(1))
Button1.place(x=10, y=350)

Button2 = ctk.CTkButton(calc, text="2", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(2))
Button2.place(x=125, y=350)

Button3 = ctk.CTkButton(calc, text="3", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(3))
Button3.place(x=240, y=350)

Button4 = ctk.CTkButton(calc, text="4", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(4))
Button4.place(x=10, y=300)

Button5 = ctk.CTkButton(calc, text="5", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(5))
Button5.place(x=125, y=300)

Button6 = ctk.CTkButton(calc, text="6", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(6))
Button6.place(x=240, y=300)

Button7 = ctk.CTkButton(calc, text="7", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(7))
Button7.place(x=10, y=250)

Button8 = ctk.CTkButton(calc, text="8", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(8))
Button8.place(x=125, y=250)

Button9 = ctk.CTkButton(calc, text="9", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                        command=lambda: press(9))
Button9.place(x=240, y=250)

Button_add = ctk.CTkButton(calc, text="+", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                           command=lambda: press("+"))
Button_add.place(x=10, y=200)

Button_sub = ctk.CTkButton(calc, text="-", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                           command=lambda: press("-"))
Button_sub.place(x=125, y=200)

Button_multi = ctk.CTkButton(calc, text="*", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                             command=lambda: press("*"))
Button_multi.place(x=240, y=200)

Button_div = ctk.CTkButton(calc, text="/", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                           command=lambda: press("/"))
Button_div.place(x=355, y=200)

Button_modu = ctk.CTkButton(calc, text="%", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                            command=lambda: press("%"))
Button_modu.place(x=355, y=250)

Button_brack = ctk.CTkButton(calc, text="()", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                             command=lambda: Brackets())
Button_brack.place(x=355, y=300)

Button_equal = ctk.CTkButton(calc, text="=", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                             command=lambda: Equal())
Button_equal.place(x=355, y=350)

Button_clear = ctk.CTkButton(calc, text="C", height=25, width=100, bg_color="#5BC0EB", font=("Outfit", 14),
                             fg_color="#E63946", command=lambda: Clear())
Button_clear.place(x=355, y=400)

calc.mainloop()