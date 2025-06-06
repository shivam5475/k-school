import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Kirti's School - Love Animations",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(-45deg, #ffeef0, #ffe4e6, #fce7f3, #f3e8ff);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #ff8e8e, #ffa8a8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5em;
        font-weight: 700;
        margin-bottom: 30px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { 
            text-shadow: 0 0 20px rgba(255, 107, 107, 0.5);
            transform: scale(1);
        }
        to { 
            text-shadow: 0 0 30px rgba(255, 107, 107, 0.8);
            transform: scale(1.02);
        }
    }
    
    .love-container {
        position: relative;
        height: 300px;
        overflow: hidden;
        border-radius: 20px;
        background: linear-gradient(135deg, 
            rgba(255, 182, 193, 0.3) 0%, 
            rgba(255, 192, 203, 0.3) 25%,
            rgba(255, 160, 122, 0.3) 50%,
            rgba(255, 182, 193, 0.3) 75%,
            rgba(255, 192, 203, 0.3) 100%);
        border: 2px solid rgba(255, 107, 107, 0.3);
        margin: 20px 0;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    
    .floating-hearts {
        font-size: 3em;
        animation: float 3s ease-in-out infinite;
        color: #ff6b6b;
        text-shadow: 0 0 20px rgba(255, 107, 107, 0.7);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-30px) rotate(10deg); }
        50% { transform: translateY(-50px) rotate(-10deg); }
        75% { transform: translateY(-30px) rotate(5deg); }
    }
    
    .pulse-heart {
        font-size: 2em;
        animation: pulse 1.5s ease-in-out infinite;
        display: inline-block;
        margin: 0 10px;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.3); opacity: 1; }
        100% { transform: scale(1); opacity: 0.7; }
    }
    
    .romantic-quote {
        text-align: center;
        font-size: 1.4em;
        font-style: italic;
        color: #d63384;
        margin: 20px 0;
        padding: 20px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        animation: fadeInOut 4s ease-in-out infinite;
        border: 1px solid rgba(255, 107, 107, 0.2);
    }
    
    @keyframes fadeInOut {
        0%, 100% { opacity: 0.8; transform: scale(0.98); }
        50% { opacity: 1; transform: scale(1); }
    }
    
    .school-badge {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 15px 30px;
        border-radius: 25px;
        display: inline-block;
        margin: 20px;
        font-weight: 600;
        font-size: 1.2em;
        animation: bounce 3s ease-in-out infinite;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-15px); }
        60% { transform: translateY(-8px); }
    }
    
    .love-stats {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        border: 2px solid rgba(255, 107, 107, 0.2);
        animation: statsGlow 3s ease-in-out infinite;
    }
    
    @keyframes statsGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 107, 107, 0.2); }
        50% { box-shadow: 0 0 30px rgba(255, 107, 107, 0.4); }
    }
    
    .stat-item {
        text-align: center;
        margin: 20px;
        animation: statFloat 4s ease-in-out infinite;
    }
    
    .stat-item:nth-child(1) { animation-delay: 0s; }
    .stat-item:nth-child(2) { animation-delay: 1s; }
    .stat-item:nth-child(3) { animation-delay: 2s; }
    .stat-item:nth-child(4) { animation-delay: 3s; }
    
    @keyframes statFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .sparkle-text {
        animation: sparkle 2s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 0.7; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.1); }
    }
    
    .footer-hearts {
        text-align: center;
        margin: 50px 0;
        font-size: 2.5em;
    }
    
    .footer-hearts span {
        display: inline-block;
        animation: heartBeat 2s ease-in-out infinite;
        margin: 0 5px;
    }
    
    .footer-hearts span:nth-child(1) { animation-delay: 0s; }
    .footer-hearts span:nth-child(2) { animation-delay: 0.3s; }
    .footer-hearts span:nth-child(3) { animation-delay: 0.6s; }
    .footer-hearts span:nth-child(4) { animation-delay: 0.9s; }
    .footer-hearts span:nth-child(5) { animation-delay: 1.2s; }
    
    @keyframes heartBeat {
        0%, 100% { transform: scale(1); }
        30% { transform: scale(1.2); }
        60% { transform: scale(0.9); }
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e8e) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4) !important;
    }
    
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    
    .rotating-text {
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'love_count' not in st.session_state:
    st.session_state.love_count = 0
if 'magic_count' not in st.session_state:
    st.session_state.magic_count = 0

# Main header
st.markdown('<div class="center-content"><h1 class="main-header">💕 Kirti\'s School of Love 💕</h1></div>', unsafe_allow_html=True)

# School badge
st.markdown('<div class="center-content"><div class="school-badge">🎓 Where Hearts Learn to Love 🎓</div></div>', unsafe_allow_html=True)

# Animated love container
st.markdown("""
<div class="love-container">
    <div class="floating-hearts">💖 💕 💝 💗 💓</div>
    <div class="sparkle-text" style="font-size: 1.5em; color: #ff6b6b; margin-top: 20px;">
        ✨ Love is in the Air ✨
    </div>
</div>
""", unsafe_allow_html=True)

# Romantic quotes
quotes = [
    "Love is not just looking at each other, it's looking in the same direction. 💕",
    "In your arms, I found my home. 🏠💖",
    "Every love story is beautiful, but ours is my favorite. 📖❤️",
    "You are my today and all of my tomorrows. 🌅💝",
    "Love is friendship set on fire. 🔥💕",
    "In a sea of people, my eyes will always search for you. 👀💖",
    "You are my sunshine on a cloudy day. ☀️💕",
    "Together is my favorite place to be. 🤗💝"
]

# Display random quote
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

st.markdown(f'<div class="romantic-quote">"{st.session_state.current_quote}"</div>', unsafe_allow_html=True)

# Interactive buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💖 New Quote"):
        st.session_state.current_quote = random.choice(quotes)
        st.rerun()

with col2:
    if st.button("🌹 Send Love"):
        st.session_state.love_count += 1
        st.balloons()
        st.success(f"Love sent successfully! 💕 (Total: {st.session_state.love_count})")

with col3:
    if st.button("✨ Magic"):
        st.session_state.magic_count += 1
        st.snow()
        st.info(f"Magic is in the air! ✨ (Spells cast: {st.session_state.magic_count})")

with col4:
    if st.button("💝 Surprise"):
        surprises = [
            "You're absolutely amazing! 🌟", 
            "You light up my world! 💡", 
            "You're my sunshine! ☀️",
            "You make my heart skip a beat! 💓",
            "You're pure magic! ✨",
            "You're my favorite person! 👑"
        ]
        st.success(random.choice(surprises))

# Love statistics with animations
st.markdown("""
<div class="love-stats">
    <h3 style="text-align: center; color: #d63384; font-size: 2em;">💕 Kirti's School Love Stats 💕</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div class="stat-item">
            <div style="font-size: 3em;" class="rotating-text">💖</div>
            <div style="font-weight: 600; font-size: 1.2em;">Hearts Connected</div>
            <div style="font-size: 2em; color: #ff6b6b; font-weight: bold;">∞</div>
        </div>
        <div class="stat-item">
            <div style="font-size: 3em;" class="pulse-heart">🌹</div>
            <div style="font-weight: 600; font-size: 1.2em;">Roses Shared</div>
            <div style="font-size: 2em; color: #ff6b6b; font-weight: bold;">999+</div>
        </div>
        <div class="stat-item">
            <div style="font-size: 3em;" class="sparkle-text">💌</div>
            <div style="font-weight: 600; font-size: 1.2em;">Love Letters</div>
            <div style="font-size: 2em; color: #ff6b6b; font-weight: bold;">∞</div>
        </div>
        <div class="stat-item">
            <div style="font-size: 3em;" class="floating-hearts">⭐</div>
            <div style="font-weight: 600; font-size: 1.2em;">Magic Moments</div>
            <div style="font-size: 2em; color: #ff6b6b; font-weight: bold;">Every Second</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Love message section
st.markdown("### 💌 Send a Love Message")
love_message = st.text_area(
    "Write your heart out...", 
    placeholder="Dear love, you mean the world to me... 💕",
    height=100
)

if st.button("💕 Send Message"):
    if love_message:
        st.success(f"Your beautiful message has been sent! 💌")
        st.markdown(f"**Your Message:** *{love_message}*")
        st.balloons()
        # Add some celebration
        st.markdown("""
        <div style="text-align: center; font-size: 2em; animation: pulse 1s ease-in-out 3;">
            💖 Message Delivered with Love! 💖
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please write a message first! 💭")

# Add some extra interactive elements
st.markdown("---")
st.markdown("### 🎮 Love Games")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 Love Fortune"):
        fortunes = [
            "Love is coming your way soon! 💕",
            "A romantic surprise awaits you! 🎁",
            "Your heart will be full of joy today! 😊",
            "Someone special is thinking of you! 💭",
            "Love will find you when you least expect it! 💫",
            "Your kindness will attract love! 🌟"
        ]
        st.info(f"🔮 Fortune: {random.choice(fortunes)}")

with col2:
    if st.button("💕 Love Meter"):
        love_level = random.randint(85, 100)
        st.success(f"💖 Love Level: {love_level}% - You're full of love!")
        # Create a simple progress bar effect
        progress_bar = "💖" * (love_level // 10)
        st.markdown(f"**Love Bar:** {progress_bar}")

# Footer with animated hearts
st.markdown("""
<div class="footer-hearts">
    <span>💖</span>
    <span>💕</span>
    <span>💝</span>
    <span>💗</span>
    <span>💓</span>
</div>
<div style="text-align: center; margin-top: 20px;">
    <p style="color: #d63384; font-weight: 600; font-size: 1.2em;">Made with 💕 at Kirti's School</p>
    <p style="color: #666; font-size: 1em;">Where every heart finds its rhythm 💓</p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh option
if st.sidebar.checkbox("🔄 Keep animations alive", value=False):
    time.sleep(2)
    st.rerun()
