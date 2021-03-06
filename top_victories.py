import berserk


#___________________________________________________________

token = "LICHESS API TOKEN" #Your lichess API token
user = "TCF_Namelecc".casefold() #User that you want top x wins of
variant = "rapid" #One of the below, exactly as written below
#ultraBullet "bullet "blitz rapid classical correspondence chess960 crazyhouse antichess atomic horde kingOfTheHill racingKings threeCheck
leaderboard_number = 20 #Number of top wins you want

#___________________________________________________________

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

stuff = client.games.export_by_player(user, rated = "true", perf_type = variant, moves = False) #get rid of the rated argument entirely for both casual and rated
games = list(stuff)
ratings = ""
users = ""
for game in games:
    if 'winner' in game:
        try:
        #print(game)
            player_color = "black"
            opponent_color = "white"
            if game['players']['white']['user']['id'] == user: 
                player_color = "white"
                opponent_color = "black"

            if player_color == game["winner"]:
                ratings = ratings + f"{game['players'][opponent_color]['rating']} "
                users = users + f"{game['players'][opponent_color]['user']['id']} "
        except:
            pass
rating_list = ratings.split()
user_list = users.split()
for repetition in range(len(rating_list)):
    for x in range(len(rating_list)):
        first = int(rating_list[repetition])
        if int(rating_list[x]) < first: 
            rating_list[repetition] = int(rating_list[x])
            rating_list[x] = first
            first_user = user_list[repetition]
            user_list[repetition] = user_list[x]
            user_list[x] = first_user
try:
    for x in range(leaderboard_number):
        print(f"Rating: {rating_list[x]}, User: {user_list[x]}")

except:
    pass
