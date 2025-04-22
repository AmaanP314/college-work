import heapq

def beam_search(initial_state, expand_fn, beam_width, max_steps):
    """
    Performs beam search.
    
    Args:
        initial_state: The starting state (could be a list, a string, etc.)
        expand_fn: A function that generates possible next states and their scores given a current state.
                   It should return a list of (state, score) tuples.
        beam_width: The number of top candidates to keep at each step.
        max_steps: The maximum number of steps to search.
        
    Returns:
        A list of the best sequences found.
    """
    # Priority queue to store the states with their cumulative scores
    beams = [(0, initial_state)]  # (score, state)
    
    for step in range(max_steps):
        # Temporary list to hold new beams for the next step
        next_beams = []
        
        # Expand all current beams
        for score, state in beams:
            expansions = expand_fn(state)
            
            # Add all expanded states to the next_beams
            for new_state, new_score in expansions:
                heapq.heappush(next_beams, (score + new_score, new_state))
        
        # Sort by score and keep the top `beam_width` beams
        beams = heapq.nlargest(beam_width, next_beams, key=lambda x: x[0])
    
    # Return the top beam
    return beams

# Example expand function: Adds one character at a time and assigns a random score
import random

def example_expand_fn(state):
    # Randomly expand the state by adding one of 'A', 'B', 'C'
    return [(state + char, random.uniform(0, 1)) for char in 'ABC']

# Example usage
initial_state = ""
beam_width = 3
max_steps = 5
best_sequences = beam_search(initial_state, example_expand_fn, beam_width, max_steps)

print("Best sequences:")
for score, sequence in best_sequences:
    print(f"Score: {score:.4f}, Sequence: {sequence}")

'''
Sure! Let's break it down:

### What is Beam Search?
Beam search is a search algorithm that tries to find the best possible solution by exploring multiple possibilities in parallel, but in a controlled way. It's like trying to find the best path in a maze, but instead of exploring all paths at once (which would be too slow), you only explore a limited number of the best paths at each step.

### Key Ideas:
1. **Exploration in Parallel**: At each step, you generate multiple possible next steps (paths) instead of just one. But you don't explore *all* of them—just the most promising ones.
  
2. **Beam Width**: This controls how many of the best paths you keep at each step. So, if you have a beam width of 3, you only keep the top 3 paths based on how good they are at each stage.

3. **Evaluation**: Each path (or sequence of choices) gets a score based on how good it is. The algorithm uses this score to decide which paths are worth continuing and which ones to ignore.

### Analogy:
Imagine you're trying to find the shortest route from point A to point B on a map. Instead of checking every single possible route (which could be too many), you decide to only check the best 3 routes at each decision point. You keep expanding the most promising 3 routes until you reach your destination.

### Example: 
Let's say you're trying to generate a sentence in a language model (like how Google Translate works). At each word, the model could generate several possible next words. Instead of checking all possible sentences, beam search keeps only the top "k" best possible partial sentences at each step. It will continue until it finishes the sentence or reaches a limit (like the number of words).

### Steps in Beam Search:
1. **Start** with the initial state (like an empty sentence or starting point).
2. **Expand** the state by looking at all possible next steps.
3. **Rank** those next steps based on how good they are (usually using some kind of scoring function).
4. **Keep the best** 'k' next steps (this is called the *beam width*).
5. Repeat until you reach a final state, like a completed sentence or a solution.

### Why Use Beam Search?
- It helps avoid checking every possible solution (which would take too long, especially in large search spaces).
- It’s much faster than exhaustive search (which looks at everything), while still being fairly good at finding high-quality solutions.

### A Simple Example in Words:
Let’s say you’re building a sentence starting with "I want to...". The model could generate several options for the next word like:
- "I want to eat"
- "I want to sleep"
- "I want to play"
- "I want to sing"

Instead of continuing with every single option, you choose the top few, say "I want to eat" and "I want to sleep" (based on some scoring). Then, from those options, you expand again, generating possible continuations for each phrase. This process continues, always keeping the best few options at each step.

### In Summary:
Beam search is a way to find good solutions more efficiently by only exploring a limited number of the most promising possibilities at each step.
'''
