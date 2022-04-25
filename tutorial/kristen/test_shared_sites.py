def all_matches(all_queries, all_matches):
    for q in range(len(all_queries)):
        q_query = all_queries[q]
        q_matches = all_matches[q]
        for m in range(len(q_match)):
            p_ss = percent_shared_sites(q_query, q_matches[m])

def percent_shared_sites(query, match):
    num_shared_sites = count_shared_sites(query, match)
    num_sites = len(query)
    return num_shared_sites/num_sites

def count_shared_sites(query, match):
    shared_sites = 0
    for s in range(len(query)):
        if query[s] == match[s]
            shared_sites += 1

    return shared_sites
