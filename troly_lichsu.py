import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64
import streamlit.components.v1 as components
import requests

# ======================
# ⚙️ CẤU HÌNH TRANG
# ======================
st.set_page_config(page_title="Trợ lý Lịch sử", layout="centered")

# ======================
# 🧠 KHỞI TẠO TRẠNG THÁI
# ======================
if "audio_unlocked" not in st.session_state:
    st.session_state["audio_unlocked"] = False

st.title("📚 TRỢ LÝ LỊCH SỬ")
st.write("👉 Bấm **BẬT ÂM THANH** (chỉ 1 lần), sau đó nhập câu hỏi rồi bấm **Trả lời**.")
st.write("📱 *IOS phải bấm nút ▶ để nghe (quy định của Safari).*")
st.write("📱 *Android/PC sẽ tự phát âm thanh.*")

# ======================
# 🔓 NÚT BẬT ÂM THANH
# ======================
if st.button("🔊 BẬT ÂM THANH (1 lần)"):
    js = """
    <script>
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            if (ctx.state === 'suspended') ctx.resume();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            gain.gain.value = 0;
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.05);
        } catch(e) {}
    </script>
    """
    components.html(js, height=0)
    st.session_state["audio_unlocked"] = True
    st.success("Âm thanh đã mở khoá!")

# ======================
# 📜 Ô nhập câu hỏi
# ======================
cau_hoi = st.text_input("❓ Nhập câu hỏi lịch sử:")

