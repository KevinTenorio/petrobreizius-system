from datetime import datetime

def merge_overlapping_events(events):
    # Sort events based on start time
    events.sort(key=lambda x: x[0])

    merged_events = []
    current_start, current_end = events[0]

    for event_start, event_end in events[1:]:
        # If the start time of the current event is before or equal to the end time of the previous event,
        # merge the events by updating the end time of the current event
        if event_start <= current_end:
            current_end = max(current_end, event_end)
        else:
            # If the current event does not overlap with the previous one, add the previous merged event
            # to the list of merged events and update the current event's start and end times
            merged_events.append((current_start, current_end))
            current_start, current_end = event_start, event_end

    # Add the last merged event to the list
    merged_events.append((current_start, current_end))

    return merged_events