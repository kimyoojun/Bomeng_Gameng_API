from client import openai

def travel_ai(req):
    openais =  openai.responses.create(
            model = "gpt-5.4",
            input = req
        )
    
    return openais.output_text
