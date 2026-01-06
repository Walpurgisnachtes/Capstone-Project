# Test objective

The objective of this test is to verify the **structural integrity and schema compliance** of the generated questions.This ensures that the LLM output strictly adheres to the predefined JSON formats for each question type—multiple-choice, fill-in-the-blank, and short-answer—to enable seamless parsing and integration into the assessment system. This validation focuses exclusively on the syntax, field presence, and internal formatting consistency of the JSON objects, independent of their conceptual or logical content.

# Methodology

The verification process employs a schema-based validation approach to audit the structure of each generated question. The following steps are performed to ensure compliance:

1.  **Base Field Verification**: 
    * Every generated object must contain the three mandatory base fields: `questionType`, `question`, and `difficulty`.
    * The `questionType` must strictly match one of the three allowed strings: `multiple-choice`, `fill-in-the-blank`, or `short-answer`.

2.  **Type-Specific Structural Audit**:
    * **Multiple-choice**:
        * The system verifies that the `answers` field is an array containing exactly four unique options.
        * The `correctAnswer` field must be an integer between 0 and 3, corresponding to the valid index of the `answers` array.
    * **Fill-in-the-blank**:
        * The `question` text is scanned to ensure it uses the required `___n___` placeholder format for blanks.
        * The `correctAnswer` field must be an array of strings.
        * The length of the `correctAnswer` array must exactly match the number of placeholders identified in the question text.
    * **Short-answer**:
        * The system verifies the presence of a single `correctAnswer` field.
        * The field must contain a string representing the model answer or a C code snippet.

3.  **Data Type and Array Validation**:
    * The entire output must be validated as a syntactically correct JSON array.
    * All text-based fields must be correctly escaped to prevent JSON parsing failures, particularly when the question or answer contains C code characters.

**Success Criteria**: 
* 100% compliance with the JSON schema definitions for the requested question types.
* Zero parsing errors when the output is processed by a standard JSON parser.

# System Prompt

You are a senior professor of Data Structures with over 20 years of teaching experience. You are developing an LLM-driven automatic question-generation system strictly aligned with a provided knowledge point list.

### **STRICT CONSTRAINT: ATOMIC SCOPE GATING**
1. **The "All-or-Nothing" Rule**: When you receive a generation request, you must audit **all** requested items and concepts simultaneously. If **ANY** single item, keyword, or concept in the user's request is out-of-scope (e.g., "efficiency", "resizing"), you must reject the **ENTIRE** request. Do not provide a partial response.
2. **Definition of "Out-of-Scope"**:
   - Any term not explicitly in the list (e.g., "performance", "Big-O", "time complexity").
   - A request for "efficiency of insertion" is OUT-OF-SCOPE because the concept of "efficiency" is not in the knowledge points, even if "insertion" is.
3. **Rejection Protocol**: If an out-of-scope violation is detected, return ONLY:
```json
{
  "errorCode": "401",
  "errorMsg": "Knowledge required out of scope."
}
```
4. **Implicit Topic Selection (Random Generation)**: If the user's request specifies quantity and difficulty but does not mention any specific topic or keyword, you must NOT return an error. Instead, you must randomly and evenly select topics from the provided "knowledge point list" to fulfill the request. Ensure the generated questions are distributed across different topics in the list.

### **STRICT CONSTRAINT: CODE VERIFIABILITY & ANSWER VERIFICATION**

1. **C99 Standard**: All code snippets, answers, and test scripts must be written in standard C (C99).
2. **Instant Verification Script**: For every code-based question (code-based multiple-choice, code-based fill-in-the-blank, or code-based short-answer), you MUST provide a field named `"testScript"`.
3. **Script Completeness**: The `"testScript"` must be a complete, copy-paste runnable C program. It must include:
   - Necessary headers (e.g., `#include <stdio.h>`, `#include <stdlib.h>`).
   - The `main` function.
   - All logic required to demonstrate that the `correctAnswer` is indeed correct through instant execution.
4. **No External Tools**: Do not assume external testing frameworks. The script itself is the test.

**Specific Handling for Mixed Requests**
- **Example (Implicit Topic Selection)**:
  - User Instruction: "Generate 3 non-code-based multiple-choice questions, including: 1 hard, 2 easy."
  - Your Action: Since no out-of-scope terms are present, you should randomly pick topics (e.g., one from "Recursion", two from "Singly Linked Lists") from the list to generate the 3 questions.
- **Example (Mixed Request with Out-of-Scope)**:
  - User Instruction: "Generate 1 easy question on array indices, and 1 hard question on array efficiency."
  - Your Action: Because "efficiency" is not in the knowledge point list, you must reject both questions and return the 401 error code.

**General Rules**
1. Terminology Adherence: Use ONLY the course’s standard terminology as defined in the list (e.g., “singly linked list,” “header and trailer sentinels,” “linear recursion”).

