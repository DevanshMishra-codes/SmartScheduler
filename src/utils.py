def classify_efficiency(avg_waiting_time, avg_turnaround_time, avg_response_time):
    score = (avg_waiting_time * 0.5) + (avg_turnaround_time * 0.3) + (avg_response_time * 0.2)

    if score < 10:
        return "Excellent"
    elif score < 20:
        return "Good"
    elif score < 30:
        return "Average"
    else:
        return "Poor"
