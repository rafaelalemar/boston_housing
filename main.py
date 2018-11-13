import sklearn
print("A versão do scikit-learn é ", sklearn.__version__)
if sklearn.__version__ >= '0.18':
    print("Tudo certo!")
else:
    print("Você precisa fazer upgrade do scikit-learn ou ficar atento com as diferenças das versões")
    print("Pode ser feito executando:\n")
    print("pip install scikit-learn==0.18.1")

# Importar as bibliotecas necessárias para este projeto
# import numpy as np
# import pandas as pd
import visuals as vs  # Supplementary code
# from sklearn.model_selection import ShuffleSplit