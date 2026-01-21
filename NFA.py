class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.start_state = start_state
        self.accept_states = set(accept_states)

        if self.start_state not in self.states:
            raise ValueError("Start state is not in all states")

        if not self.accept_states.issubset(self.states):
            raise ValueError("Accept state is not in all states")

        self.transition_function = {state: {} for state in self.states}

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

    def _epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            for nxt in self.transition_function.get(state, {}).get(None, set()):
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)

        return closure

    def accepts(self, word):
        for ch in word:
            if ch not in self.alphabet:
                return False

        current_states = self._epsilon_closure({self.start_state})

        for symbol in word:
            next_states = set()
            for state in current_states:
                next_states |= self.transition_function.get(state, {}).get(symbol, set())
            current_states = self._epsilon_closure(next_states)

            if not current_states:
                return False

        return bool(current_states & self.accept_states)

    def union(self, other):
        if self.alphabet != other.alphabet:
            raise ValueError("Alphabets must be identical for union")

        offset = max(self.states) + 1

        def rename_states(states, delta):
            return {s + delta for s in states}

        def rename_transitions(tf, delta):
            new_tf = {}
            for src, transitions in tf.items():
                new_tf[src + delta] = {}
                for symbol, dests in transitions.items():
                    new_tf[src + delta][symbol] = {d + delta for d in dests}
            return new_tf

        states1 = set(self.states)
        tf1 = self.transition_function
        start1 = self.start_state
        accepts1 = set(self.accept_states)

        states2 = rename_states(other.states, offset)
        tf2 = rename_transitions(other.transition_function, offset)
        start2 = other.start_state + offset
        accepts2 = rename_states(other.accept_states, offset)

        new_start = max(states2) + 1
        new_states = states1 | states2 | {new_start}
        new_accepts = accepts1 | accepts2

        new_tf = {s: {} for s in new_states}

        for s, trans in tf1.items():
            new_tf[s].update(trans)

        for s, trans in tf2.items():
            new_tf[s].update(trans)

        new_tf[new_start][None] = {start1, start2}

        return NFA(
            states=new_states,
            alphabet=set(self.alphabet),
            transition_function=new_tf,
            start_state=new_start,
            accept_states=new_accepts
        )


if __name__ == "__main__":
    states1 = {0, 1}
    alphabet = {"a", "b"}
    start1 = 0
    accept1 = {1}
    tf1 = {
        0: {None: {1}, "a": {0}},
        1: {"b": {1}},
    }

    nfa1 = NFA(states1, alphabet, tf1, start1, accept1)

    print("NFA1")
    print(nfa1.accepts(""))
    print(nfa1.accepts("a"))
    print(nfa1.accepts("aa"))
    print(nfa1.accepts("b"))
    print(nfa1.accepts("bbb"))
    print(nfa1.accepts("aabbb"))
    print(nfa1.accepts("ba"))
    print(nfa1.accepts("abba"))

    states2 = {0, 1}
    start2 = 0
    accept2 = {1}
    tf2 = {
        0: {"a": {1}},
        1: {"a": {1}},
    }

    nfa2 = NFA(states2, alphabet, tf2, start2, accept2)

    u = nfa1.union(nfa2)

    print("UNION")
    print(u.accepts(""))
    print(u.accepts("a"))
    print(u.accepts("aa"))
    print(u.accepts("b"))
    print(u.accepts("bbb"))
    print(u.accepts("ba"))
    print(u.accepts("abba"))
