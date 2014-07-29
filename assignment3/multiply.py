import MapReduce
import sys

"""
Part 6: Matrix
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    if matrix == 'a':
      for k in range(0, 5):
        mr.emit_intermediate((i, k), record)
    else:
      for k in range(0, 5):
        mr.emit_intermediate((k, j), record)

def reducer(key, list_of_values):
    a_s = []
    b_s = []
    for l in list_of_values:
      if l[0] == 'a':
        a_s.append(l)
      else:
        b_s.append(l)
    total = 0
    for j in range(0, 5):
      ae = 0
      be = 0
      for a in a_s:
        if a[2] == j:
          ae = a[3]
      for b in b_s:
        if b[1] == j:
          be = b[3]
      total += ae * be
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
