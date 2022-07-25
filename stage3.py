import mlflow

new_text = "hi anil"

with open("artifact_2.txt","w") as f:
    f.write(new_text+ "added lines")
mlflow.log_artifact("artifacts1.txt",artifact_path= "features")

print("end of stage3")