inport tkinter as tk
from tkinter import ttk
def submit():
    name=entry.name.get()
    gented=gender_var,get()
    hoppies=[]
    if reading_var.get():
        hoppies.append("reading")
    if singing_var.get():
        hoppiend.append("singing")
    if playing_var.get():
        hoppies.append("playing")
        
        print(f"name:{name")
        print(f"gender:{gender}")
        print(f"hobbies:{gender}")
        print(f"city:{city}")
        print("-----")
        
root=tk.Tk()
root=title("useer informartion from")


#name label and enter
label_name=tk.Lable(root,text="name")
label_name.grid(row=0,column=0,padx=10,pady=5)
enter_name=tk.enter(root)
enter_name.grid(row=0,column=1,padx=10,padty=5)

#gender radio buttons
gender_var_tk.string var(value="male")
lable_gender=tk.label(root,text="gender")
lanel_gender.grid(row=1,column=0,padx=10,pady=5)
radio_male=tk.radiobutton(root,text="male",variable=gender_var,value="male")
radio_male.grid(row=1,column=0,padx=10,pady=5)
radio_temale=Radiobutton(root,text="femle",variable=gender,var,value="femle")
radio_temale.grid(row=1,column=2,padx=10,pady=5,stick="w")
 
#hobbies checkboxes
label_hobbies=tk.label(root,text="hobbies:")
label_hobbies.grid(row=2,column=0,padx=10,pady=5
reading_var=tk.booleanvar()
ginging_var=tk.booleanvar()
palying_var=tk.booleanvar()
checkbox_reading+tk.checkbutton(root,text="reading", variable=reading_var)
checkbox_reading,grid(row=2,column=1,padx=10,pady=5,stick="w")
checkbox.singing=tk.checkbutton(root,text="singing",variable=singing_var)
checkbox_singing.grid(row=2,column=2,padx=10,pay=5,sticky="w")
checkbox_playing.grid(row=,text="palying",variable=playing_var)
checkbox_playing.grid(raw=2,column=3,padx=10,pady=5,sticky="w")

#city dropdown(lombobox)
label_city=tk.label(root,text="city")
label_city.grid(row=3,column=0,padx=10,pady=5)
city_combobox=ttk.combobox(rout,textvariable=city_var)
city_combobx['values']=("vizag","hyderabed","banagalore","mumbai","chennai")
city_combobox.grid(row=3,column=1,padx=10, pady=5)
city_combobox.current(0)

#submi button
button_submit=tk.root,text="submit", command=submit)
button_submit,grid(row=4,colunmspan=4,pady=10)

#ron the mani even loop
 root.mainloop()