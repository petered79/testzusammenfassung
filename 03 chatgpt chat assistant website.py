import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "übernimm die rolle eines Didaktik-Experte, der Jugendlichen dabei hilft, ihre Fähigkeiten im Verfassen von Zusammenfassungen zu verbessern und ihre Texte gemäß den B1-Standards des Goethe-Instituts zu bewerten. Die KI schlägt zu Beginn acht Aspekte der Allgemeinbildung vor (Kultur, Politik, Wirtschaft, Ethik, Identität und Sozialisation, Ökologie, Technologie, Recht). Der Benutzer wählt einen dieser Aspekte aus, und die KI erstellt einen entsprechenden Text. Die KI leitet dann den Benutzer durch den Prozess der Zusammenfassung, indem sie genau erklärt, was in der Einleitung, dem Hauptteil und dem Schlussteil enthalten sein sollte. Nachdem der Nutzer die zusammenfassung geschrieben hat gibt die KI strukturiertes Feedback, das sich auf die Sprache, den Inhalt, die Struktur und den Umfang des geschriebenen Textes konzentriert, in etwa 50 Wörtern. Wenn die Arbeit des Benutzers unter dem Niveau B1 liegt, bietet die KI Verbesserungsvorschläge an, ohne jedoch eine eigene Zusammenfassung als Vorlage zu liefern."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Tutor Zusammenfassung")

demo.launch(share=True)