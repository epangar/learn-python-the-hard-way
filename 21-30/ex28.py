print " 1: %r" % (True and True)  #True, because both are True
print " 2: %r" % (False and True) #False, because not all of them are True
print " 3: %r" % (1 == 1 and 2 == 1) #False, because not all of them are True
print " 4: %r" % ("test" == "test") #True, because both are True
print " 5: %r" % (1 == 1 or 2 != 1) #True, because at least one is True
print " 6: %r" % (True and 1 == 1) #True, because both are True
print " 7: %r" % (False and 0 != 0) #False, because not all of them are True
print " 8: %r" % (True or 1 == 1) #True, because at least one is True
print " 9: %r" % ("test" == "testing") #False
print "10: %r" % (1 != 0 and 2 == 1) #False, because not all of them are True
print "11: %r" % ("test" != "testing") #True
print "12: %r" % ("test" == 1) #False
print "13: %r" % (not (True and False)) #True, because it's !False (not all of them are true)
print "14: %r" % (not (1 == 1 and 0 != 1)) #False
print "15: %r" % (not (10 == 1 or 1000 == 1000)) #False, because it's !True (at least one is true) 
print "16: %r" % (not (1 != 10 or 3 == 4)) #False, because it's !True (at least one is true) 
print "17: %r" % (not ("testing" == "testing" and "Zed" == "Cool Guy")) #True
print "18: %r" % (1 == 1 and not ("testing" == 1 or 1 == 0)) #True
print "19: %r" % ("chunky" == "bacon" and not (3 == 4 or 3 == 3)) #False
print "20: %r" % (3 == 3 and not ("testing" == "testing" or "Python" == "Fun")) #False