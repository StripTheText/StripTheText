# Imports for the Streamlit app

import streamlit as st
import pyperclip
from audiorecorder import audiorecorder
from io import BytesIO
from functions.file_handling import read_docx, read_pdf, read_mp3
from functions.audio2text import fun_audio_to_text


# Definition of the Layout of the Streamlit app
def app():
    """
    Input column for the app (Text, Text Area, File Upload, Microphone, Text Compression Rate, etc.)
    :return:
    """
    # Definition of Constants
    text_input_value_bool: bool = False
    text_input_value: str = ""

    st.set_page_config(
        layout="wide",
        page_title="Strip The Text App",
        page_icon="🧊",
        initial_sidebar_state="collapsed")

    # 1. Row: Title
    row_1_container = st.container()
    with row_1_container:
        st.title("Strip the Text - Demo")

    # 2. Row
    row_2_container = st.container()
    with row_2_container:
        st.header("Parameter of the Demo")
        row_2_col_1, row_2_col_2 = st.columns([0.3, 0.7], gap="large")
        with row_2_col_1:
            # Slider for the text compression rate
            text_compression_rate = st.slider("Text Compression Rate", .0, 1.0, .50, .1)
        with row_2_col_2:
            row_2_col_2_1, row_2_col_2_2 = st.columns(2, gap="small")

            with row_2_col_2_1:
                # Radio button for the input type
                input_type = st.radio(
                    "Input Type",
                    ('Text Area', 'File Upload', 'Microphone'),
                    horizontal=True
                )
            with row_2_col_2_2:
                if input_type == 'Text Area':
                    text_input_value_bool = True

                elif input_type == 'File Upload':
                    file_in = st.file_uploader(
                        'Upload a file',
                        type=['txt', 'pdf', 'docx'],
                        accept_multiple_files=False,
                        label_visibility="hidden"
                    )
                    if file_in is not None:
                        val: str = ""
                        if file_in.type == "text/plain":
                            val = file_in.read().decode('utf-8')
                        elif file_in.type == "application/pdf":
                            val = read_pdf()
                        elif file_in.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                            val = read_docx(BytesIO(file_in.read()))
                        elif file_in.type == "audio/mpeg":
                            val = read_mp3()
                        text_input_value_bool = True
                        text_input_value = val

                elif input_type == 'Microphone':
                    audio = audiorecorder("Click to record", "Recording...")
                    if len(audio) > 0:
                        st.audio(audio.tobytes())
                        text_input_value_bool = True
                        text_input_value = fun_audio_to_text(audio)
        pass
    # 3. Row: Input & Output Column
    row_3_col_1, row_3_col_2 = st.columns(2)

    with row_3_col_1:  # Input Column
        st.header("Input for the App")

    with row_3_col_2:  # Output Column
        st.header("Output of the App")
        txt_class = st.text_input(
            'Classification of the text',
            key="class_output_field_key",
            value="",
            disabled=True
        )

    # 4. Row: Text-Fields
    row_4_col_1, row_4_col_2 = st.columns(2)

    with row_4_col_1:  # Input Column
        if text_input_value_bool:
            text_input_value = st.text_area('Original Text', key="text_input_value_field", height=500,
                                            value=text_input_value)

    with row_4_col_2:  # Output Column
        txt_summ = st.text_area('Summary of the text', key="text_output_field_key", height=500)

    # 5. Row: Buttons
    row_5_col_1, row_5_col_2 = st.columns(2)

    with row_5_col_1:
        col_5_1, col_5_2, col_5_3 = st.columns(3)
        with col_5_1:
            operation = st.selectbox(
                label="Which operation should be run?",
                options=("Text Classification", "Text Summarization", "Text Classification & Summarization"),
                key="operation",
                label_visibility="collapsed",
            )
        with col_5_2:
            go_action = st.button(
                label="Go!",
                key="action",
                use_container_width=True,
            )
            if go_action and (text_input_value != "" or None):
                if operation == "Text Classification":
                    pass  # Pipeline
                elif operation == "Text Summarization":
                    pass  # Pipeline
                elif operation == "Text Classification & Summarization":
                    pass  # Pipeline
        with col_5_3:
            st.button(
                label="Clear Input",
                key="clear_in",
                use_container_width=True,
                on_click=clear_input
            )

    with row_5_col_2:
        col_5_a, col_5_b, col_5_c = st.columns(3)
        with col_5_a:
            st.button(
                label="Copy to Clipboard",
                key="copy_clipboard",
                use_container_width=True,
                on_click=pyperclip.copy(text=txt_summ)
            )
        with col_5_b:
            st.button(
                label="Clear Input and Output Field",
                key="clear_in_out",
                use_container_width=True,
                on_click=clear_all
            )
        with col_5_c:
            st.download_button(
                label="Download Result as .txt",
                data=txt_summ,
                mime="text/plain",
                file_name="result.txt",
                use_container_width=True
            )


def clear_input():
    st.session_state["text_input_value_field"] = ""


def clear_all():
    st.session_state["text_input_value_field"] = ""
    st.session_state["class_output_field_key"] = ""
    st.session_state["text_output_field_key"] = ""


app()
