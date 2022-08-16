''' 
All vanity plates must start with at least two letters
vanity plates may contain a maximum of 6 characters (letters or numbers) 
and a minimum of 2 characters.

Numbers cannot be used in the middle of a plate; 
they must come at the end. For example, AAA222 would be an acceptable
vanity plate; AAA22A would not be acceptable. 

The first number used cannot be a ‘0’.

No periods, spaces, or punctuation marks are allowed.
'''

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    is_valid = False

    #check for valid length
    if 2 <= len(s) <= 6:
        #check for special characters and punctuation
        if s.isalnum():
            #check it starts with two letters
            if s[0:2].isalpha():
                #if only 2 letters than valid
                if len(s) == 2:
                    is_valid = True
                else:
                    #check if all letters
                    if s.isalpha():
                        is_valid = True
                    else:
                        is_valid = check_chars(s)

    return is_valid

def check_chars(p):
    valid_chars = True
    
    #if entire string is letters continue
    if p.isalpha():
        pass
    else:
        num_in_str = False
        pos = 2
        #check that the first number is not 0 and find position of 
        for char in p[2:]:
            if char.isdigit():
                if char == '0' and not num_in_str:
                    valid_chars = False
                    break
                else:
                    num_in_str = True
                    break
            else:
                pos += 1          
        #check that numbers are only at the end
        if not p[pos:].isdigit():
            valid_chars = False
    
    return (valid_chars)   

main()