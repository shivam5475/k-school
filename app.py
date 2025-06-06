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
        from { text-shadow: 0 0 20px rgba(255, 107, 107, 0.5); }
        to { text-shadow: 0 0 30px rgba(255, 107, 107, 0.8); }
    }
    
    .love-container {
        position: relative;
        height: 400px;
        overflow: hidden;
        border-radius: 20px;
        background: linear-gradient(135deg, 
            rgba(255, 182, 193, 0.2) 0%, 
            rgba(255, 192, 203, 0.2) 25%,
            rgba(255, 160, 122, 0.2) 50%,
            rgba(255, 182, 193, 0.2) 75%,
            rgba(255, 192, 203, 0.2) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 20px 0;
    }
    
    .floating-heart {
        position: absolute;
        font-size: 2em;
        animation: float 4s ease-in-out infinite;
        color: #ff6b6b;
        text-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-20px) rotate(5deg); }
        50% { transform: translateY(-40px) rotate(-5deg); }
        75% { transform: translateY(-20px) rotate(3deg); }
    }
    
    .pulse-heart {
        animation: pulse 1.5s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    .romantic-quote {
        text-align: center;
        font-size: 1.4em;
        font-style: italic;
        color: #d63384;
        margin: 20px 0;
        animation: fadeInOut 3s ease-in-out infinite;
    }
    
    @keyframes fadeInOut {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }
    
    .sparkle {
        position: absolute;
        font-size: 1.5em;
        animation: sparkle 2s ease-in-out infinite;
        color: gold;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
    
    .love-button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
        border: none;
        color: white;
        padding: 15px 30px;
        font-size: 1.2em;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        font-weight: 600;
    }
    
    .love-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }
    
    .school-badge {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        display: inline-block;
        margin: 10px;
        font-weight: 600;
        animation: bounce 2s ease-in-out infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .love-stats {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .love-container {
            background: linear-gradient(135deg, 
                rgba(139, 69, 19, 0.2) 0%, 
                rgba(160, 82, 45, 0.2) 25%,
                rgba(205, 92, 92, 0.2) 50%,
                rgba(139, 69, 19, 0.2) 75%,
                rgba(160, 82, 45, 0.2) 100%);
        }
        
        .romantic-quote {
            color: #ff8fab;
        }
        
        .love-stats {
            background: rgba(0, 0, 0, 0.2);
        }
    }
    
    .stApp > header {
        background-color: transparent;
    }
    
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
    
    /* Dark mode background */
    [data-theme="dark"] .stApp {
        background: linear-gradient(-45deg, #2d1b2e, #3d2a3e, #4a2c4a, #5a3d5a);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for advanced animations
st.markdown("""
<script>
function createFloatingHearts() {
    const container = document.querySelector('.love-container');
    if (!container) return;
    
    const hearts = ['💖', '💕', '💝', '💗', '💓', '💘', '💌', '🌹', '❤️', '💜'];
    
    setInterval(() => {
        const heart = document.createElement('div');
        heart.className = 'floating-heart';
        heart.innerHTML = hearts[Math.floor(Math.random() * hearts.length)];
        heart.style.left = Math.random() * 90 + '%';
        heart.style.animationDelay = Math.random() * 2 + 's';
        heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
        
        container.appendChild(heart);
        
        setTimeout(() => {
            if (heart.parentNode) {
                heart.parentNode.removeChild(heart);
            }
        }, 5000);
    }, 800);
}

function createSparkles() {
    const sparkles = ['✨', '⭐', '🌟', '💫', '⚡'];
    
    setInterval(() => {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.innerHTML = sparkles[Math.floor(Math.random() * sparkles.length)];
        sparkle.style.left = Math.random() * 100 + '%';
        sparkle.style.top = Math.random() * 100 + '%';
        sparkle.style.animationDelay = Math.random() * 1 + 's';
        
        document.body.appendChild(sparkle);
        
        setTimeout(() => {
            if (sparkle.parentNode) {
                sparkle.parentNode.removeChild(sparkle);
            }
        }, 2000);
    }, 1500);
}

// Initialize animations when page loads
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
        createFloatingHearts();
        createSparkles();
    }, 1000);
});

// Also try to initialize when Streamlit reruns
setTimeout(() => {
    createFloatingHearts();
    createSparkles();
}, 2000);
</script>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">💕 Kirti\'s School of Love 💕</h1>', unsafe_allow_html=True)

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="school-badge">🎓 Where Hearts Learn to Love 🎓</div>', unsafe_allow_html=True)

# Animation container
st.markdown('<div class="love-container" id="love-container"></div>', unsafe_allow_html=True)

# Romantic quotes
quotes = [
    "Love is not just looking at each other, it's looking in the same direction. 💕",
    "In your arms, I found my home. 🏠💖",
    "Every love story is beautiful, but ours is my favorite. 📖❤️",
    "You are my today and all of my tomorrows. 🌅💝",
    "Love is friendship set on fire. 🔥💕"
]

# Display random quote
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

st.markdown(f'<div class="romantic-quote">"{st.session_state.current_quote}"</div>', unsafe_allow_html=True)

# Interactive buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💖 New Quote", key="quote_btn"):
        st.session_state.current_quote = random.choice(quotes)
        st.rerun()

with col2:
    if st.button("🌹 Send Love", key="love_btn"):
        st.balloons()
        st.success("Love sent successfully! 💕")

with col3:
    if st.button("✨ Magic", key="magic_btn"):
        st.snow()
        st.info("Magic is in the air! ✨")

with col4:
    if st.button("💝 Surprise", key="surprise_btn"):
        surprises = ["You're amazing! 🌟", "You light up my world! 💡", "You're my sunshine! ☀️"]
        st.success(random.choice(surprises))

# Love statistics
st.markdown("""
<div class="love-stats">
    <h3 style="text-align: center; color: #d63384;">💕 Kirti's School Love Stats 💕</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="text-align: center; margin: 10px;">
            <div style="font-size: 2em;">💖</div>
            <div style="font-weight: 600;">Hearts Connected</div>
            <div style="font-size: 1.5em; color: #ff6b6b;">∞</div>
        </div>
        <div style="text-align: center; margin: 10px;">
            <div style="font-size: 2em;">🌹</div>
            <div style="font-weight: 600;">Roses Shared</div>
            <div style="font-size: 1.5em; color: #ff6b6b;">999+</div>
        </div>
        <div style="text-align: center; margin: 10px;">
            <div style="font-size: 2em;">💌</div>
            <div style="font-weight: 600;">Love Letters</div>
            <div style="font-size: 1.5em; color: #ff6b6b;">∞</div>
        </div>
        <div style="text-align: center; margin: 10px;">
            <div style="font-size: 2em;">⭐</div>
            <div style="font-weight: 600;">Magic Moments</div>
            <div style="font-size: 1.5em; color: #ff6b6b;">Every Second</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Love message section
st.markdown("### 💌 Send a Love Message")
love_message = st.text_area("Write your heart out...", placeholder="Dear love, you mean the world to me... 💕")

if st.button("💕 Send Message", key="message_btn"):
    if love_message:
        st.success(f"Your beautiful message has been sent! 💌\n\n*{love_message}*")
        st.balloons()
    else:
        st.warning("Please write a message first! 💭")

# Footer with pulsing hearts
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px;">
    <div style="font-size: 2em; margin-bottom: 10px;">
        <span class="pulse-heart">💖</span>
        <span class="pulse-heart" style="animation-delay: 0.5s;">💕</span>
        <span class="pulse-heart" style="animation-delay: 1s;">💝</span>
        <span class="pulse-heart" style="animation-delay: 1.5s;">💗</span>
        <span class="pulse-heart" style="animation-delay: 2s;">💖</span>
    </div>
    <p style="color: #d63384; font-weight: 600;">Made with 💕 at Kirti's School</p>
    <p style="color: #666; font-size: 0.9em;">Where every heart finds its rhythm 💓</p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh for continuous animation (optional)
if st.checkbox("🔄 Keep animations alive", value=True):
    time.sleep(0.1)
    st.rerun()
