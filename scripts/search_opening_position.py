import json
import zstandard as zstd
import chess

target_fen = chess.Board().fen()

print("Searching for:")
print(target_fen)

found = False

with open("data/lichess_db_eval.jsonl.zst", "rb") as f:
    dctx = zstd.ZstdDecompressor()

    with dctx.stream_reader(f) as reader:
        text_stream = ""

        while True:
            chunk = reader.read(1024 * 1024)

            if not chunk:
                break

            text_stream += chunk.decode("utf-8")

            lines = text_stream.split("\n")
            text_stream = lines.pop()

            for line in lines:
                if not line.strip():
                    continue

                entry = json.loads(line)

                if entry["fen"] == target_fen:
                    print("\nFOUND!")
                    print(entry)
                    found = True
                    break

            if found:
                break

print("\nDone.")