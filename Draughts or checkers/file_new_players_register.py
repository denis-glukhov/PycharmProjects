from file_reader_for_max_player_ID import max_player_id

id = int(max_player_id)+1

with open("players.txt", 'a') as file:
    file.write('\n'+str(id))
print (id)