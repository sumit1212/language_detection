import re
import pickle
from pathlib import Path

__version__ = "0.1.0"

base_dir = Path(__file__).resolve(strict=True).parent

with open(f"{base_dir}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

classes = [
    'Arabic', 'Danish', 'Dutch', 'English', 'French', 'German',
       'Greek', 'Hindi', 'Italian', 'Kannada', 'Malayalam', 'Portugeese',
       'Russian', 'Spanish', 'Sweedish', 'Tamil', 'Turkish'
]

def lang_predict(text):
    # text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    # text = re.sub(r'[[]]', ' ', text)
    # text = text.lower()
    text = re.sub(r'[!@#$(),\n"%^&*?\:;~`0-9]', ' ', text)
    # text = re.sub(r'[[]]', ' ', text)
    text = text.lower()
    print(text,'#########')
    pred = model.predict([text])
    return classes[pred[0]]

# text = "Bonjour comment allez-vous?"
# text = "नमस्ते, आप कैसे हैं?"
# res = lang_predict(text)
# print('Result : ', res)
