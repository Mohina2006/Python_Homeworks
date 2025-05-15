scores = {'Alice': 45, 'Bob': 82, 'Charlie': 60, 'Diana': 37}

filtered_scores = {k: v for k, v in scores.items() if v > 50}

print(filtered_scores)
