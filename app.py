import streamlit as st
import random
import time

# --- ARCADE SYSTEM INITIALIZATION MATRIX ---
st.set_page_config(page_title="MARS REBEL: Capital Defender", page_icon="🛸", layout="centered")

# ==================== ADVANCED VISUAL RETRO THEME ====================
st.markdown("""
    <style>
    .game-screen {
        background-color: #0c0e14;
        border: 2px solid #3498db;
        border-radius: 12px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        color: #2ecc71;
        text-align: center;
        box-shadow: 0 0 15px rgba(52, 152, 219, 0.4);
    }
    .stat-tag {
        font-size: 20px;
        font-weight: bold;
        color: #ff9900;
    }
    .game-over-alert {
        color: #e74c3c;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Courier New', monospace;
        animation: blinker 1s linear infinite;
    }
    @keyframes blinker {
        50% { opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛸 MARS REBEL: CAPITAL DEFENDER")
st.caption("Defend your R1,000 baseline capital against Liquidation Spikes and Margin Call Comets!")

# Initialize Session Memory States for Game Loops
if "wallet_balance" not in st.session_state:
    st.session_state.wallet_balance = 1000.00
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "game_log" not in st.session_state:
    st.session_state.game_log = ["🛸 System online. Capital defenses fully loaded."]

def process_turn(player_action):
    """Core game mechanics resolution algorithm logic loop."""
    if st.session_state.game_over:
        return

    # Random market hazard matrix generation
    hazard_events = [
        {"name": "📉 NFP DATA SPIKE", "damage": 250.00, "chance": 0.35, "desc": "High volatility interest rate sweep hits your parameters!"},
        {"name": "🔥 GOLD CORRIDOR SQUEEZE", "damage": 450.00, "chance": 0.20, "desc": "Oversized commodity leverage multiplier triggers heavy drawdowns!"},
        {"name": "🛑 STOP HUNT ALGO WHALE", "damage": 150.00, "chance": 0.50, "desc": "Market makers hunt liquidity pooling clusters below support!"},
        {"name": "📊 RETAIL SATELLITE NEWS RUMOR", "damage": 50.00, "chance": 0.60, "desc": "Fake sector rumors trigger quick algorithmic scalping friction."}
    ]
    
    event = random.choice(hazard_events)
    rolled_chance = random.random()
    
    if player_action == "🛡️ ENFORCE RISK ATR LIMIT (DEFEND)":
        # Defend action minimizes risk dampening damage bounds heavily
        if rolled_chance < event["chance"]:
            mitigated_damage = event["damage"] * 0.15  # Capped at strict 1.5% exposure scaling
            st.session_state.wallet_balance -= mitigated_damage
            st.session_state.game_log.insert(0, f"✅ DEFENDED: {event['name']} triggered! ATR Guard caught the move. Lost only R{mitigated_damage:.2f}")
        else:
            st.session_state.score += 10
            st.session_state.game_log.insert(0, "⏳ STANDBY: Market consolidated flat. Core baseline saved securely.")
            
    elif player_action == "🚀 SCALE 0.10 CONTRACT TICKET (ATTACK)":
        # Attack action goes for heavy capital yield gains but targets wide exposure damage
        if rolled_chance < event["chance"]:
            full_damage = event["damage"]
            st.session_state.wallet_balance -= full_damage
            st.session_state.game_log.insert(0, f"💥 BLOWN OUT: {event['name']} hit your position! {event['desc']} Lost -R{full_damage:.2f}")
        else:
            gains = random.randint(150, 350)
            st.session_state.wallet_balance += gains
            st.session_state.score += 50
            st.session_state.game_log.insert(0, f"💰 PROFIT HARVEST: Trailed the wave! Captured +R{gains:.2f} cash injection.")

    # Check terminal failure thresholds
    if st.session_state.wallet_balance <= 0:
        st.session_state.wallet_balance = 0
        st.session_state.game_over = True
        st.session_state.game_log.insert(0, "🚨 MARGIN CALL TRIGGERED: Total portfolio liquidation. Game Over.")

def reset_game():
    st.session_state.wallet_balance = 1000.00
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.game_log = ["🛸 System rebooted. Capital defenses fully loaded."]

# ==================== MAIN GAME DISPLAY INTERFACE ====================
st.markdown("<div class='game-screen'>", unsafe_allow_html=True)

# HUD Top Metric Row Displays
hud_col1, hud_col2 = st.columns(2)
with hud_col1:
    st.markdown(f"💼 PORTFOLIO BALANCE:<br><span class='stat-tag'>R{st.session_state.wallet_balance:.2f}</span>", unsafe_allow_html=True)
with hud_col2:
    st.markdown(f"🏆 PROFIT SCORE MARGIN:<br><span class='stat-tag'>{st.session_state.score} PTS</span>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Evaluate state conditions
if st.session_state.game_over:
    st.markdown("<div class='game-over-alert'>🚨 ACCOUNT LIQUIDATED 🚨</div>", unsafe_allow_html=True)
    st.markdown("Your balance hit R0.00. Broker closed your system link.")
    if st.button("🔄 REBOOT SYSTEM & DEPOSIT FRESH R1,000", use_container_width=True):
        reset_game()
        st.rerun()
else:
    st.write("Choose your immediate execution order protocol for this candle cycle:")
    
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("🛡️ ATR GUARD DEFENSE", use_container_width=True):
            process_turn("🛡️ ENFORCE RISK ATR LIMIT (DEFEND)")
            st.rerun()
    with btn_col2:
        if st.button("🚀 HIGH LEVERAGE ATTACK", use_container_width=True):
            process_turn("🚀 SCALE 0.10 CONTRACT TICKET (ATTACK)")
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Live Broadcast Event Scrolling Logs
st.markdown("### 📡 Deep Space Telemetry Logs")
for log in st.session_state.game_log[:5]:
    st.write(log)
