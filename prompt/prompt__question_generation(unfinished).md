### Expected Simplified JSON Format:

```json
[
  {
    "questionId": null,
    "questionType": "MC",
    "question": "{question text}",
    "answers": [
      { "text": "{options text}", "id": "{answer index}" },
      { "text": "{options text}", "id": "{answer index}" },
      { "text": "{options text}", "id": "{answer index}" },
      { "text": "{options text}", "id": "{answer index}" }
    ],
    "correctAnswer": ["{answer index}"],
    "questionMark": 1,
    "questionSeq": null
  }
]
```

### Response instruction:

- Create a new and unique set of questions in JSON format based on the above examples.
- Each question just accept only one correct answer choice.
- Each multiple choice questions' answer can only have one totally correct answer, while other options must be totally incorrect.
- For each of the multiple choice questions, try to reorder the answer options so that the correct answer is not always the first option (given there are 4 options for each question).
- Each question must give enough hints for the student to choose the best answer, e.g.
- For determining tenses, the question must include a very short additional information of time / event / happenings.
