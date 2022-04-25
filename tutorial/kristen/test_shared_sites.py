def all_matches(all_queries, all_matches, smf):
    for q in range(len(all_queries)):
        q_query = all_queries[q]
        q_matches = all_matches[q]
        for m in range(len(q_matches)):
            m_sample = smf[q_matches[m]]
            p_ss = percent_shared_sites(q_query, m_sample)

            print(p_ss)

def percent_shared_sites(query, match):
    num_shared_sites = count_shared_sites(query, match)
    num_sites = len(query)
    return num_shared_sites/num_sites

def count_shared_sites(query, match):
    shared_sites = 0
    for s in range(len(query)):
        if query[s] == match[s]:
            shared_sites += 1

    return shared_sites

def all_shared_sites(queries, full_database):
    accuracy_list = []

    for query_i in range(len(queries)):
        curr_query = queries[query_i]
        for sample_i in range(len(full_database)):
            curr_sample = full_database[sample_i]
            p_ss = percent_shared_sites(curr_query, curr_sample)
            try: accuracy_list[query_i].append(p_ss)
            except IndexError: accuracy_list.append([p_ss])
    return accuracy_list
