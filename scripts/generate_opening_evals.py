import json
import chess
import chess.engine
from tqdm import tqdm

STOCKFISH_PATH = "engine/stockfish-windows-x86-64-avx2.exe"

INPUT_FILE = "data/opening_fens.json"
OUTPUT_FILE = "data/opening_evals.json"

DEPTH = 15


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    openings = json.load(f)

# # TEST MODE
# openings = openings[:10]

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

results = []

for opening in tqdm(openings):
    board = chess.Board(opening["fen"])

    info = engine.analyse(
        board,
        chess.engine.Limit(depth=DEPTH)
    )

    score = info["score"].white()

    if score.is_mate():
        evaluation = f"M{score.mate()}"
    else:
        evaluation = round(score.score() / 100.0, 2)

    pv_moves = []
    pv = info.get("pv", [])

    temp_board = board.copy()

    for move in pv[:5]:
        pv_moves.append(temp_board.san(move))
        temp_board.push(move)

    best_move = pv_moves[0] if pv_moves else None

    results.append({
        "eco": opening["eco"],
        "name": opening["name"],
        "fen": opening["fen"],
        "evaluation": evaluation,
        "best_move": best_move,
        "pv": pv_moves
    })

engine.quit()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved {len(results)} evaluations to {OUTPUT_FILE}")