import torch
from transformers import AutoTokenizer, XLMRobertaModel, AutoModel
from .multi_task_model import MultiTaskModel
from vncorenlp import VnCoreNLP
print("Proccess")
annotator = VnCoreNLP("apis/vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')
print(annotator)
class DetectContent:
    def __init__(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("vinai-phoBERT")
        input_model = AutoModel.from_pretrained("vinai-phoBERT")

        input_model.resize_token_embeddings(len(self.tokenizer))
        
        self.model = MultiTaskModel(input_model=input_model)
        #self.model.load_state_dict(torch.load('apis/phoBERT/mymodel.pth', map_location=device))
        self.model.to(device)
        self.model.eval()
        self.device = device

    def test_save_model_locally(self):
        model_name = "vinai/phobert-large"

        # Download and cache the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Download and cache the model
        model = XLMRobertaModel.from_pretrained(model_name)

        # Save the model and tokenizer locally
        tokenizer.save_pretrained("phobert-large")
        model.save_pretrained("phobert-large")

    def process_vncorenlp(seft, text):
        annotator_text = annotator.tokenize(text)
        tokens = ""
        for i in range(len(annotator_text)):
            for j in range(len(annotator_text[i])):
                # tokens.append(annotator_text[i][j])
                tokens += annotator_text[i][j] + " "
        return tokens
    
    def process_input(self, text):
        lenght = text.count(" ") + 1
        inputs = self.tokenizer(text, return_tensors="pt", max_length=lenght, truncation=True, padding="max_length")
        print(input)
        return inputs

    def predict_from_input(self, input_text):
        text = self.process_vncorenlp(input_text)
        inputs = self.process_input(text)
        input_ids = inputs['input_ids'].to(self.device)
        attention_mask = inputs['attention_mask'].to(self.device)

        with torch.no_grad():
            span_logits = self.model(input_ids, attention_mask)

        span_preds = (span_logits.squeeze().cpu().numpy() > 0.5).astype(int)
        return text, span_preds
