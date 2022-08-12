def main():
    text = input('Input: ').strip()
    vowels = ['A','E','I','O','U']
    output = ''

    for i in text:
        if i.upper() in vowels:
            output = output + ''
        else:
            output = output + i
    print('Output: ' + output)

main()