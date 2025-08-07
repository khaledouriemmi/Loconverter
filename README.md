# Loconverter

A local file converter designed for users with limited internet connectivity or those who need to convert files offline. Perfect for:
- Users with slow internet connections
- Batch file conversions without internet dependency
- Privacy-conscious users who prefer local processing
- Situations where internet access is unreliable or unavailable

This versatile offline file conversion tool supports multiple formats:

## Features

- **Documents**: Convert between TXT, DOCX formats (PDF support requires Pandoc)
- **Images**: Convert between PNG, JPG, TIFF, BMP, WebP formats
- **Videos**: Convert between MP4, AVI, MOV, MKV formats (requires FFmpeg)
- **eBooks**: Convert between EPUB, MOBI, PDF formats (requires Calibre)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/khaledouriemmi/Loconverter.git
cd file-converter
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install system dependencies:

For macOS (using Homebrew):
```bash
# For document conversion
brew install pandoc

# For video conversion
brew install ffmpeg

# For ebook conversion
brew install --cask calibre
```

For Ubuntu/Debian:
```bash
# For document conversion
sudo apt-get install pandoc

# For video conversion
sudo apt-get install ffmpeg

# For ebook conversion
sudo apt-get install calibre
```

For Windows:
- Download and install [Pandoc](https://pandoc.org/installing.html)
- Download and install [FFmpeg](https://ffmpeg.org/download.html)
- Download and install [Calibre](https://calibre-ebook.com/download)

## Usage

```bash
python main.py <input_file> <output_file> --type <document|video|image|ebook> --to <format>
```

Examples:
```bash
# Convert text to DOCX
python main.py input.txt output.docx --type document --to docx

# Convert PNG to JPG
python main.py input.png output.jpg --type image --to jpg

# Convert MOV to MP4
python main.py input.mov output.mp4 --type video --to mp4

# Convert EPUB to MOBI
python main.py input.epub output.mobi --type ebook --to mobi
```

## Supported Formats

- **Documents**: TXT, DOCX (PDF with Pandoc)
- **Images**: PNG, JPG/JPEG, TIFF, BMP, WebP
- **Videos**: MP4, AVI, MOV, MKV
- **eBooks**: EPUB, MOBI (with Calibre)

## Requirements

- Python 3.8+
- See requirements.txt for Python package dependencies
- System dependencies: pandoc, ffmpeg, calibre (optional)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
