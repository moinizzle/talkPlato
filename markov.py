#!/usr/bin/env python3

import sys
import random

class Markov:
     
     def __init__(self):
          pass 
     
     def set_values(self, db, key, val):
          
          if key not in db:
               temp = list()
               temp.append(val)
               db[key] = temp
          
          else:
               db[key].append(val)

     # read text
     def reader(self, filename):
          file = open(filename)
          contents = file.read()
          contents = contents.replace('\n', ' ')
          contents = " ".join(contents.split())

          #print(contents)
          return contents

     def makeDB(self, data):

          words = data.split(" ")
          db = dict()

          map = zip(words[:-1], words[1:])

          for key, val in map:
               self.set_values(db, key, val)

          #print(db)
          return db

     def generate(self, db, n=15):
          
          key_list = list(db.keys())
          random_key = random.choice(key_list)
          first = random_key.capitalize()

          i = 0

          while (i < n):
               new_word = random.choice(db[random_key])
               random_key = new_word
               first = first + " " + new_word
               i += 1

          first += "."
          return(first)

if __name__ == '__main__':

     user_input = sys.argv[1]
     markov = Markov()
     corpus = markov.reader(user_input)
     db = markov.makeDB(corpus)

     temp = dict()
     
     n, n_key = (0, "")
     sorted_n = []

     for key in db:
          total = len(db[key])
          sorted_n.append(total)
          if (total > n):
               n, n_key = (len(db[key]), key)
     
          markov.set_values(temp, key, total)
     
     sorted_n.sort()
     
     #print(temp)
     #print(n, n_key)
     #print(sorted_n)
     length = random.randint(15, 20)
     sentence = markov.generate(db, length)
     print(sentence)

