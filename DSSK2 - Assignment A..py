def bs_func(data,func,size):
    n = len(data)
    bs_reps = np.empty(size)
    for i in range(size):
        bs_reps[i] = func(np.random.choice(data, size=n))
        return bs_reps

#-- This is the bootstrap resampling function, which takes three arguments.
#-- By iterating over an empty numpy array we can store each sample which has a function, func, applied to it.
    

if __name__ == '__main__':   #-- The main guard allows us to use the bs_func again without any baggage
    import pandas as pd
    import numpy as np
    df = pd.read_csv("gandhi_et_al_bouts.csv",skiprows = 4) #--import csv using pandas
    numpy_array = np.array(df)  #--converting to a numpy array allows easy use of simple indexing
    bout_length_wt = [value[1] for value in numpy_array if value[0] == 'wt'] #-- getting a list of the bout lengths of wild type fish
    bout_length_mut = [value[1] for value in numpy_array if value[0] == 'mut']
    mean_wt = np.mean(bout_length_wt) #-- Taking the mean before we resample
    mean_mut = np.mean(bout_length_mut)
    bs_reps_mut = bs_func(bout_length_mut,np.mean,10000) #--using the bs_func function to draw bootstrap replicates
    bs_reps_wt = bs_func(bout_length_wt,np.mean,10000)
    conf_int_wt = np.percentile(bs_reps_wt,[2.5,97.5]) #--create confidence intervals
    conf_int_mut = np.percentile(bs_reps_mut,[2.5,97.5])
    print('The confidence intervals are ',conf_int_wt,' and ',conf_int_mut,' for wild and mutant type respectively')
    print('The means of the initial data: wt = ',mean_wt,', mut = ',mean_mut)
    print('The means of the resampled data: wt = ',bs_reps_wt,', mut = ',bs_reps_mut)
    
