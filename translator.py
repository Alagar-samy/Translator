from tkinter import *  #importing tkinter module
from tkinter import ttk,messagebox
import googletrans # install in command prompt  (pip install googletrans)
from googletrans import Translator #new
import textblob # install in command prompt (pip install textblob)

window  = Tk()
window.title("translator")
window.geometry("1080x400")
window.resizable(False,False)#new
def label_change():
    c = combo_1.get()
    c1 = combo_2.get()
    label_1.configure(text=c)
    label_2.configure(text=c1)
    window.after(1000,label_change)
      
def translate_now():
    try:
        text_ = text_1.get(1.0,END)
        t1 = Translator()
        trans_text = t1.translate(text_,src=combo_1.get(),dest=combo_2.get())
        trans_text = trans_text.text
        text_2.delete(1.0,END)
        text_2.insert(END,trans_text)
    except Exception as e:
        messagebox.showerror('translator',"try agian")

#logo
logo = PhotoImage(file="C:\\Users\\win\\Documents\\sayur\\extraworks\\translators.png")
window.iconphoto(False,logo)

#conversion image
arrow = PhotoImage(file="C:\\Users\\win\\Documents\\sayur\\extraworks\\conversion_image.png")
image_label = Label(window,image=arrow,width=220)
image_label.place(x=378,y=100)


language  = googletrans.LANGUAGES
language_value = list(language.values())
lang_1 = language.keys() 

combo_1 = ttk.Combobox(window,
                       values=language_value#,state='r'
                       )
combo_1.place(x=110,y=20)
combo_1.set("English")

label_1 = Label(window,text='English',bg='#68e8e6',width=28,bd=5,relief=GROOVE)
label_1.place(x=78,y=50)

frame = Frame(window,bg='black',bd=5)
frame.place(x=10,y=118,width=350,height=210)

text_1 = Text(frame,bg='white',fg = 'blue',font=('arial',32,'bold','italic'),wrap=WORD,relief=GROOVE)
text_1.place(x=0,y=0,width=340,height=200)

scrollbar_1 = Scrollbar(frame)
scrollbar_1.pack(side='right',fill='y')

scrollbar_1.configure(command=text_1.yview)
text_1.configure(yscrollcommand=scrollbar_1.set) 


combo_2 = ttk.Combobox(window,values=language_value  #,state='r'
                       )
combo_2.place(x=730,y=20)
combo_2.set("Select Language")

frame_2 = Frame(window,bg='black',bd=5)
frame_2.place(x=620,y=118,width=350,height=210)

text_2 = Text(frame_2,bg='white',fg = 'green',font=('arial',25,'bold'),wrap=WORD,relief=GROOVE)
text_2.place(x=0,y=0,width=340,height=200)

scrollbar_2 = Scrollbar(frame_2)
scrollbar_2.pack(side='right',fill='y')

scrollbar_2.configure(command=text_2.yview)
text_2.configure(yscrollcommand=scrollbar_2.set)

label_2 = Label(window,text='English',bg='#68e8e6',width=28,bd=5,relief=GROOVE)
label_2.place(x=695,y=50)

#translate button
translate = Button(window,text='Translate',
                   activebackground='green',cursor='hand2',bd=3,bg='red',fg='white',activeforeground='black',
                   command=translate_now)
translate.place(x=453,y=345)

label_change()

window.configure(bg='white')
window.mainloop()