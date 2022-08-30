from tkinter import *
from tkinter import messagebox
import random

# TODO: build-in sort function functionality   -   DONE
# TODO: random list elements generator  -  DONE
# TODO: deleting an element from a list  -  DONE
# TODO: create an icon  -  DONE
# TODO: change a radio buttons into the dropdown menu  -  DONE
# TODO: more sorting methods
# TODO: make better comments (is this even doable?)

# An app where user inputs a numbers into an array and the list is sorted after pressing the button

num_list = []  # empty list
nums_in_list = ""  # for displaying numbers that are currently in the list
sorted_list = ""  # for displayig sorted list

root = Tk()
root.title("Sorting app")
root.geometry("600x300")
root.iconbitmap('sort_icon.ico')


# insertion sort
def insertion_sort(num_list):
    list_length = len(num_list)
    for i in range(1, list_length):
        for j in range(0, i):
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]  # swapping elements

    return num_list


# selection sort
def selection_sort(num_list):
    list_length = len(num_list)
    for i in range(0, list_length):
        minimum = i  # marking element on 'i' index the minimum number in list

        # looking for a minimum element in list
        for j in range(i+1, list_length):
            if num_list[minimum] > num_list[j]:
                minimum = j  # assigning the minimum element's index

        num_list[i], num_list[minimum] = num_list[minimum], num_list[i]  # swapping elements

    return num_list


# function that adds entered element to the list (as an integer)
def arr_add():
    global display_sorted_list
    global nums_in_list
    # checking whether entered data is correct
    if add_entry.get() == "":
        messagebox.showerror("Error!", "You didn't enter anything!")
        return
    elif add_entry.get().isnumeric() is False:
        messagebox.showerror("Error!", "You have entered a non numeric value!")
        return  # stops the function

    display_sorted_list.config(text="")

    # adding a number to the list
    num_list.append(int(add_entry.get()))

    # displaying a current items in list
    nums_in_list += f"{str(add_entry.get())}, "
    curr_array.config(text=f"Current items in list: {nums_in_list}")

    # deleting content of entry box
    add_entry.delete(0, END)


# function that display information which sorting method is picked
def display_sorting_method(event):  # with 'event' parameter the function works for some reason
    chosen_sort_method.config(text=f"You have chosen: {sorting_method.get()}")


# sorting a list using build-in function
def sort_list(sorting_method):
    global sorted_list
    global nums_in_list
    global num_list
    global display_sorted_list
    # checking if the list is empty
    if not num_list:
        messagebox.showerror("Error!", "You didn't enter any numbers!")
        return  # stops the functions

    if sorting_method == "Build-in sorting function":
        # sorting a list
        num_list.sort()

    if sorting_method == "Insertion sort":
        insertion_sort(num_list)

    if sorting_method == "Selection sort":
        selection_sort(num_list)

    # creating a string containing  sorted list to display it
    for numbers in num_list:
        sorted_list += f"{str(numbers)}, "

    # displaying sorted list
    display_sorted_list = Label(root, text=f"Sorted list: {sorted_list}", font=("Arial", 16))
    display_sorted_list.grid(row=7, column=0, columnspan=2, sticky=W)

    # emptying the list and strings after sorting items
    curr_array.config(text="Current items in list: ")
    nums_in_list = ""
    sorted_list = ""
    num_list.clear()


# generating random numbers
def generate_numbers_window():
    global generate_window
    global first_num
    global second_num
    global amount_of_items
    # creating a new window
    generate_window = Toplevel()
    generate_window.title("Generate random items")
    generate_window.iconbitmap('sort_icon.ico')

    # labels
    first_num_label = Label(generate_window, text="Start of range: ")
    first_num_label.grid(row=0, column=0)

    second_num_label = Label(generate_window, text="End of range: ")
    second_num_label.grid(row=1, column=0)

    amount_of_items_label = Label(generate_window, text="Amount of items: ")
    amount_of_items_label.grid(row=2, column=0)

    # ranges of a random number generator
    first_num = Entry(generate_window)
    first_num.grid(row=0, column=1)

    second_num = Entry(generate_window)
    second_num.grid(row=1, column=1)

    amount_of_items = Entry(generate_window)
    amount_of_items.grid(row=2, column=1)

    # buttons
    generate_button = Button(generate_window, text="Generate", command=generate, width=20)
    generate_button.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    cancel_button = Button(generate_window, text="Cancel", command=generate_window.destroy, width=20)
    cancel_button.grid(row=4, column=0, columnspan=2, pady=(20, 20))


