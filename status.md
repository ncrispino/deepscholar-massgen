### Status
- Ran baseline with 1 max new answer, minimax m2.7 (*note: the cutoff might be a problem since it might all be in the minimax memory*):
```
python -m massgen_runner.main --queries-file dataset/queries.csv --output-folder outputs/results_minimax --massgen-config configs/massgen.config.yaml --start-idx 0 --end-idx 33 &

python -m massgen_runner.main --queries-file dataset/queries.csv --output-folder outputs/results_minimax --massgen-config configs/massgen.config.yaml --start-idx 33 --end-idx 66 &
```

Ok great, this worked. Note though the dataset only 0-62 idxs, I was mistaken in thinking there would be more. Anyway, one query is broken due to timeout, rerunning:
```
python -m massgen_runner.main \
    --queries-file dataset/queries.csv \
    --output-folder outputs/results_minimax \
    --massgen-config configs/massgen.config.yaml \
    --start-idx 62 --end-idx 63
```

Also we are fixing some parsing to prefer intro.md over answer.txt, and fixing query 35 accordingly.

#### Parsing rules (in `_read_final_answer_from_result_paths`, `massgen_runner/main.py`)

The agent system message tells the model to write the final Related Works to `intro.md` in its workspace, but MassGen also writes a sibling `answer.txt`. Either file can be the wrong one to pick:
- Sometimes `answer.txt` is just narration ("Let me search...") while `intro.md` has the real content (e.g. query 35).
- Sometimes the agent leaves `intro.md` as a tiny stub (e.g. query 19: `"# Count words in Related Works section"`) and the real content is in `answer.txt`.
- Sometimes `answer.txt` runs away to ~100KB while `intro.md` is the cleaner canonical version (e.g. query 39).

Resolution order — first match wins:

1. **Pass 1 — preferred candidates with substantial content** (`>= 500 bytes` after stripping), in this order:
   1. `<final_answer_path>/<selected_agent>/workspace/intro.md`
   2. `<final_answer_path>/<selected_agent>/answer.txt`
   3. Any other `intro.md` under `final_answer_path`
   4. Any `final_report.md`
   5. Any other `answer.txt`
2. **Pass 2 — same priority list, but accept any non-empty file** (handles legitimately short outputs).
3. **Pass 3 — fallback** to any `*.md` / `*.txt` under `final_answer_path`.
4. **Last resort:** `result["final_answer"]` from the in-memory dict.

The 500-byte threshold avoids picking stub files but is well below the smallest legitimate Related Works section observed (~3000 bytes). Both `final_report.md` and `intro.md` in the per-query output dir are written from this same picked text.
