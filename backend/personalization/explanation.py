def generate_explanation(activity, user_prefs, alternatives):
    reasons = []

    if activity["category"] in user_prefs["interests"]:
        reasons.append(f"Matches your interest in {activity['category']}")

    if activity["cost_level"] <= user_prefs["budget"]:
        reasons.append("Fits within your selected budget")

    if activity["duration_hours"] <= user_prefs["pace_hours"]:
        reasons.append("Suitable for your preferred travel pace")

    explanation = {
        "activity": activity["name"],
        "why_recommended": reasons,
        "alternative": alternatives[0]["name"] if alternatives else None,
        "tradeoff": "Alternative may differ in cost, duration, or popularity."
    }

    return explanation
