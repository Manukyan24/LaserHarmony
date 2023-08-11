
import tkinter as tk
from tkinter import ttk

import UI.gui as gui
import UI.octave as octave
import UI.sound as sound
import UI.ArduinoEmulation as ardem

import Data.bin_list as binlist
#import Data.bluetoothdata as blut
import serial
import time



#Bluetooth init
#bluetooth = serial.Serial('COM4', 9600, timeout = 0.3)

DURATION = 0.5

def read_bt():                              ##### RETURNS DECIMAL NUMBER THAT INDICATES CLOSED notes
    global bluetooth
    #bluetooth.flushInput()
    #input_data = int((bluetooth.readline().strip().decode("UTF-8")))
    input_data = ardem.signal_emulator()
    time.sleep(0.3)
    
    return input_data


def note_paint_pattern_get(choose_note_list):
    act_vector = [0,0,0,0,0,0,0]
    for i in choose_note_list:
        act_vector[i] = 1

    return act_vector




def test_main_loop():
    Bluetooth_Data = read_bt() # Number that indicates closed notes
    closed_notes_indexes =  binlist.none_zero_list(Bluetooth_Data)
    #list of playing freq
    freq_list = octave.choose_notes_f(closed_notes_indexes, gui.Octave_Num)
    print(freq_list)
    # BitMask for color activation    
    color_activation_mask = note_paint_pattern_get(closed_notes_indexes)
    gui.clear_note_color_setting()
    gui.activated_note_color_setting(color_activation_mask)
    
    

    #playing sound
    tones_1 = sound.generate_tones(freq_list,DURATION)
    print(tones_1)
    sound.play_audio(tones_1)
    
    
    root.after(500, test_main_loop)
    



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
    
    #Tkinter Frames
    title_frame = ttk.Frame(root, width = 100, height = 100, borderwidth = 1)             
    notes_frame = ttk.Frame(root,width = 100, height = 100, borderwidth = 1, relief = tk.SOLID)
    adjusting_buttons_frame = ttk.Frame(root)
    
    #Displaying title and notes
    gui.display_title_in_GUI(title_frame)
    gui.init_display_notes(notes_frame)

    
    
    ###### BUTTONS ######
    
    #Oct label
    Oct_ind_label = ttk.Label(master = adjusting_buttons_frame, text = gui.Octave_Num, borderwidth = 2, relief = tk.SOLID, font = ("System",15))   
    #Octave Add btn
    Octave_Add_Btn = ttk.Button(master = adjusting_buttons_frame, text = '+', command = display_inc_oct)
    Octave_Add_Btn.pack(side = tk.LEFT)
    
    #Octave Sub btn
    Octave_Sub_Btn = ttk.Button(master = adjusting_buttons_frame, text = '-', command = display_dec_oct)
    Octave_Sub_Btn.pack(side = tk.LEFT)
    
    Oct_ind_label.pack(side = tk.LEFT, padx = 10)
    
       
    #Styles
    red_coloring_style = ttk.Style()
    red_coloring_style.configure("RedBtnStyle.TLabel", foreground = 'red')

    default_style = ttk.Style()
    default_style.configure("DefStyle.TLabel", foreground = 'black')
    
    #Packing Frames of main Window
    gui.ttk_pack_GUI_Frames(title_frame, notes_frame, adjusting_buttons_frame)
    


    root.after(2000,test_main_loop)
    root.mainloop()
    
    
