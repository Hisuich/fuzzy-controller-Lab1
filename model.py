input_lvs = [
    {
        'X': (0, 10.1, 0.01),
        'name': 'Possibility',
        'terms': {
            'None to very little':              {'umf': ('trapmf', 0, 0, 0.22, 3.16),       'lmf': ('trapmf', 0, 0, 0.02, 0.33, 1)},
            'Very low':                         {'umf': ('trapmf', 0, 0, 1.37, 3.95),       'lmf': ('trapmf', 0, 0, 0.14, 1.82, 1)},
            'Low':                              {'umf': ('trapmf', 0.38, 1.63, 3.00, 4.62), 'lmf': ('trapmf', 1.90, 2.24, 2.24, 2.51, 0.31)},
            'More or less low':                 {'umf': ('trapmf', 0.38, 2.25, 4.00, 5.92), 'lmf': ('trapmf', 2.99, 3.31, 3.31, 3.81, 0.32)},
            'From fair to more or less high':   {'umf': ('trapmf', 2.33, 5.11, 7.00, 9.59), 'lmf': ('trapmf', 5.79, 6.31, 6.31, 7.21, 0.43)},
            'More or less high':                {'umf': ('trapmf', 4.38, 6.25, 8.00, 9.62), 'lmf': ('trapmf', 6.90, 7.21, 7.21, 7.60, 0.29)},
            'High':                             {'umf': ('trapmf', 4.73, 8.82, 10, 10),     'lmf': ('trapmf', 7.68, 9.82, 10, 10, 1)},
            'Extremely high':                   {'umf': ('trapmf', 7.10, 9.80, 10, 10),     'lmf': ('trapmf', 9.74, 9.98, 10, 10, 1)},
    }
    },

    {
        'X': (0, 10.1, 0.01),
        'name': 'Impact',
        'terms': {
            'None to very little':              {'umf': ('trapmf', 0, 0, 0.22, 3.16),       'lmf': ('trapmf', 0, 0, 0.02, 0.33, 1)},
            'Extremely low':                    {'umf': ('trapmf', 0, 0, 0.46, 2.63),       'lmf': ('trapmf', 0, 0, 0.06, 0.92, 1)},
            'Very low':                         {'umf': ('trapmf', 0, 0, 1.37, 3.95),       'lmf': ('trapmf', 0, 0, 0.14, 1.82, 1)},
            'Low':                              {'umf': ('trapmf', 0.38, 1.63, 3.00, 4.62), 'lmf': ('trapmf', 1.90, 2.24, 2.24, 2.51, 0.31)},
            'More or less low':                 {'umf': ('trapmf', 0.38, 2.25, 4.00, 5.92), 'lmf': ('trapmf', 2.99, 3.31, 3.31, 3.81, 0.32)},
            'Somewhat low':                     {'umf': ('trapmf', 0.98, 2.75, 4.00, 5.46), 'lmf': ('trapmf', 2.79, 3.30, 3.30, 3.71, 0.42)},
            'Moderately low':                   {'umf': ('trapmf', 0.38, 2.50, 4.50, 6.62), 'lmf': ('trapmf', 2.95, 3.18, 3.18, 3.30, 0.15)},
            'From low to more or less fair':    {'umf': ('trapmf', 0.17, 2.73, 4.80, 7.91), 'lmf': ('trapmf', 3.29, 3.75, 3.75, 4.21, 0.31)},
            'From fair to more or less high':   {'umf': ('trapmf', 2.33, 5.11, 7.00, 9.59), 'lmf': ('trapmf', 5.79, 6.31, 6.31, 7.21, 0.43)},
            'More or less high':                {'umf': ('trapmf', 4.38, 6.25, 8.00, 9.62), 'lmf': ('trapmf', 6.90, 7.21, 7.21, 7.60, 0.29)},
            'Somewhat high':                    {'umf': ('trapmf', 4.48, 6.25, 8.15, 9.52), 'lmf': ('trapmf', 6.81, 7.27, 7.27, 7.81, 0.35)},
            'Moderately high':                  {'umf': ('trapmf', 5.59, 6.75, 8.00, 9.56), 'lmf': ('trapmf', 6.79, 7.30, 7.30, 7.71, 0.42)},
            'High':                             {'umf': ('trapmf', 4.73, 8.82, 10, 10),     'lmf': ('trapmf', 7.68, 9.82, 10, 10, 1)},
            'Very high':                        {'umf': ('trapmf', 6.05, 9.36, 10, 10),     'lmf': ('trapmf', 8.71, 9.91, 10, 10, 1)},
            'Extremely high':                   {'umf': ('trapmf', 7.10, 9.80, 10, 10),     'lmf': ('trapmf', 9.74, 9.98, 10, 10, 1)},
    }
    },
]

