from math import factorial
def permutate3(stng):
  #so swap A with consecutive letters unti you get to the end.
  #then take a "break" and swap the 2 letters at the beginning of teh string
  #swap A back to the front
  #take another break and swap the two letters at the end of the string
  #start over again
  Lst=[]
  ch=stng[0]
  #word=stng
  #actuall turn the whole thing into a list and then rewrite the entire code. wow this will be fun.
  word=stng[1:]
  for r in range(factorial(len(word))):
    for n in range(1,(len(word)+1)):
      w=word[:n]+ch+word[n:]
      if w not in Lst:
        Lst.append(w)
        r+=1
      print('4WORD ',w)
    print('lstr', Lst[len(Lst)-1])
    werd=swapFront(Lst[len(Lst)-1])
    if not werd in Lst:
      Lst.append(werd)
      r+=1
    else: return Lst
    word=werd[:len(werd)-1]

    for n in range(1,len(word)+1):
      w=word[:len(word)-n]+ch+word[len(word)-n:]
      if not w in Lst:
         Lst.append(w)
         r+=1
      else: return Lst
      print('BACKWORD ',w)
    werd=swapBk(Lst[len(Lst)-1])
    if werd not in Lst:
      Lst.append(werd)
      r+=1
    else: return Lst
    word=werd[1:]

    #start again

    for n in range(1,(len(word)+1)):
      w=word[:n]+ch+word[n:]
      if w not in Lst:
        Lst.append(w)
        r+=1
      print('4WR ',w)
    werd=swapFr(Lst[len(Lst)-1])
    if not werd in Lst:
      Lst.append(werd)
      r+=1
    else: return Lst
    word=werd[:len(werd)-1]

    for n in range(1,len(word)+1):
      w=word[:len(word)-n]+ch+word[len(word)-n:]
      if not w in Lst:
         Lst.append(w)
         r+=1
      else: return Lst
      print('BKWORD ',w)
    werd=swapBack(Lst[len(Lst)-1])
    if werd not in Lst:
      Lst.append(werd)
      r+=1
    else: return Lst
    word=werd[1:]
  return Lst

def swapFr(stng):
  if len(stng)<2:
    return stng
  stng=stng[:2]+stng[3]+stng[2]+stng[4:]
def swapFront(stng):
  if len(stng)<2:
    return stng
  stng=stng[1]+stng[0]+stng[2:]
  print('SWAPFRONT ',stng)
  return stng
def swapBk(stng):
  stng=stng[:len(stng)-3]+stng[len(stng)-2]+stng[len(stng)-3]
  return stng
def swapBack(stng):
  if len(stng)<2:
    return stng
  stng=stng[:len(stng)-2]+stng[len(stng)-1]+stng[len(stng)-2]
  print('SWAPBACK ',stng)
  return stng





def permute3(stng):
  if len(stng)==3:










































def main():
  Lst=permutate3('ABCDE')
  for a in Lst:
    print(a)


if __name__ == '__main__':main()


