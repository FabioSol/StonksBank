import pickle

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from models.request_evaluation import RequestEvaluation
from models.amortization import Amortization
from models.amortization import *

app = FastAPI()

with open('./models/model.pkl','rb') as file:
    model = pickle.load(file, fix_imports=True)

@app.get("/health")
def checkhealt():
    return{"isalive": True}

@app.post("/evaluate")
async def evaluate(req: RequestEvaluation):
    print(req)
    df = pd.DataFrame({
        "int_rate": [req.int_rate],
        "out_prncp": [req.out_prncp],
        "total_rec_prncp": [req.total_rec_prncp],
        "last_pymnt_amnt": [req.last_pymnt_amnt],
        "addr_state": [req.addr_state],
        "grade": [req.grade],
        "sub_grade": [req.sub_grade],
        "total_pymnt": [req.total_pymnt],
    })
    pred = model.predict_proba(df)[0]
    default_prob = pred[1]
    print(default_prob)
    amort = Amortization(100_000, 0.5, 12, default_prob)
    opt_rate = Amortization.optimize_expected_irr(0, amort)
    return {
        "pd": f"{default_prob*100:.2f} %",
        "interest_rate": f"{opt_rate*100:.4f} %"
    }


# comand uvicorn app.main:app --reload --port 8899

# en postamn/ headers poner json y en body poner el json con la informacion


# model = model.pkl


#dentro de utils ponemos la clase de amortizacion

# falto agregar arriba del amort df = pred[1]
# dfdf