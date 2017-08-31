import pandas

def vendorCounts(data):
    counts = {}
    for manufacturer in data["Manufacturer"]:
        manufacturerList= str(manufacturer).split(sep="/")
        manufacturerList = map(str.strip, manufacturerList)
        for item in manufacturerList:
                if item in counts:
                    counts[item] += 1
                else:
                    counts[item] = 1
    outputFile = open('vendorCounts.csv', 'a')
    outputFile.write("name,count")
    for (key, value) in sorted(counts.items(),key=lambda item: (item[1], item[0]), reverse=True):
        outputFile.write("\n"+str(key)+","+str(value))

def countryCounts(data):
    print("***Finding Country Counts***")
    counts = {}
    for country in data["Country"]:
        if country in counts:
            counts[country] += 1
        else:
            counts[country] = 1
    outputFile = open('countryCounts.csv', 'a')
    outputFile.write("name,count")
    for (key, value) in sorted(counts.items(),key=lambda item: (item[1], item[0]), reverse=True):
        outputFile.write("\n"+str(key)+","+str(value))

def regionCounts(data):
    print("***Finding Region Counts***")
    counts = {}
    for region in data["Region"]:
        if region in counts:
            counts[region] += 1
        else:
            counts[region] = 1
    outputFile = open('regionCounts.csv', 'a')
    outputFile.write("name,count")
    for (key, value) in sorted(counts.items(),key=lambda item: (item[1], item[0]), reverse=True):
        outputFile.write("\n"+str(key)+","+str(value))

def segmentCounts(data):
    print("***Finding Segment Counts***")
    counts = {}
    for segment in data["Segment"]:
        if segment in counts:
            counts[segment] += 1
        else:
            counts[segment] = 1
    outputFile = open('segmentCounts.csv', 'a')
    outputFile.write("name,count")
    for (key, value) in sorted(counts.items(),key=lambda item: (item[1], item[0]), reverse=True):
        outputFile.write("\n"+str(key)+","+str(value))

def OSCounts(data):
    print("***Finding OS Counts***")
    counts = {}
    for OS in data["OS"]:
        if OS in counts:
            counts[OS] += 1
        else:
            counts[OS] = 1
    outputFile = open('OSCounts.csv', 'a')
    outputFile.write("name,count")
    for (key, value) in sorted(counts.items(),key=lambda item: (item[1], item[0]), reverse=True):
        outputFile.write("\n"+str(key)+","+str(value))

def main():
    data = pandas.read_csv("top500.csv", encoding="ISO-8859-1")
    vendorCounts(data)
    countryCounts(data)
    regionCounts(data)
    segmentCounts(data)
    OSCounts(data)
    print("Done.")

main()


