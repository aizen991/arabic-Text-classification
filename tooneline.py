import os
count =0
filenames = next(os.walk("dataset/low"), (None, None, []))[2]
for x in filenames:	
    print(x)
    classfolder = 'dataset/low/{path}'.format(path=x)
    f = open(classfolder, 'r')
    lines = f.readlines()
    mystr = '\t'.join([line.strip() for line in lines])	
    f= open(classfolder,'w')
    mystr = mystr.replace('\t','')	
    f.write(mystr)
   