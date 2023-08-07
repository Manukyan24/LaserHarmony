import tkinter as tk
from tkinter import ttk


#/////..... GLOBAL CONSTANTS ...../////
WIN_W = 720 # Windows width
WIN_H = 480 # Windows height
notes = ['A','B','C','D','E','F','G','A','B']
notes_font = ("System",18) # Font of displaying of notes letters 
notes_borderwidth = 40 # distance beetwen two neighbour notes
Notes_Label_List = [] # Will contain notes label objects



def init_display_notes(notes_frame):
    for note in notes:
        label = ttk.Label(master = notes_frame, text = note, borderwidth = notes_borderwidth, font = notes_font)
        label.pack(side = tk.LEFT)
        Notes_Label_List.append(label)


def init_window(root):
    root.title("LaserHarmonics")
    root.geometry(str(WIN_W) + 'x' + str(WIN_H))
    

def display_title_in_GUI(ttk_title_frame):
    ttk.Label(master = ttk_title_frame, text = "LaserHarmonics", font = ("System", 14)).pack()


def activated_note_color_setting(trigered_notes_list):
    i = 0
    for labels in Notes_Label_List:
        if trigered_notes_list[i] == 1:
            labels.configure(style = "RedBtnStyle.TLabel")



def ttk_pack_GUI_Frames(title_frame,notes_frame,adjusting_buttons_frame):
    title_frame.pack()
    notes_frame.pack(padx = 10, pady = 100)
    adjusting_buttons_frame.pack(side = tk.LEFT, padx = 10)



class Octave:
    Octave_Num = 0
    def __init__(self):
        self.Octave_Num = 0
    def inc_oct(self, oct_num_ind):
        self.Octave_Num += 1
        oct_num_ind.configure(text = self.Octave_Num)
    def dec_oct(self, oct_num_ind):
        self.Octave_Num -= 1
        oct_num_ind.configure(text = self.Octave_Num)
        

#red_coloring_style = ttk.Style() # ttk Style for changing trigered notes color
#red_coloring_style.configure("RedBtnStyle.TLabel", foreground = 'red')





