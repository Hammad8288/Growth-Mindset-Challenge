import streamlit as st
import random
import datetime

# Inject Tailwind CSS
tailwind_css = """
<style>
@import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

body {
    background-color: #f8f9fa;
    color: #333;
}
.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
.btn {
    background-color: #4F46E5;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;
}
.btn:hover {
    background-color: #4338CA;
}
</style>
"""

st.markdown(tailwind_css, unsafe_allow_html=True)

# --- App Title ---
st.markdown('<h1 class="text-3xl font-bold text-center text-indigo-600">🌱 Growth Mindset Challenge</h1>', unsafe_allow_html=True)
st.markdown('<p class="text-center text-gray-500">Unlock Your Potential with Daily Challenges!</p>', unsafe_allow_html=True)

# --- Daily Challenges ---
challenges = [
    "Aaj ek naya skill seekhne ka irada karein!",
    "Ek inspiring kitab ka ek chapter parhain.",
    "Ek positive journal entry likhein.",
    "Ek chhoti si cheez seekh kar kisi aur ko sikhaain!",
    "Ek din tak negative self-talk ko avoid karein.",
    "Ek naye insan se baat karein aur unse kuch seekhne ki koshish karein.",
    "Ek motivational video dekhein aur us par sochain."
]

# --- Motivational Quotes ---
quotes = [
    "“Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston Churchill",
    "“Your only limit is your mind.”",
    "“The secret of getting ahead is getting started.” – Mark Twain",
    "“Don't watch the clock; do what it does. Keep going.” – Sam Levenson",
    "“Believe you can and you're halfway there.” – Theodore Roosevelt"
]

# --- Get Current Date for Daily Challenge ---
today = datetime.date.today()
random.seed(today.toordinal())  # Change challenge daily based on date
daily_challenge = random.choice(challenges)
daily_quote = random.choice(quotes)

# st.markdown('<div class="container bg-white p-6 mt-4 shadow-lg rounded-lg">', unsafe_allow_html=True)

st.markdown('<h2 class="text-xl font-semibold text-gray-700">📌 Aaj Ka Challenge:</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="text-lg font-medium text-gray-800">"{daily_challenge}"</p>', unsafe_allow_html=True)

st.markdown('<h2 class="text-xl font-semibold text-gray-700 mt-4">💡 Motivational Quote:</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="italic text-gray-600">{daily_quote}</p>', unsafe_allow_html=True)

# --- Progress Tracking ---
st.markdown('<h2 class="text-xl font-semibold text-gray-700 mt-6">📊 Apni Progress Track Karein</h2>', unsafe_allow_html=True)
progress = st.slider("Aaj aapka progress level kitna raha? (0-100%)", 0, 100, 50)

# --- Journal Entry ---
st.markdown('<h2 class="text-xl font-semibold text-gray-700 mt-6">📝 Aaj Ka Reflection</h2>', unsafe_allow_html=True)
journal = st.text_area("Aaj aap ne kya seekha ya mehsoos kiya?", "")

if st.button("Save Progress"):
    st.success("✅ Aapki progress aur journal save ho gaya!")

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="text-center text-gray-400 mt-6">Made with ❤️ using Streamlit | <strong>Keep Growing! 🚀</strong></div>', unsafe_allow_html=True)
