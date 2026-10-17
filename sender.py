# sender.py – core sender logic

class Sender:
    def __init__(self):
        self.config = {}

    def load_config(self, path="config.json"):
        # stub: load wallet addresses, RPC URLs, etc.
        pass

    def run(self):
        print("[Sender] Initializing...")
        self.load_config()
        print("[Sender] Ready to process transactions.")