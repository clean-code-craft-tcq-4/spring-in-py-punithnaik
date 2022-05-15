def calculateStats(numbers):
  if numbers == []:
    n = float("nan")
    d = {"avg":n,"max":n,"min":n}
  else:
    avg_num = sum(numbers)/len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    d = {"avg":avg_num,"max":max_num,"min":min_num}
  return d
