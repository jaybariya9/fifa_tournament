# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import math


# defines how to split the teams in groups x teams per group
def team_split(teams):
    x = teams
    counter = 2
    multiples = []
    while x > 1:
        if x % counter == 0:
            multiples.append(counter)
            x = int(x / counter)
        else:
            counter += 1

    # spl = round(len(multiples) / 2)
    # p1 = math.prod(multiples[:spl])
    # p2 = math.prod(multiples[spl:])
    #
    # j = max(p1, p2)
    # k = min(p1, p2)
    # if k > 4 and k % 4 == 0:
    #     j = int(j * 4)
    #     k = int(k / 4)
    # else:
    #     pass

    j = int(teams / 4)
    k = 4

    if teams % 4 != 0:
        raise TypeError(str(teams), "teams is not even-numbered!")
    else:
        return j, k


# defines the number of teams advancing to knockout rounds
def knockout_games(teams):
    x = teams
    counter = 0
    while x > 1:
        x = x / 2
        counter += x
    return counter


def closest_teams(teams):
    n = 1
    val = 2
    while teams > val ** n:
        n += 1
    return val ** (n - 1)
# defines number of knockout games based on teams


def teams_time(n_teams, ps5, half_length_league=4, half_length_knockout=5, half_length_final=6):
    # try to organize such that maximum possible teams play

    referee_time = 2
    adjustment_time = 3
    time_per_game_league = (half_length_league * 2) + referee_time + adjustment_time
    time_per_game_knockout = (half_length_knockout * 2) + referee_time + adjustment_time
    time_per_game_final: int = (half_length_final * 2) + referee_time + adjustment_time

    n_groups, n_teams_per_group = team_split(n_teams)

    n_matches_per_group = int(math.factorial(n_teams_per_group) / (
            math.factorial(n_teams_per_group - 2) * math.factorial(2)))

    n_group_matches = n_matches_per_group * n_groups

    n_group_stage_time = int((n_group_matches // ps5) * time_per_game_league + (
        time_per_game_league if (n_group_matches % ps5 != 0) else 0))

    n_teams_in_knockout = int(closest_teams(n_teams))

    n_matches_in_knockout = knockout_games(n_teams_in_knockout)

    n_knockout_stage_time = ((n_matches_in_knockout - 3) // ps5) * time_per_game_knockout + \
                            (time_per_game_knockout if ((n_matches_in_knockout - 3) % ps5 != 0) else 0) + \
                            (3 * time_per_game_final)

    total_time = n_group_stage_time + n_knockout_stage_time

    # print("It takes " + str(time_per_game_league) + " minutes per game." +
    #       " Based on " + str(n_teams) + " teams, they are divided in " + str(n_groups)
    #       + " groups and " + str(n_teams_per_group) + " teams per group."
    #       + " Total no. of matches in group stage is " + str(n_group_matches)
    #       + " and would take " + str(n_group_stage_time) + " minutes."
    #       + " No. of teams advancing in knockout stages is " + str(n_teams_in_knockout) + "."
    #       + " Total no. of matches in knockout stages is " + str(n_matches_in_knockout)
    #       + " and would take " + str(n_knockout_stage_time) + " minutes." + " Therefore, the total tournament time = "
    #       + str(n_group_stage_time) + " + " + str(n_knockout_stage_time) + " = " + str(total_time) + " minutes.")

    return total_time

# teams_list = list(range(8, 257, 4))
# for i, t in enumerate(teams_list):
#     print(teams_list[i], teams_time(t, 8))
