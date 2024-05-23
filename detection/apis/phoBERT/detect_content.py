import torch
from transformers import AutoTokenizer, XLMRobertaModel
from .multi_task_model import MultiTaskModel

class DetectContent:
    def __init__(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-large",  force_download= False)
        input_model = XLMRobertaModel.from_pretrained("vinai/phobert-large",  force_download= False)
        input_model.resize_token_embeddings(len(self.tokenizer))

        self.model = MultiTaskModel(input_model=input_model)
        self.model.load_state_dict(torch.load('apis/phoBERT/mymodel.pth', map_location=device))
        self.model.to(device)
        self.model.eval()
        self.device = device

    def process_input(self, text):
        lenght = text.count(" ") + 1
        inputs = self.tokenizer(text, return_tensors="pt", max_length=lenght, truncation=True, padding="max_length")
        return inputs

    def predict_from_input(self, input_text):
        inputs = self.process_input(input_text)
        input_ids = inputs['input_ids'].to(self.device)
        attention_mask = inputs['attention_mask'].to(self.device)

        with torch.no_grad():
            span_logits = self.model(input_ids, attention_mask)

        span_preds = (span_logits.squeeze().cpu().numpy() > 0.5).astype(int)
        return span_preds
