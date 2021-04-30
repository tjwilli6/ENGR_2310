def read_file(fname):
    infile = open(fname)
    data = infile.readlines()
    infile.close()
    param_names = []
    param_vals = []
    for line in data:
        pname,pval = line.split(':')
        param_names.append(pname)
        param_vals.append(float(pval))
    return param_names,param_vals


def main():
    fname = 'rc_config.txt'
    param_names, param_values = read_file(fname)
    for i in range(len(param_names)):
        print(param_names[i],param_values[i])

    for i in range(len(param_names)):
        if param_names[i] == 'emf':
            emf = param_values[i]
        elif param_names[i] == 'capacitance':
            cap = param_values[i]
        elif param_names[i] == 'resistance':
            res = param_values[i]
        elif param_names[i] == 'inductance':
            ind = param_values[i]

main()
