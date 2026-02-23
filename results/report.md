# LLM Evaluation Report

## Aggregate Metrics

| metric            |     mean |   median |         std |       min |      max |
|:------------------|---------:|---------:|------------:|----------:|---------:|
| bleu              | 0.47374  | 0.562341 | 0.118135    | 0.316228  | 0.562341 |
| rouge_l           | 1        | 1        | 0           | 1         | 1        |
| bertscore         | 1        | 1        | 1.18588e-07 | 1         | 1        |
| faithfulness      | 0.355433 | 0.331902 | 0.157716    | 0.124986  | 0.646707 |
| context_relevance | 0.645134 | 0.642612 | 0.096937    | 0.399524  | 0.883539 |
| answer_relevance  | 0.266934 | 0.226133 | 0.176957    | 0.0239553 | 0.66024  |

## Per-example Scores (first 25)

| query                 | expected_answer                   | model_answer                      |     bleu |   rouge_l |   bertscore |   faithfulness |   context_relevance |   answer_relevance |
|:----------------------|:----------------------------------|:----------------------------------|---------:|----------:|------------:|---------------:|--------------------:|-------------------:|
| What is AI?           | Artificial Intelligence           | Artificial Intelligence           | 0.316228 |         1 |           1 |       0.609602 |            0.883539 |          0.66024   |
| What is ML?           | Machine Learning                  | Machine Learning                  | 0.316228 |         1 |           1 |       0.381622 |            0.566327 |          0.291904  |
| What is Python?       | A programming language            | A programming language            | 0.562341 |         1 |           1 |       0.600919 |            0.79758  |          0.553371  |
| What is NLP?          | Natural Language Processing       | Natural Language Processing       | 0.562341 |         1 |           1 |       0.605335 |            0.754834 |          0.466894  |
| What is RAG?          | Retrieval Augmented Generation    | Retrieval Augmented Generation    | 0.562341 |         1 |           1 |       0.646707 |            0.602507 |          0.0588189 |
| What is Docker?       | A containerization tool           | A containerization tool           | 0.562341 |         1 |           1 |       0.369507 |            0.6283   |          0.483191  |
| What is Git?          | Version control system            | Version control system            | 0.562341 |         1 |           1 |       0.3888   |            0.593792 |          0.344384  |
| What is API?          | Application Programming Interface | Application Programming Interface | 0.562341 |         1 |           1 |       0.276135 |            0.567257 |          0.391763  |
| What is CLI?          | Command Line Interface            | Command Line Interface            | 0.562341 |         1 |           1 |       0.595494 |            0.710693 |          0.359643  |
| What is JSON?         | Data format                       | Data format                       | 0.316228 |         1 |           1 |       0.331902 |            0.685426 |          0.179462  |
| What is YAML?         | Configuration format              | Configuration format              | 0.316228 |         1 |           1 |       0.139595 |            0.751356 |          0.127974  |
| What is BLEU?         | Text evaluation metric            | Text evaluation metric            | 0.562341 |         1 |           1 |       0.318401 |            0.642762 |          0.106725  |
| What is ROUGE?        | Recall-based metric               | Recall-based metric               | 0.316228 |         1 |           1 |       0.231747 |            0.632529 |          0.0239553 |
| What is BERTScore?    | Semantic similarity metric        | Semantic similarity metric        | 0.562341 |         1 |           1 |       0.267826 |            0.711952 |          0.226133  |
| What is FastAPI?      | Python web framework              | Python web framework              | 0.562341 |         1 |           1 |       0.124986 |            0.666144 |          0.0787097 |
| What is PyTest?       | Testing framework                 | Testing framework                 | 0.316228 |         1 |           1 |       0.384786 |            0.67704  |          0.0576354 |
| What is CI/CD?        | Automation pipeline               | Automation pipeline               | 0.316228 |         1 |           1 |       0.401263 |            0.543188 |          0.0971441 |
| What is GPU?          | Graphics Processing Unit          | Graphics Processing Unit          | 0.562341 |         1 |           1 |       0.482544 |            0.626252 |          0.581314  |
| What is CPU?          | Central Processing Unit           | Central Processing Unit           | 0.562341 |         1 |           1 |       0.326442 |            0.653377 |          0.373516  |
| What is LLM?          | Large Language Model              | Large Language Model              | 0.562341 |         1 |           1 |       0.212394 |            0.634837 |          0.150721  |
| What is OpenAI?       | AI research company               | AI research company               | 0.562341 |         1 |           1 |       0.161165 |            0.565425 |          0.329994  |
| What is Anthropic?    | AI company                        | AI company                        | 0.316228 |         1 |           1 |       0.182057 |            0.399524 |          0.140958  |
| What is Transformers? | Deep learning architecture        | Deep learning architecture        | 0.562341 |         1 |           1 |       0.132986 |            0.495601 |          0.138213  |
| What is Token?        | Text unit                         | Text unit                         | 0.316228 |         1 |           1 |       0.384136 |            0.695491 |          0.237169  |
| What is Prompt?       | Input to LLM                      | Input to LLM                      | 0.562341 |         1 |           1 |       0.329468 |            0.642612 |          0.21352   |
