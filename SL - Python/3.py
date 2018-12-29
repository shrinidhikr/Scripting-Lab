class SentenceRev:
  vowels = ['a','e','i','o','u']
  vcount = 0 
  revsent = " "
  sentence = " "
  
  def __init__(self,sentence):
    self.sentence = sentence
    self.revsent = self.getReverse()
  def getReverse(self):
    return " ".join(reversed(self.sentence.split()))
  def vowelCount(self):
    self.vcount = sum(s in self.vowels for s in self.sentence.lower())
    return self.vcount

items = []

for i in range(2):
  sentence = input("Enter the string: \n")
  reverser = SentenceRev(sentence.strip())
  items.append(reverser)
  
sortedItems = sorted(items, key=lambda item: item.vowelCount(), reverse=True)
print(sortedItems)
for i in range(len(sortedItems)):
  print("Reversed: ",sortedItems[i].getReverse(), "Vowel count: ", sortedItems[i].vowelCount(),"\n")
