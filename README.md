# Python Intern Assignment

**Time:** 60 minutes

⚠️ **Important:** Use of AI tools (ChatGPT, GitHub Copilot, etc.) is not allowed for this exercise

## Task
Create a Python script that analyses customer support ticket data.

## What You Get
- `tickets.csv` file with columns: ticket_id, category, priority, resolution_hours, satisfaction, agent

## What You Build
Create `analyzer.py` with three functions:

### Function 1: Basic Stats
```python
def get_summary():
    # Calculate and return:
    # - Total number of tickets
    # - Average resolution time
    # - Average satisfaction score
```

### Function 2: Category Analysis  
```python
def analyze_categories():
    # For each category (Technical, Billing, Account), return:
    # - Number of tickets
    # - Average resolution time
    # - Average satisfaction score
```

### Function 3: Agent Performance
```python
def analyze_agents():
    # For each agent, return:
    # - Number of tickets handled
    # - Average resolution time
    # - Average satisfaction score
```

## Expected Output
```
Total Tickets: 95
Average Resolution: 12.5 hours
Average Satisfaction: 3.8/5

Categories:
Technical: 32 tickets, 18.2h avg, 3.4/5
Billing: 25 tickets, 7.1h avg, 4.2/5  
Account: 38 tickets, 11.8h avg, 3.9/5

Agents:
Alice: 28 tickets, 14.1h avg, 4.0/5
Bob: 35 tickets, 11.8h avg, 3.7/5
Carol: 32 tickets, 12.0h avg, 3.8/5
```

## Submit
Fork this repo and share the forked repo URL at hello@digilake.io

**Requirements:**
1. Working `analyzer.py` file
2. Simple README with usage instructions  
3. Push to GitHub

> **Note:** Please maintain a git history so that we can analyse how the solution was evolved  
> For any question/doubt, please reach out to hello@digilake.io  
> **Bonus:** Follow code quality best practices (linting, formatting, type hints) and set up GitHub Actions to automatically check code quality (extra credit)

That's it! Keep it simple and focus on getting it working.
