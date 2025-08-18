import random

# target size in MB
target_size_mb = 3.5
target_size = int(target_size_mb * 1024 * 1024)  

# only genome characters
bases = ['A', 'C', 'G', 'T']

# generate sequence
genome_sequence = ''.join(random.choices(bases, k=target_size))

# save to text file
with open("human.txt", "w") as f:
    f.write(genome_sequence)

print("Genome sequence file created: genome_sequence.txt (~3.5 MB)")
