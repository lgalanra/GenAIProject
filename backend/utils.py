from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from datasets import load_dataset

# Load a pre-trained model
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

# Load a dataset
dataset = load_dataset('squad', split='train[:100]')