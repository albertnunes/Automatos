def get_transition(transition_string):
    transition = transition_string.strip().split("|")
    return (int(transition[0]), transition[1], int(transition[2]))

def get_transitions(transition_lines):
    return [get_transition(transition_line) for transition_line in transition_lines]

def simulate_dfa(initial_state, final_states, transitions, word):
    current_state = initial_state
    for char in word:
        next_state = None
        for transition in transitions:
            if transition[0] == current_state and transition[1] == char:
                next_state = transition[2]
                break
        if next_state is None:
            return 0
        current_state = next_state
    return 1 if current_state in final_states else 0

def main():
    with open("dfa.txt", "r") as file:
        lines = file.readlines()
        initial_state = int(lines[0].strip())
        final_states = [int(state) for state in lines[1].strip().split(",")]
        transitions = get_transitions(lines[2:])

    with open("words.txt", "r") as file:
        words = file.readlines()

    with open("results.txt", "w") as file:
        for word in words:
            result = simulate_dfa(initial_state, final_states, transitions, word.strip())
            file.write(str(result) + "\n")

if _name_ == "_main_":
    main()