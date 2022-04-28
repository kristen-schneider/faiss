import read_vcf
import sample_major_format
import similarity_search
import shared_sites
import mann_whitney_u
import sys
import numpy as np

vcf_file = sys.argv[1]


def main():

    # read vcf file
    print('Reading VCF file...\n')
    genotypes = read_vcf.all_genotypes(vcf_file)
    print('...number of variants: ', len(genotypes))
    print('...number of samples: ', len(genotypes[0]))

    # transform / encode vcf genotype data
    print('\nTransposing genotype data to Sample Major Format (SMF)...')
    smf = sample_major_format.transpose_data(genotypes)

    # make queries
    d = len(smf[0])  # dimension
    num_queries = 4
    q_indices = [4, 728, 1786, 2311]
    queries = [smf[q_i] for q_i in q_indices]


    k = 25     # number of nearest neighbors to report

    # make (transform) genotype data the input data to similarity search
    print('\nConducting similarity search on transposed genotypes...')
    match_indices_flatL2 = similarity_search.flatL2(smf, queries, k)
    # print(match_indices_flatL2)
    # match_indices_inner_product = similarity_search.inner_product(smf, queries, k)
    # print(match_indices_inner_product)


    # shared sites
    print('\nComputing number of shared sites between query and proposed matches...')
    all_shared_sites = shared_sites.all_sample_shared_sites(queries, smf)
    indices_shared_sites = shared_sites.sort_shared_sites_percentages(all_shared_sites)

    # mann whitney u test
    print('\nComputing Man Whitney U Test for all queries...')
    sorted_p_value_indices = mann_whitney_u.mann_whitney_u_all_queries(queries, smf)
    for s in sorted_p_value_indices: print(s)

    print('\nEnd.')


    # similarity search

if __name__ == '__main__':
    main()
