from CSP_6_02_reading_files import toString, longestLine, toBinary

def test_toString():
    assert toString("myText.txt") != ""

def test_longestLine():
    assert longestLine("myText.txt") == "eojfipoqwkljnfhiu3o1ijklmjn3fbui"

def test_toBinary():
    assert toBinary("myBinary.txt") == ['01101001', '00101010', '1010']
