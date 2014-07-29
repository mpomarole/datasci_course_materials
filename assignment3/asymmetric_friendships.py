import MapReduce
import sys

"""
Part 4: Asymetric Friend
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(''.join(sorted(personA+personB)), record)

def reducer(key, list_of_values):
    if len(list_of_values) < 2:
      mr.emit((list_of_values[0][0], list_of_values[0][1]))
      mr.emit((list_of_values[0][1], list_of_values[0][0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
