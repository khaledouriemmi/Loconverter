from pathlib import Path
from docx import Document

def convert_document(input_path: str, output_path: str, target_format: str) -> None:
    """Convert documents between different formats.

    Args:
        input_path: Path to the input document
        output_path: Path where the converted document will be saved
        target_format: Desired output format (e.g., 'docx', 'pdf')

    Raises:
        Exception: If conversion fails
    """
    try:
        # Create a new Word document
        doc = Document()
        
        # Read the input file
        with open(input_path, 'r') as file:
            content = file.read()
            
        # Add the content to the document
        doc.add_paragraph(content)
        
        # Save the document
        doc.save(output_path)
            
    except Exception as e:
        raise Exception(f"Error converting document: {str(e)}")
