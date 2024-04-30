import gradio as gr
import openai
openai.api_key = "API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,

    )
    return response.choices[0].text.strip()

def chatbot(input_text):
    response = generate_response(input_text)
    return response

iface = gr.Interface(
    fn=chatbot,
    inputs=gr.inputs.Textbox(label="Enter your message here:"),
    outputs=gr.outputs.Textbox(label="Response:"),
    title="OpenAI Chatbot for Travel",
    description="Enter your message and get a response from OpenAI's GPT-3.5.",
)

iface.launch(share=True)



