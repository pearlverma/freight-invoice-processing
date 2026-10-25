# Freight Invoice Processing System

## Overview

The Freight Invoice Processing System is a Python-based project designed to extract important information from freight invoices in PDF format, validate the extracted data, and store the results in a CSV file.

The project combines PDF text extraction with AI-assisted information extraction using Google's Gemini API through LangChain.

## Features

- **PDF Text Extraction:** Extracts text from freight invoice PDF files using PyMuPDF.
- **AI-Powered Data Extraction:** Uses Gemini to identify and extract invoice details.
- **Structured Information:** Extracts the following fields:
  - Invoice Number
  - Invoice Date
  - Seller
  - Buyer
  - Invoice Total
- **Data Validation:** Checks for missing required fields and validates the invoice total.
- **Status Classification:** Classifies records as `valid`, `Needs review`, or `Invalid`.
- **CSV Storage:** Stores extracted invoice information, processing status, and review reasons in a CSV file.

## Technologies Used

- Python
- PyMuPDF
- LangChain
- Google Gemini API
- JSON
- CSV
- python-dotenv

## Project Workflow

1. Read the invoice PDF file.
2. Extract text from the PDF using PyMuPDF.
3. Send the extracted text to Gemini for structured information extraction.
4. Parse the AI-generated response into JSON.
5. Validate the extracted invoice fields.
6. Assign a processing status and a reason if the invoice requires review.
7. Append the processed record to `invoice_records.csv`.

## Project Structure

```text
freight-invoice-processing/
├── main.py
├── pdf_extraction.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pearlverma/freight-invoice-processing.git
cd freight-invoice-processing
```

### 2. Create a Virtual Environment

For macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project directory and add your Gemini API key:

```text
GOOGLE_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never upload your `.env` file or expose your API key publicly.

### 5. Add an Invoice PDF

Place a test invoice named `invoice.pdf` in the project directory. The current code expects this filename.

Use sample or anonymized invoice data for testing.

### 6. Run the Project

```bash
python main.py
```

The extracted information and validation results are intended to be stored in invoice_records.csv.

Validation Logic

The project checks whether required invoice fields are missing and whether the invoice total is numeric and greater than zero.

Depending on the validation outcome, a record is assigned a status:

valid

Needs review

Invalid

Records requiring review should be checked against the original invoice before their information is used.

Testing Status

A test run successfully received a response from Gemini and continued through the CSV-processing step. During that run, one invoice was classified as Needs review.

This demonstrates that the API request and processing flow completed for that run. However, the extracted values still need to be checked against the original invoice, and additional testing is required to assess reliability across different invoice formats.


Future Improvements

Improve API error handling and response parsing.

Add automated unit and integration tests.

Support processing multiple invoices in one run.

Detect duplicate invoices.

Add more comprehensive invoice-total and line-item validation.

Improve logging and error reporting.

Develop a user-friendly interface.

Disclaimer

This project is a prototype for freight invoice information extraction and basic validation. All extracted information should be reviewed against the original invoice before being used for financial or business decisions.
