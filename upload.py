from tkinter import ttk, Text, END, filedialog
from tkinter import *
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load default CSV file
# df = pd.read_csv('peter_testovertemp.csv')
df = pd.DataFrame()
df.to_csv('meow.csv', index=False)


# Create a list of columns
columns = list(df.columns)


def load_excel_file():
    global df, columns
    # Open file dialog to select Excel file
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx *.xls")])

    if file_path:
        # Load the selected Excel file into the DataFrame
        df = pd.read_excel(file_path)

        # Update the list of columns
        columns = list(df.columns)

        # Update the comboboxes with new column names
        combo_tab1['values'] = columns
        combo_tab3['values'] = columns

        # Update the Listbox for plotting
        listbox.delete(0, END)  # Clear existing entries in the listbox
        for col in columns:
            listbox.insert(END, col)

        main_textbox.delete(1.0, END)
        main_textbox.insert(END, "Excel file loaded successfully!")


def display_selection(combo):
    selected_column = combo.get()
    if selected_column:
        column_data = df[selected_column]
        column_data_str = column_data.to_string(index=True)
        main_textbox.delete(1.0, END)
        main_textbox.insert(
            END, f"Data from '{selected_column}' column:\n\n{column_data_str}")
    else:
        main_textbox.delete(1.0, END)
        main_textbox.insert(END, "No column selected!")


def display_dataframe():
    df_str = df.to_string(index=True)
    main_textbox.delete(1.0, END)
    main_textbox.insert(END, f"Full DataFrame:\n\n{df_str}")


def display_max(combo):
    selected_column = combo.get()
    if selected_column:
        column_data = df[selected_column].max()
        main_textbox.delete(1.0, END)
        main_textbox.insert(
            END, f"Max value from '{selected_column}' column:\n\n{column_data}")
    else:
        main_textbox.delete(1.0, END)
        main_textbox.insert(END, "No column selected!")


def display_min(combo):
    selected_column = combo.get()
    if selected_column:
        column_data = df[selected_column].min()
        main_textbox.delete(1.0, END)
        main_textbox.insert(
            END, f"Min value from '{selected_column}' column:\n\n{column_data}")
    else:
        main_textbox.delete(1.0, END)
        main_textbox.insert(END, "No column selected!")


def plot_selected_columns():
    selected_columns = listbox.curselection()
    selected_columns = [listbox.get(i) for i in selected_columns]

    if len(selected_columns) == 2:
        col1_data = df[selected_columns[0]]
        col2_data = df[selected_columns[1]]
        plt.plot(col1_data, label=selected_columns[0])
        plt.plot(col2_data, label=selected_columns[1])
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.legend()
        plt.title(f"Plot of {selected_columns[0]} and {selected_columns[1]}")
        plt.show()
    else:
        main_textbox.delete(1.0, END)
        main_textbox.insert(END, "Please select exactly two columns to plot!")


# Create the main window
main_window = tk.Tk()
main_window.config(width=1000, height=1000)
main_window.title("Data Viewer")

# tabs
my_notebook = ttk.Notebook(main_window)
my_notebook.pack(expand=1, fill=BOTH)

# Create Tabs
tab1 = ttk.Frame(my_notebook)
my_notebook.add(tab1, text="View Data")
tab2 = ttk.Frame(my_notebook)
my_notebook.add(tab2, text="Plot")
tab3 = ttk.Frame(my_notebook)
my_notebook.add(tab3, text="Min Max")
tab4 = ttk.Frame(my_notebook)
my_notebook.add(tab4, text="Upload Excel")

# Combobox for tab1
combo_tab1 = ttk.Combobox(tab1, state="readonly", values=columns)
combo_tab1.place(x=50, y=20)

# Combobox for tab3
combo_tab3 = ttk.Combobox(tab3, state="readonly", values=columns)
combo_tab3.place(x=50, y=20)

# Button to display the selected value for tab1
button_tab1 = ttk.Button(tab1, text="Display selection",
                         command=lambda: display_selection(combo_tab1))
button_tab1.place(x=50, y=50)

# Button to display the entire DataFrame
button_df = ttk.Button(tab1, text="Display Data Frame",
                       command=display_dataframe)
button_df.place(x=200, y=50)

# Listbox for multi-selection of columns in tab2
listbox = Listbox(tab2, selectmode=MULTIPLE, height=10)
for col in columns:
    listbox.insert(END, col)
listbox.place(x=50, y=10)

# Plot button in tab2
button_plot = ttk.Button(
    tab2, text="Plot Selected Columns", command=plot_selected_columns)
button_plot.place(x=275, y=85)

# Min and Max buttons in tab3
button_max = ttk.Button(
    tab3, text="Max", command=lambda: display_max(combo_tab3))
button_max.place(x=50, y=50)

button_min = ttk.Button(
    tab3, text="Min", command=lambda: display_min(combo_tab3))
button_min.place(x=150, y=50)

# New Tab4 - Upload Excel file
upload_button = ttk.Button(
    tab4, text="Upload Excel File", command=load_excel_file)
upload_button.place(x=50, y=50)

# Text widget to display the column data
main_textbox = Text(main_window, width=150, height=50, wrap=WORD)
main_textbox.place(x=50, y=150)

# Start the main event loop
main_window.mainloop()
