
    import numpy as np


    # Read Input
    
    nbits = None # number of bits per record from input
    input_ = [] # each record be array of little endian bit values
    
    with open('input', 'r') as f:
      for line in f:
        lbs = line.strip()[::-1] # little endian bit string
        if nbits is None:
          nbits = len(lbs)
        else:
          assert nbits == len(lbs), 'different number of bits from input!'
        input_.append( np.array(list(lbs), dtype= int) )


    # Part 1
    
    # little endian bit occ cnt, 0 cnts for -1
    lebc = np.sum( np.vstack(input_) * 2 - 1, axis= 0)
    
    assert np.all(lebc != 0), 'equal number of 0s and 1s from input!'
    
    gamma_bits = lebc > 0
    gamma = np.sum(gamma_bits * 2 ** np.arange(nbits))
    
    epsilon_bits = lebc < 0
    epsilon = np.sum(epsilon_bits * 2 ** np.arange(nbits))
    
    # answer
    gamma * epsilon


    # Part 2
    
    def filter_out(input_, dig, crit):
      oc = 0
      for ba in input_:
        bv = ba[dig]
        oc += bv + bv - 1
      ev = crit(oc)
      return [ba for ba in input_ if ba[dig] == ev]
    
    def search_rating(crit):
      left = input_
      dig = nbits 
      while left:
        if len(left) == 1:
          return np.sum( left[0] * 2 ** np.arange(nbits) )
        assert dig > 0, 'run out of digits!'
        dig -= 1
        left = filter_out(left, dig, crit)
      assert False, 'no number left!'
    
    oxygen_rate = search_rating( lambda oc: oc >= 0 and 1 or 0 )
    CO2_rate = search_rating( lambda oc: oc < 0 and 1 or 0 )
    
    # answer
    oxygen_rate * CO2_rate
    
