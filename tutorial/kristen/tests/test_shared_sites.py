import numpy as np

def all_matches(all_queries, all_matches, smf):
    '''
    returns a list of lists, one list for each query
    one list is the percent matches for all index matches
    '''
    for q in range(len(all_queries)):
        q_query = all_queries[q]
        q_matches = all_matches[q]
        for m in range(len(q_matches)):
            m_sample = smf[q_matches[m]]
            p_ss = percent_shared_sites(q_query, m_sample)

            #print(p_ss)

def percent_shared_sites(query, match):
    '''
    converts number of shared sites to a percentage
    '''
    num_shared_sites = count_shared_sites(query, match)
    num_sites = len(query)
    return 1-(num_shared_sites/num_sites)

def count_shared_sites(query, match):
    '''
    counts number of shared sites between a match and a query
    '''
    shared_sites = 0
    for s in range(len(query)):
        if query[s] == match[s]:
            shared_sites += 1

    return shared_sites

def all_shared_sites(queries, full_database):
    '''
    returns a list of lists, one list for each query
    one list is the percent matches for all samples in database
    '''
    accuracy_list = []

    for query_i in range(len(queries)):
        curr_query = queries[query_i]
        for sample_i in range(len(full_database)):
            curr_sample = full_database[sample_i]
            p_ss = percent_shared_sites(curr_query, curr_sample)
            try: accuracy_list[query_i].append(p_ss)
            except IndexError: accuracy_list.append([p_ss])
    return accuracy_list

def accuracy_indices(accuracty_list):
    '''
    sorts list of accuracy percentages and returns the indexes of the ordered list
    '''
    ordered_indices = []
    for l in accuracty_list:
        index_ordered = np.argsort(l)
        ordered_indices.append(index_ordered)
    return ordered_indices

def ss_vs_bf(ss_indices, bf_indices, k):
    print('SS')
    for ss in ss_indices:
        print(ss[:k])

    print('BF')
    for bf in bf_indices:
        print(bf[:k])
