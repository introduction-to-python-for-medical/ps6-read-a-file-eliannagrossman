!mkdir data # Create a folder for the data in the colab
!wget https://raw.githubusercontent.com/yotam-biu/ps6/main/data/codons.txt -O /content/data/codons.txt
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


