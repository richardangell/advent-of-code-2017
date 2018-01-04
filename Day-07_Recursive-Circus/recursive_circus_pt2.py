import sys



def read_input(file):

    file_dict = dict()
    
    with open(file) as f:
    
        lines = f.readlines()

    for i in range(len(lines)):

        split = lines[i][:(len(lines[i]) - 1)].split(" ")
    
        name = split[0]
        
        weight = int(split[1].replace("(", "").replace(")", ""))
        
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

    
   
def get_cumulative_weights(dict, prog):
    
    print("get_cumulative_weights called on ", prog, "and")
    
    print(dict[prog])
    
    if len(dict[prog]["children"]) == 0:
        
        dict[prog]["cumulative_weight"] = dict[prog]["weight"]
        
        return(dict[prog]["cumulative_weight"])
   
    else:
    
        aa = [get_cumulative_weights(dict, x) for x in dict[prog]["children"]]
    
        print(aa)
    
        dict[prog]["cumulative_weight"] = sum(aa) + dict[prog]["weight"]
        
        for i in range(len(list(dict.keys()))):
    
            print(list(dict.keys())[i], ":", dict[list(dict.keys())[i]])
        

def find_correct_weight(file, verbose = False):

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
    
    y = get_cumulative_weights(x, bottom_program)
    
    if verbose:
    
        for i in range(0 , 10):
    
            print(dictkeys[i], ":", y[dictkeys[i]])

    
    
    return(correct_weight)


if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        find_correct_weight(sys.argv[1], sys.argv[2])

    else:

        find_correct_weight(sys.argv[1])
