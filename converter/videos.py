try:
    from moviepy.editor import VideoFileClip
except ImportError:
    VideoFileClip = None
import os

def convert_video(input_path: str, output_path: str, target_format: str) -> None:
    if VideoFileClip is None:
        raise ImportError("moviepy module not properly installed. Please reinstall the package.")
    """
    Convert videos between different formats using moviepy
    Supported formats: MP4, AVI, MOV, MKV
    """
    try:
        # Load the video file
        video = VideoFileClip(input_path)
        
        # For MP4 output, use H.264 codec
        if target_format.lower() == 'mp4':
            video.write_videofile(
                output_path,
                codec='libx264',
                audio_codec='aac',
                preset='medium',  # Balance between speed and quality
                bitrate='8000k'   # Adjust bitrate as needed
            )
        else:
            # For other formats, use default settings
            video.write_videofile(output_path)
        
        # Close the video to free up resources
        video.close()
    except Exception as e:
        raise Exception(f"Error converting video: {str(e)}")
