count = 15
seq1 = 0
seq2 = 1
print(seq1, seq2, end="")
while count != 0:
  out = seq1 + seq2
  print(" " + str(out), end="")
  seq1, seq2 = (seq2, out)
  count -= 1