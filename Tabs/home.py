"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    st.image("./images/home.png", use_column_width=True)

    # Centered paragraph using markdown
    st.markdown(
    """
    <div style="text-align: justify; font-size: 20px; line-height: 1.5;">
        <p>
            In today’s fast-paced lifestyle, the significance of quality sleep often eludes many. The Smart-Yoga Pillow (SaYoPillow) aims to bridge this gap by introducing the concept of 'Smart-Sleeping' through an innovative edge device. This device incorporates an edge processor equipped with a sophisticated model that analyzes physiological sleep patterns and habits. By interpreting these sleep indicators, it predicts stress levels for the subsequent day.
        </p>
        <p>
            The SaYoPillow ensures the secure transmission of analyzed stress data and average physiological changes to the IoT cloud for storage. Additionally, it offers a secure pathway for data transfer from the cloud to third-party applications. This system is complemented by a user-friendly interface, granting users control over data accessibility and visibility.
        </p>
        <p>
            SaYoPillow stands out for its novel approach, integrating robust security features and considering sleeping habits to alleviate stress. Remarkably, it boasts an accuracy rate of up to 96%.
        </p>
    </div>

    """, unsafe_allow_html=True)

    
