def all_genotypes(vcf_file): 
    data = get_data(vcf_file)
    genotypes = get_genotypes(data)
    return genotypes
    
def get_data(vcf_file):
    o_vcf = open(vcf_file, 'r')
    
    header = []
    data = []

    for line in o_vcf:
        if line[0] == '#':
            header.append(line)
        else:
            data.append(line)

    return data
       
def get_genotypes(data):
    genotypes = []
    for v in data:
        v_list = v.split()
        v_genotypes = v_list[9:]
        v_floats = encode_floats(v_genotypes)
        genotypes.append(v_floats)

    return genotypes

def encode_floats(variant_list):
    float_variants = []

    for s in variant_list:
        if s == '0|0': float_variants.append(0)
        elif s == '0|1' or s == '1|0': float_variants.append(1)
        elif s == '1|1': float_variants.append(2)
        elif s == '.|.': float_variants.append(3)
        elif s == '0|2' or s == '2|0': float_variants.append(4)
        elif s == '0|3' or s == '3|0': float_variants.append(5)
        else: float_variants.append(6)

    return float_variants
