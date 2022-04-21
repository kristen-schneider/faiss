import read_vcf
import sample_major_format
import similarity_search
import sys

vcf_file = sys.argv[1]


def main():

    # read vcf file
    print('Reading VCF file...\n')
    genotypes = read_vcf.all_genotypes(vcf_file)
    print('...number of variants: ', len(genotypes))
    print('...number of samples: ', len(genotypes[0]))

    # transform / enconde vcf genotype data
    print('\nTransposing genotype data to Sample Major Format (SMF)...')
    smf = sample_major_format.transpose_data(genotypes)

    # make (transform) genotype data the input data to similarity search
    print('\nConducting similarity search on tranposed genotypes...')
    similarity_search.similarity_search(smf)

    # similarity search

if __name__ == '__main__':
    main()
