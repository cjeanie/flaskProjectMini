
def evenOdd(sentence):
    number = len(sentence)
    if number%2==0:
        return "Your sentence has an even number of characters. It has " + str(number) + " characters"
    else:
        return "Your sentence has an odd number of characters. It has " + str(number) + " characters"