
def isLowerCaseL(letter):
    """Checks if a letter is actually lowercase. 
    
    Parameters
    ----------
    letter : char
        The character that is being checked. 
    
    Returns
    -------
    answer : boolean
        Depends if the character is or is not a lowercase letter. 
    """
    #The letter variables are used to catch out of bounds characters
    letter_a = ord('a')
    letter_b = ord('z')
    conv = ord(letter)
    if(letter_a <= conv and conv <= letter_b):
        return True
    else:
        return False

def isLowerCaseS(string):
    """Checks if a string is actually lowercase. 
    
    Parameters
    ----------
    string : String
        The string that is being checked. 
    
    Returns
    -------
    answer : boolean
        Depends if the string is or is not a lowercase letter. 
    """
    #These if statements allow for us to weed out weirder cases 
    #like Null and empty
    if(string == None):
        return False
    if(len(string) == 0):
        return True
    i = 0
    #This loop checks each individual char in the string
    while(i < len(string)):
        ind = string[i]
        if(isLowerCaseL(ind) == False):
            return False
        i += 1
    return True

def basicEncode(pl_text, s_key):
    """Encodes a letter by the key provided basically shifting it 
    by its ascii value through the alpabet. 
    
    Parameters
    ----------
    pl_text : char
        The character that is being encrypted. 
    s_key : char
        The character that we are encrypting by.
    
    Returns
    -------
    answer : pl_text
        The hopefully new encrypted character if the input met our requirements. 
    """
    min_let = ord('a')
    max_let = ord('z')
    tmp = 0
    int_key = ord(s_key) - 1
    
    #Shift represents how much the cipher will effect the plaintext
    shift = max_let - int_key
    #PlaceHolder is used as a middle piece for the overall cipher
    place_holder = ord(pl_text) - shift
    
    #If statement that checks if the input is valid. Then it acts
    #accordingly by either printing the original input or applying
    #the shift key provided
    if(isLowerCaseS(pl_text) == True and isLowerCaseL(s_key) == True):
        if(place_holder < min_let):
            place_holder += 1
            tmp = max_let - (min_let - place_holder)
            pl_text = chr(tmp)
        else:
            tmp = ord(pl_text) - shift
            pl_text = chr(tmp)
    else:
        return pl_text
    return pl_text

def basicDecode(pl_text, s_key):
    """Deodes a letter by the key provided basically shifting it 
    by its ascii value through the alpabet. 
    
    Parameters
    ----------
    pl_text : char
        The character that is being decrypted. 
    s_key : char
        The character that we are decrypting by.
    
    Returns
    -------
    answer : pl_text
        The hopefully new decrypted character if the input met our requirements. 
    """
    min_let = ord('a')
    max_let = ord('z')
    tmp = 0
    int_key = ord(s_key) - 1
    shift = max_let - int_key
    place_holder = ord(pl_text) + shift
    
    #If statement that checks that the input is valid then
    #acts accordingly
    if(isLowerCaseS(pl_text) == True and isLowerCaseL(s_key) == True):
        if(place_holder > max_let):
            place_holder -= 1
            tmp = min_let + (place_holder - max_let)
            pl_text = chr(tmp)
        else:
            tmp = ord(pl_text) + shift
            pl_text = chr(tmp)
    else:
        return pl_text
    return pl_text

def coolEncode(pl_text, s_key):
    """Encodes a string by the key provided basically shifting it 
    by its ascii value through the alpabet. This is accomplished 
    by using a while loop to individually shift each character in 
    the string by its individual key character.
    
    Parameters
    ----------
    pl_text : String
        The string that is being encrypted. 
    s_key : String
        The string that we are encrypting by.
    
    Returns
    -------
    answer : pl_text
        The hopefully new encrypted string if the input met our requirements. 
    """
    i = 0
    repeat = 0
    ans = ""
    
    #If statements meant to catch invalid inputs
    if(len(s_key) == 0):
        return None
    if(isLowerCaseS(pl_text) == False or isLowerCaseS(s_key) == False):
        return None
   
    #While loop that applies the basic shift individually to each
    #character in the String 
    while(i < len(pl_text)):
        #pl(plaintext) Used to help check individual characters of String
        #k(key) Used to check and implement the key on ciphers
        pl = pl_text[i]
        k = s_key[repeat]
        result = basicEncode(pl, k)
        tmp = str(result)
        ans += tmp
        i = i + 1
        repeat = repeat + 1
        if(repeat == len(s_key)):
            repeat = 0
            
    return ans
    
def coolDecode(pl_text, s_key):
    """Decodes a string by the key provided basically shifting it 
    by its ascii value through the alpabet. This is accomplished 
    by using a while loop to individually shift each character in 
    the string by its individual key character.
    
    Parameters
    ----------
    pl_text : String
        The string that is being decrypted. 
    s_key : String
        The string that we are decrypting by.
    
    Returns
    -------
    answer : pl_text
        The hopefully new decrypted string if the input met our requirements. 
    """
    i = 0
    repeat = 0
    ans = ""
    if(len(s_key) == 0):
        return None
    if(isLowerCaseS(pl_text) == False or isLowerCaseS(s_key) == False):
        return None 
    
    while(i < len(pl_text)):
        #pl(plaintext) Used to help check individual characters of String
        #k(key) Used to check and implement the key on ciphers
        ct = pl_text[i]
        k = s_key[repeat]
        result = basicDecode(ct, k)
        tmp = str(result)
        ans = ans + tmp
        i = i + 1
        repeat = repeat + 1
        if(repeat == len(s_key)):
            repeat = 0
    return ans
    
    