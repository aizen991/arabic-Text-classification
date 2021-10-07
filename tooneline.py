import os
count =0
filenames = next(os.walk("."), (None, None, []))[2]
for x in filenames:	
    print(x)
    f = open(x, 'r')
    lines = f.readlines()
    mystr = '\t'.join([line.strip() for line in lines])	
    f= open(x,'w')
    mystr = mystr.replace('\t','')	
    f.write(mystr)
   