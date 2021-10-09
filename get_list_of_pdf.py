import os
import subprocess


def divived(file):
    lines_per_file =10
    count = 3438
    smallfile = None
    with open(file) as bigfile:

        for lineno, line in enumerate(bigfile):
            line = line.replace('.','')
            line = line.replace('1','')
            line = line.replace('2','')
            line = line.replace('3','')
            line = line.replace('4','')
            line = line.replace('5','')
            line = line.replace('6','')
            line = line.replace('7','')
            line = line.replace('8','')
            line = line.replace('9','')
            line = line.replace('0','')
            line = line.replace(':','')
            line = line.replace('•','')


            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'dataset/law/{}.txt'.format(count)
                smallfile = open(small_filename, "w")
                count += 1
            smallfile.write(line)
        if smallfile:
            smallfile.close()

zips = [os.path.join(dp, f) for dp, dn, filenames in os.walk("R") for f in filenames if os.path.splitext(f)[1] == '.zip']

print(zips)

for zip in zips:
   subprocess.call(['unzip', '{zip}'.format(pdf=zip)])

count=0

result = [os.path.join(dp, f) for dp, dn, filenames in os.walk("R") for f in filenames if os.path.splitext(f)[1] == '.pdf']
print(result)
for pdf in result:
    count= count+1
    subprocess.call(['pdftotext', '{pdf}'.format(pdf=pdf), 'R/text/{name}.txt'.format(name=count)])
    subprocess.call(['camel_arclean','R/text/{name}.txt'.format(name=count)])
    divived('R/text/{name}.txt'.format(name=count))



