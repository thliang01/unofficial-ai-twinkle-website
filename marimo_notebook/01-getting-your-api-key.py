import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 🚀 Getting Started: Your First Steps with the Gemini API and Nano Banana""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <table align="left">
      <td>
        <a target="_blank" href="https://colab.research.google.com/github/google-gemini/nano-banana-hackathon-kit/blob/main/guides/01-getting-your-api-key.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=30/></a>
      </td>
    </table>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Welcome, hacker! This guide will walk you through the essential steps to get your free Gemini API key and set up your development environment for the Nano Banana 48 Hour Challenge.

    Our goal is to get you from zero to your first generated image in just a few minutes.

    ### What this guide covers:
    1.  **Getting Your Free API Key** from Google AI Studio.
    2.  **Setting Up Your Project** with the necessary SDK.
    3.  **Running Your First API Call** to confirm everything works.

    Let's get started!

    ## Step 1: Get Your Free API Key

    For the 48-hour competition, you have free-tier access to the Gemini API through Google AI Studio. AI Studio is a web-based playground where you can test prompts and, most importantly, generate your API key.

    **1. Go to Google AI Studio**

    *   Use this direct link to open a new session with the Nano Banana model:
        > **[ai.studio/banana](https://ai.studio/banana)**

    *   Sign in with your Google account if prompted.

    **2. Generate Your API Key**

    1. In Google AI Studio, click [Get API key](https://aistudio.google.com/apikey) in the left navigation panel.
    2. On the next page, click Create API key.
    3. Select an existing Google Cloud project or create a new one. This project is used to manage billing for API usage.
    4. Once the process is complete, your API key will be displayed. Copy and store it securely.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ![An image of the Google AI Studio interface showing the model selection with Nano Banana selected](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o9or9z21jmxarbejhizi.png)

    _Tip: You can also vibe code Nano Banana web apps directly in AI Studio at ai.studio/apps, or explore the code and remix one of the existing apps._
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    *   Copy your new API key immediately.

    🔒 **IMPORTANT: Keep Your API Key Secure!**
    Treat your API key like a password. **Do not** share it publicly or commit it to your GitHub repository. The best practice is to use an environment variable.

    ## Step 2: Set Up Your Coding Environment

    Next, install the official Google AI SDK for your preferred language.

    #### **Python**
    Open your terminal and run:
    """
    )
    return


@app.cell
def _():
    # Install the main SDK
    # '%pip install -U google-genai' command supported automatically in marimo

    # We also recommend Pillow for handling images
    # '%pip install Pillow' command supported automatically in marimo

    # uv add google-genai Pillow
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### **JavaScript / TypeScript**

    Open your terminal and run:

    ```bash
    npm install @google/genai
    ```

    You can find the JavaScript example in the [../examples/javascript-getting-started.md](../examples/javascript-getting-started.md) file.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Step 3: Run Your First API Call (Hello, Banana!)

    Let's make sure your key and setup are working correctly by generating an image. This simple script will create a photorealistic cat.

    #### **Python Example**
    """
    )
    return


@app.cell
def _():
    import os
    from google import genai
    from PIL import Image
    from io import BytesIO
    from IPython.display import display

    # --- IMPORTANT ---
    # Paste your API key here. For better security, we recommend using environment variables.
    # For example: API_KEY=os.environ.get("GEMINI_API_KEY")
    API_KEY = "AIzaSyCx1lOK2EXjVDjhatkP5czmqMKN9YNv-hY"
    # -----------------

    # Configure the client with your API key
    client = genai.Client(api_key=API_KEY)

    # The text prompt for image generation
    prompt = "Create a photorealistic image of an orange cat with green eyes, sitting on a couch."

    print("Generating image...")

    # Call the API to generate the image
    response = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=prompt,
    )

    image_parts = [
        part.inline_data.data
        for part in response.candidates[0].content.parts
        if part.inline_data
    ]

    if image_parts:
        image = Image.open(BytesIO(image_parts[0]))
        image.save('cat.png')
        display(image)
    return


@app.cell
def _(mo):
    mo.image("cat.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    If everything is correct, you will see a `cat.png` file appear in your folder!

    ![A photorealistic image of an orange cat with green eyes sitting on a couch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k4ae99ee27jmi83rye8s.png)

    ## ✅ You're All Set! What's Next?

    Congratulations, you are now ready to build with the Gemini API! First off, check this [**second guide**](./02-use-nano-banana.ipynb) on how to use the nano banana to edit images or generate multiple ones.

    *   **Explore Project Templates**: Head over to the [`/starter-kits`](../starter-kits/) directory in this repository for ready-to-use application templates.
    *   **See More Examples**: Check out the [`/examples`](../examples/) folder for more advanced code snippets, like image editing and restoration.
    *   **Review the Rules**: Go back to the main [README](../README.md) for submission guidelines and competition details.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
