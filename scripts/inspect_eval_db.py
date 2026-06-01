import json
import zstandard as zstd

file_path = "data/lichess_db_eval.jsonl.zst"

with open(file_path, "rb") as f:
    dctx = zstd.ZstdDecompressor()

    with dctx.stream_reader(f) as reader:
        text = reader.read(500000).decode("utf-8")

lines = text.splitlines()

print("Lines found:", len(lines))

for i in range(5):
    entry = json.loads(lines[i])

    print("\nENTRY", i + 1)
    print("FEN:", entry["fen"])

    first_eval = entry["evals"][0]
    first_pv = first_eval["pvs"][0]

    print("Keys:", first_pv.keys())
    print("PV:", first_pv)