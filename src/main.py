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
        for line in f:
            line = line.strip()
            if not line:
                continue

            eco, name, moves = line.split("|")

            openings.append({
                "eco": eco,
                "name": name,
                "moves": moves.split()
            })

    return openings


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
    best_score = 0

    for opening in candidates:
        moves = opening["moves"]

        match_len = 0

        for i in range(min(len(history), len(moves))):
            if history[i] == moves[i]:
                match_len += 1
            else:
                break

        if match_len > best_score:
            best_score = match_len
            best_match = opening

    return best_match


def main():
    board = chess.Board()
    history = []

    openings = load_openings()
    index = build_index(openings)

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
    else:
        print("Unknown Opening")


if __name__ == "__main__":
    main()