# ESPN-Data-Scraping
#Collecting Cricket World Cup Data for 2019

#Group 7 :
12020067	Sayantika Banik	
12020015	Mohua Sinha	
12020044	Supriya Maheshwari	

#Part 1:
From this page: https://www.espncricinfo.com/series/icc-cricket-world-cup-2019-1144415/match-results,
we have scraped the following information:

1. Match number
2. Location
3. Date
4. Winning country
5. Other country
6. Match result
7. Score by winning country
8. Score by other country
9. Link to match report
10. Link to match summary
11. Link to match scorecard

# This is a combined code of Selenium and Beautiful Soup.


#Part 2:
For each match, we have visited each of the scorecard link like 
https://www.espncricinfo.com/series/icc-cricket-world-cup-2019-1144415/india-vs-new-zealand-1st-semi-final-1144528/full-scorecard 
and extracted the following fields:

1. Player of the match with the picture. Save the url to the picture in the tsv.
2. Country that the player of the match belongs to.
3. Runs scored by every batsman. 
4. Balls played by every batsman.
5. Strike rate for every batsman.
6. Wickets taken by every bowler.
7. Economy rate for every bowler.
8. which country won the toss.
9. who were the umpires?
10. who was the match referee


# This is a combined code of Scrapy and Selenium.
All the fields are fetched using scrapy but we faced issue of getting "Lazyimage" for the picture of the player_of_match. To meet that , selenium code is appended.
The missing values in Scrapy are fetched as blanks.
The files are named as group7_matchDetails.py ,group7_matchDetails.tsv and settings.py


##Part 3:

For each player across all matches using the player page 
like https://www.espncricinfo.com/newzealand/content/player/506612.html) 
extracted the following:

1. Full name of player.
2. Date and place of birth.
3. Current age.
4. Major teams.
5. Playing role.
5. Batting style.
6. Bowling style.
7. Highest ODI batting score.
8. ODI debut information.
9. Profile information.
10. Pic of the player. Save the url of the image in the tsv. 
11. Country of the player.

The files are named as group7_playerDetails.py ,group7_playerDetails.tsv and settings.py

#Settings File Details

We are fetching the output files as tsv files.
Also, we have set ROBOTSTXT_OBEY = False to obey robots.txt rules