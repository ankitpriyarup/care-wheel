from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import sent_tokenize, word_tokenize

data_margin = 10

model= Doc2Vec.load("../models/d2v.model")
test_data = "Hi".split(" ")
v1 = (model.docvecs.most_similar(positive=[model.infer_vector(test_data)]))
res = {}
maxV = -900
ans = 0
for item in v1:
    group = int(item[0]) // data_margin
    res[str(group)] = res.get(str(group), 0) + item[1]
    if res.get(str(group), -900) > maxV:
        maxV = res.get(str(group), -900)
        ans = group
print(maxV)
print(ans)
