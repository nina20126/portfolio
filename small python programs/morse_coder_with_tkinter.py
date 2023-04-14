'''
Create a morse coder
'''

from tkinter import *
from tkinter import messagebox

root = Tk()

variable1 = StringVar(root)
variable2 = StringVar(root)

variable1.set("lang-code")
variable2.set("lang-code")


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-',
		            'a':'.-', 'b':'-...',
					'c':'-.-.', 'd':'-..', 'e':'.',
					'f':'..-.', 'g':'--.', 'h':'....',
					'i':'..', 'j':'.---', 'k':'-.-',
					'l':'.-..', 'm':'--', 'n':'-.',
					'o':'---', 'p':'.--.', 'q':'--.-',
					'r':'.-.', 's':'...', 't':'-',
					'u':'..-', 'v':'...-', 'w':'.--',
					'x':'-..-', 'y':'-.--', 'z':'--..'}

def clearAll():
	language1_field.delete(1.0, END)
	language2_field.delete(1.0, END)

def convert():
    message = language1_field.get("1.0", "end")[:-1]
    try: 
        if variable1.get() == "Eng" and variable2.get() == "Morse":
            result = encrypt(message)

        elif variable1.get() == "Morse" and variable2.get() == "Eng":
            result = decrypt(message)

        else:
            messagebox.showerror("Something went wrong")
            return
	
    except:
        messagebox.showerror("Something went wrong")
        return
	
    language2_field.insert('end -1 chars', result)
	
		
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
			
		else:
			cipher += ' '

	return cipher


def decrypt(message):
	message += ' '
	decipher = ''
	citext = ''
	for letter in message:
		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[
							list(MORSE_CODE_DICT .values()).index(citext)]
				citext = ''
	return decipher


if __name__ == "__main__" :
	root.configure(background = '#f1faee')
	root.geometry("400x350")
	root.title("Translator")
	
	headlabel = Label(root, text = 'Welcome to Morse Code Translator', fg = 'black', bg = "#a8dadc")

	label1 = Label(root, text = "Write here -->", fg = 'black', bg = '#a8dadc')
	label2 = Label(root, text = "From Language", fg = 'black', bg = '#a8dadc')
	label3 = Label(root, text = "To Language ", fg = 'black', bg = '#a8dadc')
	label4 = Label(root, text = "Converted Language ", fg = 'black', bg = '#a8dadc')

	headlabel.grid(row = 0, column = 1) #title
	label1.grid(row = 1, column = 0) #write here
	label2.grid(row = 2, column = 0) #from languare
	label3.grid(row = 4, column = 0) #to language
	label4.grid(row = 5, column = 0) #converted language
	
	language1_field = Text(root, height = 5, width = 25, font = "lucida 13")
	language2_field = Text(root, height = 5, width = 25, font = "lucida 13")
		
	language1_field.grid(row = 1, column = 1, padx = 10)
	language2_field.grid(row = 5, column = 1, padx = 10)

	languageCode_list = ["Eng", "Morse"]

	FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
	ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)
	
	FromLanguage_option.grid(row = 2, column = 1, ipadx = 10)
	ToLanguage_option.grid(row = 4, column = 1, ipadx = 10)
	
	button1 = Button(root, text = "Convert", bg = "#1d3557", fg = "#f1faee", command = convert)
	button1.grid(row = 3, column = 1)

	button2 = Button(root, text = "Clear", bg = "#1d3557", fg = "#f1faee", command = clearAll)
	button2.grid(row = 6, column = 1)

	root.mainloop()
