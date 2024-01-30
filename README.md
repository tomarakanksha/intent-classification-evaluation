## Deployment to Render:

1. Create a new Web Service on Render.
2. Specify the URL to your git repository.
3. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
4. Specify the following as the Start Command.

    ```shell
    streamlit run Home.py
    ```

6. Click Create Web Service.