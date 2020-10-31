import sys

def parse_fasta(file_name):
    base_dic = {}
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            for s in line.strip():
                if s not in base_dic:
                    base_dic[s] = 1
                else:
                    base_dic[s] += 1
    return base_dic

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta]")
    sys.exit()

file_name = sys.argv[1]
base_dic = parse_fasta(file_name)
print(base_dic)
