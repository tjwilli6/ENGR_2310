def read_file(fname):
    infile = open(fname)
    #data = infile.read()
    #lines = data.split('\n')
    lines = infile.readlines()
    infile.close()
    params = {}
    for line in lines:
        pname,pval = line.split(':')
        params[pname] = float(pval)
    return param


def main():
    fname = 'rc_config.txt'
    params = read_file(fname)
    emf = params['emf']
    cap = params['capacitance']
    


main()
