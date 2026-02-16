def score_activity(activity, user_prefs):
    score = 0

    # Interest match
    if activity["category"] in user_prefs["interests"]:
        score += 5

    # Budget compatibility
    if activity["cost_level"] <= user_prefs["budget"]:
        score += 3

    # Pace compatibility
    if activity["duration_hours"] <= user_prefs["pace_hours"]:
        score += 2

    # Constraint penalty
    if user_prefs.get("avoid_outdoor") and activity["is_outdoor"]:
        score -= 5

    return score


def rank_activities(activities, user_prefs):
    return sorted(
        activities,
        key=lambda a: score_activity(a, user_prefs),
        reverse=True
    )
