#!/usr/bin/env python3
"""
Local File Converter
A command-line tool for converting files between different formats.
"""

import argparse
import sys
from pathlib import Path
from converter.documents import convert_document
from converter.videos import convert_video
from converter.images import convert_image
from converter.ebooks import convert_ebook

def main():
    parser = argparse.ArgumentParser(
        description="Convert files between different formats",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.txt output.docx --type document --to docx
  %(prog)s input.png output.jpg --type image --to jpg
  %(prog)s input.mov output.mp4 --type video --to mp4
  %(prog)s input.epub output.mobi --type ebook --to mobi
        """
    )
    parser.add_argument('input', help='Input file path')
    parser.add_argument('output', help='Output file path')
    parser.add_argument(
        '--type',
        choices=['document', 'video', 'image', 'ebook'],
        required=True,
        help='Type of file to convert'
    )
    parser.add_argument(
        '--to',
        required=True,
        help='Target format (e.g., pdf, docx, mp4, jpg, epub, mobi)'
    )
    args = parser.parse_args()

    # Validate input file exists
    if not Path(args.input).is_file():
        print(f"Error: Input file '{args.input}' does not exist")
        sys.exit(1)

    # Ensure output directory exists
    output_dir = Path(args.output).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        if args.type == 'document':
            convert_document(args.input, args.output, args.to)
        elif args.type == 'video':
            convert_video(args.input, args.output, args.to)
        elif args.type == 'image':
            convert_image(args.input, args.output, args.to)
        elif args.type == 'ebook':
            convert_ebook(args.input, args.output, args.to)
        
        print(f"Successfully converted {args.input} to {args.output}")
    except NotImplementedError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
