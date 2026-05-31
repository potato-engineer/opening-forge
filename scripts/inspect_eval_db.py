import zstandard as zstd
import json

FILE = "data/lichess_db_eval.jsonl.zst"

def stream_lines(file_path):
    with open(file_path, "rb") as f:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(f) as reader:
            buffer = ""
            while True:
                chunk = reader.read(16384)
                if not chunk:
                    break

                buffer += chunk.decode("utf-8", errors="ignore")
                lines = buffer.split("\n")

                for line in lines[:-1]:
                    yield line

                buffer = lines[-1]

def main():
    count = 0

    for line in stream_lines(FILE):
        try:
            obj = json.loads(line)
            print("\n--- ENTRY ---")
            print(obj)

            count += 1
            if count == 3:
                break

        except Exception:
            continue

if __name__ == "__main__":
    main()