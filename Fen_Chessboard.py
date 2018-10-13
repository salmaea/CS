def fen(s):
    row = s.split('/')                                                 
    count = 8 
    t = ''
 
    for i in range(len(row)): 
        t += str(count)
        for letter in row[i]:
            if letter.isalpha():
                t+= '  ' + letter
            elif letter.isdigit():
                t += letter.replace(letter, "  ."*int(letter)) 
        t += '\n'
        count = count - 1
        
    t1 = '   a  b  c  d  e  f  g  h'
    return t + t1

s = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
board = fen(s)
#print(board)
