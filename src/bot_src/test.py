from tournament import Tournament
from participant import Participant

tournament_instance = Tournament()

def generate_participants(participant_count):

    for i in range(0,participant_count):
        new_participant = Participant()
        new_participant.nick = "Name%s" % str(i)
        new_participant.id = "ID%s" % str(i)
        new_participant.seed = i

        tournament_instance.participants.append(new_participant)

def test_generate_matches():
    tournament_instance.generate_matches()

if __name__ == "__main__":
    generate_participants(15)
    test_generate_matches()
    for i in range(0, len(tournament_instance.matches)):
        print("Match %d | Stage %d" % (i, tournament_instance.matches[i].stage))
        for j in range(0, len(tournament_instance.matches[i].players)):
            player = tournament_instance.matches[i].players[j]
            print("Name: %s | seed: %d" % (player.nick, player.seed))
        print("-----------")