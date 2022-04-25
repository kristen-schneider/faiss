import read_vcf
import sample_major_format
import similarity_search
import test_shared_sites
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

    # make (transform) genotype data the input data to similarity search
    print('\nConducting similarity search on transposed genotypes...')
    match_indices = similarity_search.similarity_search(smf, queries)

    # test accuracy
    print('\nComputing number of shared sites between query and proposed matches...')
    test_shared_sites.all_matches(queries, match_indices, smf)

    print('\nFull shared sites...')
    accuracy_list = test_shared_sites.all_shared_sites(queries, smf)
    for l in accuracy_list:
        print('STARTING OVER')
        max_value = max(l)
        for v in range(len(l)):
            if l[v] == max_value: print(v)
    print('end')


    # similarity search

if __name__ == '__main__':
    main()
