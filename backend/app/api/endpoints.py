from fastapi import APIRouter
from fastapi import Query
from app.core.models import ask_openai, ask_gemini, ask_claude, ask_command,ask_deepseek
router = APIRouter()

@router.get("/generate/deepseek", summary="Generate text using DeepSeek model")
async def generate_deepseek(
    prompt: str,
    temperature: float = Query(0.7, ge=0.0, le=1.0),  
    max_tokens: int = Query(200, ge=50, le=1000)   
):
    """
    Generate text using DeepSeek model.

    Parameters
    ----------
    prompt : str
        Input text to generate a response.
    temperature : float, optional
        Controls randomness in the response, default is 0.7.
    max_tokens : int, optional
        Maximum number of tokens in the response, default is 200.

    Returns
    -------
    dict
        Generated text response from DeepSeek.
    """
    response = ask_deepseek(prompt, temperature, max_tokens)
    return {"response": response}

@router.get("/generate/openai", summary="Generate text using OpenAI GPT model")
async def generate_openAI(
    prompt: str,
    temperature: float = Query(0.7, ge=0.0, le=1.0),  
    max_tokens: int = Query(200, ge=50, le=1000)   
):
    """
    Generate text using OpenAI's GPT model.

    Parameters
    ----------
    prompt : str
        Input text to generate a response.
    temperature : float, optional
        Controls randomness in the response, default is 0.7.
    max_tokens : int, optional
        Maximum number of tokens in the response, default is 200.

    Returns
    -------
    dict
        Generated text response from OpenAI.
    """
    response = ask_openai(prompt, temperature, max_tokens)
    return {"response": response}

@router.get("/generate/gemini", summary="Generate text using Google Gemini model")
async def generate_google_gemini(
    prompt: str,
    temperature: float = Query(0.7, ge=0.0, le=1.0),  
):
    """
    Generate text using Google Gemini model.

    Parameters
    ----------
    prompt : str
        Input text to generate a response.
    temperature : float, optional
        Controls randomness in the response, default is 0.7.

    Returns
    -------
    dict
        Generated text response from Google Gemini.
    """
    response = ask_gemini(prompt=prompt, temperature=temperature)
    return {"response": response}

@router.get("/generate/anthropic", summary="Generate text using Anthropic Claude model")
async def generate_anthropic(
    prompt: str,
    temperature: float = Query(0.7, ge=0.0, le=1.0),  
    max_tokens: int = Query(200, ge=50, le=1000)   
):
    """
    Generate text using Anthropic Claude model.

    Parameters
    ----------
    prompt : str
        Input text to generate a response.
    temperature : float, optional
        Controls randomness in the response, default is 0.7.
    max_tokens : int, optional
        Maximum number of tokens in the response, default is 200.

    Returns
    -------
    dict
        Generated text response from Anthropic Claude.
    """
    response = ask_claude(prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    return {"response": response}

@router.get("/generate/command", summary="Generate text using Cohere Command model")
async def generate_command(
    prompt: str,
    temperature: float = Query(0.7, ge=0.0, le=1.0),  
    max_tokens: int = Query(200, ge=50, le=1000)   
):
    """
    Generate text using Cohere Command model.

    Parameters
    ----------
    prompt : str
        Input text to generate a response.
    temperature : float, optional
        Controls randomness in the response, default is 0.7.
    max_tokens : int, optional
        Maximum number of tokens in the response, default is 200.

    Returns
    -------
    dict
        Generated text response from Cohere Command.
    """
    response = ask_command(prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    return {"response": response}

@router.get("/health/", summary="Check API health status")
async def health_check():
    """
    Check the health status of the API.

    Returns
    -------
    dict
        API health status message.
    """
    return {"status": "healthy"}
