import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="MyFunction", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def MyFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = "helloworld !!"  # Hardcoded Variable Here ✅

    return func.HttpResponse(f"{name}", status_code=200)
