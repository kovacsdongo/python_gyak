import csv

def seged(source_data,slice_path, result_in):
    if not slice_path:
        print "empty"
        result_in.append(source_data)
    else:
        print "not empty"
        parts = slice_path.split(".")
        #print parts

        if parts[0] == "index":
            print "1", parts
            parts.remove(parts[0])
            print "2", parts
            for listElement in source_data:
                seged(listElement,'.'.join(parts),result_in)
        else:
            parts[0] == "key"
            parts.remove(parts[0])
            for k in source_data:
                seged(source_data[k], '.'.join(parts), result_in)

def _slice_data_structure(source_data, slice_path):
    result_dict = []
    seged(source_data, slice_path, result_dict)
    write_to_file (result_dict)
    return result_dict

def write_to_file(final_data):
    with open('index.csv', 'w') as f:
        reader = csv.reader(f)
        w = csv.writer(f,delimiter=',')
        w.writerow(final_data)

ach = _slice_data_structure([[[1,2,3],[3,2,1]], [[4,5,6],[1,2,3]], [[1,2,3],[1,2,3]]], 'index.index.index')
#ach = _slice_data_structure([[1,2], [3,4], [5,6]], 'index.index')
#ach = _slice_data_structure([[1,2], [3,4], [5,6]], 'index')
#ach  = _slice_data_structure([{'a':1, 'b':2, 'c':3}, {'d':4, 'e':5, 'f':6}], 'index.key')
#ach = _slice_data_structure({'a':[1,2], 'b':[3,4], 'c':[5,6]}, "key.index")

print ach