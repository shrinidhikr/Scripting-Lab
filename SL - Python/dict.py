def countDict():
  escape = open('Hakuna Matata.txt')
  wordDict={}
  
  for line in escape:
    print(line)
    mylist = line.split()
    print(mylist)
    
    for word in mylist:
      w = wordDict.get(word,0)
      print("No. of times %s has appeared is %d\n"%(word,w))
      wordDict[word] = w +1
      print("After adding the new word %s\n"%word)
      print("No. of times %s has appeared is %d"%(word,wordDict[word]))
      
  print("\n", wordDict, "\n")
  
  ans='y'
  while ans == 'y' or ans =='Y':
    key=input("Enter the word to return it's count\n")
    if key in wordDict:
      print("%s has appeared %d times\n" %(key,wordDict[key]))
    else:
      print("Word not found\n")
    ans=input("Enter Y or N to search the next word\n")
countDict()

