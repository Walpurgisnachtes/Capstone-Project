Create a set of data structure knowledge points and exercises from the provided textbook.

### Expected Output Format:

```json
{
  "chapter_code": "Chapter 99",
  "chapter_title": "Hello World",
  "knowledge_points": [
    {
      "topic": "Topic 0",
      "topic_knowledge_points": ["Point 1", "Point 2", "Point 3"]
    }
  ],
  "exercises": [
    {
      "topic_exercise": {
        "reinforcement": [
          { "exercise_code": "R-99.1", "exercise_content": "exercise 1" }
        ],
        "creativity": [
          { "exercise_code": "C-99.1", "exercise_content": "exercise 1" }
        ],
        "projects": [
          { "exercise_code": "P-99.1", "exercise_content": "exercise 1" }
        ]
      }
    }
  ]
}
```

### Response Instruction:

- Respond with the above JSON format.
- Create a set of data structure knowledge points and exercises in JSON format based on the above examples.
- For the data structure knowledge, it contains only data structure knowledge points. Ignore anything that is not related to data structure knowledge, for example, an introduction to a programming language.
- Do not use your own knowledge. Refers only to the knowledge of this textbook, even though you think it is wrong.
- Provide knowledge points each in 1 sentence only. Be clear, concise, and accurate.
- For the exercises part, extract the exercises in the textbook. Do not provide exercise that does not exist in the textbook. Do not miss any exercise.
- Ignore code fragments and examples.
- Provide FULL results.
