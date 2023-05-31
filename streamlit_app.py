import subprocess
import sys

def install(streamlit_chat):
    subprocess.check_call([sys.executable, "-m", "pip", "install", streamlit_chat])


from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right
