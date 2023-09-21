filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentation.txt']

for name in filenames:
    name = name.replace('.','-',1)
    print(name)