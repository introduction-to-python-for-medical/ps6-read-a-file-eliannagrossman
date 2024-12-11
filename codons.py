
def create_codon_dict(file_path):
  path = "/content/data/codons.txt"
  file = open(path)
  rows = file.readlines()
  file.close()
  codon_dict={}
  for row in rows:
    row=row.strip().split('\t')
    if len(row)>=3:
      codon,amino=row[0],row[2]
      codon_dict[codon]=amino
  return codon_dict


