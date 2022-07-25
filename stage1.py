import mlflow

text=  "input 1"

with open("artifact_1.txt","w") as f:
    f.write(text)
mlflow.log_artifact("artifact_1.txt",artifact_path= "features")
