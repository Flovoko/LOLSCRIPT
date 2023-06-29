vars_dict = {}
out = []
skip_inp = False
brk = False

print("INFO-----------------------------------------------------------------------------------------------------")
print("LOLSCRIPT V:0.1")
print("---------------------------------------------------------------------------------------------------------")

while True:
    if(brk == True):
        break
    if(skip_inp == False):
        print("")
        inp = input(">")
        print("")
    else:
        skip_inp = False
    inp_split = inp.split(" ")
    for i in range(len(inp_split)):
        if(inp_split[i] == "OUT"):
            for j in range(i,len(inp_split)):
                if(j != i):
                    if(inp_split[j] not in ["OUT", "CALC", "VAR", "VAR_LS", "HELP"]):
                        if(inp_split[j] in vars_dict.keys()):
                            out.append(vars_dict.get(inp_split[j]))
                        else:
                            out.append(inp_split[j])
                    else:
                        break
            print(" ".join(out))
            out = []
        if(inp_split[i] == "CALC"):
            try:
                for j in range(len(inp_split)):
                    if(j != 0):
                        if(inp_split[j] in vars_dict.keys()):
                            inp_split[j] = vars_dict.get(inp_split[j])
                if(inp_split[i + 2] == "+"):
                    print(int(inp_split[i + 1]) + int(inp_split[i + 3]))
                if(inp_split[i + 2] == "-"):
                    print(int(inp_split[i + 1]) - int(inp_split[i + 3]))
                if(inp_split[i + 2] == "*"):
                    print(int(inp_split[i + 1]) * int(inp_split[i + 3]))
                if(inp_split[i + 2] == "/"):
                    print(int(inp_split[i + 1]) / int(inp_split[i + 3]))
            except ValueError:
                print("VALUE ERROR")
        if(inp_split[i] == "VAR"):
            vars_dict.update({inp_split[i + 1]: inp_split[i + 2]})
        if(inp_split[i] == "VAR_LS"):
            print(vars_dict)
        if(inp_split[i] == "FILE"):
            with open(inp_split[i + 1]) as f: inp = f.read()
            skip_inp = True
        if(inp_split[i] == "HELP"):
            print("HELP-----------------------------------------------------------------------------------------------------")
            print("OUT    -> Outputs to console, usage: OUT [TEXT or VAR_NAME]")
            print("CALC   -> Calculates exqasions, usage: CALC [NUMBER1 or VAR_NAME] [(+)/(-)/(*)/(/)] [NUMBER2 or VAR_NAME]")
            print("VAR    -> Creates variables, usage: VAR [VAR_NAME] [VALUE]")
            print("VAR_LS -> Lists all variables")
            print("---------------------------------------------------------------------------------------------------------")
        if(inp_split[i] == "QUIT"):
            brk = True