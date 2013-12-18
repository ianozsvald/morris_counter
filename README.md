morris_counter
==============

Probabilistic Morris Counter (counts 2^n using e.g. just a byte)

https://en.wikipedia.org/wiki/Approximate_counting_algorithm

Probabilistically updating counter, uses a tiny amount of RAM (1 byte by default in this implementation) to count to 2^2^bits (2^2^8 == 1e77)

The constructor will take other type codes (e.g. b'I' for 4 bytes on 64 bit systems). 

The counter uses `array.array` so it can hold a large set of counters, see second example below.

Usage:
-----

    import morris_counter
    mc = morris_counter.MorrisCounter()
    print mc.get()  # 1
    mc.add()
    print mc.get()  # 2
    mc.add()
    print mc.get()  # 4 or maybe still 2
    mc.add()
    print mc.get()  # 4 or maybe still 2 or maybe higher
    mc.add()
    print mc.get()  # 8 (or 2 or 4 or more)
    _ = [mc.add() for n in xrange(1000)]  # add another 1000
    print mc.get()  # 1024 (or more or less by a power of 2, but roughly 1024)

    mc = morris_counter.MorrisCounter()
    mc.add_counter()
    mc.add()  # add to 0th counter
    mc.add(1)  # add to 1st counter
    print mc.get(1)  # get from 1st counter

    _ = [mc.add(1) for n in xrange(100000)]  # add 100,000
    print mc.get(1)  # 65536 (or greater/lesser by powers of 2)


Tests:
-----

If you have `nose` installed then:

    $ nosetests
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.003s

    OK
    
