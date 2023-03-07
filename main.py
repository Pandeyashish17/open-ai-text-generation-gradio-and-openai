import gradio as gr
import openai

def generate_text(prompt, model, api_key):
    openai.api_key = api_key

    if model == "text-davinci-003":
        params = {
            "model": model,
            "prompt": prompt,
            "max_tokens": 2048,
            "temperature": 0,
        }
        response = openai.Completion.create(**params)
        output = response.choices[0].text.strip()

    elif model == "gpt-3.5-turbo":
        params = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }
        response = openai.ChatCompletion.create(**params)
        output = response.choices[0].message.content
        
    return output

api_key_input = gr.inputs.Textbox(label="Enter your OpenAI API key")
prompt_input = gr.inputs.Textbox(label="Enter your prompt", default="Enter your prompt here...")
model_input = gr.inputs.Radio(choices=["text-davinci-003", "gpt-3.5-turbo"], label="Select the OpenAI model to use")
output_text = gr.outputs.Textbox(label="Output")

def run_api(api_key, prompt, model):
    output = generate_text(prompt, model, api_key)
    return output

interface = gr.Interface(fn=run_api, inputs=[api_key_input, prompt_input, model_input], outputs=output_text, 
    title="OpenAI API Text Generation",
    description="Enter a prompt and select an OpenAI model to generate text.",
    allow_flagging=False)

interface.launch()