2. Negative Example for Scope Rejection:
- User Instruction: "Generate 1 medium question about resizing arrays when full."
- Your Action: Since the list only mentions "fixed maximum size" and does not mention "resizing", you must return the 401 error JSON.

1. Logical Rigor: Ensure the logic is rigorous, correct, and unambiguous.

2. Difficulty definitions (based on Bloom’s Taxonomy):
   - easy (lower-order cognition): corresponds to Remember and Understand; only requires recalling facts, terms, or basic concepts, or providing simple explanations.
   - medium (mid-order cognition): corresponds to Apply and Analyze; requires applying knowledge in new situations or breaking down information to examine relationships.
   - hard (higher-order cognition): corresponds to Synthesize and Evaluate; requires making judgments based on standards or generating new ideas (e.g., designing, evaluating, synthesizing multi-step reasoning).

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

Important rules:

1. Absolutely do not output anything outside the JSON — no extra text or reasoning.

2. Multiple-choice distractors must be plausible but strictly incorrect.

3. All code-related content must be compilable standard C.

Now wait for the user to provide specific generation instructions.

# User Prompt Test + LLM Result

0. knowledge point list

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

1. Testing FITB Question

## Prompt
```md
Generate 1 non-code-based fill-in-the-blank question.
```

## Actual Result
```json
[
  {
    "questionType": "fill-in-the-blank",
    "question": "In the context of recursion, a function calls itself to solve smaller instances of the same problem, and the condition that stops this process is called the ___1___. In a linear recursion, there is at most ___2___ recursive call per function invocation.",
    "difficulty": "easy",
    "correctAnswer": ["base case", "one"]
  }
]
```

2. Testing MC Question

## Prompt
```md
Generate 1 non-code-based multiple-choice question.
```

## Actual Result
```json
[
  {
    "questionType": "multiple-choice",
    "question": "In a doubly linked list that uses header and trailer sentinel nodes, what is the primary purpose of these dummy nodes?",
    "difficulty": "medium",
    "answers": [
      "To store metadata about the list, such as its current size and maximum capacity.",
      "To simplify insertion and removal operations by eliminating special cases for the beginning and end of the list.",
      "To improve traversal speed by providing shortcuts between distant nodes in the list.",
      "To enable the list to be stored in non-contiguous memory blocks without requiring pointer adjustments."
    ],
    "correctAnswer": 1
  }
]
```


3. Testing Short-Answer Question

## Prompt
```md
Generate 1 non-code-based hard short-answer question.
```

## Actual Result
```json
[
  {
    "questionType": "short-answer",
    "question": "Compare and contrast the logic and procedural steps required to insert a new element at a specific index within (a) a fixed-size array and (b) a singly linked list (without sentinel nodes). For each structure, design a multi-step plan outlining the necessary actions, explicitly identifying the key differences in how elements are accessed and shifted. Your answer must synthesize knowledge of both data structures.",
    "difficulty": "hard",
    "correctAnswer": "(a) Array Insertion Plan:\n1. **Validation**: Check if the index is within the valid range (0 to current size - 1) and if the array has capacity for one more element (current size < maximum size).\n2. **Space Creation**: Starting from the last element in the array up to the target index, shift each element one position to the right. This creates an empty slot at the target index.\n3. **Assignment**: Place the new element into the now-vacant slot at the target index.\n4. **Update**: Increment the variable tracking the current size of the array.\n\n**Key Characteristics for Array**: Access is by integer index. The shift operation physically moves data in memory, affecting all elements from the insertion point to the end.\n\n(b) Singly Linked List Insertion Plan:\n1. **Traversal & Access**: If inserting at the front (index 0), skip to step 3. Otherwise, traverse the list from the head node. Use a counter to move a 'current' pointer through the list until it points to the node *just before* the desired index (i.e., at position index-1). This requires sequential access, not direct indexing.\n2. **Node Creation**: Create a new node and store the new element in it.\n3. **Pointer Manipulation**: \n   - For insertion at the front: Set the new node's 'next' pointer to point to the current head node, then update the 'head' pointer of the list to point to the new node.\n   - For insertion elsewhere: Set the new node's 'next' pointer to point to the node currently after the 'current' node (i.e., `newNode->next = current->next`). Then, update the 'next' pointer of the 'current' node to point to the new node (`current->next = newNode`).\n4. **Special Case**: If the insertion point is at the end (i.e., after the tail), the new node's 'next' becomes NULL, and the previous tail's 'next' pointer is updated, making the new node the new tail.\n\n**Key Characteristics for Singly Linked List**: Access is sequential via node links. No existing elements are shifted or copied; only the links (pointers) of the new node and its predecessor are changed to integrate it into the sequence.\n\n**Contrast**: The fundamental difference lies in data access (direct index vs. sequential traversal) and the mechanism for making space (physically shifting all subsequent elements in an array vs. changing a constant number of pointers in a linked list). The array operation's cost is proportional to the number of elements after the insertion point, while the linked list operation's primary cost is proportional to the traversal to find the insertion point."
  }
]
```

# Total test number
9