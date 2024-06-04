def main():
  x = int(input())
  n = int(input())
  i = 0
  arr = []
  results = []
  while i < n:
    el = int(input())
    arr.append(el)
    i += 1

  for i in range(len(arr)):
    for j in range(i, len(arr), x):
      if j+x <= len(arr):
        results.append(arr[i:i+x])

  real_results = []
  for i in results:
    real_results.append(min(i))

  print(max(real_results))

if __name__ == "__main__":
  main()