from src.TextSummerizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
import os 
from dotenv import load_dotenv
load_dotenv()


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained('google/pegasus-cnn_dailymail')
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model='xonic48/pegasus-samsum',tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output