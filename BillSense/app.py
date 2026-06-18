import streamlit as st
import requests

st.set_page_config(page_title="BillSense Dashboard", page_icon="favicon.ico",layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


with st.sidebar:
    st.image("PhotoshopExtension_Image.jpeg", width=750) 
    st.title("BillSense")
    dark_mode = st.toggle(" Dark Mode")
    if dark_mode:
        dark_css = """
        <style>
        [data-testid="stAppViewContainer"] { background-color: #0f172a !important; }
        [data-testid="stHeader"] { background-color: #0f172a !important; }
        [data-testid="stSidebar"] { background-color: #1e293b !important; border-right: 1px solid #334155 !important; }
        
        h1, h2, h3, p, span, label, li { color: #f8fafc !important; }
        
        
        
        [data-testid="stSpinner"] svg circle {
            stroke: #3b82f6 !important; /* Bright Blue */
        }
        
        
        [data-testid="stSpinner"] > div:first-of-type {
            border-color: rgba(255, 255, 255, 0.1) !important;
            border-top-color: #3b82f6 !important; 
        }
        
       
        [data-testid="stSpinner"] p {
            color: #f8fafc !important; 
        }
        
        
        [data-testid="stFileUploader"] section { 
            background-color: #1e293b !important; 
            border: 1px dashed #475569 !important; 
        }
        
        [data-testid="stFileUploader"] section div,
        [data-testid="stFileUploader"] section ul,
        [data-testid="stFileUploader"] section li {
            background-color: transparent !important;
            box-shadow: none !important;
        }
        
        [data-testid="stFileUploader"] section * {
            color: #f8fafc !important;
        }
        
        [data-testid="stUploadedFile"] svg {
            filter: invert(1) brightness(2) !important;
        }
        
        [data-testid="stFileUploader"] button {
            background-color: #334155 !important;
            color: #f8fafc !important;
            border: 1px solid #475569 !important;
        }
        
        hr { border-color: #334155 !important; }
        </style>
        """
        st.markdown(dark_css, unsafe_allow_html=True)


    st.markdown("---")
    st.markdown("**How it works:**")
    st.markdown("1. Drag and drop your invoice.")
    st.markdown("2. Llama 3.1 extracts the data.")
    st.markdown("3. Data is pushed to Google Sheets.")
    st.markdown("---")
    st.caption("Running locally via n8n & Ollama")


st.title("BillSense – Smart Invoice Reader")
st.subheader("Tired of manual invoice entry?")
st.markdown("Upload your invoice and let AI handle the rest. This system extracts structured data from invoices and organizes it automatically for smarter expense tracking.")
st.write("") 


N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/invoice-upload"

uploaded_file = st.file_uploader("Drag and drop or click to upload your PDF", type=["pdf"])
    
    # Create the trigger button
if st.button("Process Invoice", type="primary", use_container_width=True):

    if uploaded_file is not None:
        with st.spinner("BillSense is analyzing your document... Please wait."):
            
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            
            try:
                response = requests.post(N8N_WEBHOOK_URL, files=files)
                
                if response.status_code == 200:
                    result_data = response.json()
                    is_fraud = result_data.get("fraud_flag", False)
                    
                    if is_fraud:
                        reason = result_data.get("fraud_reason", "Unknown compliance issue.")
                        st.error("**Audit Failed: Fraud/Compliance Issue Detected**")
                        st.error(f"**Reason:** {reason}")
                    else:
                        st.success("Success! Data extracted and logged to Sheets.") 
                else:
                    st.error(f"Error: n8n responded with status {response.status_code}")
                    
            except Exception as e:
                st.error(f"Network Error: Could not connect to n8n backend.")
    else:
        st.warning("Please upload an invoice file before processing.")



st.markdown("---") 

footer_html = """
<div style="text-align: center; color: #94a3b8; font-size: 14px; margin-top: 20px;">
    <div style="font-weight: bold; margin-bottom: 4px;">BillSense AI • Smart Invoice Processing Engine</div>
    <div style="font-size: 12px; color: #64748b; margin-bottom: 12px;">Powered by n8n, Llama 3.1, and local processing for maximum privacy.</div>
    <div style="margin-bottom: 4px;">Made with ❤️ by <strong>KaustubhOps</strong></div>
    <div style="font-size: 12px;">
        <a href="https://github.com/KaustubhOps27" target="_blank" style="color: #3b82f6; text-decoration: none; font-weight: bold;">GitHub</a> • 
        <a href="https://linkedin.com/in/kaustubhnikam" target="_blank" style="color: #3b82f6; text-decoration: none; font-weight: bold;">LinkedIn</a>
    </div>
    <div style="font-size: 11px; color: #64748b; margin-top: 12px;">© 2026 All rights reserved.</div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

