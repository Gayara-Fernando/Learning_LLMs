import os

def set_environment():
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""  # <- this has to be your api key!
    # I'm omitting all other keys