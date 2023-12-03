
import streamlit as st

def main():
    # Move set_page_config to the beginning of the script
    st.set_page_config(
        page_title="Assembly AI Video Transcription",
        page_icon=":memo:",
        layout="wide",
        initial_sidebar_state="expanded",  # Sidebar expanded by default
    )

    # Change the background color and add some padding
    st.markdown(
        """
        <style>
            body {
                background-color: #f8f9fa;  /* Set your desired background color */
                padding: 20px;
            }
            .st-df {
                max-width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Include the HTML content
    st.markdown(open("index.html").read(), unsafe_allow_html=True)

    st.image("https://cdn.analyticsvidhya.com/wp-content/uploads/2023/09/blog1_qvx54ye.jpg", width=1000)

    # Customize the header style
    st.title("Assembly AI Video Transcription")



    # Add an interactive button with a callback
    if st.button("Click me for a surprise"):
        st.balloons()

    # Add a slider for font size
    font_size = st.slider("Adjust Font Size", min_value=10, max_value=50, value=20)
    st.markdown(f'<div style="font-size: {font_size}px;">WELCOME TO OUR VIDEO TRANSCRIPTION AND SUMMARIZATION APP!</div>', unsafe_allow_html=True)

    # Use st.container() instead of st.beta_container()
    footer = st.container()

    with footer:
        st.write("For more information, visit Assembly AI's website.")

if __name__ == "__main__":
    main()
