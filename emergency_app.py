import streamlit as st
import urllib.parse

st.set_page_config(page_title="Emergency Help", page_icon="🆘")
st.title("🆘 SACHIN BHAI KA EMERGENCY APP 👑")
st.write("Ek click me apno ko khabar karo")

num1 = st.text_input("Maa/Papa ka Number", placeholder="91XXXXXXXXXX")
num2 = st.text_input("Dost ka Number", placeholder="91XXXXXXXXXX")
num3 = st.text_input("Bhai/Behen ka Number", placeholder="91XXXXXXXXXX")

if st.button("🚨 EMERGENCY HELP BHEJO 🚨", type="primary"):
    if num1 or num2 or num3:
        msg = "EMERGENCY! Main musibat me hu. Please call karo. Location: https://maps.google.com"
        msg_encoded = urllib.parse.quote(msg)
        st.success("Neeche wale button dabao aur Send kar do")
        
        if num1: st.link_button(f"Maa/Papa ko WhatsApp", f"https://wa.me/{num1}?text={msg_encoded}")
        if num2: st.link_button(f"Dost ko WhatsApp", f"https://wa.me/{num2}?text={msg_encoded}")
        if num3: st.link_button(f"Bhai/Behen ko WhatsApp", f"https://wa.me/{num3}?text={msg_enconded}")
    else: 
        st.error("kam se kam 1 number to daal bhai")
