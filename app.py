import ipldb as ipl
import pprint

if __name__ == "__main__":
    t_names=ipl.get_team_names()
    t_labels=ipl.get_team_labels()
    for ele in range(0,8):
        print(t_names[ele],":",t_labels[ele])

    t_details=ipl.get_team_details()

    print("*"*100)

    pprint.pprint(t_details)

    print("*"*100)

    p_details=ipl.get_players()
    pprint.pprint(p_details)

    print("*"*100)

    rcb_play=ipl.get_team_players("RCB")

    print("Players of RCB are:")
    print("*"*100)

    pprint.pprint(rcb_play)

    print("*"*100)