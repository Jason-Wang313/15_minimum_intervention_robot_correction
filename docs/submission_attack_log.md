# Submission Attack Log

Checked: 2026-06-13 00:12:34 +01:00

## Hostile Round 1: The certificate assumes the update channel is exactly known

Result: Recoverable.

Action: Added estimated-update-channel stress. UBC solves using a noisy `H_hat` and is evaluated against the true future margins. Unguarded success drops to 0.330 at sigma 0.10 and 0.260 at sigma 0.20.

## Hostile Round 2: A robust version may need larger corrections

Result: Claim narrowed.

Action: Added a guarded variant that inflates the required margins. It reaches 0.750 success at sigma 0.10 and 0.600 at sigma 0.20, but the manuscript now says this gives up the exact minimum-correction interpretation.

## Hostile Round 3: The paper reads too strong for a synthetic local certificate

Result: Claim narrowed.

Action: The abstract, results, limitations, claims ledger, and reviewer response now emphasize that the guarantee is local, learner-relative, and conditional on a trusted or validated update Jacobian.
