def main():
  
  string = input()
  k = int(input())
  print(perfect_substring(string, k))

def perfect_substring(string, k):
  result = 0

  for i in range(len(string)):
    frequency = [0] * 10
    for j in range(i, len(string)):


      frequency[int(string[j])] += 1
      is_true = True

      if frequency[int(string[j])] > k:
        break

      for l in frequency:
        if l != 0 and l != k:
          is_true = False
      
      if is_true and frequency[int(string[j])] == k:
        result += 1
  
  return result

if __name__ == "__main__":
  main()