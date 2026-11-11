
def score_backlog(items):
    result = []

    for item in items:
        if item["effort"] <= 0:
            continue

        score = round(item["value"] / item["effort"], 2)
        result.append((item["id"], score))

    result.sort(key=lambda x: (-x[1], x[0]))

    return result


def validate_user_story(story):
    if not isinstance(story, str) or not story.strip():
        return False

    if not story.startswith("As a "):
        return False

    parts = story[5:].split(", I want ")

    if len(parts) != 2:
        return False

    role = parts[0]
    goal_benefit = parts[1].split(", so that ")

    if len(goal_benefit) != 2:
        return False

    goal = goal_benefit[0]
    benefit = goal_benefit[1]

    if not role.strip() or not goal.strip() or not benefit.strip():
        return False

    return True
