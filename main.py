letterValue ={
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

letterType10 =['I','X','C','M']
letterType5 =['V','L','D']




def roman_to_decimal(romannum : str):
    romannum.capitalize()

    if haveRomanCharacters(romannum)==False:
        raise Exception("The characters doesn't belong to roman number characters") 
    index =0
    decimalnum=0
    while True:
        #if index = len-1 simplemente sumar
        if compareRoman(romannum[index],romannum[index+1])== 1:#mayor
            decimalnum+=letterValue[romannum[index]]
            index+=1

        elif compareRoman(romannum[index],romannum[index+1])== -1:#menor
            if romannum[index] in letterType5:
                raise Exception("Characters of type 5 cannot substract")

            if canSubstract(romannum[index],romannum[index+1])== False:
                raise Exception("This substraction is prohibited")

            if compareRoman(romannum[index],romannum[index+2]) == -1:
                raise Exception("Substraction after two bigger characters")

            if romannum[index] == romannum[index-1]:
                raise Exception("two same characters substracting")

            if romannum[index] == romannum[index+2]:
                raise Exception("Adding and substracting the same number")

            decimalnum= decimalnum - letterValue[romannum[index]] + letterValue[romannum[index+1]]
            index+=2

        else:#igual

            decimalnum+=(letterValue[romannum[index]]*2)
            index+=2  
            if romannum[index] in letterType5:
                    raise Exception("Two repeated characters of type 5")

            if romannum[index] == romannum[index+2]:

                decimalnum+=letterValue[romannum[index]]
                index+=1

                if romannum[index] == romannum[index+3]:
                    raise Exception("More than 3 repeated characters in a row")
        
        if index==len(romannum):
            return decimalnum
                


def  compareRoman(letter1, letter2):
    if letterValue[letter1]>letterValue[letter2]:
        return 1
    elif letterValue[letter1]<letterValue[letter2] :
        return -1
    else:
        return 0



def haveRomanCharacters(romannum :str):
    for character in romannum:
        if character not in ['I','V','X','L','C','D','M']:
            return False
    return True

def canSubstract(letter1, letter2):
    if letter2 in letterType5:
        return True

    if letter1=='I' and letter2=='X':
        return True
    elif letter1=='X' and letter2=='C':
        return True
    elif letter1=='C' and letter2=='M':
        return True
    else:
        return False