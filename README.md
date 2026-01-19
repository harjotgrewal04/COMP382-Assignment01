# **COMP382-Assignment01**
## **Team Members: Darius, Harjot**

---

### **1. Project Overview**
This project implements a NFA class which includes a memeber function and will perform the operation of a union with another NFA. The program will be able to check the input given to recognize the string in the language. The NFA class created includes the represnted states,alphabets,transition functions and the start & accept states. Using multiple test cases the functinality and correctness of the implementations are verified. 

---

### **2. Non-Deterministic Finite Automaton**

#### **2.1 Finite Automaton**
Finite Automan are machines which determine if a string is apart of some language. Based upon input of symbols or characters which are given to the machine it wil processe each one step-by-step. If the input leaves the machine in an accepting state then the input is accepted whereas if it is any other state it will be rejected. 

Finite Automaton is configured of a 5-tuple notation:
  - Q is the finite set of states
  - Σ is a finite set of alphabet
  - δ is the transition function defined by δ: Q x Σ --> Q
  - q₀ is the assigned start state
  - F ⊆ Q is the set of accept states which must belong to the set of all states

#### **2.2 Types of Finite Automata **
- There are two main types of finite automate which include deterministic Finite Automata (DFA) and Non-Deterministic Finite Automata (NFA). This project is based upon NFA.

DFA:
  - For each input symbol there can only be one transition state
  - There are no null transitions
  - All DFA are NFA

NFA:
  - For each input symbol there can be multiple transition states
  - Will allow for null moves (ε) meaning the machine can change states without taking in any input.
  - Not all NFAs are equal to DFAs

---

### **3. References**
- GeeksforGeeks. (2020, May 16). Difference between DFA and NFA. GeeksforGeeks. https://www.geeksforgeeks.org/theory-of-computation/difference-between-dfa-and-nfa/
- Finite Automata Part One. (n.d.). https://web.stanford.edu/class/archive/cs/cs103/cs103.1184/lectures/14/Small14.pdf
‌- Campbell, R. (2026). Sec 1.1 Finite Automata Lecture slides COMP-382-ON1: Language, Computation and Machines. University of the Fraser Valley
- Campbell, R. (2026). Sec 1.2 Nondeterminism Lecture slides COMP-382-ON1: Language, Computation and Machines. University of the Fraser Valley
