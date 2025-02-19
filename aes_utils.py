def get_hex_str(byte):
    hexa = hex(byte)[2:]
    while len(hexa) < 2:
        hexa = "0" + hexa
    return hexa


def show_substate(row, end=""):
    for byte in row:
        hexa = get_hex_str(byte)
        print(hexa, end=" ")
        print("", end=end)


def show_state(state_list, row_major=True):
    if row_major:
        print("┌─ row-major ─┐")
    else:
        print("┌column──major┐")
    for word in state_list:
        print("│ ", end="")
        show_substate(word)
        print("│")
    print("└─────────────┘")


def show_state_dec(state_list, row_major=True):
    if row_major:
        print("┌─── row-major ───┐")
    else:
        print("┌──column──major──┐")
    for substate in state_list:
        print("│ ", end="")
        for value in substate:
            if len(str(value)) == 1:
                padded_value = " " + str(value) + " "
            elif len(str(value)) == 2:
                padded_value = str(value) + " "
            else:
                padded_value = str(value)
            print(padded_value, end=" ")
        print("│")

    print("└──── base10 ─────┘")


##################### Key extension specific #####################

def show_word(word):
    for byte in word:
        hexa = get_hex_str(byte)
        print(hexa, end=" ")
    print()


def show_words(word_list):
    #print(word_list)
    print("-  Round words -")
    for nb, word in enumerate(word_list):
        print(f"word {nb}", end="")
        if nb < 10:
            print(" ", end="")
        print(": ", end="")
        show_word(word)
