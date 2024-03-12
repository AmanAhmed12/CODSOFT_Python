import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    text_result.configure(fg="black")
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
   
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)

    except:
        clear_field()
        text_result.configure(fg="red")
        text_result.insert(1.0,"Error")
        
       

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")


root=tk.Tk()
root.geometry("325x350")

text_result=tk.Text(root,height=2,width=17,font=("Arial",24),fg="black",bg="grey")
text_result.grid(columnspan=6, padx=8, pady=5)

btn_1=tk.Button(root,text="1" ,command= lambda:add_to_calculation(1),width=5,font=("Arial",14),fg="white", bg="black")
btn_1.grid(row=2,column=1,pady=7)

btn_2=tk.Button(root,text="2" ,command= lambda:add_to_calculation(2),width=5,font=("Arial",14),fg="white", bg="grey")
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3" ,command= lambda:add_to_calculation(3),width=5,font=("Arial",14),fg="white", bg="black")
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4" ,command= lambda:add_to_calculation(4),width=5,font=("Arial",14),fg="white", bg="grey")
btn_4.grid(row=3,column=1,pady=7)

btn_5=tk.Button(root,text="5" ,command= lambda:add_to_calculation(5),width=5,font=("Arial",14),fg="white", bg="black")
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6" ,command= lambda:add_to_calculation(6),width=5,font=("Arial",14),fg="white", bg="grey")
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7" ,command= lambda:add_to_calculation(7),width=5,font=("Arial",14),fg="white", bg="black")
btn_7.grid(row=4,column=1,pady=7)

btn_8=tk.Button(root,text="8" ,command= lambda:add_to_calculation(8),width=5,font=("Arial",14),fg="white", bg="grey")
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9" ,command= lambda:add_to_calculation(9),width=5,font=("Arial",14),fg="white", bg="black")
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root,text="0" ,command= lambda:add_to_calculation(0),width=5,font=("Arial",14),fg="white", bg="black")
btn_0.grid(row=5,column=2)

btn_Plus=tk.Button(root,text="+" ,command= lambda:add_to_calculation("+"),width=5,font=("Arial",14),fg="white", bg="grey")
btn_Plus.grid(row=2,column=4)

btn_Minus=tk.Button(root,text="-" ,command= lambda:add_to_calculation("-"),width=5,font=("Arial",14),fg="white", bg="black")
btn_Minus.grid(row=3,column=4)

btn_Mul=tk.Button(root,text="*" ,command= lambda:add_to_calculation("*"),width=5,font=("Arial",14),fg="white", bg="grey")
btn_Mul.grid(row=4,column=4)

btn_Div=tk.Button(root,text="/" ,command= lambda:add_to_calculation("/"),width=5,font=("Arial",14),fg="white", bg="black")
btn_Div.grid(row=5,column=4)

btn_Open=tk.Button(root,text="(" ,command= lambda:add_to_calculation("("),width=5,font=("Arial",14),fg="white", bg="grey")
btn_Open.grid(row=5,column=1,pady=7)

btn_Close=tk.Button(root,text=")" ,command= lambda:add_to_calculation(")"),width=5,font=("Arial",14),fg="white", bg="grey")
btn_Close.grid(row=5,column=3)

btn_Clear=tk.Button(root,text="C" ,command=clear_field,width=11,font=("Arial",14),fg="white", bg="black")
btn_Clear.grid(row=6,column=1,columnspan=2)

btn_Equal=tk.Button(root,text="=" ,command= evaluate_calculation,width=11,font=("Arial",16),fg="white", bg="grey")
btn_Equal.grid(row=6,column=3,columnspan=2)


root.mainloop()