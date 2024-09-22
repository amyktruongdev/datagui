import pandas as pd
from tkinter import *

df = pd.read_csv('pokemon_data.csv')
df.to_csv('modified.csv', index=False)
# print(df[['Name','Type 1','HP']])
# print(df.iloc[3,2])
# for index, row in df.iterrows():
# print(index,row['Name'])

# print(df.loc[df['Type 1'] == "Fire"])
# print(df.head(5))

# create window
# RIGHT ONE window = Tk()


def submit():
    print(listbox.get(listbox.curselection()))


root = Tk()

listbox = Listbox(root, width=12, bg='grey',
                  activestyle='dotbox', font=("Helvetica", 35), fg="yellow")
listbox.insert(1, df.loc[df['Type 1'] == "Fire"])
listbox.insert(2, df[['Name', 'Type 1', 'HP']])
listbox.insert(3, "honk")
listbox.insert(4, "beep")


listbox.pack()
listbox.config(height=listbox.size())

submitButton = Button(root, text="submit", command=submit)
submitButton.pack()

myLabel1 = Label(root, text=df)
myLabel1.config(bg='pink')
myLabel1.pack()


# myLabel2 = Label(root, text=df.loc[df['Type 1'] == "Fire"], width=100)
# myLabel2.config(bg='blue')
# myLabel3 = Label(root, text=df[['Name', 'Type 1', 'HP']])
# myLabel3.config(bg='orange')

# myLabel1.grid(row=0, column=0, padx=10, pady=10)
# myLabel2.grid(row=0, column=1, padx=10, pady=10)
# myLabel3.grid(row=0, column=3, padx=10, pady=10)
# window.geometry("1000x1000")
# window.configure(bg='lightblue')
# l = Label(window, text="Pokemon GUI")
# l.config(font=("Courier", 14), bg="lightblue")


# def filter():
# mao = Label(window, text=df.loc[df['Type 1'] == "Fire"])
# mao.config(font=("Courier", 10), bg="pink", width=120, height=90)
# mao.pack()


# def click():

# stats = Label(window, text=df[['Name', 'Type 1', 'HP']])
# stats.config(font=("Courier", 10), bg="pink", width=1000)
# stats.pack()


# button = Button(window, text='Click to Display Data')
# button.config(command=click, bg="lightpink")

# filterTest = Button(window, text='Filter by Fire')
# filterTest.config(command=filter)

# l.pack()

# filterTest.pack()
# button.pack()


root.mainloop()
