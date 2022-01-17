# edit-distance

- The minimum edit distance between two strings
- Is the minimum number of editing options
  - Insertion
  - Deletion
  - Substitution
- Needed to transform one to another

Example:

```
I N T E * N T I O N
| | | | | | | | | |
* E X E C U T I O N
d s s   i s
```
- If one operation has a cost of 1
  - Distance between these is 5
- If substitutions cost 2 (Levenshtein)
  - Distance between them is 8

--

Setup
```bash
python3 -m venv .venv
source .venv/bin/activate  # . activate.sh
pip install -r requirements.txt
```

Debug Script
```bash
python3 edit_distance.py tomayto tomahto --log=debug
```

Run Pre-commit
```bash
pre-commit run --all-files
```

TODO:
- [X] Add Tests
- [X] Add CI
- [ ] Make pip package
