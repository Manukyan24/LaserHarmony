
#octave list
note_dict = {
    0: [32.70, 36.95, 41.21, 43.65, 49.00, 55.00, 61.74], # Контp октава
    1: [32.70*2, 36.95*2, 41.21*2, 43.65*2, 49.00*2, 55.00*2, 61.74*2], # Большая октава
    2: [32.70*4, 36.95*4, 41.21*4, 43.65*4, 49.00*4, 55.00*4, 61.74*4], # Малая октава
    3: [32.70*8, 36.95*8, 41.21*8, 43.65*8, 49.00*8, 55.00*8, 61.74*8], # 1 октава (default N=3)
    4: [32.70*16, 36.95*16, 41.21*16, 43.65*16, 49.00*16, 55.00*16, 61.74*16], # 2 октава
    5: [32.70*32, 36.95*32, 41.21*32, 43.65*32, 49.00*32, 55.00*32, 61.74*32], # 3 октава
    6: [32.70*64, 36.95*64, 41.21*64, 43.65*64, 49.00*64, 55.00*64, 61.74*64], # 4 октава
             }

def choose_notes_f(recieved_data, N_oct):
    send_data = []
    for i in recieved_data:
        send_data.append(note_dict[N_oct][i])
    return send_data


#print(choose_notes_f([1,3,5], 2))

# def create_note_list(C,D,E,F,G,A,B):
#     note_dict = {}
#     for i in range(7):
#         note_dict.append
        


# recieved_data = [1,3,5]
# send_data = [] 
# note_list = [32.70, 36.95, 41.21, 43.65, 49.00, 55.00, 61.74]
# N = 3 # default value

# for i in range(len(recieved_data)):
#     send_data.append(note_list[recieved_data[i]]*N)
# print(send_data)







