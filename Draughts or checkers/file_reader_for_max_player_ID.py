players_list = [0]
with open("players.txt", 'r') as file:
    rows = file.readlines()
    for row  in rows:
        row = str(row).replace('\n', '').replace('', '0')
        players_list.append(int(row))
max_player_id = (max(players_list))
