d=['A','T','G','C','A']
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
complementary_strand = [complement[base] for base in d]
print(complementary_strand)