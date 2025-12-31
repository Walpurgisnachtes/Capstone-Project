# Prompt

你是一位資深 Data Structures 課程教授，擁有超過 20 年教學經驗，精通陣列、鏈結串列（單向、雙向、循環）、遞迴、樹狀結構、圖形、雜湊等基礎資料結構。你正在開發一個 LLM 驅動的自動出題系統，目標是為 Data Structures 課程生成高品質、嚴格對齊課程知識點的評估題目。

你的任務是根據使用者提供的指令，生成指定數量與難度的題目。支援的題型包括：
- multiple-choice（多選題，固定 4 個選項，可為概念性或 code-based）
- fill-in-the-blank（填空題，可為概念性或 code-based）
- short-answer（簡答題，可為概念性或 code-based）

所有題目必須嚴格遵守以下規則：
1. 完全基於提供的「知識點清單」，不得引入清單以外的概念、術語或外部知識。
2. 使用課程標準術語（如 "singly linked list"、"header and trailer sentinels"、"linear recursion" 等）。
3. 確保邏輯嚴謹、正確無誤、無歧義。
4. 難度定義（基於 Bloom's Taxonomy）：
   - easy（低階認知）：對應 Remember 和 Understand 層級，僅需回憶事實、術語或基本概念，或簡單解釋概念。
   - medium（中階認知）：對應 Apply 和 Analyze 層級，需應用知識於新情境或分解資訊以檢視關係。
   - hard（高階認知）：對應 Evaluate 和 Create 層級，需基於標準進行判斷或生成新想法（如設計、評估、綜合多步驟推理）。
5. 若題目涉及程式碼（code-based），必須明確說明使用 C 語言，並提供完整、可直接 copy-paste 執行的測試腳本。

輸出必須嚴格為英文 JSON 陣列，每個物件結構如下（所有題目共用基礎屬性，依題型動態擴展）：

基礎屬性（所有題目必填）：
{
  "questionType": "multiple-choice | fill-in-the-blank | short-answer",
  "question": "完整問題文字",
  "difficulty": "easy | medium | hard"
}

- multiple-choice（概念性或 code-based）：
  {
    ...基礎屬性,
    "answers": ["選項A文字", "選項B文字", "選項C文字", "選項D文字"] （固定 4 個選項，隨機排列正確答案位置，不得出現 A)、B) 等標記）,
    "correctAnswer": 正確答案在 answers 陣列中的索引（整數，從 0 開始）
  }

- fill-in-the-blank（概念性或 code-based）：
  {
    ...基礎屬性,
    "question": "完整問題文字，使用 ___1___ 表示單一空白，或 ___1___、___2___ 表示多個有序空白",
    "correctAnswer": ["正確填空答案1", "正確填空答案2", ...] （按空白順序排列）
  }

- short-answer（概念性或 code-based）：
  {
    ...基礎屬性,
    "correctAnswer": "模型標準答案（若為 code-based 則為完整 C 程式碼片段，含必要註解）"
  }

若題目涉及程式碼（code-based multiple-choice、code-based fill-in-the-blank 或 code-based short-answer），必須額外加入：
  "testScript": "完整、可直接 copy-paste 執行的 C 語言測試腳本（包含 main 函數、必要標頭、編譯後可運行並驗證正確性）"

重要規則：
1. 絕對不要在 JSON 外輸出任何其他文字、思考過程或額外說明（DeepSeek V3.2 的 reasoning 會自動內部處理）。
2. multiple-choice 題只有一個完全正確選項，其他三個必須是常見錯誤觀念或細微差異造成的合理干擾項。
3. 若使用者指定生成特定數量的 easy / medium / hard 題目、特定題型，或是否為 code-based，請嚴格遵守。
4. 題目風格應參考大學電腦科學基礎課程的期中/期末考試或作業題型。
5. 所有程式碼相關內容（答案、測試腳本）一律使用標準 C 語言（ANSI C 或 C99）。

現在等待使用者提供具體生成指令，請根據指令精準執行。

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

生成2條code-based multiple-choice問題，其中包括: 
1條easy，1條medium

及

生成3條non-code-based multiple-choice問題，其中包括: 
1條easy，1條medium，1條hard

# Result

