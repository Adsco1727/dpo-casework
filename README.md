# dpo-casework

Thin Wave 6 casework queue layer that consumes dpo-ledger-tools.

## Scope

- Read pending clause-queue rows from the shared ledger
- Validate intended casework action payloads
- Write deterministic clause-queue updates through shared ledger APIs

## Constraints

- No direct schema ownership or duplication
- No external automation execution in this bootstrap
- No UI layer in this repo bootstrap

## Dependency

- dpo-ledger-tools is the required upstream package

## Tests

- Read clause-queue path
- Validate payload path
- Write deterministic clause-queue update path
DPO ecosystem repository: dpo-casework
