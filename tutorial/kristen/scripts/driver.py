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
    queries = np.asarray([[0] * d, [1] * d, [2] * d], dtype='float32')
    k = 80  # number of nearest neighbors to report

    # make (transform) genotype data the input data to similarity search
    print('\nConducting similarity search on transposed genotypes...')
    match_indices = similarity_search.similarity_search(smf, queries, k)


    # test accuracy
    print('\nComputing number of shared sites between query and proposed matches...')
    percent_similar = shared_sites.all_indexed_matches(queries, match_indices, smf)
    # print(percent_similar)

    print('\nComparing FAISS to brute force...')
    bf_similarities = shared_sites.all_database(queries, smf)
    bf_indices = shared_sites.accuracy_indices(bf_similarities)
    x = shared_sites.ss_vs_bf(match_indices, bf_indices, 80)
    print(x)


    print('\nEnd.')


    # similarity search

if __name__ == '__main__':
    main()
