#%%
import re
import random
import time
import numpy as np
def turm_trainer(n_digits = 4):
    '''
    Copyright (C) SH
    '''
    num = "0"
    # for safety max while loop
    n_max = 10
    n = 0
    # in case there are zeros in number -> draw again
    while len(re.findall(pattern = "0", string = num)) > 0 and n <= n_max:
        num = str(random.randint(10 ** (n_digits - 1), 10 ** (n_digits) - 1))
        n = n + 1
    print("Calculate: {}".format(num))
    start = time.clock()
    input("Press <ENTER> for solution..")
    end = time.clock()
    print("--" * 40)
    tmp = int(num)
    print("\n{} * 2".format(tmp))
    for i in range(2, 10):
        tmp = tmp * i
        if i == 9:
            print("\n{} : 2".format(tmp))
        else:
            print("\n{} * {}".format(tmp, i + 1))
    tmp = tmp / 2
    for i in range(3, 10):
        print("\n{} : {}".format(int(tmp), i))
        tmp = tmp / i
    print("\n{}".format(int(tmp)))
    print("--" * 40)
    print("\nTime: {} sec ({} min)".format(np.round(end-start, 1), np.round((end-start)/60, 2)))
    return(True)