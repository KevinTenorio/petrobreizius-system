def check_meeting_collision(new_start, new_end, meetings):
    for meeting_start, meeting_end in meetings:
        print(meeting_start, meeting_end, new_start, new_end)
        if (new_start < meeting_end) and (new_end > meeting_start):
            return True  # Collision detected
    return False  # No collision found