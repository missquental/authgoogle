import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Ambil Code OAuth", layout="centered")

st.title("🔑 Ambil Code OAuth")

# Ambil query parameter
query_params = st.experimental_get_query_params()
code = query_params.get("code", [""])[0]

if code:
    st.success("Code berhasil ditemukan")

    st.text_input(
        "Code OAuth (siap copas)",
        value=code,
        key="oauth_code"
    )

    # Tombol Copy (JS)
    components.html(
        f"""
        <button onclick="navigator.clipboard.writeText('{code}')"
        style="
            padding:10px 16px;
            font-size:16px;
            border:none;
            border-radius:8px;
            background:#4CAF50;
            color:white;
            cursor:pointer;
        ">
        📋 Copy Code
        </button>
        """,
        height=60
    )

else:
    st.warning("Parameter `code` tidak ditemukan di URL.")
    st.info("Pastikan URL mengandung `?code=...`")
