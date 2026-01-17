
class NFA: 
    def __init__(self,states,alphabet,transition_function,start_state,accept_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.start_state = start_state
        self.accept_states = set(accept_states)

        if self.start_state not in self.states:
            raise ValueError("Start state is not in all states")
        
        if not self.accept_states.issubset(self.states):
            raise ValueError("Accept state is not in all states")
        
        self.transition_function = {}
        
        for state in self.states:
            self.transition_function[state]={}

        for src, transitions in transition_function.items():
            if src not in self.states:
                raise ValueError(f"Unknown state in transitions: {src}")
        
            for symbol, dests in transitions.items():
                if symbol is not None and symbol not in self.alphabet:
                    raise ValueError(f"Incorrect symbol {symbol}")

                dests = set(dests)
                if not dests.issubset(self.states):
                    raise ValueError(f"Transition to unknown states {dests}")
                
                self.transition_function[src][symbol] = dests

states = {0, 1}
alphabet = {"a", "b"}
start_state = 0
accept_states = {1}

transition_function = {
    0: {
        None: {1},   # epsilon
        "a": {0}
    },
    1: {
        "b": {1}
    }
}

nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

print("NFA constructed successfully!")
print("States:", nfa.states)
print("Start:", nfa.start_state)
print("Accepts:", nfa.accept_states)
print("Transitions:", nfa.transition_function)

  