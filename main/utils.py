
import google.generativeai as genai

genai.configure(api_key="AIzaSyDgdPtzGHr2bXBWd_uj7YJJrHdNqtaWYw0")


def generate_page_code(title, description, style):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Create an HTML and CSS page. 
    Title: {title}
    Description: {description}
    Style: {style}
    Provide HTML and CSS code in one HTML file without first line like '```html', starting from doctype and so on formatted with proper indentation.
    """

    response = model.generate_content(prompt)
    return response.text