import requests
import time
from typing import Optional

def generate_with_freepik(api_key: str, prompt: str, height: int = 1024, width: int = 1024) -> str:
    """
    Generate an image using Freepik's Mystic AI API.
    
    Args:
        api_key (str): Freepik API key
        prompt (str): Text prompt for image generation
        height (int): Height of the generated image (determined by resolution and aspect ratio)
        width (int): Width of the generated image (determined by resolution and aspect ratio)
    
    Returns:
        str: URL of the generated image
    """
    if not api_key:
        raise ValueError("Freepik API key is required.")

    headers = {
        'x-freepik-api-key': api_key,
        'Content-Type': 'application/json'
    }

    # Calculate appropriate aspect ratio based on dimensions
    ratio = width / height
    if ratio == 1:
        aspect_ratio = "square_1_1"
    elif ratio == 4/3:
        aspect_ratio = "classic_4_3"
    elif ratio == 16/9:
        aspect_ratio = "widescreen_16_9"
    else:
        # Default to square if no matching ratio
        aspect_ratio = "square_1_1"

    # Determine resolution based on dimensions
    resolution = "4k" if width > 2048 or height > 2048 else "2k"

    # Initial request to start generation
    data = {
        "prompt": prompt,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
        "realism": True,  # Enable realistic mode
        "creative_detailing": 50,  # Medium level of detail
        "engine": "magnific_sharpy"  # Best for realistic images with sharp details
    }

    response = requests.post(
        'https://api.freepik.com/v1/ai/mystic',
        headers=headers,
        json=data
    )
    response.raise_for_status()
    task_id = response.json()['task_id']

    # Poll for task completion
    max_attempts = 30  # Maximum number of polling attempts
    attempt = 0
    while attempt < max_attempts:
        status_response = requests.get(
            f'https://api.freepik.com/v1/ai/mystic/{task_id}',
            headers=headers
        )
        status_response.raise_for_status()
        status_data = status_response.json()

        if status_data['status'] == 'completed':
            # Return the URL of the generated image
            return status_data['result']['url']
        elif status_data['status'] == 'failed':
            raise Exception(f"Image generation failed: {status_data.get('error', 'Unknown error')}")
        
        attempt += 1
        time.sleep(2)  # Wait 2 seconds before polling again

    raise TimeoutError("Image generation timed out")