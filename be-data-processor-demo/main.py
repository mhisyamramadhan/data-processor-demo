from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io
import uvicorn
import os
import importlib
import pandas as pd
import csv
import pytz
from datetime import datetime
from fastapi import Request
from datetime import datetime
from dummy_data import generate_dummy_df

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)


@app.post("/process")
async def process_file(
    code: str = Form(...),
    file: UploadFile = File(...),
    timezone: str = Form("Asia/Jakarta")
):

    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be CSV format (.csv).")
    
    code = code.strip().lower()

    df = generate_dummy_df(code)
    
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    try:
        tz = pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        tz = pytz.timezone("UTC")

    timestamp = datetime.now(tz).strftime("%Y%m%d_%H%M%S")
    output_filename = f"{code}_{timestamp}.csv"

    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{output_filename}"'}
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)