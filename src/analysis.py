import scipy.stats as stats
import numpy as np

def identify_n_p_variable(df, column):
    x=df.groupby(column).agg({'TERMINATIONID':lambda x:x.mean()-60, column:lambda x:x.value_counts()})
    x=x.rename(columns={column:'count'})
    x=x.reset_index()
    return_list=[]
    for index, row in x.iterrows():
        n=row['count']
        p=row['TERMINATIONID']
        variable=row[column]
        return_list.append([n,p,variable])
    return return_list 
        

def find_confidence_intervals_binomial(n,p,variable):
    binomial = stats.binom(n, p)
    binomial_mean = n*p
    binomial_var = n*p*(1-p)
    normal_approx = stats.norm(binomial_mean, np.sqrt(binomial_var))

    CI_low=(normal_approx.ppf(.0025))/n
    CI_high=(normal_approx.ppf(.975))/n

    print("Sample Mean for {} success: {:2.2}".format(variable, p))
    print("95% confidence interval for the population mean: [{:2.2}, {:2.2}]".format(
    CI_low, CI_high))
    