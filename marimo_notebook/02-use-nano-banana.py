# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "google-genai",
#     "pillow==11.3.0",
#     "watchdog",
#     "python-dotenv==1.1.1",
#.    "openai",
# ]
# ///

import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Copyright 2025 Google LLC.""")
    return


@app.cell
def _():
    # @title Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    # https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Use Nano-banana""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <table align="left">
      <td>
        <a target="_blank" href="https://colab.research.google.com/github/google-gemini/nano-banana-hackathon-kit/blob/main/guides/02-use-nano-banana.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=30/></a>
      </td>
      <td></td>
      <td><a href="https://aistudio.google.com/apps/bundled/get_started_image_out">Javascript version on AI Studio</a></td>
    </table>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    This notebook will show you how to use the nano banana multimodal capabilities to output both images and texts, and iterate on an image through a discussion.

    This model is really good at:

    * **Maintaining character consistency**: Preserve a subject’s appearance across multiple generated images and scenes
    * **Performing intelligent editing**: Enable precise, prompt-based edits like inpainting (adding/changing objects), outpainting, and targeted transformations within an image
    * **Compose and merge images**: Intelligently combine elements from multiple images into a single, photorealistic composite
    * **Leverage multimodal reasoning**: Build features that understand visual context, such as following complex instructions on a hand-drawn diagram

    Following this guide, you'll learn how to do all those things and even more.

    **Note**: This guide is a simplified version of the [cookbook guide](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Image_out.ipynb#scrollTo=5a3a7f45ea5e) of the nano banana model. Check-out the original version for more examples
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Setup""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Install SDK""")
    return


@app.cell
def _():
    # '%pip install -U -q "google-genai>=1.32.0" # minimum version needed for the parts accessor' command supported automatically in marimo
    return


@app.cell
def _():
    # uv add google-genai
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Setup your API key

    To run the following cell, your API key must be stored in a `.env` file. Create a `.env` file in your project root with:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

    If you don't already have an API key, check out the [01-getting-your-api-key.ipynb](./01-getting-your-api-key.ipynb) guide.
    """
    )
    return


@app.cell
def _():
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    # Find the project root directory (where .env file should be located)
    current_dir = Path(__file__).parent if hasattr(Path(__file__), 'parent') else Path.cwd()
    project_root = current_dir.parent if current_dir.name == 'marimo_notebook' else current_dir

    # Load environment variables from .env file
    env_file = project_root / '.env'
    print(f"🔍 Looking for .env file at: {env_file}")
    print(f"📁 .env file exists: {env_file.exists()}")

    load_dotenv(dotenv_path=env_file)

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    if not GOOGLE_API_KEY:
        print(f"❌ Current working directory: {Path.cwd()}")
        print(f"❌ Script location: {Path(__file__) if '__file__' in locals() else 'Not available'}")
        raise ValueError(f"GOOGLE_API_KEY not found. Looked in: {env_file}")

    print(f"✅ Successfully loaded API key: {GOOGLE_API_KEY[:8]}...{GOOGLE_API_KEY[-4:]}")

    return (GOOGLE_API_KEY,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Initialize SDK client

    With the new SDK you now only need to initialize a client with your API key (or OAuth if using Vertex AI). The model is now set in each call.
    """
    )
    return


@app.cell
def _(GOOGLE_API_KEY):
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=GOOGLE_API_KEY)
    return client, types


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Select a model

    `gemini-2.5-flash-image-preview` is the latest and the state-of-the-art Gemini model capable of generating images.
    """
    )
    return


@app.cell
def _():
    MODEL_ID = "gemini-2.5-flash-image-preview"
    return (MODEL_ID,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Utils""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    These two functions will help you manage the outputs of the model.

    Compared to when you simply generate text, this time the output will contain multiple parts, some one them being text while others will be images. You'll also have to take into account that there could be multiple images so you cannot stop at the first one.
    """
    )
    return


@app.cell
def _(mo):
    import pathlib
    from PIL import Image
    from io import BytesIO

    def display_response(response):
        content = []
        for part in response.parts:
            if part.text:
                content.append(mo.md(part.text))
            elif hasattr(part, 'as_image') and (image := part.as_image()):
                content.append(mo.image(src=image))
        return mo.vstack(content) if content else mo.md("No content to display")

    def save_image(response, path):
        for part in response.parts:
            if hasattr(part, 'as_image') and (image := part.as_image()):
                image.save(path)
                return True
        return False

    return (save_image,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Generate images

    Using the Gemini Image generation model is the same as using any Gemini model: you simply call `generate_content`.

    You can set the `response_modalities` to indicate to the model that you are expecting an image in the output but it's optional as this is expected with this model.
    """
    )
    return


@app.cell
def _(MODEL_ID, client, save_image, types):
    _prompt = 'Create a photorealistic image of a siamese cat with a green left eye and a blue right one and red patches on his face and a black and pink nose'
    _response = client.models.generate_content(model=MODEL_ID, contents=_prompt, config=types.GenerateContentConfig(response_modalities=['Text', 'Image']))
    save_image(_response, 'cat.png')
    return


@app.cell
def _(mo):
    mo.image("cat.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Edit images

    You can also do image editing, simply pass the original image as part of the prompt. Don't limit yourself to simple edit, Gemini is able to keep the character consistency and reprensent you character in different behaviors or places.
    """
    )
    return


