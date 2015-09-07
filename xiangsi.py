#coding:utf-8

import gensim,sys

query = sys.argv[1]

model = gensim.models.Word2Vec.load_word2vec_format("shiyan.vector", binary=False)

for line in  model.most_similar(query.decode('utf8'),topn=40):
	print line[0],line[1]