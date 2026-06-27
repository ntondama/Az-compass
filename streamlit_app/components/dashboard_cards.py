import streamlit as st


def metric_card(title, value, delta="", emoji="📊"):

    st.markdown(
        f"""
<div style="
padding:20px;
border-radius:12px;
background:white;
box-shadow:0 2px 10px rgba(0,0,0,.08);
border-left:6px solid #0F62FE;
">

<h5>{emoji} {title}</h5>

<h2>{value}</h2>

<p style="color:green;">
{delta}
</p>

</div>

""",
        unsafe_allow_html=True,
    )
