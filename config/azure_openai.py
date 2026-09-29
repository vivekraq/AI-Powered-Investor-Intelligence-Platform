import os


def get_api_version() -> str:
    """Return the configured Azure OpenAI API version."""
    api_version = (
        os.getenv("AZURE_OPENAI_API_VERSION")
        or os.getenv("AZURE_OPENAI_EMBEDDING_VERSION")
        or os.getenv("AZURE_OPENAI_API_EMBEDDING_VERSION")
    )

    if not api_version:
        raise RuntimeError(
            "Missing Azure OpenAI API version. Set AZURE_OPENAI_API_VERSION "
            "in the environment."
        )

    return api_version


def get_endpoint() -> str:
    """Return the configured Microsoft Foundry endpoint."""
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    if not endpoint:
        raise RuntimeError(
            "Missing Azure OpenAI endpoint. Set AZURE_OPENAI_ENDPOINT in the environment."
        )
    return endpoint.rstrip("/") + "/openai/v1/"
