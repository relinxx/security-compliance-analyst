# AI Use Case Assessor

A small AI agent that helps a security and AI governance team check a proposed AI use case against the rules AI-001 to AI-008, with proof for every result.

## What it does

1. **Understands the request**: the AI reads the use case and pulls out the key facts (data used, human review, third-party AI, logging, access control).
2. **Decides what it needs**: the AI suggests which tools to run. Code only allows approved tools and adds any required ones it missed.
3. **Gets and processes information**: loads the 8 rules, finds sensitive data and sets a risk level using simple code (no AI).
4. **Structured result**: each rule gets Met, Partially met, Not met, Not enough information or Not applicable.
5. **Evidence**: each result quotes the use case. Code rejects any quote that is not really in the text.
6. **Risks and gaps**: lists what is missing or risky.
7. **Actions**: gives steps to fix each gap, linked to a rule.
8. **Safety checks**: see below.

## Safety checks

- Blocks input that tries to give the AI orders (prompt injection), before any AI call.
- Hides emails and phone numbers before the text goes to the AI (AI-002).
- Every AI answer must match a fixed format, or it is rejected.
- Only approved tools can run.
- Quotes are checked against the input text.
- A person must review high-risk cases or failures on AI-002, AI-003 or AI-008.
- Every run is saved to `logs/audit.jsonl`, with the input stored as a hash, not in full (AI-004).

## Run it

```bash
pip install -r requirements.txt
```

Add a `.env` file:

```
GEMINI_API_KEY=your-key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Then:

```bash
streamlit run app.py
```

## Screenshots

### Use case A
![](screenshots/usecase%20a/1.png)
![](screenshots/usecase%20a/2.png)
![](screenshots/usecase%20a/3.png)

### Use case B
![](screenshots/usecase%20b/1.png)
![](screenshots/usecase%20b/2.png)
![](screenshots/usecase%20b/3.png)

### Use case C (needs human review)
![](screenshots/usecase%20c/1.png)
![](screenshots/usecase%20c/2.png)
![](screenshots/usecase%20c/3.png)

### Prompt injection blocked
![](screenshots/prompt%20injection%20blocked.png)

## Design decisions

- Simple checks (sensitive data, risk level) use plain code, so they give the same result every time. The AI is only used where judgement is needed, and code checks its proof.
- Missing information is shown as "Not enough information" instead of guessed, because a missing control is a gap in itself.
- During testing the AI returned "Not applicable", which was not in the allowed format. The format check rejected it. I reviewed it and added it on purpose.
- Two AI calls per check keep it fast and cheap.

## Limitations

- The sensitive data check uses keywords, so it can miss other wording.
- The quote check proves the words exist, not that the reasoning is right.
- The AI can give slightly different answers on different runs.
- The injection check is based on patterns and would need more work for production.
- No login in this version.

## Use of AI tools

I used an AI assistant for help and debugging. I reviewed and tested the code and can explain all of it.
