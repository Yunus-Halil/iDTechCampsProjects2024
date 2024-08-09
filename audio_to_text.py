from openai import OpenAI

client = OpenAI(
    api_key = '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'
)
def transcribe():

    audiofile = open("audio.wav",'rb')

    transcript = client.audio.transcriptions.create(
        model='whisper-1',
        file=audiofile
    )
    print(transcript.text)

transcribe()


