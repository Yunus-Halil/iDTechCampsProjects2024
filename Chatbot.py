import pyttsx3
from openai import OpenAI
import audio_to_text
import recording
import pyttsx3

client = OpenAI(
    api_key="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"
)

end_program = False

while not end_program:
    recording.record()
    get_input = audio_to_text.transcribe()
    if get_input.lower() == 'goodbye' or get_input.lower() == 'exit':
        end_program = True
        print("Have a nice day!")
    else:
        system_data = [
            {'role':'system','content':'you are a nonchalant assistant who is a master coder and startup founder and chill'},
            {'role':'user','content':get_input}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = system_data
        )
        AI_response = response.choices[0].message.content
        
        engine = pyttsx3.init()
        engine.say(AI_response)
        engine.runAndWait()
        
        print(AI_response)


