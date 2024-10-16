

import re


def getNumericData(user_input):

    try:
        data=''.join(filter(str.isdigit,user_input))

        return data
    except:
        return print("no numeric value")
        