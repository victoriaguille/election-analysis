# Election Analysis
## Project Overview
#### 
Two employees of the Colorado Board of Elections have been tasked with performing an election audit of a recent local congressional election using Python 3.6.1 and Visual Studio Code, 1.38.1. While performing the election audit, the election commission requires the results to be broken down into a simple report with the results displayed by both candidates and counties. The election results data, stored in a CSV file, are much too large and cumbersome for any one person to go through by hand, resulting in the need for Python. The Python code, being written and run in Visual Studio Code, is then used to pull the necessary information using lines of code. This method made going through the original CSV file with the election results possible. Using the new lines of Python code, we are able to print the audit results to the terminal and save them to a text file. 

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
#### 
The shared Python code for this particular audit is relatively simple and straightforward. Creating needed variables pushes the code forward into several with, for, and if statements. Each statement either builds upon itself or creates new ways to break down the results in a readable and useful format for the audit from a long string of names and counties provided in the CSV file. Taking the information from the CSV file, the Python code is then written to write the output of the for/with/if statements onto a text file. Each nested statement allows for code that can be used for both large or small samples, the only thing needing to change would be the opening of a specific file path at the beginning of the code. 
### Proposal for Additional Changes
#### 
In this particular audit, the main emphais was on who won the election. However, depending on the purpose of looking at this election data or any others, it may be of use to look at who lost or which county had the lowest turnout. The Python code that has been shared is written to pull the winning stats from the CSV file, with variables such as "winning_county" and "winning_count." If members of the election commission wanted to know which county had the lowest turnout of those that voted, it would be as simple as adding a variable and performing a "minimum" function. In the below example, the variable "losing_county" has been added along with removing any code attempting to find the winning county. Beneath the for loop used to gather the county election results, a simple line stating "losing_county = min(county_votes)" has been added. This function pulls the minimum number amongst the county votes, in turn finding the county with the lowest turn out. 
#### ![variable image](https://github.com/victoriaguille/election-analysis/blob/main/resources/losing_county_variable.png)
#### ![losing county code](https://github.com/victoriaguille/election-analysis/blob/main/resources/losing_county_code.png)
#### 
If the election commission would like to see this change printed to the text file meant to record the audit results, one would need to replace the "largest_county_turnout" with a new print and txt_file.write statement. A quick and efficient way to do so would be to use "lowest_county_turnout" as the variable name and then slowly replace anything regarding a "winning" statement with the new "losing_county" line. It is best not to forget to make corresponding changes to the text file display portion. Below are these print outs and changes performed in Visual Studio Code. 
#### ![losing code](https://github.com/victoriaguille/election-analysis/blob/main/resources/smallest_county_print_code.png)
#### ![print out](https://github.com/victoriaguille/election-analysis/blob/main/resources/smallest_county_interactive_display.png)
#### 
Overall, the structure of the Python code is solid and would require very few changes if it were to be used for larger elections as the code itself is set up to create and add to pre-defined lists. If there were any changes needed to be made, it would not be difficult as, again, much of the Python code is built around not knowing the exact values or range of values from a CSV file. This Python code could potentially be used as is or with minimal refactoring for quite some time if it is being used for the sole purpose of election audits. 