@app.cell
def _(MODEL_ID, client, save_image):
    import PIL
    _text_prompt = 'Create a side view picture of that cat, in a tropical forest, eating a nano-banana, under the stars'
    _response = client.models.generate_content(model=MODEL_ID, contents=[_text_prompt, PIL.Image.open('cat.png')])
    save_image(_response, 'cat_tropical.png')
    return (PIL,)


@app.cell
def _(mo):
    mo.image_compare(
        before_image="cat.png",
        after_image="cat_tropical.png"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Get multiple images (ex: tell stories)

    So far you've only generated one image per call, but you can request way more than that! Let's try a baking receipe or telling a story.
    """
    )
    return


@app.cell
def _(MODEL_ID, client):
    _prompt = 'Create a beautifully entertaining 8 part story with 8 images with two blue characters and their adventures in the 1960s music scene. The story is thrilling throughout with emotional highs and lows and ending on a great twist and high note. Do not include any words or text on the images but tell the story purely through the imagery itself. '
    _response = client.models.generate_content(model=MODEL_ID, contents=_prompt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The output of the previous code cell could not be saved in the notebook without making it too big to be managed by Github, but here are some examples of what it should look like when you run it when asking for a story, or for a baking receipe:

    ----------
    **Prompt**: *Create a beautifully entertaining 8 part story with 8 images with two blue characters and their adventures in the 1960s music scene. The story is thrilling throughout with emotional highs and lows and ending on a great twist and high note. Do not include any words or text on the images but tell the story purely through the imagery itself.*
    ![Azure tone story](https://storage.googleapis.com/generativeai-downloads/images/azuretones.png)
    (Images have been stitched together)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Chat mode (recommended method)

    So far you've used unary calls, but Image-out is actually made to work better with chat mode as it's easier to iterate on an image turn after turn.
    """
    )
    return


@app.cell
def _(MODEL_ID, client):
    chat = client.chats.create(
        model=MODEL_ID,
    )
    return (chat,)


@app.cell
def _(chat):
    _message = "Create a image of a plastic toy fox figurine with a blue planet on its helmet in a kid's bedroom, it can have accessories but no weapon"
    _response = chat.send_message(_message)
    return


@app.cell
def _(chat):
    _message = 'Move that figurine on a beach'
    _response = chat.send_message(_message)
    return


@app.cell
def _(chat):
    _message = 'Now it should be base-jumping from a spaceship with a wingsuit'
    _response = chat.send_message(_message)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Mix multiple pictures""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can also mix multiple images (up to 3), either because there are multiple characters in your image, or because you want to hightlight a certain product, or set the background.""")
    return


@app.cell
def _(MODEL_ID, PIL, client):
    _text_prompt = 'Create a picture of that figurine riding that cat in a fantasy world.'
    _response = client.models.generate_content(model=MODEL_ID, contents=[_text_prompt, PIL.Image.open('cat.png'), PIL.Image.open('figurine.png')])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Next Steps
    ### Useful documentation references:

    Check the [documentation](https://ai.google.dev/gemini-api/docs/image-generation#gemini) for more details about the image generation capabilities of the model. To improve your prompting skills, check out the [prompt guide](https://ai.google.dev/gemini-api/docs/image-generation#prompt-guide) for great advices on creating your prompts.

    ### Play with the AI Studio apps

    Theses 5 AI Studio apps are all great showcases of Gemini image generation capabilities:
    * [Past Forward](https://aistudio.google.com/apps/bundled/past_forward) lets you travel through time
    * [Home Canvas](https://aistudio.google.com/apps/bundled/home_canvas) lets your try out new furniture
    * [Gembooth](https://aistudio.google.com/apps/bundled/gembooth) places you into a comic book or a Renaissance painting
    * [Gemini Co-drawing](https://aistudio.google.com/apps/bundled/codrawing) lets you draw alongside with Gemini
    * [Pixshop](https://aistudio.google.com/apps/bundled/pixshop), an AI-powered image editor
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
