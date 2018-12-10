#!/usr/bin/python3
import datetime
from operator import itemgetter

records = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        # Ignore the year, since they're all the same
        rest = line.partition("-")[2]
        month, __, rest = rest.partition("-")
        month = int(month)
        day, __, rest = rest.partition(" ")
        day = int(day)
        hour, __, rest = rest.partition(":")
        hour = int(hour)
        minute, __, text = rest.partition("] ")
        minute = int(minute)
        # Store all the records, with int timestamps separated
        records.append((month, day, hour, minute, text))

# We can now sort the records, which will sort first by month, then day, etc
records.sort()

# Group the records into sleeping periods
sleep_times = {}
guard = None
sleep_start = None
for record_num, (month, day, hour, minute, text) in enumerate(records):
    if text.startswith("Guard "):
        # New guard started shift
        guard = text.split()[1]
    elif text == "falls asleep":
        # Record the start time of the sleep
        sleep_start = (month, day, hour, minute)
    elif text == "wakes up":
        # End of a sleep
        if sleep_start is None:
            # Weren't expecting this here: something must have gone wrong in our ordering
            raise ValueError("unexpected sleep end at record {}".format(record_num))
        sleep_times.setdefault(guard, []).append((sleep_start, (month, day, hour, minute)))
        # Reset the start time so we know if the ordering's wrong
        sleep_start = None

sleep_lengths = {}
for guard, sleeps in sleep_times.items():
    for (month0, day0, hour0, minute0), (month1, day1, hour1, minute1) in sleeps:
        # Count the number of minutes slept
        sleep_length = datetime.datetime(year=1518, month=month1, day=day1, hour=hour1, minute=minute1) - \
                       datetime.datetime(year=1518, month=month0, day=day0, hour=hour0, minute=minute0)
        minutes_slept = int(sleep_length.total_seconds() / 60)
        sleep_lengths.setdefault(guard, []).append(minutes_slept)

# Count up how many minutes each guard is asleep for
# I don't think we're supposed to average, just sum up all the sleeps
guard_sleep_lengths = [(guard, sum(sleeps)) for (guard, sleeps) in sleep_lengths.items()]
sleepiest_guard = max(guard_sleep_lengths, key=itemgetter(1))[0]
print("Sleepiest guard: {}".format(sleepiest_guard))

# Look at this guards sleeping times to find out in which minute s/he is most asleep
minutes = {}
for start, end in sleep_times[sleepiest_guard]:
    start_min = start[3]
    end_min = end[3]
    for minute in range(start_min, end_min):
        # Mark this minute as slept in once (more)
        minutes[minute] = minutes.get(minute, 0) + 1
most_slept_minute = max(minutes.items(), key=itemgetter(1))[0]
print("Slept most in minute {}".format(most_slept_minute))

# Compute the answer to submit
answer = int(sleepiest_guard[1:]) * most_slept_minute
print("{} * {} = {}".format(sleepiest_guard[1:], most_slept_minute, answer))

### PART 2
guard_minutes = {}
for guard, sleeps in sleep_times.items():
    for start, end in sleeps:
        start_min = start[3]
        end_min = end[3]
        for minute in range(start_min, end_min):
            # Mark this minute as slept in once (more) by this guard
            guard_minutes[(guard, minute)] = guard_minutes.get((guard, minute), 0) + 1

most_slept_guard, most_slept_guard_minute = max(guard_minutes.items(), key=itemgetter(1))[0]
print("Guard {} most frequently asleep in minute {}".format(most_slept_guard, most_slept_guard_minute))

# Compute the answer to submit
answer2 = int(most_slept_guard[1:]) * most_slept_guard_minute
print("{} * {} = {}".format(most_slept_guard[1:], most_slept_guard_minute, answer2))