```json
[
  {
    "questionType": "multiple-choice",
    "question": "Consider the following C code snippet that implements insertion into a sorted array using insertion-sort logic:\n\n```c\nvoid insertSorted(int arr[], int *n, int maxSize, int value) {\n    if (*n >= maxSize) {\n        printf(\"Array is full.\\n\");\n        return;\n    }\n    int i = *n - 1;\n    while (i >= 0 && arr[i] > value) {\n        arr[i + 1] = arr[i];\n        i--;\n    }\n    arr[i + 1] = value;\n    (*n)++;\n}\n```\n\nWhat is the purpose of the `while` loop condition `i >= 0 && arr[i] > value`?",
    "difficulty": "easy",
    "answers": ["To find the first element from the left that is less than or equal to the value.", "To find the correct position for insertion by shifting all elements greater than the value to the right.", "To count the number of elements greater than the value.", "To check if the array is already sorted in ascending order."],
    "correctAnswer": 1,
    "testScript": "#include <stdio.h>\nvoid insertSorted(int arr[], int *n, int maxSize, int value) {\n    if (*n >= maxSize) {\n        printf(\"Array is full.\\n\");\n        return;\n    }\n    int i = *n - 1;\n    while (i >= 0 && arr[i] > value) {\n        arr[i + 1] = arr[i];\n        i--;\n    }\n    arr[i + 1] = value;\n    (*n)++;\n}\nint main() {\n    int arr[10] = {10, 20, 30, 40};\n    int n = 4;\n    int maxSize = 10;\n    int value = 25;\n    printf(\"Before insertion: \");\n    for (int i = 0; i < n; i++) printf(\"%d \", arr[i]);\n    printf(\"\\n\");\n    insertSorted(arr, &n, maxSize, value);\n    printf(\"After insertion: \");\n    for (int i = 0; i < n; i++) printf(\"%d \", arr[i]);\n    printf(\"\\n\");\n    return 0;\n}"
  },
  {
    "questionType": "multiple-choice",
    "question": "Given a C structure for a singly linked list node and a function to insert at the front:\n\n```c\ntypedef struct Node {\n    int data;\n    struct Node* next;\n} Node;\n\nvoid insertFront(Node** headRef, int value) {\n    Node* newNode = (Node*)malloc(sizeof(Node));\n    newNode->data = value;\n    newNode->next = *headRef;\n    *headRef = newNode;\n}\n```\n\nWhat will be the output of the following code if the initial list is 1 -> 2 -> 3?\n\n```c\nNode* head = NULL;\ninsertFront(&head, 3);\ninsertFront(&head, 2);\ninsertFront(&head, 1);\nprintList(head); // assume prints list sequentially\ninsertFront(&head, 4);\nprintList(head);\n```",
    "difficulty": "medium",
    "answers": ["1 -> 2 -> 3", "4 -> 1 -> 2 -> 3", "1 -> 2 -> 3 -> 4", "4 -> 3 -> 2 -> 1"],
    "correctAnswer": 1,
    "testScript": "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct Node {\n    int data;\n    struct Node* next;\n} Node;\nvoid insertFront(Node** headRef, int value) {\n    Node* newNode = (Node*)malloc(sizeof(Node));\n    newNode->data = value;\n    newNode->next = *headRef;\n    *headRef = newNode;\n}\nvoid printList(Node* head) {\n    Node* current = head;\n    while (current != NULL) {\n        printf(\"%d \", current->data);\n        current = current->next;\n    }\n    printf(\"\\n\");\n}\nint main() {\n    Node* head = NULL;\n    insertFront(&head, 3);\n    insertFront(&head, 2);\n    insertFront(&head, 1);\n    printf(\"Initial list: \");\n    printList(head);\n    insertFront(&head, 4);\n    printf(\"After inserting 4 at front: \");\n    printList(head);\n    return 0;\n}"
  },
  {
    "questionType": "multiple-choice",
    "question": "Which of the following is a correct description of the 'head' and 'tail' in a singly linked list?",
    "difficulty": "easy",
    "answers": ["Head is the first node, tail is the last node with next pointer null.", "Head is the node with the largest value, tail is the node with the smallest value.", "Head is a dummy node at the beginning, tail is a dummy node at the end.", "Head and tail are always the same node in a non-empty list."],
    "correctAnswer": 0
  },
  {
    "questionType": "multiple-choice",
    "question": "In the context of recursion, which statement accurately describes 'linear recursion'?",
    "difficulty": "medium",
    "answers": ["It makes at most one recursive call per invocation.", "It always makes exactly two recursive calls per invocation.", "It is a special case where the recursive call is the first operation.", "It must have exactly one base case and one recursive case."],
    "correctAnswer": 0
  },
  {
    "questionType": "multiple-choice",
    "question": "When implementing a doubly linked list with header and trailer sentinels, which of the following operations is simplified the MOST compared to a doubly linked list without sentinels? Consider edge cases such as insertion into an empty list or removal of the only element.",
    "difficulty": "hard",
    "answers": ["Insertion at the front when the list is empty, because we always insert between header and trailer.", "Removal of the last element, because we can directly access the tail pointer.", "Search for an element, because sentinels act as markers for the start and end of the data section.", "Counting the number of elements, because sentinels are not counted."],
    "correctAnswer": 0
  }
]
```