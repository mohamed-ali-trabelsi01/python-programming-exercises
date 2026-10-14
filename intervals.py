def merge(intervals):

    if len(intervals) == 0:
        return []


    n = len(intervals)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if intervals[j][0] > intervals[j + 1][0]:
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]


    merged = []

    for interval in intervals:
        if len(merged) == 0:
            merged.append([interval[0], interval[1]])
        else:
            last = merged[-1]
            if interval[0] > last[1]:

                merged.append([interval[0], interval[1]])
            else:
                # Überlapp – Endwert anpassen
                if interval[1] > last[1]:
                    last[1] = interval[1]

    return merged