output_lv = {
    'X': (0, 10.1, 0.01),
    'name': 'Risk',
    'terms': {
        'None to very little': {'umf': ('trapmf', 0, 0, 0.22, 3.16), 'lmf': ('trapmf', 0, 0, 0.02, 0.33, 1)},
        'Very low': {'umf': ('trapmf', 0, 0, 1.37, 3.95), 'lmf': ('trapmf', 0, 0, 0.14, 1.82, 1)},
        'Low': {'umf': ('trapmf', 0.38, 1.63, 3.00, 4.62), 'lmf': ('trapmf', 1.90, 2.24, 2.24, 2.51, 0.31)},
        'More or less low': {'umf': ('trapmf', 0.38, 2.25, 4.00, 5.92), 'lmf': ('trapmf', 2.99, 3.31, 3.31, 3.81, 0.32)},
        'From fair to more or less high': {'umf': ('trapmf', 2.33, 5.11, 7.00, 9.59), 'lmf': ('trapmf', 5.79, 6.31, 6.31, 7.21, 0.43)},
        'More or less high': {'umf': ('trapmf', 4.38, 6.25, 8.00, 9.62), 'lmf': ('trapmf', 6.90, 7.21, 7.21, 7.60, 0.29)},
        'High': {'umf': ('trapmf', 4.73, 8.82, 10, 10), 'lmf': ('trapmf', 7.68, 9.82, 10, 10, 1)},
        'Extremely high': {'umf': ('trapmf', 7.10, 9.80, 10, 10), 'lmf': ('trapmf', 9.74, 9.98, 10, 10, 1)},
    }
}

inputTerms = []
outputTerms = []
for term_name, term in output_lv['terms'].items():
    outputTerms.append(term_name)

for index, values  in enumerate(input_lvs):
    inputTerms.append([])
    for term_name, term in input_lvs[index]['terms'].items():
        inputTerms[index].append(term_name)

rules = [] 
totalTermsCount = sum(len(row) for row in inputTerms)
outputTermsCount = len(outputTerms)
for i, iterm in enumerate(inputTerms[0]):
    for j, jterm in enumerate(inputTerms[1]):
        outputTermNumber = round(((i+j+2)/totalTermsCount)*outputTermsCount)
        rules.append(((iterm, jterm), outputTerms[outputTermNumber-1]))

#for i, rule in enumerate(rules):
#    print(rule)

