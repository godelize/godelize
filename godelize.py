"""
godelize.py
by James Graham
"""

from math import sqrt

def main():
    #Get user's input to godelize
    encodeInput = getInput()
    #This is the character length of the input
    inputLength = getInputLength(encodeInput)
    #These are the input characters converted to unicode
    unisymbols = convertUni(encodeInput)
    #This is a list of prime numbers from 2 through inputLength
    primeList = generatePrimeList(inputLength)
    #This is the input turned into a godel number
    godelNumber = createGodelNumber(primeList, unisymbols)
    #This is an array of the prime factorization of the godel number
    output = decodeGodel(godelNumber)
    #These are the number of each prime in the array
    symbols = getSymbols(output, primeList, inputLength)
    #This shows the original input by the user
    originalInput(symbols, encodeInput, godelNumber, output)
    
def getInput():
    """
    This get the input from the user to godelize

    Parameters:
    No arguments

    Returns:
    The entered input from the user

    """
    print("Enter something to encode:")
    encodeInput = input()
    print("You entered:" + encodeInput)
    return encodeInput

def getInputLength(n):
    """
    This counts the number of characters to encode

    Parameters:
    encodeInput

    Returns:
    inputLenth

    """
    inputLength = len(n)
    print("Your input is " + str(inputLength) + " characters")
    return inputLength

def convertUni(n):
    """
    This converts the input characters to unicode

    Parameters:
    encodeInput

    Returns:
    unisymbols array

    """
    unisymbols = [ord(c) for c in n]
    print(unisymbols)
    return unisymbols

def generatePrimeList(ilength):
    """
    This generates list of beginngin primes through size of input

    Parameters:
    inputLength

    Returns:
    primeList

    """
    number = 1
    primeList = []
    while(number <= 100):
        count = 0
        i = 2

        while(i <= number // 2):
            if(number % i == 0):
                count = count + 1
                break
            i = i + 1

        if(count == 0 and number != 1):
            primeList.append(number)
        number = number + 1
        print(primeList)
    return primeList

def createGodelNumber(p,u):
    """
    This zips one array of primes with the unicode
    characters. It raises each prime to the power of
    the unicode character and multiplies the resulting
    number with the next, creating the godel number
    for the input.

    Parameters:
    primeList, uniSymbols

    Returns:
    godelNumber

    """
    godelEach = [a**b for a,b in zip(p,u)]
    godelNumber = 1
    for i in godelEach:
        godelNumber = godelNumber * i
        print("godelNumber:", godelNumber)
    return godelNumber

def decodeGodel(n):
    """
    This performs the prime factorization of
    the godelNumber. Then creates an array of
    the primes that make up that number

    Parameters:
    godelNumber

    Returns:
    output

    """
    output = []
    d = 2
    while d*d <= n:
        while(n % d) == 0:
            output.append(d)
            print(output)
            n //= d
        d +=1
    if n > 1:
        output.append(n)
    return output

def getSymbols(o,p,ilength):
    """
    This counts the number of primes from
    output and determines which unicode matches

    Parameters:
    output, primeList, inputLength

    Returns:
    symbols

    """
    symbols = []
    for j in range(ilength):
        count = o.count(p[j])
        symbols.append(count)
    symbols = symbols[-ilength:]
    return symbols

def originalInput(s,e,n,o):
    """
    This turns the symbols into input characters
    then creates a string showing the oringinal input

    Parameters:
    symbols, encodeInput, godelNumber, output

    Retruns:
    nothing

    """
    print(s)
    decodeInput = [chr(c) for c in s]
    origInput = ''.join(decodeInput)
    print("You entered: " + e)
    print("The godel number for this is; " + str(n))
    print("The prime factorization of this is: " + str(o))
    print("The unicode symbols are: " + str(s))
    print("Your decodeed input is: " + origInput)
    
main()
