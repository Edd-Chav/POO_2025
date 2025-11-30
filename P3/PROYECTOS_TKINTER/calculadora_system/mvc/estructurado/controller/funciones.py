from tkinter import messagebox

def operaciones(n1,n2,signo):
    if signo=="+":
        ope=n1+n2
        tipo="Suma"
    elif signo=="-":
        ope=n1-n2
        tipo="Resta"
    elif signo=="x":
        ope=n1*n2
        tipo="Multiplicacion"
    elif signo=="/":
        ope=n1/n2
        tipo="Division"
    messagebox.showinfo(title=tipo,message=f"{n1}{signo}{n2} = {ope}")