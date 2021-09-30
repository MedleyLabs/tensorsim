import pandas as pd

from fastapi import FastAPI

from sim import TensorSim


app = FastAPI()

df = pd.DataFrame([[0, 0], [1, 1], [2, 2], [3, 3]], columns=['x', 'y'])

sim = TensorSim(df,
                data_cols=['x'],
                target_cols=['y'],
                sim_accuracy=0.8,
                shuffle=True)


@app.get('/predictions/{prediction_id}')
def get_prediction(prediction_id: int):

    data, prediction = next(sim)

    response = {
        'prediction_id': prediction_id,
        'data': data.to_json(),
        'prediction': prediction.to_json()
    }

    return response
