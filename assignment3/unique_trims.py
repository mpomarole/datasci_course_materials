import MapReduce
import sys

"""
Part 5: Unique trims
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #sequence_id = record[0]
    nucle = record[1]
    listnucle = list(nucle)
    del listnucle[-10:]
    mr.emit_intermediate(''.join(listnucle), [])

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
