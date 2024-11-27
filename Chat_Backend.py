#Import pydantic for defining data models and pymongo for MongoDB
from pydantic import BaseModel 
import pymongo

#Import traceback for error handling 
import traceback 

#Import os and sys for system-related operations 
import os, sys 

#Import FastAPI components for building the web applications 
from fastapi import(
    FastAPI,
    UploadFile,
    status,
    HTTPException)
from fastapi.responses import JSONResponse # Import JSONResponse for returning JSON responses 
from fastapi.middleware.cors import CORSMiddleware #CORS middleware to handle cross-Origin Resources 

#Import langchain for building applications powered by language models 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores import FAISS 
from langchain_community.document_loaders import S3FileLoader
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain_community.callbacks import get_openai_callback
from langchain.chains import ConversationalRetrievalChain 
from langchain_openai import chatopenAI

import gc 
import urllib
import awswrangler 
import boto3 

#Setting environment variables  and defining variables for AWS S3 config 
os.environ['OPEN_API_KEY']="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"
S3_KEY = ""
S3_BUCKET = ""
S3_REGION = ""
S3_PATH = ""

#Setting up MongoDB 
try:
    MONGO_URL = ""

    #Connect to MongoDB using the provided MONGO_URL
    