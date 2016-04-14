data_filename = nltk.data.path[0] + '/mini_data_1.csv'

with open(data_filename, 'r') as rf:
    for line in rf:
        line = line.rstrip('\n').split(',')
        print line
        [rt, filename] = line
        filename = filename.split('_')
        if len(filename)== 3:
            [word, sex, lang] = filename
            [lang, extension] =	lang.split('.')
            print word+'\t'+sex+'\t'+lang
	    print '\t'.join([rt, word, sex, lang])
