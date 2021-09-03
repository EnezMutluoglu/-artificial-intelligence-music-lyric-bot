import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer



from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import Sequential

import numpy as np

#with open("song.txt") as f:
#    for i in range(10):
#        a=f.readline()
#        print(a)

f=open("song.txt","r",encoding="utf-8")
print(f.readline())
f.close()
f=open("song.txt","w",encoding="utf-8")
f.writelines("")


#lines = text.lower().split("\n")
#print(lines)
#
#tokenizer = Tokenizer()
#
#tokenizer.fit_on_texts(lines)
#
#total_words = len(tokenizer.word_index) + 1
#
#input_sequences = []
#
#for line in lines:
#
#    token_list = tokenizer.texts_to_sequences([line])[0]
#
#    for i in range(1, len(token_list)):
#
#        tokens = token_list[:i + 1]
#
#        input_sequences.append(tokens)
#
#print(input_sequences)
#
#maxlen = max([len(x) for x in input_sequences])
#
#padding = "pre"
#
#input_sequences = np.array(pad_sequences(input_sequences, padding=padding, maxlen=maxlen))
#
#xs, labels = input_sequences[:,:-1], input_sequences[:,-1]
#
#ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)
#
#
#model = Sequential([
#
#    tf.keras.layers.Embedding(total_words, 100, input_length=maxlen - 1),
#
#    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(100)),
#
#    tf.keras.layers.Dense(total_words, activation="softmax")
#
#])
#
#model.compile(loss="categorical_crossentropy", optimizer=tf.keras.optimizers.Adam(learning_rate=0.06), metrics=["accuracy"])
#
#history = model.fit(xs, ys, epochs=10, verbose=1)
#
#
#seed = "meinBakhuda tumhi"
#
#token_list = tokenizer.texts_to_sequences([seed])[0]
#
#token_list = pad_sequences([token_list], maxlen=maxlen-1, padding=padding)
#
#predicted = np.argmax(model.predict(token_list), axis=-1)
#
#output_word = ""
#
#for word, index in tokenizer.word_index.items():
#
#    if index == predicted:
#
#        output_word = word
#
#        break
#
#print(output_word)