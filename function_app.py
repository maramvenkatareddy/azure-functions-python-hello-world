import azure.functions as func
import logging
import random

app = func.FunctionApp()

@app.route(route="MyFunction", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def MyFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = "Working As a DevOps Engineer"

    # List of Colors 🔥
    colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink"]

    # Pick Random Color
    random_color = random.choice(colors)

    html_content = f"<html><body><h1 style='color:{random_color};'>{name}</h1></body></html>"

    return func.HttpResponse(html_content, status_code=200, mimetype="text/html")

def venkat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = "I am Venkat"

    # List of Colors 🔥
    colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink"]

    # Pick Random Color
    random_color = random.choice(colors)

    html_content = f"<html><body><h1 style='color:{random_color};'>{name}</h1></body></html>"

    return func.HttpResponse(html_content, status_code=200, mimetype="text/html")
