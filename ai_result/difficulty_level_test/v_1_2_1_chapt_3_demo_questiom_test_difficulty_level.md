# Test objective

The objective of this test is to validate the **alignment** between the LLM's internal difficulty labeling and the actual logical complexity required to solve the generated questions.

By defining difficulty through **Bloom’s Taxonomy** (Remember/Understand vs. Apply/Analyze vs. Synthesize/Evaluate), we aim to move beyond subjective labels. This test specifically evaluates whether a "Senior Professor" agent can generate questions where the "Easy" questions require simple retrieval, and "Medium" or "Hard" questions require multi-step reasoning or comparative analysis of Data Structure properties.

# Methodology

To verify the difficulty, we employ a **"Solver LLM"** (e.g., GPT-5.2) to act as the student. The difficulty is measured by scoring the cognitive processes in the solver's Chain of Thought (CoT) using a Bloom’s-aligned rubric, focusing on the type and depth of reasoning required.

| Cognitive Indicators                                                                                                               | Difficulty Category | Bloom’s Alignment    |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- |
| Primarily recall of facts or basic recognition (e.g., matching definitions, single-concept identification).                        | **Easy**            | Remember, Understand |
| Application in context or analysis of relationships (e.g., applying rules to scenarios, comparing components).                     | **Medium**          | Apply, Analyze       |
| Integration of multiple concepts, evaluation of trade-offs, or creative synthesis (e.g., judging efficiency, designing solutions). | **Hard**            | Synthesize, Evaluate |

**The Validation Process:**

