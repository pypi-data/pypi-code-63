from pynecone import Command


class Logout(Command):

    def __init__(self):
        super().__init__("logout")

    def run(self, args):
        print("logging out")