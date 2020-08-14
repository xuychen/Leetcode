from collections import defaultdict
import heapq

def topKFrequent(keywords, reviews, k):
    keywords_set = set(keywords)
    counter = defaultdict(int)

    for review in reviews:
        for word in set(map(lambda x: x.lower(), review.split())):
            if word in keywords_set:
                counter[word] += 1
                
    return heapq.nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))

# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#   "Anacell provides the best services in the city",
#   "betacellular has awesome services",
#   "Best services provided by anacell, everyone should use anacell",
# ]

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

print(topKFrequent(keywords, reviews, k))