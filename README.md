# practice-decision-making-strings-lists-and-methods

Introduction									
The aim of this assignment is to practice decision-making, strings, lists and methods. The use of if statements as well as string and list methods is due to the nature of the problem; that is, you cannot finish this take-home exam without using them. 

Description
The time has arrived, and a global sporting event has begun! Countries are forming their teams and participating in this prestigious tournament. Each day, there will be two matches between four teams. The team that wins the match will earn 1 point. No draws are allowed and points gained will be summed up at the end to calculate the total score of each country.

For this take-home examination, you will write a Python program that displays team stats at the end of each day by updating the scores of the winning teams. 

Your program will prompt the user for two inputs:
●	Results of the matches played within the day,
●	Global standings of countries with their respective points.
The task is simple. You will be updating the prompted scoreboard by using the match results. Each day, there will be exactly 2 matches. For each match, there will always be one winner. You will increment the corresponding winner’s scoreboard values by 1 and display the updated scoreboard.

Both inputs come with a strict template. The matches in the first input are splitted by using a comma (,) character, while the score results of matches are splitted from team names by using a semicolon (;) character. The score of the left-hand side team of the hyphen (-) is the score that appears on the left-hand side of the hyphen (-). Validity checks will be conducted to ensure that scores are entered correctly (hint: isdigit()). Your program will notify the user if any match score is entered incorrectly. If errors are found in both matches due to typos, your program will inform the user accordingly.

The second input consists of the total scores of the countries. Team batches are splitted by using commas (,) and scores are splitted from team names by using colons (:). Your program will validate whether the input scores for the winning teams are correct. It's assumed that the user correctly enters all scores but they can make mistakes in the winning teams’ scores only. The team number within the second input may vary; so you cannot make any assumptions regarding the team number. You may assume that teams from the first input will always be inside of the second input. However, team names appear case insensitively, which means the country “China” may appear as “cHina” in the first input while “CHina” in the second input. You will display the updated scoreboard as how they appear in the second input (if China appears as cHina, display it as cHina). We also assume that users cannot prompt input errors for both inputs at the same time. At each execution, there may be at most one input error in either first input or second input (if an input error exists in today’s matches, there cannot be an error in global standings and vice-versa).

Inputs
The inputs of the program and their order are explained below. It is extremely important to follow this order with the same characters since we automatically process your programs. Thus, your work will be graded as 0 unless the order is entirely correct. Please see the "Sample Runs" section for some examples. 

The prompts of the input statements to be used have to be exactly the same as the prompts of the "Sample Runs".

Here is the detailed information on the inputs and the input checks:
●	The results of the matches played within the day
Format: team1-team2;team1score-team2score,team3-team4;team3score-team4score.	
	i.e. "Argentina-Iran;77-86,Russia-South Africa;102-99."
○	Comma (",") is used to separate matches.
○	Semicolons (";") are used between team names and scores.
○	Hyphens ("-") are used to separate the information of two teams. The information to the left of the hyphen represents one team, while the information to the right represents the other team.
○	Input ends with a dot (.).
○	Your program needs to validate whether "team1score", "team2score", "team3score", and "team4score" are numbers.
○	If either "team1score" or "team2score" is not a number, an error message will be displayed indicating there is an input error for the first match (look at the sample runs 1 and 2).
○	If either "team3score" or "team4score" is not a number, an error message will be displayed indicating an input error in the second match (look at the sample run 3).
○	If both matches include a score that is not a number, an error message will be displayed indicating an input error in both matches (look at the sample run 4).
○	Team names are case insensitive (look at the sample run 6).
○	There will always be exactly two matches and there will always be exactly two winners.
○	You may assume that there won't be any duplicated team names within this input. You may also assume that the team names and scores will not contain the "-", "," and ";" characters.
○	You may check Sample Runs, for more examples. However, please keep in mind that sample runs may not cover all possible cases mentioned in this document.

●	The global scoreboard of countries with their respective points.
Format: team1:score1,team2:score2,...,teamN:scoreN.
	i.e. "ecuador:32,South Africa:42,ruSSia:40,IrAn:41,usA:40."
