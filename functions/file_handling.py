# Import libraries
from docx import Document
from io import BytesIO
from functions.audio2text import fun_audio_to_text


def read_pdf() -> str:
    """
    Read a pdf file using OCR (Optical Character Recognition) from Tesseract
    :return: str: Text from the docx file
    """
    pass


def read_docx(doc_bytes: BytesIO) -> str:
    """
    Read a docx file using python-docx
    :return: str: Text from the docx file
    """
    doc = Document(doc_bytes)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return text


def read_mp3() -> str:
    """
    Read a mp3 file using the Open AI-Whisper Model and convert it to text
    :return: str: Text from the mp3 file
    """
    pass
