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


class OScope:
    def __init__(self, master):
        self.master = master
        master.title("O-Scope GUI")

        self.header = tk.Label(master, text="Please select the desired images")
        self.header.pack()

        self.var = tk.IntVar()
        self.ints = tk.IntVar
        c = tk.Checkbutton(master, text="scope_1",
                           variable=self.var, command=self.test)
        c.pack()

        self.button = tk.Button(master, text="Create collages", command=self.collage)
        self.button.pack()

    def test(self):
        print("the variable is ", self.var.get())

    def collage(self):
        self.create_collages(new_list)

    def create_collages(self, new_list):
        templates = imageEditing.create_templates(new_list)
        imageEditing.create_collages(new_list, templates)


root = tk.Tk()
my_gui = OScope(root)
root.mainloop()
