import os
import time
from datetime import datetime, timedelta

# Function to simulate a commit for a specific date
def make_commit(commit_date: str):
    # Write the commit information to 'data.txt'
    with open('data.txt', 'a') as file:
        file.write(f'{commit_date} - Commit\n')

    # Stage the file for committing
    print(f"Staging commit for {commit_date}...")
    os.system('git add .')

    # Commit the change with a custom message that includes the commit date
    commit_message = f"Commit on {commit_date}"
    commit_command = f'git commit --date="{commit_date}" -m "{commit_message}"'
    print(f"Committing: {commit_message}...")
    os.system(commit_command)

# Function to make commits from 2008 to 2024 (1 commit per day)
def make_commits_for_years():
    # Start date: January 1, 2008
    start_date = datetime(2008, 1, 1)
    
    # End date: December 31, 2024
    end_date = datetime(2024, 12, 31)
    
    # Loop over each day from start_date to end_date
    current_date = start_date
    day_num = 1

    while current_date <= end_date:
        # Format the commit date to match Git's expected format
        commit_date = current_date.strftime('%a %b %d %H:%M:%S %Y %z')

        # Make a commit for this day
        print(f"Processing day {day_num} ({commit_date})...")
        make_commit(commit_date)

        # Perform a Git pull to ensure we are up-to-date (optional, if you're pushing to a remote)
        print("Pulling changes from the remote repository...")
        os.system('git pull origin main')

        # Push the changes after each commit
        print("Pushing changes to the remote repository...")
        os.system('git push origin main')

        # Move to the next day
        current_date += timedelta(days=1)
        day_num += 1

# Start the process for commits from 2008 to 2024
make_commits_for_years()
