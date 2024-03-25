from streamlit_option_menu import option_menu
import streamlit as st


st.set_page_config(
    page_title="Autism Spectrum Disorder Detection",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)


st.title('Autism Spectrum Disorder Detection App 🧠')



selected = option_menu(
    menu_title=None,
    options=["Home", "Testing", "Prediction"],
    icons=["window", "globe", "cpu"],
    orientation="horizontal",
    default_index=0,
    styles={
        "nav-link-selected": {"background-color": "#A0153E"},
    }
)


if selected == "Home":
    with st.container():

        target_url = "#"
        image_url = "https://images.unsplash.com/photo-1620230874645-0d85522b20f9?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        
        st.markdown(
            f'<a href="{target_url}" target="_blank"><img src="{image_url}" alt="Cover Image" width="100%" height="250px"></a>',
            unsafe_allow_html=True
        )

        st.markdown(
            """

            <h2 style="color:#FF204E">Project Overview</h2>

            <p style="color:white">
                The main objective of this project to develop a machine learning model to classify individuals with ASD and those with TD based on structural and functional Magnetic Resonance Imaging (MRI) scans.
            </p>

            <h2 style="color:#FF204E">Data Source</h2>

            <p style="color:white">
                The project utilizes the KKI dataset from the Autism Brain Imaging Data Exchange (ABIDE) repository. This dataset provides MRI scans from both ASD and TD individuals.
            </p>

            <h2 style="color:#FF204E">Data Preprocessing</h2>

            <p style="color:white">
                Raw MRI images were preprocessed using Python's nilearn library. Preprocessing steps likely included:
                <ul>
                    <li><b>Normalization:</b> Ensuring images have consistent intensity values across participants.</li>
                    <li><b>Skull Stripping:</b> Removing non-brain tissue from the image.</li>
                    <li><b>Spatial Smoothing:</b> Blurring the image slightly to reduce noise.</li>
                    <li><b>Independent Component Analysis (ICA) and Dictionary Learning:</b> These techniques might have been used to extract features from the brain scans that are relevant for ASD classification.</li>
                </ul>
            </p>

            <h2 style="color:#FF204E">Data Separation</h2>

            <p style="color:white">
                A separate script likely utilizes phenotypic data (information about the participants' diagnosis) from a CSV file to categorize the preprocessed MRI scans into two folders: one containing scans from individuals with ASD and another containing scans from those with TD.
            </p>

            <h2 style="color:#FF204E">Classification Model</h2>

            <p style="color:white">
                The project employs a Convolutional Neural Network (CNN) architecture called VGGNET16 for classification. CNNs are well-suited for analyzing image data like MRI scans. VGGNET16 is a pre-trained model on a large image dataset, which can then be fine-tuned for the specific task of classifying ASD vs. TD.
            </p>

            <h2 style="color:#FF204E">Current Performance</h2>

            <p style="color:white">
                The model achieves an accuracy of 63.75% at 5 epochs. This indicates that the model can correctly classify ASD or TD in roughly 64 out of every 100 cases after 10 training iterations.
            </p>
            """,
            unsafe_allow_html=True
        )

    

if selected == "Testing":

    st.markdown(
    f"""
    <h2 style="color:#176397">Testing Page</h2>


    """,
    unsafe_allow_html=True)


if selected == "Prediction":

    st.markdown(
    f"""
    <h2 style="color:#176397">Prediction Page</h2>


    """,
    unsafe_allow_html=True)


    st.write("---")

    