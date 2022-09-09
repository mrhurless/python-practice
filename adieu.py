"""
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. 
Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names 
with two commas and one and, and n names with n−1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""
import inflect

p = inflect.engine()

names = []

try:
    while True:
        names.append(input('Name: '))
except EOFError:
    if len(names) == 1:
        print('\nAdieu, adieu, to ' + names[0])
    else:
        name_list = p.join((names[:]))
        print('\nAdieu, adieu, to ' + name_list)
    