import numpy as np

def __normalization(x, _range):
    x_min, x_max, dx = _range
    return (x - x_min) / (x_max - x_min) * 10


def fuzzification(crisp_values, input_lvs):
    """
    Returns the result of Fuzzification.
    """
    result = {}
    for index, crisp_value in enumerate(crisp_values):
        x = __normalization(crisp_value, input_lvs[index]['X'])
        x_curr = np.argmax(input_lvs[index]['U'] >= x)
        #print(x_curr)
        result[index] = {}
        for term_name, term in input_lvs[index]['terms'].items():
            #print(term_name)
            #print(term['umf'][x_curr])
            #print(term['lmf'][x_curr])
            if term['umf'][x_curr] > 0:
                #print(term['umf'][x_curr])
                #print(term['lmf'][x_curr])
                result[index][term_name] = term['lmf'][x_curr], term['umf'][x_curr]

    return result

