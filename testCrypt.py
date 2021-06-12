import cryptMethods as cry
def test_myProject():
    assert cry.coolEncode("josedeleon", "cogs") == "lcywfsrwqb"
    assert cry.coolDecode("lcywfsrwqb", "cogs") == "josedeleon"
    assert cry.isLowerCaseS("") == True
    assert cry.isLowerCaseL("A") == False
    assert cry.isLowerCaseS("hello") == True
