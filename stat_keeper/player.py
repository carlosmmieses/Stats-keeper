
class Player:
    def __init__(self, player_stat, player_team):
        self.team = str(player_team).upper()
        self.number = str(player_stat[0]).upper()
        if "*" in player_stat[1]:
            self.name = str(player_stat[1].split(" ")[1]).upper()
        else:
            self.name = str(player_stat[1]).upper()
        self.tfg = player_stat[2]
        self._2fg = player_stat[3]
        self._3pt = player_stat[4]
        self.ft = player_stat[5]
        self.pts = int(player_stat[6])
        self.orb = int(player_stat[7])
        self.drb = int(player_stat[8])
        self.tr = int(player_stat[9])
        self.pf = int(player_stat[10])
        self.fd = int(player_stat[11])
        self.ast = int(player_stat[12])
        self.aa = int(player_stat[13])
        self.to = int(player_stat[14])
        self.bs = int(player_stat[15])
        if isinstance(player_stat[16], str) and len(player_stat) < 18:
            self.st = int(player_stat[16].split(" ")[0])
            if "DNP" in player_stat[16]:
                self.minutes = "00:00"
                self.games_played = 0
            else:
                self.minutes = player_stat[16].split(" ")[1]
                self.games_played = 1
        else:
            self.st = int(player_stat[16])
            if isinstance(player_stat[17], str) and "DNP" in player_stat[17]:
                self.minutes = "00:00"
                self.games_played = 0
            else:
                self.minutes = player_stat[17]
                self.games_played = 1
        if len(player_stat) > 18:
            self.games_played = player_stat[18]
        if self.games_played:
            self.pts_per_game = self.pts / self.games_played
            self.drb_per_game = self.drb / self.games_played
            self.orb_per_game = self.orb / self.games_played
            self.tr_per_game = self.tr / self.games_played
            self.pf_per_game = self.pf / self.games_played
            self.fd_per_game = self.fd / self.games_played
            self.ast_per_game = self.ast / self.games_played
            self.aa_per_game = self.aa / self.games_played
            self.to_per_game = self.to / self.games_played
            self.bs_per_game = self.bs / self.games_played
            self.st_per_game = self.st / self.games_played
        else:
            self.pts_per_game = 0
            self.drb_per_game = 0
            self.orb_per_game = 0
            self.tr_per_game = 0
            self.pf_per_game = 0
            self.fd_per_game = 0
            self.ast_per_game = 0
            self.aa_per_game = 0
            self.to_per_game = 0
            self.bs_per_game = 0
            self.st_per_game = 0