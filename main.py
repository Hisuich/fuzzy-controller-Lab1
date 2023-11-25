import model
import random
import inference_mamdani
import fuzzy_operators

def manual_var_input(name, units, minValue, maxValue):
    while(True):
        value = input(f"Enter a {name} ({units}) {minValue} - {maxValue}: ")
        try:
            value = int(value)
            return value
        except ValueError:
            print("Invalid input. Repeat the input")

def manual_input():
    size = manual_var_input("size", "m^2", 9, 120)
    age = manual_var_input("age", "year", 0, 100)
    infrastructure = manual_var_input("infrastructure", "points", 0, 100)
    location = manual_var_input("location", "points", 0, 100)
    return [size,age,infrastructure,location]

def random_input(n):
    crisp_values = []
    for _ in range(n):
        crisp_values.append([random.randint(9, 120), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)])
    return crisp_values

inference_mamdani.preprocessing(model.input_lvs, model.output_lv)

while(True):
    command = input(f"Enter a command: m - manual input, r (N) - random input of N number of variabels, e - exit:\n")

    cmds = command.split()
    if cmds[0] == "m":
        crisp_values = manual_input()
        result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp_values)
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
            result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp_value)
            print(f"size: {crisp_value[0]}")
            print(f"age: {crisp_value[1]}")
            print(f"infrastructure: {crisp_value[2]}")
            print(f"location:{crisp_value[3]}")
            print(result)
    elif cmds[0] == "e":
        break;

crisp = manual_input()

result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)

print(result)

#for lv in model.input_lvs:
#    fuzzy_operators.draw_lv(lv)
fuzzy_operators.draw_lv(model.output_lv)