# generate function to actually generate random numbers in list
def generate():
    global nums_in_list
    global num_list
    # checking if user entered data into the entry fields
    if (amount_of_items.get() == "" or first_num.get() == "" or second_num.get() == "") \
            or (amount_of_items.get().isnumeric() is False or first_num.get().isnumeric() is False
                or second_num.get().isnumeric() is False):
        messagebox.showerror("Error!", "You have to enter numbers!")
        return  # ending a function

    # generating random numbers in list
    for i in range(0, int(amount_of_items.get())):
        number = random.randint(int(first_num.get()), int(second_num.get()))
        num_list.append(number)
        nums_in_list += f"{number}, "

    curr_array.config(text=f"Current items in list: {nums_in_list}")
    generate_window.destroy()  # closing a window after adding elements to the list


# removing a number from list
def remove_number():
    global remove_window
    global number_to_remove
    global num_list
    # checking whether the list is empty
    if not num_list:
        messagebox.showerror("Error!", "List has no numbers in it!")
        return

    # creating a new window
    remove_window = Toplevel()
    remove_window.title("Remove a number")
    remove_window.iconbitmap('sort_icon.ico')

    # label
    remove_a_number_label = Label(remove_window, text="What number do you want to remove?")
    remove_a_number_label.grid(row=0, column=0)

    # entry
    number_to_remove = Entry(remove_window)
    number_to_remove.grid(row=1, column=0)

    # buttons
    remove_button = Button(remove_window, text="Remove", command=number_removal, width=20)
    remove_button.grid(row=2, column=0, pady=(20, 20))

    cancel_button = Button(remove_window, text="Cancel", command=remove_window.destroy, width=20)
    cancel_button.grid(row=4, column=0, columnspan=2, pady=(3, 20))


# number removal function
def number_removal():
    global num_list
    global nums_in_list
    # checking if the entered data is correct
    if number_to_remove.get() == "" or number_to_remove.get().isnumeric() is False:
        messagebox.showerror("Error!", "You have to enter a number!")
        return

    if int(number_to_remove.get()) not in num_list:
        messagebox.showerror("Error!", "Entered number is not in list!")
        return

    # deleting an item
    num_list.remove(int(number_to_remove.get()))

    nums_in_list = ""
    # updating the list
    for number in num_list:
        nums_in_list += f"{number}, "

    curr_array.config(text=f"Current items in list: {nums_in_list}")
    remove_window.destroy()  # closing a window after removing an element from the list


# sorting methods list for a dropdown box
sorting_methods = [
    "Build-in sorting function",
    "Insertion sort",
    "Selection sort"
]

# adding a number
add_label = Label(root, text="Add numbers to the list", font=("Arial", 18))
add_label.grid(row=0, column=0, columnspan=2, sticky=W)

add_entry = Entry(root)
add_entry.grid(row=1, column=0, sticky=W, pady=20, padx=(0, 60))

add_btn = Button(root, text="Add to the list", command=arr_add)
add_btn.grid(row=1, column=1, sticky=W)

# displaying current items in list
curr_array = Label(root, text="Current items in list: ", font=("Arial", 16))
curr_array.grid(row=2, column=0, columnspan=4, sticky=W, pady=(0, 20))

# choosing a sorting method
choose_label = Label(root, text="Choose a sorting method", font=("Arial", 14))
choose_label.grid(row=3, column=0, columnspan=2, sticky=W)

sorting_method = StringVar(value="Build-in sorting function")

sorting_methods_dropdown = OptionMenu(root, sorting_method, *sorting_methods, command=display_sorting_method)
sorting_methods_dropdown.grid(row=4, column=0, sticky=W)

# displaying chosen sort method
chosen_sort_method = Label(root, text="You have chosen: ", font=("Arial", 14))
chosen_sort_method.grid(row=5, column=0, columnspan=4, sticky=W)

# random numbers generator
generate_random_button = Button(root, text="Generate random numbers in a list", command=generate_numbers_window)
generate_random_button.grid(row=0, column=3)

# number removal
remove_number_button = Button(root, text="Remove a number from the list", command=remove_number)
remove_number_button.grid(row=1, column=3)

# sort button
sort_button = Button(root, text="Sort", command=lambda: sort_list(sorting_method.get()), width=20)
sort_button.grid(row=6, column=0, columnspan=2, sticky=W)

display_sorting_method(sorting_method.get())  # executes the function so it displays the default value

root.mainloop()
