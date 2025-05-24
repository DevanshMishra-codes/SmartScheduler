def classify_efficiency(avg_waiting_times, avg_turnaround_times, avg_response_times):
    scores = [
        (w * 0.5 + t * 0.3 + r * 0.2)
        for w, t, r in zip(avg_waiting_times, avg_turnaround_times, avg_response_times)
    ]

    min_score = min(scores)
    max_score = max(scores)
    threshold = (max_score - min_score) / 3 if max_score != min_score else 1  # Avoid zero division

    labels = []
    for score in scores:
        if score <= min_score + threshold:
            labels.append('High')
        elif score <= min_score + 2 * threshold:
            labels.append('Mid')
        else:
            labels.append('Low')

    return labels

   
