import random
import model
import t2_mandani_inference

def manual_var_input(name, units, minValue, maxValue):
    while(True):
        value = input(f"Enter a {name} ({units}) {minValue} - {maxValue}: ")
        try:
            value = int(value)
            return value
        except ValueError:
            print("Invalid input. Repeat the input")

def manual_input():
    posibility = manual_var_input("posibility", "%", 0, 100)
    impact = manual_var_input("impact", "points", 0, 100)
    return [posibility,impact]

def random_input(n):
    crisp_values = []
    for _ in range(n):
        crisp_values.append([random.randint(1, 100), random.randint(1, 100)])
    return crisp_values    

t2_mandani_inference.preprocessing(model.input_lvs, model.output_lv)

while(True):
    command = input(f"Enter a command: m - manual input, r (N) - random input of N number of variabels, e - exit:\n")

    cmds = command.split()
    if cmds[0] == "m":
        crisp_values = manual_input()
        result = t2_mandani_inference.process(model.input_lvs, model.output_lv, model.rule_base, crisp_values)
        print(result)
    elif cmds[0] == "r":
        crisp_values = random_input
        try:
            N = int(cmds[1])
        except IndexError:
            N = 1
        except ValueError:
            N = 1
            
        crisp_values = random_input(N)
        for i, crisp_value in enumerate(crisp_values):
            result = t2_mandani_inference.process(model.input_lvs, model.output_lv, model.rule_base, crisp_value)
            print(f"posibility: {crisp_value[0]}")
            print(f"impact: {crisp_value[1]}")
            print(result)
    elif cmds[0] == "e":
        break;
   
