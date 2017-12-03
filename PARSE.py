import pprint
import csv
import os
import statistics


def three_average(path,headerID):
    averages= dict()
    for level in ["1","2","3"]:
        averages[level] = average(path + level +".txt",headerID)
        #pprint.pprint(averages)
        #print "Value : %s" % averages.get('2')
    with open('excell.csv', 'w') as f:
        w = csv.writer(f, delimiter=";")
        f.write("Value text2: %s" % averages.get('2'))
        f.write("\nValue text3: %s" % averages.get('3'))
        sum2 = averages.get('3')+averages.get('2')
        avg = sum2 /2
        f.write("\nAVG text2 and text3: %3d.2" % avg)
    return averages

def average(txtpath,headerID):
    with open(txtpath) as t:
        total=0
        summ=0
        txt_lines=t.readlines()
        headerline = txt_lines[0]
        headerline = headerline.split(",")
        headerindex = headerline.index(headerID)
        for row in txt_lines[1:]:
            columns= row.split(",")
            total += float(columns[headerindex])
            summ += 1
        avg = total / summ
        return avg

#print three_average("c:/work/hazik/gyak/PARSE/mappa/submappa_1/text_","ketto")

def folderID(path):
    dirs = os.listdir(path)
    print dirs
    for dir in dirs:
        id=dir
        txt_path = os.path.join(path, dir, "text_")
        #print txt_path
        value = three_average(txt_path,"ketto")
        my_dic = {id: value}
        pprint.pprint(my_dic)


result = folderID("c:/work/gyak/mappa/")    #subfolder print




