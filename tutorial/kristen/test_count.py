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
