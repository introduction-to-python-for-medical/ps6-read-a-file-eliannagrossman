
def create_codon_dict(file_path):
  path = "/content/data/codons.txt"
  file = open(path)
  rows = file.readlines()
  file.close()
  lala={}
  for row in rows:
    row=row.strip().split('\t')
    codon,amino=row[0],row[2]
    lala[codon]=amino
  return lala 


