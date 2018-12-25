import tkinter as tk
import imageEditing


def create_image_list():
    starting_list = []
    error_limit = 20
    # This loop creates a list of all of the images in the folder
    for i in range(100):
        try:
            fp = open("scope_" + str(i) + ".png", 'r')
            starting_list.append("scope_" + str(i) + ".png")
            error_limit = 20
        except FileNotFoundError:
            if error_limit <= 0:
                break
            else:
                error_limit -= 1
                continue
    return starting_list


def create_buttons(orig_image_list, b_list):
    var_list = [0]*len(orig_image_list)
    for i in orig_image_list:
        index = orig_image_list.index(i)
        temp_button = tk.Checkbutton(root, text=i, variable=var_list[index])
        temp_button.pack()
        b_list.append(temp_button)
    return b_list, var_list


def create_collages():
    print("testing")
    print("")


root = tk.Tk()

one = tk.Label(root, text="Please select the desired images")
one.pack()

button_list = create_buttons(create_image_list(), [])[0]
variables = create_buttons(create_image_list(), [])[1]

collage_b = tk.Button(root, text="Create collages", command=create_collages)
collage_b.pack()

root.mainloop()










