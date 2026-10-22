# AI Use Case Assessor

Checks an AI use case against rules AI-001 to AI-008 and shows the result with proof.

## How it works

1. AI pulls the key facts from the use case.
2. AI picks tools to run. Only approved tools are allowed.
3. Code finds sensitive data and sets a risk level.
4. AI rates each rule and quotes the use case as proof. Code checks the quote is real.
5. App shows gaps, actions, and flags high-risk cases for human review.

## Safety

- Blocks prompt injection.
- Hides emails and phone numbers before sending to the AI.
- Rejects AI answers in the wrong format.
- Logs every run to `logs/audit.jsonl`.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Needs a `.env` with `GEMINI_API_KEY` and `GEMINI_MODEL`.

## Screenshots

### Use case A
![](screenshots/usecase%20a/1.png)
![](screenshots/usecase%20a/2.png)
![](screenshots/usecase%20a/3.png)

### Use case B
![](screenshots/usecase%20b/1.png)
![](screenshots/usecase%20b/2.png)
![](screenshots/usecase%20b/3.png)

### Use case C
![](screenshots/usecase%20c/1.png)
![](screenshots/usecase%20c/2.png)
![](screenshots/usecase%20c/3.png)

### Prompt injection blocked
![](screenshots/prompt%20injection%20blocked.png)

## Limits

- Keyword checks can miss other wording.
- Results can vary slightly between runs.

I used an AI assistant for help and debugging, and reviewed all the code myself.
