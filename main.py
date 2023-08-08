
import tkinter as tk
from tkinter import ttk

import UI.gui as gui
import UI.bin_list as binlist



def display_inc_oct():
    gui.inc_oct()
    Oct_ind_label.configure(text = gui.Octave_Num)
    
def display_dec_oct():
    gui.dec_oct()
    Oct_ind_label.configure(text = gui.Octave_Num)


if __name__ == "__main__":
## Starting and initializing tkinter
    root = tk.Tk()

    gui.init_window(root)
    
    #Frames
    title_frame = ttk.Frame(root, width = 100, height = 100, borderwidth = 1)             
    notes_frame = ttk.Frame(root,width = 100, height = 100, borderwidth = 1, relief = tk.SOLID) # ////////// Frames of window //////////
    adjusting_buttons_frame = ttk.Frame(root)
    
    #Displaying title and notes
    gui.display_title_in_GUI(title_frame)
    gui.init_display_notes(notes_frame)
    #////////////////
    
    

    ###### BUTTONS ######

    #// OCT LABEL
    Oct_ind_label = ttk.Label(master = adjusting_buttons_frame, text = gui.Octave_Num, borderwidth = 2, relief = tk.SOLID, font = ("System",15))   
    #///////// Octave Add btn ////////////
    Octave_Add_Btn = ttk.Button(master = adjusting_buttons_frame, text = '+', command = display_inc_oct)
    Octave_Add_Btn.pack(side = tk.LEFT)
    
    #//////////// Octave  Sub btn //////////
    Octave_Sub_Btn = ttk.Button(master = adjusting_buttons_frame, text = '-', command = display_dec_oct)
    Octave_Sub_Btn.pack(side = tk.LEFT)
    #//////////////////////////////
    Oct_ind_label.pack(side = tk.LEFT, padx = 10)
    
    
    #Styles
    red_coloring_style = ttk.Style()
    red_coloring_style.configure("RedBtnStyle.TLabel", foreground = 'red')
    
    

    #Packing Frames of main Window
    gui.ttk_pack_GUI_Frames(title_frame, notes_frame, adjusting_buttons_frame)
    


root.mainloop()
