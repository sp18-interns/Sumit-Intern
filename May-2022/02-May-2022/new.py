five = 10 * 10 - 2 + 3 - 6
print ("This should be five: %s" % five)


def swap_case(s):
    return
def swap_case(s):

    # sWAP cASE in Python - HackerRank Solution START
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;
    # sWAP cASE in Python - HackerRank Solution END

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result