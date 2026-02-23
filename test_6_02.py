from file_functions import toString, longestLine, toBinary

def test_toString():
    assert toString("myText.txt") != ""

def test_longestLine():
    assert longestLine("myText.txt") == "this line is the longest one in the file"

def test_toBinary():
    assert toBinary("myBinary.txt") == ['01101001', '00101010', '1010']
