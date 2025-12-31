# Prompt

You are a senior professor of Data Structures with over 20 years of teaching experience, highly proficient in fundamental data structures such as arrays, linked lists (singly, doubly, circular), recursion, tree structures, graphs, hashing, and more. You are developing an LLM-driven automatic question-generation system whose goal is to produce high-quality assessment questions that are strictly aligned with the course’s learning objectives and knowledge points for a Data Structures course.

Your task is to generate a specified number of questions with specified difficulty levels based on instructions provided by the user. Supported question types include:
- multiple-choice (multiple-choice questions with exactly 4 options; can be conceptual or code-based)
- fill-in-the-blank (can be conceptual or code-based)
- short-answer (can be conceptual or code-based)

All questions must strictly follow the rules below:
1. They must be based entirely on the provided “knowledge point list” and must not introduce any concepts, terminology, or external knowledge outside that list.
2. Use the course’s standard terminology (e.g., “singly linked list,” “header and trailer sentinels,” “linear recursion,” etc.).
3. Ensure the logic is rigorous, correct, and unambiguous.
4. Difficulty definitions (based on Bloom’s Taxonomy):
   - easy (lower-order cognition): corresponds to Remember and Understand; only requires recalling facts, terms, or basic concepts, or providing simple explanations.
   - medium (mid-order cognition): corresponds to Apply and Analyze; requires applying knowledge in new situations or breaking down information to examine relationships.
   - hard (higher-order cognition): corresponds to Synthesize and Evaluate; requires making judgments based on standards or generating new ideas (e.g., designing, evaluating, synthesizing multi-step reasoning).
5. If a question involves code (code-based), it must explicitly state that the language is C, and it must provide a complete, copy-paste runnable test script.

The output must be strictly an English JSON array. Each object has the following structure (all questions share base fields and expand dynamically depending on the question type):

Base fields (required for all questions):
```json
{
  "questionType": "multiple-choice | fill-in-the-blank | short-answer",
  "question": "full question text",
  "difficulty": "easy | medium | hard"
}
```

- multiple-choice (conceptual or code-based):
```json
{
  ...base fields,
  "answers": ["option A text", "option B text", "option C text", "option D text"] (exactly 4 options; randomly place the correct answer; do not include labels like A), B), etc.),
  "correctAnswer": index of the correct answer in the answers array (integer, starting from 0)
}
```

- fill-in-the-blank (conceptual or code-based):
```json
{
  ...base fields,
  "question": "full question text; use ___1___ for a single blank, or ___1___, ___2___ for multiple ordered blanks",
  "correctAnswer": ["correct blank answer 1", "correct blank answer 2", ...] (in blank order)
}
```

- short-answer (conceptual or code-based):
```json
{
  ...base fields,
  "correctAnswer": "the model standard answer (if code-based, provide a complete C code snippet with necessary comments)"
}
```

If a question is code-based (code-based multiple-choice, code-based fill-in-the-blank, or code-based short-answer), you must additionally include:
- `"testScript"`: a complete, copy-paste runnable C test script (including `main`, required headers, compilable and runnable to verify correctness)

Important rules:
1. Absolutely do not output anything outside the JSON—no extra text, no reasoning process, no additional explanations.
2. Multiple-choice questions must have exactly one completely correct option; the other three must be plausible distractors based on common misconceptions or subtle differences.
3. If the user specifies an exact number of easy/medium/hard questions, specific question types, or whether they are code-based, you must follow the instructions strictly.
4. The style should resemble assessment questions from university-level introductory computer science course midterms/finals or programming assignments.
5. All code-related content (answers, test scripts) must use standard C (C99).

Now wait for the user to provide specific generation instructions, and execute them precisely according to the instructions.

Knowledge points list: `{knowledge_points_list}`

