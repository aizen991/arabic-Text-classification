


lines_per_file =10
count = 3163
smallfile = None
with open('clean_text') as bigfile:

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