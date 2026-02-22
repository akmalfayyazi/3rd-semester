import os
import json
from typing import List, Dict, Any


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
HIGH_SCORE_PATH = os.path.join(DATA_DIR, "high_scores.json")


class HighScoreManager:
    def __init__(self, max_entries: int = 10):
        self.max_entries = max_entries
        os.makedirs(DATA_DIR, exist_ok=True)
        self.scores: List[Dict[str, Any]] = self._load_scores()

    def _load_scores(self) -> List[Dict[str, Any]]:
        if not os.path.exists(HIGH_SCORE_PATH):
            return []
        try:
            with open(HIGH_SCORE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
        except Exception:
            pass
        return []

    def _save_scores(self):
        with open(HIGH_SCORE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=2)

    def add_score(self, name: str, score: int):
        self.scores.append({"name": name, "score": int(score)})
        # Urutkan dari score terbesar ke terkecil
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        # Batasi jumlah entri
        self.scores = self.scores[: self.max_entries]
        self._save_scores()

    def get_top_scores(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self.scores[:limit]