# ♟️ Opening Forge

A data-driven chess opening analysis platform built on top of the complete Lichess ECO database.

Opening Forge helps players identify openings, explore variations, analyze positions, and discover openings that fit their style. The long-term vision is to combine opening theory, engine evaluations, and real-game statistics into a single open-source platform for chess players.

---

## ✨ Features

### Current Features

- Detect chess openings from user-entered moves
- Support for the complete Lichess ECO database
- Recognition of **3700+ openings and variations**
- Fast indexed lookup for opening identification
- SAN move validation using `python-chess`
- Deepest fully-reached opening detection
- Command-line interface for testing and exploration

### Planned Features

- Engine evaluation for every opening
- Opening popularity and win-rate statistics
- Opening explorer dashboard
- Opening recommendation system based on playstyle
- Position-to-opening recognition using FEN hashing
- PGN import and analysis
- Opening comparison tools
- Interactive web application
- Pokémon-style opening cards
- Personalized opening repertoire builder

---

## 🚀 Example

### Input

```text
e4
e5
Nf3
Nc6
Bc4
```

### Output

```text
Opening Name:
Italian Game (C50)
```

---

## 🏗️ Project Structure

```text
opening-forge/
│
├── data/
│   └── eco.tsv
│
├── src/
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

## 📚 Data Source

Opening Forge currently uses the Lichess ECO opening database.

The database contains:

- ECO codes
- Opening names
- Official move sequences
- Thousands of opening variations

Current database size:

```text
3704 openings
```

---

## ⚙️ How It Works

### Opening Parsing

Each opening is loaded from the ECO database and converted into a structured move list.

Example:

```text
C50 | Italian Game | 1. e4 e5 2. Nf3 Nc6 3. Bc4
```

becomes

```python
{
    "eco": "C50",
    "name": "Italian Game",
    "moves": ["e4", "e5", "Nf3", "Nc6", "Bc4"]
}
```

### Indexed Lookup

To avoid searching through thousands of openings repeatedly, openings are indexed by their first move.

Example:

```python
{
    "e4": [...],
    "d4": [...],
    "c4": [...],
    "Nf3": [...]
}
```

This significantly reduces the search space during opening detection.

### Opening Detection

Opening Forge identifies the deepest opening that has been fully reached.

Example:

| Moves Played | Result |
|-------------|---------|
| e4 d5 | Scandinavian Defense |
| e4 d5 exd5 | Scandinavian Defense |
| e4 d5 exd5 Nf6 | Scandinavian Defense: Modern Variation |

This approach mirrors how modern opening explorers behave.

---

## 🛠️ Installation

### Clone the repository

```bash
git clone https://github.com/AyushSinha2603/opening-forge.git
cd opening-forge
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python src/main.py
```

Example session:

```text
Enter move (or 'exit'): e4
Enter move (or 'exit'): e5
Enter move (or 'exit'): Nf3
Enter move (or 'exit'): Nc6
Enter move (or 'exit'): Bc4
Enter move (or 'exit'): exit

Opening Name:
Italian Game (C50)
```

---

## 🎯 Vision

Most opening tools focus on memorization.

Opening Forge aims to help players understand:

- Which openings fit their playstyle
- Which openings perform best statistically
- How engine evaluations compare across openings
- How popular openings evolve over time
- Which repertoires suit specific player profiles

The goal is to build an open-source platform that combines opening theory, engine analysis, and data science into a single experience.

---

## 🔮 Roadmap

### Phase 1 — Foundation ✅

- [x] ECO database integration
- [x] Opening parsing
- [x] Indexed lookup
- [x] Opening detection

### Phase 2 — Evaluation Engine

- [ ] Import Lichess evaluation database
- [ ] Generate FEN positions for all openings
- [ ] Attach engine evaluations to openings
- [ ] Build opening evaluation dataset

### Phase 3 — Analytics

- [ ] Popularity metrics
- [ ] Win-rate analysis
- [ ] Complexity scoring
- [ ] Aggression and risk metrics

### Phase 4 — Recommendation System

- [ ] Playstyle profiling
- [ ] Personalized opening suggestions
- [ ] Repertoire generation

### Phase 5 — Interactive Platform

- [ ] Dashboard
- [ ] Opening explorer
- [ ] Visual opening cards
- [ ] PGN analysis tools

---

## 🤝 Contributing

Contributions are welcome.

Whether you're interested in:

- Chess theory
- Python development
- Data engineering
- Analytics
- Machine learning
- Frontend development
- UI/UX design

feel free to open an issue, start a discussion, or submit a pull request.

---

## 📄 License

This project is currently under active development.

A formal open-source license will be added soon.

---

## ⭐ Support

If you find the project interesting, consider starring the repository.

Feedback, ideas, feature requests, and contributions are always appreciated.

---

> Opening Forge is an attempt to transform raw opening theory into actionable chess insights using data, engines, and analytics.