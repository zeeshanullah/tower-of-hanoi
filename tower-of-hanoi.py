def tower_of_hanoi(n,A,C):
    assert 0<A<=3 and 0<C<=3 and A!=C
    B=2
    if n==1:
        print ("move the top disk from A to C")
    elif n==0:
        return None
    elif n==2:
        print ("move the top disk from A to B")
        print ("move the top disk from A to C")
        print ("move the top disk from B to C")
    else:
        print ("move the top disk from A to B")
        print ("move the top disk from A to C")
        print ("movethe top disk from B to C")
        return tower_of_hanoi(n-1,A,C)
