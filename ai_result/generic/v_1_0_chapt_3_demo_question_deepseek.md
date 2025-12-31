# Prompt

你是 Data Structures 課程的資深教授。

基於以下知識點清單生成 5 條{type: multiple-choice}概念問題，主題為{level}。難度：{level: easy - 單點；medium - 2-3 點；hard - 多步驟綜合}。問題需對齊課程術語，並使用逐步推理生成。

生成 2 條{level: easy}問題，2 條{level: medium}問題及 1 條{level: hard}問題。

知識點清單：{knowledge_points_list}

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
      "Insertion in a circularly linked list adds after the cursor, handling empty list by pointing to itself.",
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
      "Binary recursion makes two recursive calls, like summing array by splitting into halves.",
      "Computing Fibonacci naively with binary recursion is inefficient, better with linear recursion returning pairs.",
      "Multiple recursion makes more than two recursive calls, useful for enumerating configurations in puzzles."
    ]
  }
]
```

範例：

- 問題：{question} {level: medium}
  Which of the following best provides a recursive definition of a singly linked list?

A) A collection of nodes where each node contains a data field and a pointer to the previous node in the sequence.

B) A data structure where each element is an object that contains a value and a reference to another data structure of the same type, or a null value.

C) A linear array of elements where each element's position is determined by its index and the size of the total list.

D) A set of nodes where the final node points back to the first node, creating a continuous loop of data.

- 答案：{correctAnswer}

B)

輸出英文 JSON：

```json
[
  {
    "question": "問題文字",
    "answers": ["多項選擇題中的所有答案，包含正確答案。不可以包括問題序號，例如1)、A)或甲)"],
    "correctAnswer": "正確答案在answers數組中的索引",
    "explanation": "答案的逐步解釋",
    "difficulty": "{level}",
    "verification": "檢查邏輯一致性"
  }
]
```

# Result

```json
[
  {
    "question": "What is the purpose of shifting elements during the removal of an entry from a standard array?",
    "answers": ["To randomize the array order for faster access.", "To increase the maximum size of the array.", "To compact the array by filling the gap left by the removed entry.", "To create a new array with updated indices."],
    "correctAnswer": 2,
    "difficulty": "easy"
  },
  {
    "question": "In a linear recursive function, what is the maximum number of recursive calls made per invocation?",
    "answers": ["Zero", "One", "Two", "Unlimited"],
    "correctAnswer": 1,
    "difficulty": "easy"
  },
  {
    "question": "In the insertion-sort algorithm, if you have a sorted prefix of size k, and you need to insert the (k+1)-th element, what is the worst-case number of element shifts required?",
    "answers": ["0", "k", "k+1", "log(k)"],
    "correctAnswer": 1,
    "difficulty": "medium"
  },
  {
    "question": "When implementing a generic singly linked list using templates, what is the main advantage?",
    "answers": ["It automatically sorts the elements upon insertion.", "It can store elements of arbitrary, specified types without rewriting the node class.", "It guarantees constant-time access to any element by index.", "It eliminates the need for a head pointer."],
    "correctAnswer": 1,
    "difficulty": "medium"
  },
  {
    "question": "Consider a function that recursively sums an array using binary recursion by splitting it into two halves. If the array has n elements, what is the recurrence relation for the time complexity T(n)?",
    "answers": ["T(n) = T(n-1) + O(1)", "T(n) = 2T(n/2) + O(1)", "T(n) = T(n/2) + O(1)", "T(n) = T(n-1) + O(n)"],
    "correctAnswer": 1,
    "difficulty": "hard"
  }
]
```
