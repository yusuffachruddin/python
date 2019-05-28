# Import Spark NLP
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp.embeddings import *
import sparknlp

import findspark
findspark.init("D:\\Python\\SRC\\spark-2.4.3-bin-hadoop2.7\\spark-2.4.3-bin-hadoop2.7")

# Start Spark Session with Spark NLP
spark = sparknlp.start()

# Download a pre-trained pipeline
pipeline = PretrainedPipeline('explain_document_dl', lang='en')

# Your testing dataset
text = """
The Mona Lisa is a 16th century oil painting created by Leonardo.
It's held at the Louvre in Paris.
"""

# Annotate your testing dataset
result = pipeline.annotate(text)

# What's in the pipeline
list(result.keys())
Output: ['entities', 'stem', 'checked', 'lemma', 'document',
'pos', 'token', 'ner', 'embeddings', 'sentence']

# Check the results
result['entities']
Output: ['Mona Lisa', 'Leonardo', 'Louvre', 'Paris']
