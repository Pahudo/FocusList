from fastapi import FastAPI
from . import models, database, routes

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include the router
app.include_router(routes.router)