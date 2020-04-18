fh = open("C:/Users/xc/Downloads/sequence.fasta", "r")

counter = 1
lst = []
body = ''

# Lempel-Ziv converter
def l_ziv(b):
    lst_1 = []
    pos = 0
    length = 1

    while pos+length < 1 + len(b):
        substr = b[pos:pos+length]
        if substr in lst_1 and pos+length != len(b):
            length += 1
        elif substr in lst_1 and pos+length == len(b):
            lst_1.append(substr)
            break
        else:
            lst_1.append(substr)
            substr = ''
            pos += length
            length = 1
    return len(lst_1)


# Reading input file
for line in fh:
    if line.startswith('>'):
        name = line.rstrip('\n')
        body = ''
    else:
        if line != '\n' or '':
            line = line.rstrip('\n')
            body += line
        else:
            lz = l_ziv(body)
            tpl = (lz, name, body)
            lst.append(tpl)

# Function to print readable output of NCD
def print_output(seq1, seq2, lz_sum):
    lz_seq1 = lst[seq1][0]
    lz_seq2 = lst[seq2][0]
    ncd = (lz_sum - min(lz_seq1, lz_seq2))/max(lz_seq1, lz_seq2) # ncd
    print('\nFor {} \nand {} \nNCD = {}\n\n'.format(lst[seq1][1], lst[seq2][1], ncd))

# Normalized Compression Distance (all to all)
size = len(lst) # 13 in test example
pos = 0
move = pos + 1


for pos in range(size):
    for move in range(1, size):
        if pos + move < size:
            substr = lst[pos][2].rstrip('\n') + lst[pos+move][2].rstrip('\n')
            lz = l_ziv(substr)
            print_output(pos, pos+move, lz)
            # print(pos, pos+move, lz, substr)
        move += 1
    pos += 1
    move = pos +1


