#http://tinyurl.com/tastybiriyani
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

for i in list:
	# print(i)
	d=""
	for j in i:
		# print(j)
		d=d + j + " "
		
	# print("d",d)
	if(d in di):
		di[d]=di[d]+1 
	else:
		di[d]=1

print(di)

