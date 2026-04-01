#!/usr/bin/env python3
"""
HyperSearch - Semantic Search Engine for HyperGold AI Hub
Allows AI agents and humans to discover compatible components programmatically.
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    SEMANTIC_AVAILABLE = True
except ImportError:
    SEMANTIC_AVAILABLE = False


class HyperSearch:
    """Semantic search over the HyperGold AI Hub metadata index."""

    def __init__(self, index_path: str = "metadata/index.json"):
        self.index_path = Path(index_path)
        self.assets = self._load_index()
        self.model = None
        if SEMANTIC_AVAILABLE:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self._embeddings = self._build_embeddings()

    def _load_index(self) -> List[Dict]:
        if not self.index_path.exists():
            raise FileNotFoundError(f"Index not found: {self.index_path}")
        with open(self.index_path) as f:
            data = json.load(f)
        return data.get("assets", [])

    def _build_embeddings(self):
        texts = [
            f"{a['name']} {a.get('description', '')} {' '.join(a.get('tags', []))}"
            for a in self.assets
        ]
        return self.model.encode(texts, convert_to_numpy=True)

    def query(self, query_text: str, top_k: int = 5) -> List[Dict]:
        """Semantic search — returns top_k most relevant assets."""
        if not SEMANTIC_AVAILABLE or self.model is None:
            return self._keyword_search(query_text, top_k)
        import numpy as np
        q_emb = self.model.encode([query_text], convert_to_numpy=True)
        scores = np.dot(self._embeddings, q_emb.T).squeeze()
        top_indices = np.argsort(scores)[::-1][:top_k]
        return [
            {**self.assets[i], "score": float(scores[i])}
            for i in top_indices
        ]

    def _keyword_search(self, query: str, top_k: int) -> List[Dict]:
        """Fallback keyword search when sentence-transformers not available."""
        q_lower = query.lower()
        results = []
        for asset in self.assets:
            text = f"{asset['name']} {' '.join(asset.get('tags', []))}".lower()
            score = sum(1 for w in q_lower.split() if w in text)
            if score > 0:
                results.append({**asset, "score": score})
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

    def list_all(self) -> List[Dict]:
        return self.assets

    def get_by_type(self, asset_type: str) -> List[Dict]:
        return [a for a in self.assets if a.get("type") == asset_type]


def main():
    parser = argparse.ArgumentParser(description="HyperSearch - AI Hub Semantic Search")
    parser.add_argument("--query", "-q", help="Search query", default=None)
    parser.add_argument("--top", "-k", type=int, default=5, help="Number of results")
    parser.add_argument("--type", "-t", help="Filter by asset type", default=None)
    parser.add_argument("--list", action="store_true", help="List all assets")
    args = parser.parse_args()

    hub = HyperSearch()

    if args.list:
        for a in hub.list_all():
            print(f"[{a['type'].upper()}] {a['name']} — {a['path']}")
    elif args.type:
        for a in hub.get_by_type(args.type):
            print(f"{a['name']} ({a['version']}) — {a['path']}")
    elif args.query:
        results = hub.query(args.query, top_k=args.top)
        print(f"\n🔍 Top {args.top} results for: '{args.query}'\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. [{r['type'].upper()}] {r['name']}")
            print(f"   Path: {r['path']}")
            print(f"   Tags: {', '.join(r.get('tags', []))}")
            print(f"   Score: {r.get('score', 'N/A'):.3f}\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
