import re 

class Team:
    def __init__(self):
        self.goal_count = 0
        self.open_cnt = 0
        self.matches = 0
    def mean(self):
        return self.goal_count/self.matches

class Player:
    def __init__(self,team):
        self.team = team
        self.goal_count = 0
        self.goal_minutes = [0 for i in range(91)]
        self.open_cnt = 0
    
    def goal(self, minute,is_open):
        self.goal_minutes[minute] += 1
        self.goal_count += 1

        if is_open:
            self.open_cnt += 1
            self.team.open_cnt += 1

        self.team.goal_count += 1

    def mean(self):
        return self.goal_count/self.team.matches
        
    def first_t_minutes(self,t):
        ans = 0
        for i in range(t+1):
            ans += self.goal_minutes[i]
        return ans

    def last_t_minutes(self, t):
        ans = 0
        for i in range(91-t,91):
            ans += self.goal_minutes[i]
        return ans

    def on_minutes(self, t):
        return self.goal_minutes[t]

team_dict = dict()
player_dict = dict()

out = open('output.txt','w')

with open('input.txt','r') as f:
    line = f.readline()
    c = 1
    while line:
        
        match_obj = re.match(r'(\D+) - (\D+) (\d+):(\d+)', line)
        if match_obj is not None:
            team1, team2, score1, score2 = match_obj.groups()

            score1 = int(score1)
            score2 = int(score2)
            
            game = []

            t = 0 
            while t < score1:
                s = f.readline()
                player_name, minute = re.match(r'(\D+) (\d+)\'',s).groups()
            
                game.append((player_name,team1,int(minute)))
                t+=1
                
            t = 0 
            while t < score2:
                s = f.readline()
                player_name, minute = re.match(r'(\D+) (\d+)\'',s).groups()
                
                game.append((player_name,team2,int(minute)))
                t+=1
            
            if team1 not in team_dict.keys():
                team_dict[team1] = Team()

            if team2 not in team_dict.keys():
                team_dict[team2] = Team()

            team_dict[team1].matches += 1
            team_dict[team2].matches += 1

            game.sort(key=lambda x: x[2])

            for i in range(len(game)):
                player_name,team,minute = game[i]
                if player_name not in player_dict.keys():
                    player_dict[player_name] = Player(team_dict[team])
                player_dict[player_name].goal(minute,i==0)

        elif re.match(r'Total goals for (\D+)', line) is  not None:
            team = re.match(r'Total goals for (\D+)', line).group(1)
            team = team.strip()

            if team in team_dict.keys():
                print(team_dict[team].goal_count, file=out)
            else:
                print(0, file=out)

        elif re.match(r'Total goals by (\D+)', line) is  not None:
            name = re.match(r'Total goals by (\D+)', line).group(1)
            name = name.strip()

            if name in player_dict.keys():
                print(player_dict[name].goal_count, file=out)
            else:
                print(0, file = out)

        elif re.match(r'Mean goals per game by (\D+)', line) is  not None:
            name = re.match(r'Mean goals per game by (\D+)', line).group(1)
            name = name.strip()

            if name in player_dict.keys():
                print(player_dict[name].mean(), file=out)
            else:
                print(0, file=out)

        elif re.match(r'Mean goals per game for (\D+)', line) is  not None:
            name = re.match(r'Mean goals per game for (\D+)', line).group(1)
            name = name.strip()

            if name in team_dict.keys():
                print(team_dict[name].mean(), file=out)
            else:
                print(0, file=out)
        
        elif re.match(r'Score opens by (\D+)', line) is  not None:
            name = re.match(r'Score opens by (\D+)', line).group(1)
            name = name.strip()

            if name in player_dict.keys():
                print(player_dict[name].open_cnt, file=out)
            elif name in team_dict.keys():
                print(team_dict[name].open_cnt, file=out)
            else:
                print(0, file=out)
        
        elif re.match(r'Goals on minute (\d+) by (\D+)', line) is not None:
            minutes, name = re.match(r'Goals on minute (\d+) by (\D+)', line).groups()
            minutes = int(minutes.strip())
            name = name.strip()

            if name in player_dict.keys():
                print(player_dict[name].on_minutes(minutes), file=out)
            else:
                print(0, file=out)


        elif re.match(r'Goals on first (\d+) minutes by (\D+)', line) is not None:
            minutes, name = re.match(r'Goals on first (\d+) minutes by (\D+)', line).groups()
            minutes = int(minutes.strip())
            name = name.strip()

            if name in player_dict.keys():
                print(player_dict[name].first_t_minutes(minutes), file=out)
            else:
                print(0, file=out)
        
        elif re.match(r'Goals on last (\d+) minutes by (\D+)', line) is not None:
            minutes, name = re.match(r'Goals on last (\d+) minutes by (\D+)', line).groups()
            minutes = int(minutes.strip())
            name = name.strip()

            if name in player_dict.keys():
                print(player_dict[name].last_t_minutes(minutes), file=out)
            else:
                print(0, file=out)

        line = f.readline()
        
