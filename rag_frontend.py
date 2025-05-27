# The below frontend code is provided by AWS and Streamlit. I have only modified it to make it look attractive.
import streamlit as st 
import rag_backend as demo

st.set_page_config(page_title="HR Assistant (PavanTech Solutions Pvt. Ltd)")

# Add image (you can use a local file path or a URL)
st.image("pavantechlogo.png", width=150)  # adjust width as needed

# Styled title with "Pavan" in blue
title = '''
<p style="font-family:sans-serif; color:blue; font-size: 42px;">
    HR Assistant <span style="color:green; font-size: 30px;">Pavan Tech Solutions Pvt. Ltd</span>
</p>
'''
st.markdown(title, unsafe_allow_html=True)

if 'vector_index' not in st.session_state: 
    with st.spinner("⏳ Be right with you!"): ###spinner message
        st.session_state.vector_index = demo.hr_index() ### Your Index Function name from Backend File

input_text = st.text_area("Input text", label_visibility="collapsed") 
go_button = st.button("Ask HR", type="primary")


if go_button: 
    
    with st.spinner("🔍 Searching HR Policy. Please wait"):
        response_content = demo.hr_rag_response(index=st.session_state.vector_index, question=input_text) ### replace with RAG Function from backend file
        st.write(response_content) 