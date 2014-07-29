import MapReduce
import sys

"""
Part 3: Friend Count
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    personA = record[0]
    #personB = record[1]
    mr.emit_intermediate(personA, 1)

def reducer(key, list_of_values):
    total = 0
    for friend in list_of_values: 
      total += friend
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
