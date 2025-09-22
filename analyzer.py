# analyzer.py
import csv

def get_summary(tickets):
    total_tickets = len(tickets)
    total_resolution = 0
    total_satisfaction = 0

    for ticket in tickets:
        total_resolution += float(ticket['resolution_hours'])

    for ticket in tickets:
        total_satisfaction += float(ticket['satisfaction'])

    if total_tickets > 0:
        avg_resolution = total_resolution / total_tickets
        avg_satisfaction = total_satisfaction / total_tickets
    else:
        avg_resolution = 0
        avg_satisfaction = 0
    
    return total_tickets, avg_resolution, avg_satisfaction

def analyze_categories(tickets):
    category_data = {}

    for ticket in tickets:
        cat = ticket['category']
        if cat not in category_data:
            category_data[cat] = {'count': 0, 'res_sum': 0, 'sat_sum': 0}
        category_data[cat]['count'] += 1
    
    for ticket in tickets:
        cat = ticket['category']
        category_data[cat]['res_sum'] += float(ticket['resolution_hours'])
        
    for ticket in tickets:
        cat = ticket['category']
        category_data[cat]['sat_sum'] += float(ticket['satisfaction'])

    analysis = {}
    for cat, data in category_data.items():
        count = data['count']
        if count > 0:
            avg_res = data['res_sum'] / count
            avg_sat = data['sat_sum'] / count
        else:
            avg_res = 0
            avg_sat = 0

        analysis[cat] = {
            'num_tickets': count,
            'avg_resolution': avg_res,
            'avg_satisfaction': avg_sat,
        }
    return analysis

def analyze_agents(tickets):
    agent_data = {}

    for ticket in tickets:
        agent = ticket['agent']
        if agent not in agent_data:
            agent_data[agent] = {'count': 0, 'res_sum': 0, 'sat_sum': 0}
        agent_data[agent]['count'] += 1
            
    for ticket in tickets:
        agent = ticket['agent']
        agent_data[agent]['res_sum'] += float(ticket['resolution_hours'])

    for ticket in tickets:
        agent = ticket['agent']
        agent_data[agent]['sat_sum'] += float(ticket['satisfaction'])

    analysis = {}
    for agent, data in agent_data.items():
        count = data['count']
        if count > 0:
            avg_res = data['res_sum'] / count
            avg_sat = data['sat_sum'] / count
        else:
            avg_res = 0
            avg_sat = 0

        analysis[agent] = {
            'num_tickets': count,
            'avg_resolution': avg_res,
            'avg_satisfaction': avg_sat,
        }
    return analysis

with open('tickets.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    tickets_data = list(reader)

total, avg_res, avg_sat = get_summary(tickets_data)
print(f"Total Tickets: {total}")
print(f"Average Resolution: {avg_res:.1f} hours")
print(f"Average Satisfaction: {avg_sat:.1f}/5\n")

category_stats = analyze_categories(tickets_data)
print("Categories:")
for category, stats in category_stats.items():
    print(
        f"{category}: {stats['num_tickets']} tickets, "
        f"{stats['avg_resolution']:.1f}h avg, "
        f"{stats['avg_satisfaction']:.1f}/5"
    )

print()

agent_stats = analyze_agents(tickets_data)
print("Agents:")
for agent, stats in agent_stats.items():
    print(
        f"{agent}: {stats['num_tickets']} tickets, "
        f"{stats['avg_resolution']:.1f}h avg, "
        f"{stats['avg_satisfaction']:.1f}/5"
    )
