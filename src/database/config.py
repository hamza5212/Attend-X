import os
from pathlib import Path
import tomllib

import streamlit as st

from supabase import Client, create_client  # type: ignore[reportMissingImports]


def _load_secrets_from_file(path: str | Path) -> dict:
    try:
        file_path = Path(path)
        if not file_path.exists():
            return {}
        with file_path.open("rb") as file:
            data = tomllib.load(file)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _get_supabase_client() -> Client | None:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        for candidate in (
            Path(".streamlit/secrets.toml"),
            Path("streamlit/secrets.toml"),
            Path.home() / ".streamlit" / "secrets.toml",
        ):
            secrets = _load_secrets_from_file(candidate)
            url = url or secrets.get("SUPABASE_URL")
            key = key or secrets.get("SUPABASE_KEY")
            if url and key:
                break

    if not url or not key:
        try:
            url = url or st.secrets.get("SUPABASE_URL")
            key = key or st.secrets.get("SUPABASE_KEY")
        except Exception:
            return None

    if not url or not key:
        return None

    return create_client(url, key)


supabase: Client | None = _get_supabase_client()