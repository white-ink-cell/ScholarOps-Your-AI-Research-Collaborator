# Synthetic input

A long-running project contains:

- `.scholarops/STATE.md` saying: `FORMAL_MAIN_RESULT_STATUS=COMPLETE`;
- an artifact registry pointing to `results/main_results.csv`;
- the registered result file is missing;
- the latest execution log ends with a model error before result export;
- an old conversation summary says “the main results are finished.”

The user invokes `RE`.
