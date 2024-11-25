# stable_marriage.py

def stable_marriage(n, boy_preferences, girl_preferences):
    # Initialize free boys and engaged girls
    free_boys = list(range(n))
    girls_partners = [-1] * n
    boys_next_proposal = [0] * n
    girls_preferences_rank = [[0] * n for _ in range(n)]

    # Create a ranking matrix for girls' preferences
    for girl in range(n):
        for rank, boy in enumerate(girl_preferences[girl]):
            girls_preferences_rank[girl][boy - 1] = rank

    while free_boys:
        boy = free_boys.pop(0)
        girl_index = boy_preferences[boy][boys_next_proposal[boy]] - 1
        boys_next_proposal[boy] += 1

        if girls_partners[girl_index] == -1:
            girls_partners[girl_index] = boy
        else:
            current_partner = girls_partners[girl_index]
            if girls_preferences_rank[girl_index][boy] < girls_preferences_rank[girl_index][current_partner]:
                girls_partners[girl_index] = boy
                free_boys.append(current_partner)
            else:
                free_boys.append(boy)

    return [(boy + 1, girl + 1) for girl, boy in enumerate(girls_partners)]

