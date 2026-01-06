# Design Note – Confidence-Based Routing

## Confidence Model

The system assigns a confidence score to each extracted order based on
deterministic and explainable signals.

Confidence is reduced when:
- Known ASR ambiguities are detected in transcription
- The product cannot be confidently identified
- Quantity is inferred rather than explicit

This avoids treating speech recognition output as ground truth.

---

## Routing Decision

A single confidence threshold controls automation behavior.

- confidence ≥ 0.75 → auto_process
- confidence < 0.75 → needs_human_review

This threshold is intentionally conservative. It favors correctness over
automation and can be tuned based on observed error rates.

---

## Human Review Strategy

Orders routed for review include explicit reasons explaining why confidence
was reduced.

This allows:
- Fast human correction
- Clear operator trust
- Feedback collection for future improvement

Automation never silently overrides uncertainty.

---

## Why This Approach

The goal is not maximum automation, but safe automation.

By making confidence and routing explicit, the system supports gradual
automation as data quality and model performance improve.
