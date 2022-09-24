_end = '_end_'
def Trie(words):
  root = dict()
  for word in words:
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
  #print(root)
  return root

def LongestCompoundWord(original_trie, trie, word, level=0):
  try:
    first_letter = word[0]
  except:
    first_letter=''
  if not first_letter in trie:
    return False
  if len(word)==1 and _end in trie[first_letter]:
    return level>0
  if _end in trie[first_letter] and LongestCompoundWord(original_trie, original_trie, word[1:], level+1):
    return True
  return LongestCompoundWord(original_trie, trie[first_letter], word[1:], level)

#Words that were in your question
f=open("Input_01.txt","r")
s=f.read()
words =list(map(str,s.split("\n")))
trie = Trie(words)

#Sort words in order of decreasing length
words = sorted(words, key=lambda x: len(x), reverse=True)
#print(words)

for word in words:
  if LongestCompoundWord(trie,trie,word):
    x=('{:}'.format(word))
    print("Longest Compound Word:",x)
    words.remove(x)
    break

for word in words:
  if LongestCompoundWord(trie,trie,word):
    x='{:}'.format(word)
    print("Second Longest Compound Word:",x)
    break
    