○	Colons (":") are used to separate team names from their scores.
○	Semicolons (",") are used to separate team batches from each other.
○	Input always ends with a dot.
○	Team names are case insensitive (look at the sample run 6).
○	If the scores of today's winning teams are not numbers, an error message will be displayed indicating which match's winner has a non-number score. If both winning teams have non-numeric scores, an error message will be displayed indicating that both match winners do not have numeric scores. (look at the sample runs 7, 8, 9)
○	You will only make the numeric validation for today's winning teams.
○	You may assume that teams that are shown in today’s matches will always be on the global scoreboard.
○	There could be teams that stand on the scoreboard but not have a match within the day in consideration.
○	You cannot make an assumption regarding the number of teams inside of the global scoreboard.
○	You will increment the winner teams’ global scores by one.



Output

If either team1score or team2score is not a number, then your program should display an error message saying "Invalid score input for match 1.". 

If either team3score or team4score is not a number, then your program should display an error message saying "Invalid score input for match 2.". 

If there are at least one input errors from both of the matches (error in team1score or team2score for the first match and  error in team3score or team4score for the second match), then your program should display an error message saying "Invalid score input for both matches.".

If the global score of the first match’s winner is not a number, then your program should display an error message saying "Invalid scoreboard entry for match 1's winner: match1winnerscore", where "match1winnerscore" is the value that is written incorrectly for the first match’s winner in global scoreboard.

If the global score of the second match’s winner is not a number, then your program should display an error message saying "Invalid scoreboard entry for match 2's winner: match2winnerscore", where "match2winnerscore" is the value that is written incorrectly for the second match’s winner in global scoreboard.

If the global score of the both matches’ winners are not numbers, then your program should display an error message saying "Invalid scoreboard entry for both matches' winners.".

If both of the inputs pass from validations, your program should print the following output: "Updated scoreboard after today's matches: team1:score1,...teamN:scoreN". Note that, you need to increment winning teams scores by one, and display the global scoreboard as it is.

You may check the "Sample Runs" section given below for some examples.




Sample Runs
Below, we provide some sample runs of the program that you will develop. The italic and bold phrases are inputs taken from the user. You have to display the required information in the same order and with the same words and characters as below. 

Sample Run 1 
Please enter today's match results: China-Germany;47atav-24,Brazil-Norway;32-5.
Please enter the scoreboard: China:9,Germany:8,Japan:12,Brazil:9,Norway:10.
Invalid score input for match 1.

Sample Run 2
Please enter today's match results: China-Germany;47-jska28d,Brazil-Norway;32-5.
Please enter the scoreboard: China:9,Germany:8,Japan:12,Brazil:9,Norway:10.
Invalid score input for match 1.

Sample Run 3
Please enter today's match results: China-Germany;47-24,Brazil-Norway;hruwe-5.
Please enter the scoreboard: China:9,Germany:8,Japan:12,Brazil:9,Norway:10.
Invalid score input for match 2.

Sample Run 4
Please enter today's match results: China-Germany;47atav-24,Brazil-Norway;32-qweı42.
Please enter the scoreboard: China:9,Germany:8,Japan:12,Brazil:9,Norway:10.
Invalid score input for both matches.

Sample Run 5
Please enter today's match results: China-Germany;47-24,Brazil-Norway;32-42.
Please enter the scoreboard: China:9,Germany:8,Japan:12,Brazil:9,Norway:10.
Updated scoreboard after today's matches: China:10,Germany:8,Japan:12,Brazil:9,Norway:11.

Sample Run 6
Please enter today's match results: Argentina-IRAn;77-86,RUssia-South Africa;102-99.
Please enter the scoreboard: ecuador:32,South Africa:42,ruSSia:40,IrAn:41,usA:40,Argentina:43.
Updated scoreboard after today's matches: ecuador:32,South Africa:42,ruSSia:41,IrAn:42,usA:40,Argentina:43.

Sample Run 7
Please enter today's match results: Argentina-Iran;77-86,Russia-South Africa;102-99.
Please enter the scoreboard: Ecuador:32,South Africa:42,Russia:4aa0,Iran:41,USA:40,Argentina:43.
Invalid scoreboard entry for match 2's winner: 4aa0.

Sample Run 8
Please enter today's match results: Argentina-Iran;77-86,Russia-South Africa;102-99.
Please enter the scoreboard: Ecuador:32,South Africa:42,Russia:40,Iran:kweraCDW,USA:40,Argentina:43.
Invalid scoreboard entry for match 1's winner: kweraCDW.

Sample Run 9
Please enter today's match results: Argentina-Iran;77-86,Russia-South Africa;102-99.
Please enter the scoreboard: Ecuador:32,South Africa:42,Russia:4aa0,Iran:kweraCDW,USA:40,Argentina:43.
Invalid scoreboard entry for both matches' winners.
