import base64
import html
import random
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Eyron James Baldomero | Profile",
    page_icon="👋",
    layout="wide",
)

if "theme" not in st.session_state:
    st.session_state.theme = "Light"
if "greeting_index" not in st.session_state:
    st.session_state.greeting_index = 0
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = []

PHOTO_PATH = Path(__file__).resolve().parent / "ej.jpeg"
if not PHOTO_PATH.is_file():
    st.error(f"Profile photo not found: {PHOTO_PATH.name}")
    st.stop()

with PHOTO_PATH.open("rb") as photo_file:
    photo_data = base64.b64encode(photo_file.read()).decode("ascii")

name = "Eyron James Baldomero"
role = "Personal Profile"
introduction = "Welcome to my profile."
photo_alt = html.escape(f"Profile photo of {name}", quote=True)
greetings = (
    "Hey there! Welcome to my profile!",
    "Feel free to explore!",
    "Nice to meet you!",
    "I’m so happy you stopped by!",
    "Ready for a little look around?",
)
quotes = (
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Small steps every day become remarkable journeys.", "Unknown"),
    ("Your time is limited, so make it meaningful.", "Steve Jobs"),
    ("Learn continuously. Improve patiently.", "Anonymous"),
)

manila_now = datetime.now(ZoneInfo("Asia/Manila"))
manila_hour = manila_now.hour
if manila_hour < 12:
    time_greeting = "Good morning"
elif manila_hour < 18:
    time_greeting = "Good afternoon"
else:
    time_greeting = "Good evening"


def show_next_greeting():
    st.session_state.greeting_index = (
        st.session_state.greeting_index + 1
    ) % len(greetings)


