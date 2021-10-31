# Election Analysis
## Project Overview
#### Two employees of the Colorado Board of Elections have been tasked with performing an election audit of a recent local congressional election using Python 3.6.1 and Visual Studio Code, 1.38.1. While performing the election audit, the election commission requires the results to be broken down into a simple report with the results displayed by both candidates and counties. The election results data, stored in a text file, are much too large and cumbersome for any one person to go through by hand, resulting in the need for Python. The Python code, being written and run in Visual Studio Code, is then used to pull the necessary information using lines of code. This method made going through the original CSV file with the election results possible. Using the new lines of Python code, we are able to print the audit results to the terminal and save them to a text file. 

## Election Audit Results 
#### Below are the following findings from the audit. 
    - There were 369,711 votes cast in the elections. 
    -The counties involved in the election results were:
        - Arapahoe
        - Jefferson
        - Denver
    - Denver county had the largest turnout with 82.8% of the vote and 306,055 number of votes. 
    - The candidates up for election were: 
        - Charles Casper Stockham
        - Diana DeGette
        - Raymon Anthony Doane
    - The winner of the election was: 
        - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 
        
## Election Audit Summary
#### The shared Python code for this particular audit is relatively simple and straightforward. Creating needed variables pushes the code forward into several with, for, and if statements. Each statement either builds upon itself or creates new ways to break down the results in a readable and useful format for the audit from a long string of names and counties provided in a CSV file. Each nested statement allows for a code that can be used for both large or small samples, the only thing needing to change would be the opening of a specific file path at the beginning of the code. 
### Proposal for Additional Changes
#### In this particular audit, the main emphais was on who won the election. However, depending on the purpose of looking at this election data or any others, it may be of use to look at who lost or which county had the lowest turnout. The Python code that has been shared is written to pull the winning stats from the CSV file, with variables such as "winning_candidate" and "winning_percentage."

can be used for both small elections and large elections. can keep same variables, just add new csv file. if want to track other variables, simply plug them in such as losing candidate instead of the winner. 

(insert example screenshots of changes)
