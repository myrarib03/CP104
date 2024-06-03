"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Myra Ribeiro
ID:      169030590
Email:   ribe0590@mylaurier.ca
__updated__ = "2023-09-24"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


PrincipalAmount = float(input("Principal: $"))
rate_interest = float(input("Interest (%):"))
converted_interest = rate_interest/100
time_left = int(input("Number of years:"))
num_compounded_interest = int(
    input("Number of times interest compounded per year:"))

money_accumulated = PrincipalAmount * \
    ((1+(converted_interest/num_compounded_interest))
     ** (time_left*num_compounded_interest))
print(money_accumulated)
