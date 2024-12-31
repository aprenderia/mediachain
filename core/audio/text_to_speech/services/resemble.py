import requests
import uuid
from pathlib import Path

def generate_resemble_text_to_speech(api_key: str, text: str, voice: str = "default") -> str:
    """
    Generate text-to-speech audio using Resemble.ai API
    
    Args:
        api_key (str): Resemble.ai API key
        text (str): Text to convert to speech
        voice (str): Name or ID of the voice to use
    
    Returns:
        str: Path to the generated audio file
    """
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # Synthesis endpoint from Resemble.ai documentation
    url = "https://f.cluster.resemble.ai/synthesize"
    
    data = {
        "text": text,
        "voice_uuid": voice
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
    # Generate unique filename
    tmp_dir = Path("tmp")
    tmp_dir.mkdir(exist_ok=True)
    output_file = tmp_dir / f"tts_audio_{uuid.uuid4()}.mp3"
    
    # Save the audio content
    with open(output_file, "wb") as f:
        f.write(response.content)
    
    return str(output_file)