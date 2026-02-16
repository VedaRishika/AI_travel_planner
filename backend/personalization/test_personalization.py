from ranking import rank_activities
from explanation import generate_explanation

# Sample activities
activities = [
    {
        "name": "Free Walking Tour",
        "category": "culture",
        "cost_level": 0,
        "duration_hours": 2,
        "is_outdoor": True
    },
    {
        "name": "Private River Cruise",
        "category": "sightseeing",
        "cost_level": 5,
        "duration_hours": 3,
        "is_outdoor": False
    }
]

# Sample user preferences
user_prefs = {
    "interests": ["culture"],
    "budget": 2,
    "pace_hours": 3,
    "avoid_outdoor": False
}

# Rank activities
ranked = rank_activities(activities, user_prefs)

# Generate explanation for top activity
explanation = generate_explanation(ranked[0], user_prefs, ranked[1:])

print("Top Recommendation:")
print(explanation)
