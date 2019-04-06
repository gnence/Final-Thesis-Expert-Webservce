import dialogflow_v2 as dlfv2
from google.api_core import exceptions
class manageDLF:

    def __init__(self, projectID, sessionID):
        self.project_id = projectID
        self.session_id = sessionID
        self.initial_dlf()

    #Begin Dialogflow
    def initial_dlf(self):
        self.intents_client = dlfv2.IntentsClient()
        self.session_client = dlfv2.SessionsClient()
        self.parent = self.intents_client.project_agent_path(self.project_id)
        self.session = self.session_client.session_path(self.project_id, self.session_id)

    #Create Intent
    def create_intent(self, display_name, training_phrases_parts, message_texts):
        training_phrases = []
        for training_phrases_part in training_phrases_parts:
            part = dlfv2.types.Intent.TrainingPhrase.Part(text=training_phrases_part)
            # Here we create a new training phrase for each provided part.
            training_phrase = dlfv2.types.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)
        text = dlfv2.types.Intent.Message.Text(text=message_texts)
        message = dlfv2.types.Intent.Message(text=text)
        intent = dlfv2.types.Intent(display_name=display_name,
                                    training_phrases=training_phrases,
                                    messages=[message])
        try:
            response = self.intents_client.create_intent(self.parent, intent)
        except Exception as exc:
            print(exc.args)
            return 0
        print('Intent created: {}'.format(response))
        return response

    #Detect Intent
    def detect_intent_texts(self, texts, language_code):
        print('Session path: {}\n'.format(self.session))
        result = None
        intent_name = None
        for text in texts:
            text_input = dlfv2.types.TextInput(text=text, language_code=language_code)
            query_input = dlfv2.types.QueryInput(text=text_input)
            response = self.session_client.detect_intent(session=self.session, query_input=query_input)

            print('=' * 40)
            result = response.query_result.fulfillment_text
            intent_name = response.query_result.intent.display_name
            intent_confident = response.query_result.intent_detection_confidence
            print('Query text: {}'.format(response.query_result.query_text))
            print('Detected intent: {} (confidence: {})'.format(intent_name, intent_confident))
            print('Fulfillment text: {}\n'.format(result))
        return result, intent_name