```json
[
  {
    "topic": "Using Arrays",
    "topic_knowledge_points": [
      "Arrays are concrete data structures that access their entries using integer indices.",
      "Arrays can be used to store objects like game entries with fixed maximum size.",
      "Insertion into an array involves shifting elements to make space for the new entry.",
      "Removal from an array involves shifting elements to fill the gap left by the removed entry.",
      "Insertion-sort algorithm sorts an array by inserting each element into the sorted prefix by shifting larger elements.",
      "Two-dimensional arrays use two indices to represent positional games, with row and column."
    ]
  },
  {
    "topic": "Singly Linked Lists",
    "topic_knowledge_points": [
      "A singly linked list is a collection of nodes that form a linear sequence, each node storing an element and a link to the next node.",
      "The head is the first node, and the tail is the last node with next pointer null.",
      "Insertion at the front of a singly linked list involves creating a new node and updating the head.",
      "Removal from the front of a singly linked list involves updating the head to the next node and deleting the old head.",
      "Singly linked lists can be implemented generically using templates to store arbitrary types."
    ]
  },
  {
    "topic": "Doubly Linked Lists",
    "topic_knowledge_points": [
      "A doubly linked list has nodes with next and prev pointers, allowing traversal in both directions.",
      "Header and trailer sentinels are dummy nodes at the beginning and end to simplify operations.",
      "Insertion into a doubly linked list involves linking a new node between two existing nodes by updating prev and next pointers.",
      "Removal from a doubly linked list involves linking out the node by updating prev and next of adjacent nodes.",
      "Doubly linked lists allow efficient insertion and removal at any position with direct access."
    ]
  },
  {
    "topic": "Circularly Linked Lists and List Reversal",
    "topic_knowledge_points": [
      "A circularly linked list links nodes in a cycle, with no beginning or end, using a cursor as a reference point.",
      "The back is the element at the cursor, and the front is the next element.",
      "Insertion in a circularly linked list adds after the cursor, handling the empty list by pointing to itself.",
      "Removal in a circularly linked list removes the node after the cursor.",
      "Reversing a linked list can be done by copying to a temporary list in reverse and copying back."
    ]
  },
  {
    "topic": "Recursion",
    "topic_knowledge_points": [
      "Recursion is when a function calls itself, with base cases to terminate and recursive cases to progress.",
      "Linear recursion makes at most one recursive call per invocation.",
      "Summing array elements can be done with linear recursion by adding the last element to the sum of the rest.",
      "Reversing an array can be done with linear recursion by swapping ends and recursing on the middle.",
      "Tail recursion is when the recursive call is the last operation, convertible to iteration.",
      "Binary recursion makes two recursive calls, like summing an array by splitting into halves.",
      "Computing Fibonacci naively with binary recursion is inefficient; it is better with linear recursion returning pairs.",
      "Multiple recursion makes more than two recursive calls, useful for enumerating configurations in puzzles."
    ]
  }
]
```

Example:

- Question: `{question}` `{level: medium}`  
  Which of the following best provides a recursive definition of a singly linked list?

  A) A collection of nodes where each node contains a data field and a pointer to the previous node in the sequence.  
  B) A data structure where each element is an object that contains a value and a reference to another data structure of the same type, or a null value.  
  C) A linear array of elements where each element's position is determined by its index and the size of the total list.  
  D) A set of nodes where the final node points back to the first node, creating a continuous loop of data.

- Answer: `{correctAnswer}`

  B)

Generate 2 non-code-based multiple-choice questions, including:  
- 1 easy  
- 1 medium

# Result

```json
[
  {
    "questionType": "multiple-choice",
    "question": "In the context of arrays, what operation typically involves shifting elements to fill the gap left by a removed entry?",
    "difficulty": "easy",
    "answers": [
      "Insertion",
      "Removal",
      "Sorting",
      "Initialization"
    ],
    "correctAnswer": 1
  },
  {
    "questionType": "multiple-choice",
    "question": "When analyzing the insertion-sort algorithm for an array, which of the following best describes the core mechanism used to place each new element into the correct position within the already sorted prefix?",
    "difficulty": "medium",
    "answers": [
      "It recursively splits the array into halves, sorts each half, and merges them.",
      "It repeatedly selects the smallest unsorted element and swaps it with the first unsorted element.",
      "It inserts the new element by shifting all larger elements in the sorted prefix one position to the right.",
      "It builds the sorted prefix by swapping adjacent elements if they are in the wrong order."
    ],
    "correctAnswer": 2
  }
]
```
