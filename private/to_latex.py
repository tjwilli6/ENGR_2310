import sys

fname = sys.argv[1]

with open(fname) as f:
    lines = f.readlines()
    for l in lines:
        rawline = l.replace('\n','')
        preamble = ''
        while "    " in rawline:
            rawline=rawline.replace("    ","",1)
            preamble += '\quad\quad'
        if preamble:
            preamble = r'\null' + preamble
        print(preamble,end='')
        print(r'\texttt{',end='')
        print(rawline,end='')
        print(r'}\\')
