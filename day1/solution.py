    import numpy as np
    
    input_ = np.loadtxt('input')
    
    # part 1
    np.sum(input_[1:] > input_[:-1])
    
    # part 2 - more clever version figured out in writing the Haskell version
    np.sum(input_[3:] > input_[:-3])
    
    # part 2 - less clever
    input_sum3 = input_[2:] + input_[1:-1] + input_[:-2]
    np.sum(input_sum3[1:] > input_sum3[:-1])