rule_base = rules
'''
[
    (('None to very little', 'None to very little'), 'None to very little')
(('None to very little', 'Extremely low'), 'None to very little')
(('None to very little', 'Very low'), 'None to very little')
(('None to very little', 'Low'), 'Very low')
(('None to very little', 'More or less low'), 'Very low')
(('None to very little', 'Somewhat low'), 'Very low')
(('None to very little', 'Moderately low'), 'Low')
(('None to very little', 'From low to more or less fair'), 'Low')
(('None to very little', 'From fair to more or less high'), 'Low')
(('None to very little', 'More or less high'), 'More or less low')
(('None to very little', 'Somewhat high'), 'More or less low')
(('None to very little', 'Moderately high'), 'From fair to more or less high')
(('None to very little', 'High'), 'From fair to more or less high')
(('None to very little', 'Very high'), 'From fair to more or less high')
(('None to very little', 'Extremely high'), 'More or less high')
(('Very low', 'None to very little'), 'None to very little')
(('Very low', 'Extremely low'), 'None to very little')
(('Very low', 'Very low'), 'Very low')
(('Very low', 'Low'), 'Very low')
(('Very low', 'More or less low'), 'Very low')
(('Very low', 'Somewhat low'), 'Low')
(('Very low', 'Moderately low'), 'Low')
(('Very low', 'From low to more or less fair'), 'Low')
(('Very low', 'From fair to more or less high'), 'More or less low')
(('Very low', 'More or less high'), 'More or less low')
(('Very low', 'Somewhat high'), 'From fair to more or less high')
(('Very low', 'Moderately high'), 'From fair to more or less high')
(('Very low', 'High'), 'From fair to more or less high')
(('Very low', 'Very high'), 'More or less high')
(('Very low', 'Extremely high'), 'More or less high')
(('Low', 'None to very little'), 'None to very little')
(('Low', 'Extremely low'), 'Very low')
(('Low', 'Very low'), 'Very low')
(('Low', 'Low'), 'Very low')
(('Low', 'More or less low'), 'Low')
(('Low', 'Somewhat low'), 'Low')
(('Low', 'Moderately low'), 'Low')
(('Low', 'From low to more or less fair'), 'More or less low')
(('Low', 'From fair to more or less high'), 'More or less low')
(('Low', 'More or less high'), 'From fair to more or less high')
(('Low', 'Somewhat high'), 'From fair to more or less high')
(('Low', 'Moderately high'), 'From fair to more or less high')
(('Low', 'High'), 'More or less high')
(('Low', 'Very high'), 'More or less high')
(('Low', 'Extremely high'), 'More or less high')
(('More or less low', 'None to very little'), 'Very low')
(('More or less low', 'Extremely low'), 'Very low')
(('More or less low', 'Very low'), 'Very low')
(('More or less low', 'Low'), 'Low')
(('More or less low', 'More or less low'), 'Low')
(('More or less low', 'Somewhat low'), 'Low')
(('More or less low', 'Moderately low'), 'More or less low')
(('More or less low', 'From low to more or less fair'), 'More or less low')
(('More or less low', 'From fair to more or less high'), 'From fair to more or less high')
(('More or less low', 'More or less high'), 'From fair to more or less high')
(('More or less low', 'Somewhat high'), 'From fair to more or less high')
(('More or less low', 'Moderately high'), 'More or less high')
(('More or less low', 'High'), 'More or less high')
(('More or less low', 'Very high'), 'More or less high')
(('More or less low', 'Extremely high'), 'High')
(('From fair to more or less high', 'None to very little'), 'Very low')
(('From fair to more or less high', 'Extremely low'), 'Very low')
(('From fair to more or less high', 'Very low'), 'Low')
(('From fair to more or less high', 'Low'), 'Low')
(('From fair to more or less high', 'More or less low'), 'Low')
(('From fair to more or less high', 'Somewhat low'), 'More or less low')
(('From fair to more or less high', 'Moderately low'), 'More or less low')
(('From fair to more or less high', 'From low to more or less fair'), 'From fair to more or less high')
(('From fair to more or less high', 'From fair to more or less high'), 'From fair to more or less high')
(('From fair to more or less high', 'More or less high'), 'From fair to more or less high')
(('From fair to more or less high', 'Somewhat high'), 'More or less high')
(('From fair to more or less high', 'Moderately high'), 'More or less high')
(('From fair to more or less high', 'High'), 'More or less high')
(('From fair to more or less high', 'Very high'), 'High')
(('From fair to more or less high', 'Extremely high'), 'High')
(('More or less high', 'None to very little'), 'Very low')
(('More or less high', 'Extremely low'), 'Low')
(('More or less high', 'Very low'), 'Low')
(('More or less high', 'Low'), 'Low')
(('More or less high', 'More or less low'), 'More or less low')
(('More or less high', 'Somewhat low'), 'More or less low')
(('More or less high', 'Moderately low'), 'From fair to more or less high')
(('More or less high', 'From low to more or less fair'), 'From fair to more or less high')
(('More or less high', 'From fair to more or less high'), 'From fair to more or less high')
(('More or less high', 'More or less high'), 'More or less high')
(('More or less high', 'Somewhat high'), 'More or less high')
(('More or less high', 'Moderately high'), 'More or less high')
(('More or less high', 'High'), 'High')
(('More or less high', 'Very high'), 'High')
(('More or less high', 'Extremely high'), 'High')
(('High', 'None to very little'), 'Low')
(('High', 'Extremely low'), 'Low')
(('High', 'Very low'), 'Low')
(('High', 'Low'), 'More or less low')
(('High', 'More or less low'), 'More or less low')
(('High', 'Somewhat low'), 'From fair to more or less high')
(('High', 'Moderately low'), 'From fair to more or less high')
(('High', 'From low to more or less fair'), 'From fair to more or less high')
(('High', 'From fair to more or less high'), 'More or less high')
(('High', 'More or less high'), 'More or less high')
(('High', 'Somewhat high'), 'More or less high')
(('High', 'Moderately high'), 'High')
(('High', 'High'), 'High')
(('High', 'Very high'), 'High')
(('High', 'Extremely high'), 'Extremely high')
(('Extremely high', 'None to very little'), 'Low')
(('Extremely high', 'Extremely low'), 'Low')
(('Extremely high', 'Very low'), 'More or less low')
(('Extremely high', 'Low'), 'More or less low')
(('Extremely high', 'More or less low'), 'From fair to more or less high')
(('Extremely high', 'Somewhat low'), 'From fair to more or less high')
(('Extremely high', 'Moderately low'), 'From fair to more or less high')
(('Extremely high', 'From low to more or less fair'), 'More or less high')
(('Extremely high', 'From fair to more or less high'), 'More or less high')
(('Extremely high', 'More or less high'), 'More or less high')
(('Extremely high', 'Somewhat high'), 'High')
(('Extremely high', 'Moderately high'), 'High')
(('Extremely high', 'High'), 'High')
(('Extremely high', 'Very high'), 'Extremely high')
(('Extremely high', 'Extremely high'), 'Extremely high')
]
'''
