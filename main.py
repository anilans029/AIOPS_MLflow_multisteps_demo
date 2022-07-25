import mlflow

def main():
    with mlflow.start_run():
        mlflow.run(".","stage1",use_conda=False)
        mlflow.run(".","stage2",use_conda=False)
        mlflow.run(".","stage3",use_conda=False)

if __name__=="__main__":
    main()