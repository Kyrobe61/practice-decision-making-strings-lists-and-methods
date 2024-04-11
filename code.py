# 1 - input today's match results and list them

match_results = input("Please enter today's match results: ").lower()

match_results = match_results.replace("-", ",")
match_results = match_results.replace(";", ",")
match_results = match_results.replace(".", "")
match_results = match_results.split(",")

score_1 = str(match_results[2])
score_2 = str(match_results[3])
score_3 = str(match_results[6])
score_4 = str(match_results[7])

# initial match results = Argentina-IRAn;77-86,RUssia-South Africa;102-99.
# final match results = ['argentina', 'iran', '77', '86', 'russia', 'south africa', '102', '99']
#                             0          1      2     3       4          5            6      7
# ----------------------------------------------------------------------------------------------------------------------------------

# 2 - input scoreboard

i_scoreboard = input("Please enter the scoreboard: ")

# ----------------------------------------------------------------------------------------------------------------------------------
# 3 - check valid entry for match results

if (not score_3.isdigit() or not score_4.isdigit()) and (not score_1.isdigit() or not score_2.isdigit()):
  print("Invalid score input for both matches.")

elif not score_3.isdigit() or not score_4.isdigit():
  print("Invalid score input for match 2.")

elif not score_1.isdigit() or not score_2.isdigit():
  print("Invalid score input for match 1.")

else:

# ----------------------------------------------------------------------------------------------------------------------------------
# 4 - determine the winner

      if int(score_1) > int(score_2):
          winner_1 = match_results[0]

      elif int(score_1) < int(score_2):
          winner_1 = match_results[1]

      if int(score_3) > int(score_4):
          winner_2 = match_results[4]

      elif int(score_3) < int(score_4):
          winner_2 = match_results[5]

# ----------------------------------------------------------------------------------------------------------------------------------
# 5 - find their scores in scoreboard

      i_scoreboard = i_scoreboard.replace(".", ",")

      winner_idx_1 = ("," + i_scoreboard).lower().find("," + winner_1 +":")
      colon_idx_1 = i_scoreboard.find(":", winner_idx_1)
      comma_idx_1 = i_scoreboard.find(",", colon_idx_1)
      scor_1_str = i_scoreboard[colon_idx_1 + 1 : comma_idx_1]
      
      winner_idx_2 = ("," + i_scoreboard).lower().find("," + winner_2 +":")
      colon_idx_2 = i_scoreboard.find(":", winner_idx_2)
      comma_idx_2 = i_scoreboard.find(",", colon_idx_2)
      scor_2_str = i_scoreboard[colon_idx_2 + 1 : comma_idx_2]

# ----------------------------------------------------------------------------------------------------------------------------------
# 6 - check valid entry for scoreboard

      if not str(scor_1_str).isdigit() and not str(scor_2_str).isdigit():
          print("Invalid scoreboard entry for both matches' winners.")

      elif not str(scor_1_str).isdigit():
          print("Invalid scoreboard entry for match 1's winner: ", str(scor_1_str), ".", sep="")

      elif not str(scor_2_str).isdigit():
          print("Invalid scoreboard entry for match 2's winner: ", str(scor_2_str), ".", sep="")

      else: 

# ----------------------------------------------------------------------------------------------------------------------------------
# 7 - increment their scores in scoreboard     
          winner_2_score = int(scor_2_str) + 1
          i_scoreboard = i_scoreboard[:colon_idx_2 + 1] + str(winner_2_score) + i_scoreboard[comma_idx_2:]

          winner_1_score = int(scor_1_str) + 1
          i_scoreboard = i_scoreboard[:colon_idx_1 + 1] + str(winner_1_score) + i_scoreboard[comma_idx_1:]

          i_scoreboard = i_scoreboard[:-1]
          i_scoreboard = i_scoreboard + "."

# ----------------------------------------------------------------------------------------------------------------------------------
# 8 - print the updated scoreboard

          print("Updated scoreboard after today's matches: ", i_scoreboard, sep="")
