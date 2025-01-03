from core.image.generation.services.dalle.dalle_generation import generate_with_dalle
from core.image.generation.services.freepik.freepik_generation import generate_with_freepik
from core.image.generation.services.pollinations.pollinations_generation import generate_with_pollinations

import os
from typing import Literal
import logging

async def generate_image(service: Literal["dalle", "pollinations", "freepik"], api_key: str = None, prompt: str = "tobey maguire", width: int = 1024, height: int = 1024) -> str:
    logging.info(f"Generating image with service: {service}")
    logging.info(f"Prompt: {prompt}")
    
    try:
        if service == "dalle":
            result = generate_with_dalle(api_key, prompt, width, height)
            logging.info(f"DALLE result: {result}")
            return result
        elif service == "pollinations":
            result = await generate_with_pollinations(prompt, width, height)
            logging.info(f"Pollinations result: {result}")
            return result
        elif service == "freepik":
            result = generate_with_freepik(api_key, prompt, width, height)
            logging.info(f"Freepik result: {result}")
            return result
            
    except Exception as e:
        logging.error(f"Error in generate_image: {str(e)}")
        logging.error(f"Service: {service}")
        raise
