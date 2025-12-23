# Design Note – Audio to Structured Order

## Architecture Overview

This solution is designed as a simple, modular pipeline that reflects how a production system would be built.

Audio input flows through a small number of clearly separated stages:

Audio input  
→ Speech-to-text (Whisper)  
→ Text normalization  
→ Order extraction  
→ Confidence scoring  
→ Downstream decision

Each step is independent and can be replaced without affecting the rest of the pipeline.  
The goal is correctness and clarity, not model complexity.

---

## Human-in-the-Loop Approach

Voice input is inherently ambiguous. The system is designed to assume this from the start.

Human review is required when:
- The confidence score falls below a defined threshold (e.g. 0.75)
- The product cannot be confidently identified
- The quantity is ambiguous or inferred from speech correction

When a human intervenes, the corrected result is treated as a learning signal.  
Over time, this feedback can be used to improve normalization rules, extraction logic, or model prompts.

Automation never silently overrides uncertainty.

---

## Automation Boundaries

### What Is Automated First

- Audio transcription
- Basic text cleanup
- Structured order extraction
- Confidence calculation
- Routing decisions (auto vs review)

These steps are deterministic and reversible.

### What Is Not Automated Initially

- Final order confirmation
- Pricing decisions
- Inventory commitments
- Exception resolution

These actions remain human-controlled until accuracy and confidence are consistently proven in production.

---

## Scaling Considerations

This solution is intentionally minimal.

Future improvements would include:
- Replacing rule-based extraction with LLM-based structured parsing
- Expanding domain vocabulary (products, units, slang)
- Supporting multiple languages and accents
- Using historical corrections to refine confidence scoring

The current structure supports these changes without redesign.
