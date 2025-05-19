def classify_efficiency(avg_waiting_time, avg_turnaround_time, avg_response_time):
    
    scores = ((avg_waiting_time * 0.5) + (avg_turnaround_time * 0.3) + (avg_response_time * 0.2)) / 3

    if not scores:
        return []

    min_score = min(scores)
    max_score = max(scores)
    score_range = max_score - min_score
    threshold = score_range / 3

    labels = []
    for score in scores:
        if score <= min_score + threshold:
            labels.append('High')
        elif score <= min_score + 2 * threshold:
            labels.append('Mid')
        else:
            labels.append('Low')

    return labels
   
