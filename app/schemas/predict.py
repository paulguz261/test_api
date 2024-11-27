from typing import Any, List, Optional

from pydantic import BaseModel
from model.processing.validation import DataInputSchema

# Esquema de los resultados de predicción
class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]

# Esquema para inputs múltiples
class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "gender":"Female",
                        "age":57.0,
                        "hypertension":0,
                        "heart_disease":1,
                        "ever_married":"Yes",
                        "work_type":"Private",
                        "Residence_type":"Urban",
                        "avg_glucose_level":216.58,
                        "bmi":31.0,
                        "smoking_status":"Unknown",
                    }
                ]
            }
        }
