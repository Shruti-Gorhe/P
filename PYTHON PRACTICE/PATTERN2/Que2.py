# Call Center
# Problem Description
# A call center records the number of calls handled by different agents. The program should store the total number of calls handled by each agent and identify the agent with the highest number of calls.

# Function 1
# Function Name: record_calls

# Parameters:
# agent_name, calls, callboard

# Requirements:
# Convert the agent name to uppercase before storing it.
# If calls <= 0, do not add the calls to the dictionary.
# If the agent already exists in the dictionary, add the new calls to the agent's existing calls.
# If the agent does not exist, create a new entry.
# Return the updated dictionary.

# Function 2

# Function Name: find_top_agent
# Parameter:
# callboard

# Requirements:
# Return the agent who has handled the highest number of calls.
# If the dictionary is empty, return:
# ("", 0)
# If two or more agents have the same maximum number of calls, the first inserted agent wins.

def record_calls(agent_name, calls, callboard):
    agent_name = agent_name.upper()
    if calls <= 0:
        return callboard
    if agent_name in callboard:
        callboard[agent_name] += calls
    else:
        callboard[agent_name] = calls
    return callboard

def find_top_agent(callboard):
    if not callboard:
        return ("", 0)
    top_agent = max(callboard, key=callboard.get)
    return top_agent, callboard[top_agent]

def main():
    callboard = {}

    n = int(input("Enter number of agents: "))

    print("Enter agent calls:")

    for i in range(n):
        name = input("Enter agent name: ")
        calls = int(input(f"Enter {name}'s calls: "))

        callboard = record_calls(name, calls, callboard)

    print("\nCall Summary:")

    for name, calls in callboard.items():
        print(f"{name}:{calls}")

    name, calls = find_top_agent(callboard)

    print("\nTop Agent")
    print(f"{name}:{calls}")


if __name__ == "__main__":
    main()