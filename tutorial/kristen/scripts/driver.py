import read_vcf
import sample_major_format
import similarity_search
import shared_sites
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
    queries = [[0] * d, [1] * d]
    # for q in range(num_queries-1):
    #     queries.append(np.random.randint(0, high=4, size=d, dtype=int))

    k = 25     # number of nearest neighbors to report

    # make (transform) genotype data the input data to similarity search
    print('\nConducting similarity search on transposed genotypes...')
    match_indices_flatL2 = similarity_search.flatL2(smf, queries, k)
    print(match_indices_flatL2)
    # match_indices_inner_product = similarity_search.inner_product(smf, queries, k)
    # print(match_indices_inner_product)


    # test accuracy
    print('\nComputing number of shared sites between query and proposed matches...')
    percent_similar = shared_sites.all_indexed_matches(queries, match_indices_flatL2, smf)


    print('\nComparing FAISS to brute force...')
    bf_similarities = shared_sites.all_database(queries, smf)
    bf_indices = shared_sites.accuracy_indices(bf_similarities)
    print('indices:\n', bf_indices)
    # print('percent similiar:\n', percent_similar)
    x = shared_sites.ss_vs_bf(match_indices_flatL2, bf_indices, k)


    print('\nEnd.')


    # similarity search

if __name__ == '__main__':
    main()
