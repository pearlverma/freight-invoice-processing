# Freight Invoice Processing System

## Overview

The Freight Invoice Processing System is a Python-based project designed to extract important information from freight invoices in PDF format, validate the extracted data, and store the results in a CSV file.

The project uses PDF text extraction, AI-assisted information extraction, data validation, and structured data storage.

## Features

- Extract text from PDF invoices using PyMuPDF.
- Use Google's Gemini API through LangChain for AI-assisted invoice field extraction.
- Extract invoice number, invoice date, seller, buyer, and invoice total.
- Validate required fields and invoice totals.
- Store processed invoice records in CSV format.
- Flag records that require further review.

## Technologies Used

- Python
- PyMuPDF
- LangChain
- Google Gemini API
- JSON
- CSV
- python-dotenv

## How It Works

1. Read the invoice PDF.
2. Extract text from the PDF.
3. Send the extracted text to Gemini with instructions to return structured JSON.
4. Parse the extracted information.
5. Validate the required fields and invoice total.
6. Assign a processing status and review reason.
7. Append the result to a CSV file.

## Extracted Fields

- Invoice Number
- Invoice Date
- Seller
- Buyer
- Invoice Total

## Validation

The application checks for missing required fields and invalid invoice totals. It assigns a status and records a reason when an invoice needs review.

## Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd freight-invoice-processing
```

Replace `YOUR_REPOSITORY_URL` with your repository's HTTPS URL.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project directory:

```text
GOOGLE_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never commit the `.env` file to GitHub.

### 5. Add a test invoice

Place a test PDF named `invoice.pdf` in the project directory, matching the filename expected by the application.

Use synthetic or anonymized invoice data for testing.

### 6. Run the project

```bash
python main.py
```

The intended output is a CSV file containing extracted invoice fields, processing status, and review reasons.

## Current Status

The PDF extraction and validation workflow has been implemented. The Gemini API integration is still awaiting a successful end-to-end test because the API returned temporary availability errors during testing.

Successful AI extraction and CSV generation should be verified when the model is available.

## Future Improvements

- Add robust API error handling and retries.
- Implement a Python-based fallback for supported invoice formats.
- Detect duplicate invoices.
- Improve invoice-total reconciliation.
- Add automated tests.
- Support batch processing of multiple invoices.
- Add logging and a user-friendly interface.

## Disclaimer

This project is a prototype. Extracted invoice data should be reviewed before being used for financial or business decisions.