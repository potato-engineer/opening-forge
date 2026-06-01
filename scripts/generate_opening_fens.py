import chess
import json
import os


def load_openings():
    openings = []

    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "eco.tsv"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)

        for line in f:
            line = line.strip()

            if not line:
                continue

            eco, name, pgn = line.split("\t")

            moves = []

            for token in pgn.split():
                if token.endswith("."):
                    continue

                moves.append(token)

            openings.append({
                "eco": eco,
                "name": name,
                "moves": moves
            })

    return openings


def generate_fens(openings):
    results = []

    for opening in openings:
        board = chess.Board()

        try:
            for move in opening["moves"]:
                board.push_san(move)

            results.append({
                "eco": opening["eco"],
                "name": opening["name"],
                "fen": board.fen()
            })

        except Exception:
            print("Skipped:", opening["name"])

    return results


def main():
    openings = load_openings()

    print(f"Loaded {len(openings)} openings")

    results = generate_fens(openings)

    output_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "opening_fens.json"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Generated {len(results)} opening positions")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()