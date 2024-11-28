from fastapi import FastAPI, UploadFile,HTTPException
from fastapi.responses import JSONResponse
import os 
from datetime import datetime 
import boto3 
import awswrangler as wr
from pymongo import MongoClient
import pymongo

#Initialize FastAPI app



# Initialize S3 boto3 session and MongoDB client (adjust your connection as needed)
aws_s3 = boto3.Session(
    aws_access_key_id=""
    aws_secret_access_key=""
    region_name="us-east-2" 
)
client = MongoClient("mongodb://localhost:27017")
db = client["local"]

#Define your S3 bucket and path 
S3_BUCKET = "docchat"
S3_PATH = "downloads/"

@app.post("/uploadFile")
async def uploadtos3(data_file: UploadFile):

    try:
        file_name = data_file.filename.split
