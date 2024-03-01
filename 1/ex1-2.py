import pandas as pd
import numpy as np
import random

g = np.random.default_rng(0)
nums = g.integers(70, 101, 10)
months = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split()
scores = pd.Series(nums, index=months)


mean = scores.mean()
first = scores.head().mean()
second = scores.tail().mean()


print(f"mean: {mean}")
print(f"first half mean: {first}")
print(f"second half mean: {second}")

if second > first:
    print(f"improved: {second - first}")
elif first > second:
    print(f"dropped: {first - second}")
else:
    print("no change")

print("5 highest scores")
print(scores.sort_values().iloc[5:])

