import numpy as np

def count_shared_sites(query, match):
    '''
    counts number of shared sites between a match and a query
    '''
    shared_sites = 0
    for s in range(len(query)):
        if query[s] == match[s]:
            shared_sites += 1

    return shared_sites

def percent_shared_sites(query, match):
    '''
    converts number of shared sites to a percentage
    '''
    num_shared_sites = count_shared_sites(query, match)
    num_sites = len(query)
    return (num_shared_sites/num_sites)

def all_sample_shared_sites(queries, all_samples):
    '''
    returns a list of lists, one list for each query
    one list is the percent matches for all samples in database
    '''
    shared_sites_all_samples = []

    for query_i in range(len(queries)):
        curr_query = queries[query_i]
        for sample_i in range(len(all_samples)):
            curr_sample = all_samples[sample_i]
            p_ss = percent_shared_sites(curr_query, curr_sample)
            try:
                shared_sites_all_samples[query_i].append(p_ss)
            except IndexError:
                shared_sites_all_samples.append([p_ss])
    return shared_sites_all_samples

def sort_shared_sites_percentages(shared_sites_all_samples):
    '''
    sorts list of accuracy percentages and returns the indexes of the ordered list
    '''
    ordered_indices = []
    for s in shared_sites_all_samples:
        index_ordered = np.argsort(s)
        ordered_indices.append(np.flip(index_ordered))
    return ordered_indices

# def all_faiss_matches(all_queries, all_matches, smf):
#     '''
#     returns a list of lists, one list for each query
#     one list is the percent matches for all index matches
#     '''
#
#     pss_ss_index = []
#
#     for q in range(len(all_queries)):
#         q_query = all_queries[q]
#         q_matches = all_matches[q]
#         for m in range(len(q_matches)):
#             m_sample = smf[q_matches[m]]
#             p_ss = percent_shared_sites(q_query, m_sample)
#             try:
#                 pss_ss_index[q].append(p_ss)
#             except IndexError:
#                 pss_ss_index.append([p_ss])
#     return pss_ss_index

# def ss_vs_bf(ss_indices, bf_indices, k):
#
#     for i in range(len(ss_indices)):
#         ss_k = ss_indices[i][:k]
#         bf_k = bf_indices[i][:k]
#         print(set(ss_k) == set(bf_k))
#
#
# def old_ss_vs_bf(ss_indices, bf_indices, k):
#     tf_list = []
#     for s in range(len(ss_indices)):
#         curr_ss = ss_indices[s]
#         curr_bf = bf_indices[s]
#         flag = True
#         for i in range(k):
#             if curr_ss[i] == curr_bf[i]:
#                 continue
#             else:
#                 flag = False
#                 break
#         tf_list.append(flag)
#     return tf_list