from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# first 10 for greetings, next 10 for praises
data = ["Hey how are you",
        "Hi",
        "Hello",
        "Yo",
        "Sup",
        "Whats up",
        "How have you been",
        "Yolo",
        "Namashkaar",
        "Hello ji",
        "thanks :) :D",
        "shukriyaa",
        "dhanyaawaad",
        "nice",
        "you're life saver :D",
        "Thank you so much",
        "You're a big help",
        "Nice catch",
        "What will I do without you",
        "Just perfect."]

tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]

max_epochs = 100
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=vec_size, alpha=alpha, min_alpha=0.00025, min_count=1, dm =1)  
model.build_vocab(tagged_data)
for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.iter)
    model.alpha -= 0.0002
    model.min_alpha = model.alpha

model.save("../models/d2v.model")
