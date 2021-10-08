import os
import re
count =0
filenames = next(os.walk("dataset/law"), (None, None, []))[2]
for x in filenames:	
    print(x)
    classfolder = 'dataset/law/{path}'.format(path=x)
    f = open(classfolder, 'r')
    lines = f.readlines()
    mystr = '\t'.join([line.strip() for line in lines])	
    f= open(classfolder,'w')
    mystr = re.sub('\W+',' ', mystr)
    mystr = mystr.replace('\t','')
    mystr= re.sub(r'\s*[A-Za-z]+\b', '' , mystr)
    mystr = mystr.rstrip()	
    f.write(mystr)
    
   