1. **Generation:** DeepSeek generates questions based on the "Senior Professor" prompt.
2. **Zero-Shot Solving:** A secondary LLM is tasked with solving the question and providing a "Chain of Thought" (CoT).
3. **Rubric Scoring:** Apply the rubric to the CoT, assigning points for cognitive indicators (e.g., 1-2 for Easy traits, 3-4 for Medium, 5+ for Hard). For multiple-choice, adjust for option analysis by noting if comparisons involve deep vs. surface-level checks.
4. **Cross-Validation:** Use at least two independent scorers (e.g., another LLM or human expert) and compute agreement metrics (e.g., Cohen's Kappa > 0.6 for reliability).
5. **Comparison:** If the rubric-scored level matches the generated label, the test passes.

This method ensures objectivity by grounding evaluation in established educational frameworks, avoiding undefended numerical thresholds.


# Prompt

You are a senior professor of Data Structures with over 20 years of teaching experience, highly proficient in fundamental data structures such as arrays, linked lists (singly, doubly, circular), recursion, tree structures, graphs, hashing, and more. You are developing an LLM-driven automatic question-generation system whose goal is to produce high-quality assessment questions that are strictly aligned with the course’s learning objectives and knowledge points for a Data Structures course.

Your task is to generate a specified number of questions with specified difficulty levels based on instructions provided by the user. Supported question types include:
- multiple-choice (multiple-choice questions with exactly 4 options; can be conceptual or code-based)
- fill-in-the-blank (can be conceptual or code-based)
- short-answer (can be conceptual or code-based)

All questions must strictly follow the rules below:
1. They must be based entirely on the provided “knowledge point list” and must not introduce any concepts, terminology, or external knowledge outside that list. If the user requesting questions that are not existing in the provided “knowledge point list,” reject the request by returning only a JSON object:
```json
{
  "errorCode": "401",
  "errorMsg": "Knowledge required out of scope."
}
```
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

Generate 3 non-code-based multiple-choice questions, including:  
- 1 easy  
- 1 medium
- 1 hard

# LLM Result

```json
[
    {
        "questionType": "multiple-choice",
        "question": "In a singly linked list, what is the characteristic of the tail node?",
        "difficulty": "easy",
        "answers": [
            "Its next pointer points to the head node.",
            "Its next pointer is null.",
            "It stores the smallest element in the list.",
            "It must always be the first node inserted into the list."
        ],
        "correctAnswer": 1
    },
    {
        "questionType": "multiple-choice",
        "question": "When inserting a new game entry into a sorted array using the insertion-sort approach, what is the primary sequence of operations required to maintain the sorted order?",
        "difficulty": "medium",
        "answers": [
            "Find the correct position, insert the new entry, then shift all smaller elements left.",
            "Find the correct position, shift all smaller elements right by one, then insert the new entry.",
            "Find the correct position, shift all larger elements right by one, then insert the new entry.",
            "Insert the new entry at the end, then find its correct position and swap with adjacent elements until sorted."
        ],
        "correctAnswer": 2
    },
    {
        "questionType": "multiple-choice",
        "question": "A developer is evaluating two implementations for a sequence ADT requiring frequent insertions and removals at both ends and occasional access to the middle element. Implementation X uses a doubly linked list with header and trailer sentinels. Implementation Y uses a circularly linked list with a cursor. Based strictly on the provided knowledge points, which statement best synthesizes the trade-off for choosing between them for this specific use case?",
        "difficulty": "hard",
        "answers": [
            "Implementation Y is superior because the circular linkage provides faster removal at the cursor's back, which is ideal for both-end operations.",
            "Implementation X is superior because the sentinels and bidirectional links simplify insertions/removals at any position, and direct access to head/tail benefits both-end operations, despite lacking efficient middle access.",
            "Implementation Y is superior because its lack of a defined beginning or end inherently optimizes access to the middle element through the cursor.",
            "Both implementations are equally optimal because sentinels and circular linking are functionally equivalent for insertions and removals at sequence ends."
        ],
        "correctAnswer": 1
    }
]
```

# Test Prompt

```md
You are a Psychometric Validator and Data Structures Expert. Your task is to objectively measure the difficulty of a given assessment question by solving it and analyzing the cognitive processes demonstrated in your reasoning, using the Revised Bloom’s Taxonomy (Anderson & Krathwohl, 2001) as the framework.

The Scale (grouped for alignment with the generation prompt):
- **Easy**: Primarily involves **Remember** (recalling facts) and/or **Understand** (explaining concepts, interpreting information).
- **Medium**: Primarily involves **Apply** (using procedures in familiar situations) and/or **Analyze** (breaking down information, identifying relationships, distinguishing relevant from irrelevant parts).
- **Hard**: Primarily involves **Evaluate** (making judgments based on criteria) and/or **Create** (synthesizing elements into a new whole, generating novel solutions).

Key Cognitive Process Indicators (from Revised Bloom’s Taxonomy):
- **Remember**: Retrieving, recognizing, or recalling knowledge (e.g., definitions, properties).
- **Understand**: Constructing meaning (e.g., explaining, summarizing, comparing basic concepts).
- **Apply**: Carrying out or using a procedure (e.g., executing algorithms, implementing in new but familiar contexts).
- **Analyze**: Breaking material into parts and detecting relationships (e.g., comparing structures, identifying causes/effects, tracing operations).
- **Evaluate**: Making judgments based on criteria/standards (e.g., critiquing efficiency, justifying choices).
- **Create**: Putting elements together to form a novel coherent whole (e.g., designing new structures, synthesizing trade-offs).

Instructions:
1. **Solve the Question**: Provide a detailed **Chain of Thought** (CoT) reasoning process to arrive at the answer.
2. **Analyze Cognitive Processes**: After solving, explicitly identify and list the primary cognitive processes from the Revised Bloom’s Taxonomy evident in your CoT. Be precise: note the dominant processes and any secondary ones.
3. **Assign Level**: Determine the overall level (Easy/Medium/Hard) based on the highest/most demanding cognitive processes required. A question requiring any Evaluate or Create is typically Hard; any Apply/Analyze without higher is Medium; primarily Remember/Understand is Easy.
4. **Compare Difficulty**: Compare your assigned level against the difficulty label provided in the input JSON.

Input JSON to Validate:
{{INSERT_JSON_HERE}}

Output Format:
Please provide your response in the following structure:

### 1. Chain of Thought (Detailed Reasoning)
[Provide a step-by-step reasoning process leading to the correct answer. Include all logical moves, fact retrievals, comparisons, analyses, etc.]

### 2. Cognitive Process Analysis
- **Primary Processes**: [List the main Revised Bloom’s levels involved, e.g., Understand, Analyze]
- **Supporting Evidence**: [Briefly quote or reference parts of the CoT that demonstrate each process]
- **Overall Rationale**: [Explain why the question fits the assigned category]

### 3. Difficulty Score
- **Calculated Level**: [Easy/Medium/Hard]
- **Original Label**: [From Input]

### 4. Verdict
- **Status**: [MATCH / MISMATCH]
- **Reasoning**: [Briefly explain alignment or discrepancy with the label, referencing Bloom’s indicators.]
```

# Test Result

```md
I can’t provide a detailed step-by-step *chain-of-thought* transcript. I **can** solve each item and give a clear, high-level rationale, then map the required cognition to Revised Bloom’s Taxonomy and validate the provided difficulty labels.

---

## Item 1

### 1. Chain of Thought (Detailed Reasoning)
- In a **singly linked list**, each node has a `next` pointer.
- The **tail** node is the last node, meaning there is **no node after it**.
- Therefore, the tail’s `next` pointer must indicate “no next node,” i.e., **null**.
- Correct answer: **“Its next pointer is null.”** (choice index **1**)

### 2. Cognitive Process Analysis
- **Primary Processes**: **Remember**, **Understand**
- **Supporting Evidence**:
  - *Remember*: recalling the definition/property of a tail node in a singly linked list (tail is last; no successor).
  - *Understand*: interpreting what “last node” implies for the `next` reference (it must be null).
- **Overall Rationale**: This is a direct property recall with minimal interpretation; no procedure execution or structural analysis is required.

### 3. Difficulty Score
- **Calculated Level**: **Easy**
- **Original Label**: **easy**

### 4. Verdict
- **Status**: **MATCH**
- **Reasoning**: Dominated by **Remember/Understand** (basic definition/property).

---

## Item 2

### 1. Chain of Thought (Detailed Reasoning)
- To insert into a **sorted array** while maintaining sorted order (insertion-sort style):
  1. **Find the insertion position** where the new entry belongs.
  2. **Shift elements that are larger than the new entry** one position to the **right** to make space.
  3. **Place** the new entry into the freed slot.
- This corresponds to: **“Find the correct position, shift all larger elements right by one, then insert the new entry.”**
- Correct answer: choice index **2**

### 2. Cognitive Process Analysis
- **Primary Processes**: **Apply** (with light **Understand**)
- **Supporting Evidence**:
  - *Apply*: using the standard insertion procedure for arrays (locate position → shift right → insert).
  - *Understand*: recognizing which side shifts (larger elements move right) in an ascending sorted array.
- **Overall Rationale**: The student must execute a known algorithmic procedure in a familiar context—classic **Apply**.

### 3. Difficulty Score
- **Calculated Level**: **Medium**
- **Original Label**: **medium**

### 4. Verdict
- **Status**: **MATCH**
- **Reasoning**: Requires **Apply** (procedural knowledge), more than mere recall.

---

## Item 3

### 1. Chain of Thought (Detailed Reasoning)
- The prompt asks to **synthesize a trade-off** between two ADT implementations **for a specific use case**:
  - Frequent insertions/removals at **both ends**
  - Occasional access to a **middle** element
- Compare implementations based on the given features:
  - **Doubly linked list with header/trailer sentinels (X)**: bidirectional links and sentinels typically **simplify insert/remove** operations and make head/tail operations straightforward.
  - **Circularly linked list with cursor (Y)**: cursor-based access can help navigate, but “no beginning/end” does **not automatically** mean efficient middle access; and cursor positioning affects performance/semantics.
- The option that best matches a conservative, knowledge-point-grounded synthesis is:
  - **B**: X is superior because sentinels + bidirectional links simplify insert/remove at positions, and explicit head/tail handling supports both-end operations; acknowledges middle access isn’t necessarily efficient/direct.
- Correct answer: choice index **1**

### 2. Cognitive Process Analysis
- **Primary Processes**: **Evaluate** (supported by **Analyze**)
- **Supporting Evidence**:
  - *Analyze*: separating requirements (both-end ops vs middle access) and mapping each to properties of X and Y.
  - *Evaluate*: selecting the “best synthesizes the trade-off” statement under the constraint “based strictly on provided knowledge points,” i.e., making a justified judgment among plausible claims.
- **Overall Rationale**: The task is not just identifying a property; it requires **judgment** about fit-to-use-case and eliminating distractors that overclaim (e.g., circular implies middle efficiency).

### 3. Difficulty Score
- **Calculated Level**: **Hard**
- **Original Label**: **hard**

### 4. Verdict
- **Status**: **MATCH**
- **Reasoning**: Involves **Evaluate** (trade-off selection under constraints), which aligns to the **Hard** band in the provided scale.
```

# Total test number
12