st.markdown(
    """
    <style>
    :root {
        color-scheme: light;
    }
    .stApp {
        background:
            radial-gradient(ellipse at 5% 0%, #e8f1ff 0, transparent 36%),
            linear-gradient(145deg, #f8faff 0%, #f6f7fc 55%, #fff8f2 100%);
        color: #23304a;
    }
    .stApp.dark-theme {
        background:
            radial-gradient(ellipse at 5% 0%, #1a315e 0, transparent 38%),
            linear-gradient(145deg, #10182a 0%, #162238 55%, #241e1a 100%);
        color: #edf3ff;
    }
    .theme-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 18px;
    }
    .clock-card {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        min-height: 44px;
        padding: 8px 14px;
        border: 1px solid #e1e8f4;
        border-radius: 14px;
        background: rgba(255,255,255,.82);
        color: #354662;
        box-shadow: 0 8px 24px rgba(34,52,94,.06);
    }
    .dark-theme .clock-card,
    .dark-theme .welcome-card,
    .dark-theme .content-card,
    .dark-theme .interest-card {
        border-color: #334158;
        background: rgba(22,34,56,.94);
        color: #edf3ff;
    }
    .dark-theme .section-heading,
    .dark-theme .interest-title,
    .dark-theme .hero-name {
        color: #f4f7ff;
    }
    .dark-theme .interest-copy,
    .dark-theme .detail-copy,
    .dark-theme .content-card p,
    .dark-theme .footer,
    .dark-theme .music-caption,
    .dark-theme .music-artist {
        color: #b6c2d8;
    }
    .dark-theme .music-card {
        border-color: rgba(214,225,255,.22);
        background: linear-gradient(145deg, rgba(35,47,74,.86), rgba(25,34,56,.76));
        color: #edf3ff;
    }
    .dark-theme .music-heading,
    .dark-theme .music-track-title {
        color: #f4f7ff;
    }
    .dark-theme .music-kicker,
    .dark-theme .music-caption,
    .dark-theme .music-artist,
    .dark-theme .music-album {
        color: #c4cde0;
    }
    .dark-theme .music-player-shell {
        border-color: rgba(222,231,255,.18);
        background: rgba(12,19,34,.48);
    }
    .dark-theme .speech-bubble {
        background: #263650;
        color: #edf3ff;
    }
    .dark-theme .project-note {
        background: #20324f;
        color: #ced9ed;
    }
    .block-container {
        max-width: 1120px;
        padding: 2.8rem 1.4rem 2rem;
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    .hero {
        position: relative;
        overflow: hidden;
        padding: clamp(24px, 5vw, 52px);
        border: 1px solid rgba(255,255,255,.7);
        border-radius: 30px;
        background: linear-gradient(130deg, #172554 0%, #2346a5 58%, #4774d7 100%);
        box-shadow: 0 24px 60px rgba(35, 70, 165, .17);
        color: white;
        animation: arrive .7s ease-out both;
    }
    .hero::after {
        position: absolute;
        top: -110px;
        right: -80px;
        width: 290px;
        height: 290px;
        border: 1px solid rgba(255,255,255,.14);
        border-radius: 50%;
        content: "";
        box-shadow: 0 0 0 34px rgba(255,255,255,.035), 0 0 0 68px rgba(255,255,255,.025);
        pointer-events: none;
    }
    .hero-photo {
        width: min(100%, 300px);
        aspect-ratio: 1 / 1;
        margin: 0 auto;
        overflow: hidden;
        border: 5px solid rgba(255,255,255,.78);
        border-radius: 28px;
        box-shadow: 0 18px 42px rgba(8, 20, 58, .3);
        transform: rotate(-2deg);
        transition: transform .3s ease, box-shadow .3s ease;
    }
    .hero-photo:hover {
        box-shadow: 0 22px 48px rgba(8, 20, 58, .38);
        transform: rotate(0) scale(1.025);
    }
    .hero-photo img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .hero-copy {
        position: relative;
        z-index: 1;
        padding: 12px 0;
    }
    .eyebrow {
        margin: 0 0 14px;
        color: #c9d8ff;
        font-size: .78rem;
        font-weight: 800;
        letter-spacing: .15em;
        text-transform: uppercase;
    }
    .hero-name {
        margin: 0 0 12px;
        color: white;
        font-size: clamp(2.2rem, 5vw, 3.8rem);
        font-weight: 850;
        letter-spacing: -.045em;
        line-height: 1.06;
    }
    .hero-role {
        margin: 0 0 18px;
        color: #d7e3ff;
        font-size: 1.15rem;
        font-weight: 650;
    }
    .hero-intro {
        max-width: 540px;
        margin: 0;
        color: #edf2ff;
        font-size: 1.08rem;
        line-height: 1.75;
    }
    .welcome-card, .content-card, .interest-card {
        border: 1px solid #e8edf6;
        border-radius: 22px;
        background: rgba(255,255,255,.88);
        box-shadow: 0 12px 35px rgba(34, 52, 94, .055);
        transition: transform .22s ease, box-shadow .22s ease;
    }
    .welcome-card:hover, .content-card:hover, .interest-card:hover {
        box-shadow: 0 16px 38px rgba(34, 52, 94, .10);
        transform: translateY(-3px);
    }
    .welcome-card {
        display: flex;
        align-items: center;
        gap: 18px;
        margin: 24px 0 28px;
        padding: 20px 24px;
    }
    .assistant-avatar {
        display: grid;
        width: 58px;
        height: 58px;
        flex: 0 0 58px;
        place-items: center;
        border-radius: 20px;
        background: linear-gradient(145deg, #fff0cf, #ffd8b5);
        box-shadow: inset 0 0 0 1px rgba(235, 155, 94, .16);
        font-size: 1.8rem;
        animation: bob 2.8s ease-in-out infinite;
    }
    .speech-bubble {
        position: relative;
        margin: 0;
        padding: 13px 17px;
        border-radius: 16px;
        background: #f0f5ff;
        color: #263b70;
        font-weight: 650;
        line-height: 1.5;
    }
    .assistant-label {
        display: block;
        margin-bottom: 3px;
        color: #74819b;
        font-size: .73rem;
        font-weight: 750;
        letter-spacing: .1em;
        text-transform: uppercase;
    }
    .section-heading {
        margin: 6px 0 15px;
        color: #1d2b49;
        font-size: 1.55rem;
        font-weight: 800;
        letter-spacing: -.025em;
    }
    .content-card {
        padding: clamp(20px, 4vw, 30px);
    }
    .content-card p {
        color: #53617b;
        line-height: 1.8;
    }
    .interest-card {
        min-height: 145px;
        padding: 22px;
    }
    .interest-icon {
        font-size: 1.8rem;
    }
    .interest-title {
        margin: 10px 0 5px;
        color: #243454;
        font-weight: 750;
    }
    .interest-copy, .detail-copy {
        color: #62708a;
        line-height: 1.65;
    }
    .music-card {
        position: relative;
        isolation: isolate;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,.72);
        border-radius: 30px;
        background: linear-gradient(145deg, rgba(255,255,255,.72), rgba(244,239,255,.56));
        -webkit-backdrop-filter: blur(28px) saturate(175%);
        backdrop-filter: blur(28px) saturate(175%);
        box-shadow: 0 28px 70px rgba(70, 72, 125, .17),
                    inset 0 1px 0 rgba(255,255,255,.8);
        color: #23304a;
        transition: transform .35s ease, box-shadow .35s ease;
    }
    .music-card::before {
        position: absolute;
        z-index: 0;
        inset: 0;
        background:
            radial-gradient(ellipse at 8% 10%, rgba(255,190,211,.5), transparent 37%),
            radial-gradient(ellipse at 96% 28%, rgba(147,171,241,.38), transparent 42%),
            radial-gradient(ellipse at 44% 100%, rgba(244,208,184,.3), transparent 48%);
        content: "";
        pointer-events: none;
    }
    .music-card::after {
        position: absolute;
        z-index: 2;
        top: 0;
        right: 12%;
        left: 12%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,.95), transparent);
        content: "";
        pointer-events: none;
    }
    .music-card:hover {
        box-shadow: 0 34px 78px rgba(70, 72, 125, .23),
                    inset 0 1px 0 rgba(255,255,255,.86);
        transform: translateY(-4px);
    }
    .music-inner {
        position: relative;
        z-index: 1;
        padding: 20px 16px 16px;
    }
    .music-kicker {
        margin: 0 0 4px;
        color: #77819a;
        font-size: .67rem;
        font-weight: 800;
        letter-spacing: .17em;
        text-align: center;
        text-transform: uppercase;
    }
    .music-heading {
        margin: 0;
        color: #202b45;
        font-size: clamp(1.45rem, 2.2vw, 1.85rem);
        font-weight: 820;
        letter-spacing: -.055em;
        text-align: center;
    }
    .music-caption {
        margin: 4px 0 17px;
        color: #69758e;
        font-size: .84rem;
        line-height: 1.5;
        text-align: center;
    }
    .music-player-shell {
        position: relative;
        overflow: hidden;
        width: 100%;
        aspect-ratio: 16 / 9;
        box-sizing: border-box;
        margin-bottom: 16px;
        padding: 5px;
        border: 1px solid rgba(255,255,255,.72);
        border-radius: 20px;
        background: rgba(255,255,255,.4);
        box-shadow: 0 8px 24px rgba(39, 48, 82, .1),
                    inset 0 1px 0 rgba(255,255,255,.72);
        -webkit-backdrop-filter: blur(18px) saturate(150%);
        backdrop-filter: blur(18px) saturate(150%);
        animation: artwork-float 6.5s ease-in-out infinite;
        transition: box-shadow .35s ease, transform .35s ease;
    }
    .music-card:hover .music-player-shell {
        box-shadow: 0 14px 34px rgba(39, 48, 82, .18),
                    inset 0 1px 0 rgba(255,255,255,.82);
        transform: translateY(-2px);
    }
    .music-player-shell iframe {
        display: block;
        width: 100%;
        height: 100%;
        border: 0;
        border-radius: 15px;
    }
    .music-meta {
        margin: 0 0 14px;
        text-align: center;
    }
    .music-track-title {
        margin: 0;
        color: #202b45;
        font-size: 1.34rem;
        font-weight: 850;
        letter-spacing: -.04em;
    }
    .music-artist {
        margin: 3px 0 0;
        color: #46536c;
        font-size: .91rem;
        font-weight: 730;
    }
    .music-album {
        margin: 2px 0 0;
        color: #77819a;
        font-size: .77rem;
        font-weight: 550;
    }
    .project-note {
        padding: 22px;
        border-radius: 18px;
        background: #f2f6ff;
        color: #4a5c7e;
        line-height: 1.75;
    }
    div[data-testid="stButton"] > button {
        min-height: 44px;
        border: 1px solid #dce5f6;
        border-radius: 13px;
        background: #fff;
        color: #24458f;
        font-weight: 700;
        transition: transform .18s ease, box-shadow .18s ease;
    }
    div[data-testid="stButton"] > button:hover {
        border-color: #b9c9ee;
        box-shadow: 0 7px 18px rgba(35, 70, 165, .12);
        color: #173a86;
        transform: translateY(-2px);
    }
    button[data-baseweb="tab"] {
        font-weight: 700;
    }
    [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
        color: #2346a5;
    }
    .footer {
        margin-top: 40px;
        padding: 20px 0 4px;
        border-top: 1px solid #e5eaf2;
        color: #78849b;
        text-align: center;
        font-size: .9rem;
    }
    @keyframes arrive {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes bob {
        0%, 100% { transform: translateY(0) rotate(-3deg); }
        50% { transform: translateY(-6px) rotate(3deg); }
    }
    @keyframes artwork-float {
        0%, 100% { transform: translateY(0) rotate(-.6deg); }
        50% { transform: translateY(-7px) rotate(.6deg); }
    }
    @media (max-width: 640px) {
        .block-container { padding: 1.4rem .8rem 1.5rem; }
        .hero { border-radius: 22px; }
        .hero-photo { width: min(70vw, 240px); }
        .welcome-card { align-items: flex-start; gap: 12px; padding: 16px; }
        .assistant-avatar { width: 48px; height: 48px; flex-basis: 48px; }
        .music-card { max-width: 440px; margin: 0 auto; }
    }
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: .01ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
            transition-duration: .01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

theme_choice = st.toggle(
    "🌙 Dark mode",
    value=st.session_state.theme == "Dark",
)
st.session_state.theme = "Dark" if theme_choice else "Light"

if theme_choice:
    st.markdown(
        """
        <style>
        .stApp {
            background: radial-gradient(ellipse at 5% 0%, #1a315e 0, transparent 38%),
                        linear-gradient(145deg, #10182a 0%, #162238 55%, #241e1a 100%) !important;
            color: #edf3ff;
        }
        .welcome-card, .content-card, .interest-card,
        .clock-card, [data-testid="stTextInput"] > div,
        [data-testid="stTextArea"] > div {
            border-color: #334158 !important;
            background: rgba(22,34,56,.94) !important;
            color: #edf3ff !important;
        }
        .music-card {
            border-color: rgba(214,225,255,.22) !important;
            background: linear-gradient(145deg, rgba(35,47,74,.86), rgba(25,34,56,.76)) !important;
            color: #edf3ff !important;
        }
        .music-card::before {
            background:
                radial-gradient(ellipse at 8% 10%, rgba(171,133,190,.25), transparent 37%),
                radial-gradient(ellipse at 96% 28%, rgba(105,137,204,.24), transparent 42%),
                radial-gradient(ellipse at 44% 100%, rgba(180,137,139,.18), transparent 48%) !important;
        }
        .section-heading, .interest-title, .detail-copy,
        .interest-copy, .content-card p, .footer,
        .music-kicker, .music-caption, .music-artist, .music-album {
            color: #b6c2d8 !important;
        }
        .music-heading, .music-track-title { color: #f4f7ff !important; }
        .music-player-shell {
            border-color: rgba(222,231,255,.18) !important;
            background: rgba(12,19,34,.48) !important;
        }
        .speech-bubble { background: #263650 !important; color: #edf3ff !important; }
        .project-note { background: #20324f !important; color: #ced9ed !important; }
        div[data-testid="stButton"] > button {
            border-color: #40506a !important;
            background: #1c2b43 !important;
            color: #e8efff !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

clock_left, clock_right = st.columns([2, 1], vertical_alignment="center")
with clock_left:
    st.markdown(
        f"""
        <div class="clock-card">🇵🇭 <span><strong>{time_greeting}!</strong>
        &nbsp;Philippine Time · Asia/Manila</span></div>
        """,
        unsafe_allow_html=True,
    )
with clock_right:
    components.html(
        """
        <div id="clock" style="font-family:Arial,sans-serif;color:#354662;
             min-height:44px;display:flex;align-items:center;
             border:1px solid #e1e8f4;border-radius:14px;
             background:#fff;padding:8px 14px;box-sizing:border-box;
             box-shadow:0 8px 24px rgba(34,52,94,.06);"></div>
        <script>
        const updateClock = () => {
          document.getElementById("clock").textContent =
            new Intl.DateTimeFormat("en-PH", {
              timeZone:"Asia/Manila",
              weekday:"short",month:"short",day:"numeric",
              hour:"2-digit",minute:"2-digit",second:"2-digit"
            }).format(new Date());
        };
        updateClock();
        setInterval(updateClock, 1000);
        </script>
        """,
        height=62,
    )

photo_src = f"data:image/jpeg;base64,{photo_data}"
left, right, music_column = st.columns(
    [0.85, 1.5, 1.05],
    gap="large",
    vertical_alignment="center",
)

with left:
    st.markdown(
        f"""
        <div class="hero-photo">
            <img src="{photo_src}" alt="{photo_alt}">
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        f"""
        <div class="hero">
            <p class="eyebrow">A little corner of the internet</p>
            <h1 class="hero-name">{html.escape(time_greeting)}, I’m {html.escape(name)}!</h1>
            <p class="hero-role">{html.escape(role)}</p>
            <p class="hero-intro">{html.escape(introduction)}
            I’m glad you’re here. Take a look around and get to know me.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with music_column:
    st.markdown(
        """
        <section class="music-card" aria-label="My Soundtrack music player">
          <div class="music-inner">
            <header class="music-header">
              <p class="music-kicker">A little corner of my world</p>
              <h2 class="music-heading">My Soundtrack</h2>
              <p class="music-caption">A little piece of my world, on repeat.</p>
            </header>
            <div class="music-player-shell">
              <iframe
                  src="https://www.youtube-nocookie.com/embed/OiwtQDRpl7U?autoplay=1&amp;controls=1&amp;playsinline=1&amp;rel=0"
                  title="LANY - XXL (Official Music Video)"
                  allow="autoplay; encrypted-media; picture-in-picture; web-share"
                  referrerpolicy="strict-origin-when-cross-origin"
                  allowfullscreen
              ></iframe>
            </div>
            <div class="music-meta">
              <h3 class="music-track-title">XXL</h3>
              <p class="music-artist">LANY</p>
              <p class="music-album">a beautiful blur</p>
            </div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

assistant_col, action_col = st.columns([5, 1.2], vertical_alignment="center")
with assistant_col:
    st.markdown(
        f"""
        <div class="welcome-card">
            <div class="assistant-avatar" aria-hidden="true">👋</div>
            <p class="speech-bubble">
                <span class="assistant-label">Your friendly guide</span>
                {html.escape(greetings[st.session_state.greeting_index])}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with action_col:
    st.button("Say hello 👋", on_click=show_next_greeting, use_container_width=True)

quote_text, quote_author = quotes[st.session_state.quote_index]
quote_col, quote_action = st.columns([5, 1.2], vertical_alignment="center")
with quote_col:
    st.markdown(
        f"""
        <div class="content-card">
            <span class="assistant-label">A thought for today</span>
            <p style="margin:8px 0 4px;font-size:1.12rem;">
                “{html.escape(quote_text)}”
            </p>
            <div class="detail-copy">— {html.escape(quote_author)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with quote_action:
    def next_quote():
        choices = [index for index in range(len(quotes))
                   if index != st.session_state.quote_index]
        st.session_state.quote_index = random.choice(choices)

    st.button("Another quote ✨", on_click=next_quote, use_container_width=True)

about_tab, interests_tab, projects_tab, contact_tab = st.tabs(
    ["About Me", "My Interests", "My Projects", "Contact Me"]
)

with about_tab:
    st.markdown('<h2 class="section-heading">A little about me</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="content-card">
            <p>Welcome to my personal profile! This is my little space on the web
            where you can learn more about me. I’m excited to share my profile
            with you and connect with others.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with interests_tab:
    st.markdown('<h2 class="section-heading">Things I enjoy exploring</h2>', unsafe_allow_html=True)
    interest_columns = st.columns(4, gap="medium")
    interests = [
        ("💻", "Technology", "Discovering useful tools and new ideas."),
        ("🐍", "Python", "Learning by building with Python."),
        ("🌐", "Web & apps", "Exploring web and app development."),
        ("📚", "Learning", "Always curious and learning new things."),
    ]
    for column, (icon, title, description) in zip(interest_columns, interests):
        with column:
            st.markdown(
                f"""
                <div class="interest-card">
                    <div class="interest-icon">{icon}</div>
                    <div class="interest-title">{title}</div>
                    <div class="interest-copy">{description}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

with projects_tab:
    st.markdown('<h2 class="section-heading">A work in progress</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="content-card">
            <div class="project-note">
                ✨ I’m looking forward to sharing projects here. In the meantime,
                feel free to explore my interests and check back for future updates.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with contact_tab:
    st.markdown('<h2 class="section-heading">Let’s connect</h2>', unsafe_allow_html=True)
    contact_left, contact_right = st.columns(2, gap="large")
    with contact_left:
        st.markdown(
            """
            <div class="content-card">
                <div class="section-heading">📍 Location</div>
                <div class="detail-copy">Hinatuan, Surigao del Sur, Philippines</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with contact_right:
        st.markdown(
            """
            <div class="content-card">
                <div class="section-heading">✉️ Email</div>
                <div class="detail-copy">ejbaldomero.nemsu@gmail.com</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('<h2 class="section-heading">Visitor feedback</h2>', unsafe_allow_html=True)
    with st.form("visitor_feedback", clear_on_submit=True):
        feedback_name = st.text_input("Name (optional)")
        feedback_message = st.text_area("Share a message", max_chars=500)
        feedback_rating = st.slider("Rating", min_value=1, max_value=5, value=5)
        feedback_submitted = st.form_submit_button(
            "Send feedback",
            use_container_width=True,
        )
    if feedback_submitted:
        if feedback_message.strip():
            st.session_state.feedback.append({
                "name": feedback_name.strip() or "A visitor",
                "message": feedback_message.strip(),
                "rating": feedback_rating,
            })
            st.toast("Thank you for your feedback! 😊")
        else:
            st.warning("Please add a message before sending.")

    st.button(
        "Thanks for visiting!",
        on_click=lambda: st.toast("Thanks for stopping by my profile! 😊"),
    )

st.markdown(
    '<div class="footer">Made with care and Python using Streamlit</div>',
    unsafe_allow_html=True,
)
