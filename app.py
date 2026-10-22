import streamlit as st
from tools import detect_sensitive_data, classify_risk_tier

SAMPLES = {
    "A: Customer Support Assistant": "A customer support team wants to use an LLM to summarize customer conversations and suggest responses to support agents. The system will process customer names, account information, support tickets, and conversation history. A human support agent will review the generated response before sending it to the customer. The application will use a third-party hosted LLM API.",
    "B: Internal Security Assistant": "The cybersecurity team wants to deploy an internal AI assistant that can analyze security alerts and recommend investigation steps. The assistant will have access to internal security logs and selected threat intelligence sources. Security analysts will review recommendations before taking action. The system will be deployed within the organization's cloud environment.",
    "C: Automated Employee Decisions": "HR wants to use an AI system to analyze employee performance information and automatically recommend employees for promotion. The system will process employee performance records and HR information. HR intends for the AI system's recommendation to be used as the primary input into promotion decisions.",
}

st.title("AI Use Case Assessor")
st.caption("Assesses a proposed AI use case against governance requirements AI-001 to AI-008.")

choice = st.selectbox("Load a sample use case", ["(write my own)"] + list(SAMPLES))
default = SAMPLES.get(choice, "")
text = st.text_area("Use case description", value=default, height=180)


if st.button("Assess"):
    sensitive = detect_sensitive_data(text)
    tier, reasons = classify_risk_tier(text, sensitive)

    st.subheader(f"Risk tier: {tier}")
    for r in reasons:
        st.write("- " + r)

    st.subheader("Sensitive data detected")
    if sensitive:
        for category, hits in sensitive.items():
            st.write(f"- **{category}**: {', '.join(hits)}")
    else:
        st.write("None detected.")