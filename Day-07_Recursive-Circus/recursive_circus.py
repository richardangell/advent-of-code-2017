import sys



def read_input(file):

    file_dict = dict()
    
    with open(file) as f:
    
        lines = f.readlines()

    for i in range(len(lines)):

        split = lines[i][:(len(lines[i]) - 1)].split(" ")
    
        name = split[0]
        
        weight = split[1].replace("(", "").replace(")", "")
        
        if len(split) > 2:
        
            children = [x.replace(",", "") for x in split[3:]]
        
        else:
        
            children = []
        
        file_dict[name] = {"weight": weight, "children": children}
    
    file_dict_keys = list(file_dict.keys())
    
    for i in range(len(file_dict_keys)):
        
        children = file_dict[file_dict_keys[i]]["children"]
        
        n_children = len(children)
        
        if n_children > 0:
            
            for j in range(n_children):
                
                file_dict[children[j]]["parent"] = file_dict_keys[i]
            
    return(file_dict)

    
    
    

def get_bottom_program(file, verbose = False):

    x = read_input(file)
    
    verbose = bool(verbose)
    
    dictkeys = list(x.keys())
    
    if verbose:
    
        for i in range(0 , 10):
    
            print(dictkeys[i], ":", x[dictkeys[i]])

    for i in range(len(dictkeys)):
    
        if not "parent" in x[dictkeys[i]]:
        
            bottom_program = dictkeys[i]
            
            break

    print(bottom_program)
    
    return(bottom_program)


if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        get_bottom_program(sys.argv[1], sys.argv[2])

    else:

        get_bottom_program(sys.argv[1])
