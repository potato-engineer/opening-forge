import chess
import json
import os

def print_board(board):
    print(board)
    print("\nFEN:", board.fen())


def load_openings():
    openings = []

    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "eco.tsv"
    )

    # print("DEBUG FILE PATH:", file_path)

    if not os.path.exists(file_path):
        print("❌ FILE NOT FOUND")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)  # skip header row

        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split("\t")

            if len(parts) != 3:
                print("BAD LINE:")
                print(repr(line))
                print("PARTS:", len(parts))
                continue

            eco, name, pgn = parts

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

def load_evaluations():
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "opening_evals.json"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    eval_map = {}

    for entry in data:
        eval_map[entry["name"]] = entry

    return eval_map

def build_index(openings):
    index = {}

    for opening in openings:
        first_move = opening["moves"][0]

        if first_move not in index:
            index[first_move] = []

        index[first_move].append(opening)

    return index


def detect_opening(history, index):
    if not history:
        return None

    candidates = index.get(history[0], [])

    best_match = None

    for opening in candidates:
        moves = opening["moves"]

        # Opening moves must be completely contained
        # in the played history
        if len(moves) > len(history):
            continue

        if history[:len(moves)] == moves:
            if (
                best_match is None
                or len(moves) > len(best_match["moves"])
            ):
                best_match = opening

    return best_match


def main():
    board = chess.Board()
    history = []

    openings = load_openings()
    index = build_index(openings)
    evaluations = load_evaluations()

    print(f"Loaded {len(openings)} openings")

    while True:
        move = input("Enter move (or 'exit'): ").strip()

        if move.lower() == "exit":
            break

        san_move = move.strip()

        try:
            board.push_san(san_move)
            history.append(san_move)
        except Exception as e:
            print("Invalid move:", e)
            continue

    print_board(board)
    print("\nMove list:", history)

    opening = detect_opening(history, index)

    print("\nOpening Name:")
    if opening:
        print(opening["name"], f"({opening['eco']})")

        eval_data = evaluations.get(opening["name"])

        if eval_data:
            print(f"Evaluation: {eval_data['evaluation'] / 100:.2f}")
            print(f"Best Move: {eval_data['best_move']}")
            print("PV:", " ".join(eval_data["pv"]))

    else:
        print("Unknown Opening")


if __name__ == "__main__":
    main()