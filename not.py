def text_to_notes(text, piano_model):
    notes = []

    for char in text:
        if char in piano_model:
            notes.append(piano_model[char])
        else:
            # Se o caractere não estiver no modelo, mantenha o caractere original
            notes.append(char)

    return notes

# Piano model = VirtualPiano.net
piano_model = {
    '1': 'C2', '!': 'C#2', '2': 'D2', '@': 'D#2', '3': 'E2', '4': 'F2', '$': 'F#2', '5': 'G2', '%': 'G#2',
    '6': 'A2', '^': 'A#2', '7': 'B2', '8': 'C3', '*': 'C#3', '9': 'D3', '(': 'D#3', '0': 'E3', 'q': 'F3', 'Q': 'F#3',
    'w': 'G3', 'W': 'G#3', 'e': 'A3', 'E': 'A#3', 'r': 'B3', 't': 'C4', 'T': 'C#4', 'y': 'D4', 'Y': 'D#4', 'u': 'E4',
    'i': 'F4', 'I': 'F#4', 'o': 'G4', 'O': 'G#4', 'p': 'A4', 'P': 'A#4', 'a': 'B4', 's': 'C5', 'S': 'C#5', 'd': 'D5',
    'D': 'D#5', 'f': 'E5', 'g': 'F5', 'G': 'F#5', 'h': 'G5', 'H': 'G#5', 'j': 'A5', 'J': 'A#5', 'k': 'B5', 'l': 'C6',
    'L': 'C#6', 'z': 'D6', 'Z': 'D#6', 'x': 'E6', 'c': 'F6', 'C': 'F#6', 'v': 'G6', 'V': 'G#6', 'b': 'A6', 'B': 'A#6',
    'n': 'B6', 'm': 'C7'
}

# Input file name
# Arquivo de entrada ex: 'lista do virtual piano.txt'
input_file_name = 'conv.txt'

# Reading the content of the file and assigning it to the variable text_example
# Lendo o conteúdo do arquivo e atribuindo à variável texto_example
with open(input_file_name, 'r') as input_file:
    text_example = input_file.read()

# Converting the text to piano notes // Convertendo o texto para notas de piano
resultant_notes = text_to_notes(text_example, piano_model)

# Printing the resultant notes as text // notas como texto
resultant_text = ' '.join(resultant_notes)
print(resultant_text)

# Output file name
# Nome do arquivo de saída
output_file_name = 'Gwyn - lord of cinder.txt'

# Saving the result to a new file
with open(output_file_name, 'w') as output_file:
    output_file.write(resultant_text)
