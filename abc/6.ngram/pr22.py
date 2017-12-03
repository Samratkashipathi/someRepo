from nltk import word_tokenize

file_content = open("in1.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def getNGrams(input_list, n):
    print('\n',n,'_Grams:\n')
    return [input_list[i:i+n] for i in range(len(input_list)-(n-1))]

list =getNGrams(wordlist, 1)
di=dict()
count=0
for i in list:
	d=""
	for j in i:
		d=d + j + " "
		count=count+1
	print(d)
	if(d in di):
		di[d]=di[d]+1 
	else:
		di[d]=1

print(di)


