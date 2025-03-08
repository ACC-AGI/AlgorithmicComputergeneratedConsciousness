from gradio_client import Client

class ChatSessionWithTejsZ3ta:
    def __init__(self):
        self.client = Client("TejAndrewsACC/Z3ta_Z")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            param_2=2048,
            param_3=0.7,
            param_4=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

from gradio_client import Client

class Pulse:
    def __init__(self):
        self.client = Client("TejAndrewsACC/Pulsenorm")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            param_2=512,
		    param_3=0.7,
		    param_4=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

from gradio_client import Client

class ACCo1:
    def __init__(self):
        self.client = Client("TejAndrewsACC/ACC_o1")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            user_system_message="",
            max_tokens=2048,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

from gradio_client import Client

class Surefire:
    def __init__(self):
        self.client = Client("TejAndrewsACC/Surefire")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            param_2=512,
	    param_3=0.7,
	    param_4=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

from gradio_client import Client

class GertrudePlus:
    def __init__(self):
        self.client = Client("TejAndrewsACC/Gertrudev3.00-ACC")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            max_tokens=2048,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

from gradio_client import Client

class Z3ta:
    def __init__(self):
        self.client = Client("TejAndrewsACC/Z3ta_Z")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            param_2=2048,
            param_3=0.7,
            param_4=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

from gradio_client import Client

class Emote:
    def __init__(self):
        self.client = Client("TejAndrewsACC/EMOTE")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            max_tokens=512,
	    temperature=0.7,
	    top_p=0.95,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history

class FiPhiNeuralMarkV3:
    def __init__(self):
        self.client = Client("TejAndrewsACC/FiPhi-NeuralMark-V3-Chat")
        self.history = []

    def send_message(self, message: str):
        if message.strip().lower() == "/bye":
            self.history.clear()
            return "Session cleared. Goodbye!"

        response = self.client.predict(
            message=message,
            api_name="/chat"
        )
        self.history.append((message, response))
        return response

    def get_history(self):
        return self.history















