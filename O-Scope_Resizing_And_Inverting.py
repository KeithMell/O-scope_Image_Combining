import tkinter as tk
import imageEditing


def create_image_list():
    starting_list = []
    starting_dict = {}
    error_limit = 20
    # This loop creates a list of all of the images in the folder
    for i in range(100):
        try:
            open("scope_" + str(i) + ".png", 'r')
            new_string = "scope_" + str(i) + ".png"
            starting_dict.update({new_string: 0})
            error_limit = 20
        except FileNotFoundError:
            if error_limit <= 0:
                break
            else:
                error_limit -= 1
                continue
    print(starting_dict)
    return starting_dict


class OScope:
    image_dict = None

    def __init__(self, master, i_list):
        self.master = master
        master.title("O-Scope GUI")

        self.header = tk.Label(master, text="Please select the desired images")
        self.header.pack()

        for x in i_list:
            i_list[x] = tk.Variable()
            i_list[x].set(1)
            c = tk.Checkbutton(master, text=x, onvalue=1, offvalue=0,
                               variable=i_list[x])
            c.pack()

        self.button = tk.Button(master,
                                text="Create collages", command=self.collage)
        self.button.pack()

        self.image_dict = i_list

    def collage(self):
        i_dict = self.image_dict
        new_list = []
        for key, value in i_dict.items():
            if value.get() == 1:
                new_list.append(key)
            print(value.get())
        print(new_list)
        templates = imageEditing.create_templates(new_list)
        if templates:
            imageEditing.create_collages(new_list, templates)
            print(new_list, "creating Collages")
        else:
            print("No images found")

root = tk.Tk()
orig_list = create_image_list()
my_gui = OScope(root, orig_list)
root.mainloop()
