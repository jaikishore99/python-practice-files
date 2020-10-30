#list1 = [1, 2, 3, 4]
#list2 = ['jai', 'kishore', 'raj', 'kumar']

#zipped = list(zip(list1, list2))

# print(zipped)

#unzipped = list(zip(*zipped))
# print(unzipped)

# for (l1, l2) in zip(list1, list2):
#   print(l1)
#  print(l2)

cloth = ['shirt', 't-shirt', 'denim']
quantity = [3, 2, 1]
price = [200, 300, 400]

sentences = []
for (C, Q, P) in zip(cloth, quantity, price):
    sentence = 'i bought ' + str(Q) + " " + str(C) + 'for ' + \
        str(P) + 'rupees = total price is ' + str(Q*P)+'.'
    sentences.append(sentence)
print(sentences)
