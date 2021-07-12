# Best-Victories
Some people want to see more than just their top 5 victories in a variant (https://lichess.org/forum/lichess-feedback/best-rated-victories-2), so this is the code that enables you to do so

**How to Set Up**

1. Get a Lichess API Access token by following the directions here https://lichess.org/account/oauth/token
2. In order to use berserk, lichess's python API client, install it: https://berserk.readthedocs.io/en/master/installation.html. This code is going to require python, so you might as well get python installed on your computer and get an editor (such as Visual Study Code) as well. 
3. Put the code into the python editor
4. A part of the code is enclosed by commented out lines... this is the stuff you are going to want to fill out
5. First, put your API access token where the token variable is defined
6. Now put the user you want a top-x victories list from in the user variable
7. Enter the name of the variant into the variable variable. Must be one of the following (written exactly as they are here): ultraBullet bullet blitz rapid classical correspondence chess960 crazyhouse antichess atomic horde kingOfTheHill racingKings threeCheck
8. Enter the number of top wins you want into the leaderboard_number variable 
9. Run the code... if things go wrong, please make an issue!
10. This does take some time as exporting is throttled, so depending on the number of games you have in any given variant, this process could take a while (from a few minutes to an hour or so if you have a ton of games like say german11
