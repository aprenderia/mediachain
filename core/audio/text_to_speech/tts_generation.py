from core.audio.text_to_speech.services.openai import generate_openai_text_to_speech
from core.audio.text_to_speech.services.azure_openai import generate_azure_openai_text_to_speech
from core.audio.text_to_speech.services.resemble import generate_resemble_text_to_speech
from typing import Literal

# todo: Literal for voice in each service. E.g. resemble voice IDs, openai voice ["alloy", "echo", "fable", "nova", "shimmer"]

def generate_text_to_speech(service: Literal["openai", "azure_openai", "resemble"], api_key: str, text: str, voice: str, azure_config: dict = None) -> str:
    if service == "openai":
        try:
            return generate_openai_text_to_speech(api_key, text, voice)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with OpenAI: {e}")
    elif service == "azure_openai":
        try:
            return generate_azure_openai_text_to_speech(api_key, text, voice, azure_config)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with Azure OpenAI: {e}")
    elif service == "resemble":
        try:
            return generate_resemble_text_to_speech(api_key, text, voice)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with Resemble.ai: {e}")
    else:
        raise ValueError(f"Invalid text-to-speech service: {service}")