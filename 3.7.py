char = input('Inserisci un carattere: \n')
word_1 = input('inserisci una stringa: \n')

while word_1.count(char) < 2: 
    word_1 = input('inserisci una stringa: \n')
    

print('Il carattere', char, 'compare', word_1.count(char), 'volte')
