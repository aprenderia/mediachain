import os
import sys
import asyncio
from dotenv import load_dotenv
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from core.image.generation.image_generation import generate_image
from core.audio.text_to_speech.tts_generation import generate_text_to_speech

async def test_services():
    # Load environment variables
    load_dotenv()
    
    freepik_key = os.getenv('FREEPIK_API_KEY')
    resemble_key = os.getenv('RESEMBLE_API_KEY')
    
    if not freepik_key or not resemble_key:
        print("Error: Missing API keys in .env file")
        return
    
    print("\n=== Testing Freepik Image Generation ===")
    try:
        image_url = await generate_image(
            service="freepik",
            api_key=freepik_key,
            prompt="A beautiful sunset over mountains",
            width=1024,
            height=1024
        )
        print(f"✅ Image generation successful!")
        print(f"Image URL: {image_url}")
    except Exception as e:
        print(f"❌ Image generation failed: {str(e)}")
    
    print("\n=== Testing Resemble.ai Text-to-Speech ===")
    try:
        audio_path = generate_text_to_speech(
            service="resemble",
            api_key=resemble_key,
            text="Hello! This is a test of the Resemble.ai text-to-speech service.",
            voice="default"  # Using default voice
        )
        print(f"✅ Text-to-speech generation successful!")
        print(f"Audio file saved to: {audio_path}")
    except Exception as e:
        print(f"❌ Text-to-speech generation failed: {str(e)}")

if __name__ == "__main__":
    # Run the async test
    asyncio.run(test_services())