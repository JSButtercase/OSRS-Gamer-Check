from osrs_api import Hiscores

class GamerCheck:

    player_list = []
    player_dict = {}

    def __init__(self, p):
        for username in p.values():
            self.player_list.append(username)

    def lookup(self):
        for name in self.player_list:
            inferno_kc = Hiscores(name).bosses['TzKal-Zuk'].kills
            self.player_dict[name] = inferno_kc

    def display(self):
        for kc in self.player_dict:
            if self.player_dict[kc] > 0:
                print(kc, "is a gamer")
            else:
                print(kc, "is not a gamer :/")


while True:
    player_count = input("How many players are we checking?: ")
    try:
        # Convert to Int
        player_count = int(player_count)
        print("ValidInput: ", player_count, "players")
        break

    except ValueError:
        print("Integer input required")

rat_pack = {}
for players in range(player_count):
    print("Details for player", players+1)
    irl_name = input("Whats your name player?: ")
    irl_name = str(irl_name)
    ign = input("Whats your IGN (your username)?: ")
    ign = str(ign)
    rat_pack[irl_name] = ign

RatPack_check = GamerCheck(rat_pack)
RatPack_check.lookup()
RatPack_check.display()


