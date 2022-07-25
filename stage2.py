import mlflow

with open("artifact_1.txt","r") as f:
    text = f.read()
mlflow.log_artifact("artifacts1.txt",artifact_path= "features")

print(text)
