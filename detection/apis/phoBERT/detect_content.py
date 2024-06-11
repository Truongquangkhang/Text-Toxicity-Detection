import numpy as np
import onnxruntime
from transformers import AutoTokenizer
from vncorenlp import VnCoreNLP

# Load VnCoreNLP
annotator = VnCoreNLP("apis/vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')
# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("phobert-large")

class DetectContent:
    def __init__(self):
        self.ort_session = onnxruntime.InferenceSession("apis/phoBERT/mymodel.onnx")

    def process_vncorenlp(self, text):
        annotator_text = annotator.tokenize(text)
        tokens = ""
        for i in range(len(annotator_text)):
            for j in range(len(annotator_text[i])):
                tokens += annotator_text[i][j] + " "
        return tokens
    
    def process_input(self, text):
        inputs = tokenizer(text, return_tensors="np", max_length=64, truncation=True, padding="max_length")
        return inputs

    def predict_from_input(self, input_text):
        text = self.process_vncorenlp(input_text)
        inputs = self.process_input(text)

        # Update input names according to the ONNX model
        ort_inputs = {
            "input_ids": inputs["input_ids"].astype(np.int64),
            "attention_mask": inputs["attention_mask"].astype(np.int64)
        }

        ort_outs = self.ort_session.run(None, ort_inputs)
        span_preds = (ort_outs[0].squeeze() > 0.5).astype(int)

        return text, span_preds
