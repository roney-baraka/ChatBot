from fastapi import FastAPI, UploadFile,HTTPException
from fastapi.responses import JSONResponse
import os 
from datetime import datetime 
import boto3 
import awswrangler as wr
from pymongo import MongoClient
import pymongo

#Initialize FastAPI app

