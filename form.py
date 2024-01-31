import streamlit as st
st.header(":mailbox: Get in Touch with us!")


contact_form="""
        <form action="https://formsubmit.co/devangmestry3@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email"  placeholder="Your Email" required>  
            <textarea name="message" placeholder="Your Message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """
st.markdown(contact_form,unsafe_allow_html=True)
        
        #USer local CSS file

with open("FormStyle.css", "r") as f:
    css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)