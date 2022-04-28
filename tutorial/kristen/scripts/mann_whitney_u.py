import scipy.stats as stats
import numpy as np

def mann_whitney_u_test(group1, group2):
    '''
    H0: The mpg is equal between the two groups
    HA: The mpg is not equal between the two groups

    If the p-value is less than 0.05, we reject the null hypothesis.
    Meaning, the true mean mpg is significantly different between the two groups.
    '''

    mwu = stats.mannwhitneyu(group1, group2, alternative='two-sided')
    return [mwu[0], mwu[1]]

def mann_whitney_u_one_query(query, population):
    p_values = []
    for p in population:
        mwu_p = mann_whitney_u_test(query, p)
        p_values.append(mwu_p[1])

    return p_values

def mann_whitney_u_all_queries(queries, population):
    all_p_values = []
    for q in queries:
        p_value_q = mann_whitney_u_one_query(q, population)
        p_value_sorted_indices = np.argsort(p_value_q)
        all_p_values.append(np.flip(p_value_sorted_indices))
    return all_p_values
