from appcode import leon_module

def test_testisprime():
    assert leon_module.testisprime(7) == True
    assert leon_module.testisprime(13) == True
    assert leon_module.testisprime(3) == True
    assert leon_module.testisprime(2) == False
    assert leon_module.testisprime(1) == False
    assert leon_module.testisprime(15) == False

 

def test_reverseastring():
    assert leon_module.reverseastring('cat') == 'tac'
    assert leon_module.reverseastring('racecar')  == 'racecar'
    assert leon_module.reverseastring('spoon')  != 'cheese'

#def test_sqlselect():
#    for test in leon_module.sqlquery('SELECT company_no FROM company WHERE company_no = 1000'):
#        assert test == '(1000,)'
    

def test_maxthreennumbers():
    assert leon_module.maxthreenumbers(1,2,3) == 3
    assert leon_module.maxthreenumbers(3,2,1) == 3
    assert leon_module.maxthreenumbers(2,3,1) == 3
    assert leon_module.maxthreenumbers(2,1,3) == 3