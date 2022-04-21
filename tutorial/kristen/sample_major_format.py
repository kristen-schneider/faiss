def transpose_data(genotypes):
    smf = []
    num_samples = len(genotypes[0])
    s = 0

    for v in range(len(genotypes)):
        while s < num_samples:
            try:
                smf[s].append(genotypes[v][s])
            except IndexError:
                smf.append([genotypes[v][s]])
            s += 1
        s = 0

    return smf
