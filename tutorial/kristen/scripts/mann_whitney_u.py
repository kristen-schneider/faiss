import scipy.stats as stats

def mann_whitney_u_test(group1, group2):
    '''
    H0: The mpg is equal between the two groups
    HA: The mpg is not equal between the two groups

    If the p-value is less than 0.05, we reject the null hypothesis.
    Meaning, the true mean mpg is significantly different between the two groups.
    '''
    mwu = stats.mannwhitneyu(group1, group2, alternative='two-sided')
    return [mwu[0], mwu[1]]


