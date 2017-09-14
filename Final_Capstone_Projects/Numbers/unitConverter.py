"""
 Converts various units between one another. The user enters the type of unit being entered,
 the type of unit they want to convert to and then the value. The program will then make the conversion.
"""

supported_conversions = {
    # Number of feet per unit
    'length': {'feet': 1,
               'inch': 12,
               'yard': 1/3,
               'mile': 0.000189394,
               'millimeter': 304.8,
               'centimeter': 30.48,
               'meter': 0.3048,
               'kilometer': 0.0003048},
    # Number of seconds per unit
    'time': {'seconds': 1,
             'minute': 0.0166667,
             'hour': 0.00027777833333,
             'day': 1.1574e-5,
             'week': 1.6534e-6,
             'month': 3.80508076156e-7,
             'year': 3.171e-8,
             'decade': 3.1710001268e-9,
             'century': 3.17100012680000627e-10},
    # Number of pounds per unit
    'mass': {'pound': 1,
             'ounce': 16,
             'milligram': 453592,
             'gram': 453.59199986863,
             'kilogram': 0.45359199986863002474,
             'metric ton': 0.000453592,
             'us ton': 0.000499999592144814947}
}


def convert_length(input_unit, new_unit, units, conversion_dict):
    feet = (units / conversion_dict[input_unit])
    return feet * conversion_dict[new_unit]


def get_conversion_type(supported_conversions):
    while True:
        print(supported_conversions.keys())
        response = input('What would you like to conversion: ')
        if response in supported_conversions.keys():
            return response


def get_conversion_unit(prompt, conversion_dict):
    while True:
        unit = input(prompt)
        if unit not in conversion_dict.values():
            print("That unit is not supported")
            continue
        return unit


def get_numerical_input(prompt):
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print("That's not a number")
            continue
        else:
            return response

conversion = get_conversion_type()
print(supported_conversions[conversion].values())
input_unit = ('Enter your desired starting unit', supported_conversions[conversion])
units = get_numerical_input('Please enter the number of units')
new_unit = ('Enter your desired starting unit', supported_conversions[conversion])
