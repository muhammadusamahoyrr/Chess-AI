
# ♟️ Chess Engine

A terminal-based chess game in Python with a smart AI opponent, Unicode board, and algebraic notation input.

---

## 🚀 Features

- ♔ **Complete Rules**: Standard chess logic — piece movement, captures, turns  
- 🧠 **AI Opponent**: Alpha-beta pruning with iterative deepening  
- 🎲 **Adjustable Difficulty**: Configure AI depth (1–5+)  
- 🔠 **Algebraic Input**: Simple move format (e.g., `e2 e4`)  
- ♟ **Unicode Board**: Clean visual layout using Unicode pieces  
- 📈 **Smart Evaluation**: Considers material, mobility, center control, king safety

---

## 🛠 Requirements

- Python 3.6+
- UTF-8 supported terminal

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/chess-engine.git
cd chess-engine
python chess.py
```

---

## 🎮 How to Play

- 📥 Input moves like: `e2 e4`, `g1 f3`  
- ❌ Type `quit` or `exit` to end  
- 📊 AI evaluates and replies after each move  

---

### 📋 Sample Board
```
  a   b   c   d   e   f   g   h
  -----------------------------
8 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | 8
7 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | 7
6 |   |   |   |   |   |   |   |   | 6
5 |   |   |   |   |   |   |   |   | 5
4 |   |   |   |   |   |   |   |   | 4
3 |   |   |   |   |   |   |   |   | 3
2 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | 2
1 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | 1
  -----------------------------
  a   b   c   d   e   f   g   h
```

---

## 🧠 AI Overview

- 🔍 **Alpha-Beta Pruning**: Fast, optimized move search  
- 🕒 **Iterative Deepening**: Searches deeper over time  
- 📊 **Evaluation**:  
  - Pawn: 100  
  - Knight: 320  
  - Bishop: 330  
  - Rook: 500  
  - Queen: 900  
  - King: 20,000

Modify AI level in `main()`:
```python
ai_depth = 3  # Change between 1–5+
```

---

## 📂 Key Functions

- `initialize_board()` – Setup pieces  
- `print_board()` – Display board in terminal  
- `is_valid_move()` – Move legality check  
- `evaluate_board()` – Score the position  
- `alpha_beta()` – AI search algorithm  
- `get_best_move()` – Get optimal move  

---

## ⚠️ Known Limitations

- 🚫 Castling, En Passant, Pawn Promotion not implemented  
- ⚔️ King capture ends game (basic win detection)  
- 🔁 No save/load or move history  

---

## 🧩 To-Do

- [ ] Castling & En Passant  
- [ ] Pawn Promotion  
- [ ] Checkmate/Stalemate logic  
- [ ] Opening Book  
- [ ] Save/Load Game  
- [ ] Multiplayer Support  
- [ ] Game History & Analysis  

---

## 🤝 Contributing

1. Fork repo  
2. Create branch: `feature/amazing-feature`  
3. Commit: `git commit -m "Add amazing feature"`  
4. Push: `git push origin feature/amazing-feature`  
5. PR it!

---

## 📝 License

MIT © [Your Name] — See [LICENSE](LICENSE)

---

## 🙏 Acknowledgments

- Unicode chess characters  
- Alpha-beta pruning search  
- Standard algebraic notation  

> _“When you see a good move, look for a better one.” – Emanuel Lasker_
