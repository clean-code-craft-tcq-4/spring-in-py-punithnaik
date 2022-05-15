def calculateStats(numbers):
  avg_num = sum(numbers)/len(numbers)
  max_num = max(numbers)
  min_num = min(numbers)
  d = {"avg":avg_num,"max":max_num,"min":min_num}
  return d
