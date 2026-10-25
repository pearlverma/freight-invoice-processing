import os,json,csv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pdf_extraction import read_pdf


load_dotenv()
print("Gemini key loaded:", bool(os.getenv("GOOGLE_API_KEY")))

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    timeout=30,
    max_retries=2
)

details=("Invoice Number","Invoice Date","Seller","Buyer","Invoice Total")

def validate_invoice(details1):
    missing=[]
    status= "valid"
    reason=""
    
    for x in details:
        if not details1[x]:
            missing.append(x)
            status="Needs review"
    
    try:
        if details1["Invoice Total"]:
            details1["Invoice Total"]= float(details1["Invoice Total"])
            if details1["Invoice Total"]<=0:
                status = "Invalid"
                reason="invalid Total"
    except ValueError:
        status= "Needs review"
        reason="invalid total"
    if missing:
        reason=reason +"; missing:"+" ".join(missing)
   
        
    details1["status"]= status
    details1["why review"]=reason
    return status

def process_invoice(data):
    valid=0
    review=0
    invalid=0
    for field in details:
        data.setdefault(field, "")
    
    fieldname = details + ("status","why review")
    with open ('invoice_records.csv','a',newline="", encoding="utf-8")as file:
        print("file opened succesfully") 
        writer = csv.DictWriter(file, fieldnames=fieldname)
        if os.path.getsize("invoice_records.csv") == 0:
            writer.writeheader()
        
        validate_invoice(data)
        if data["status"] == "valid":
                valid += 1
        elif data["status"] == "Needs review":
                review += 1
        else:
                invalid += 1
            
        writer.writerow(data)
    print(f"processing summary:\n valid: {valid} \n invalid:{invalid} \n needs review: {review} \n " )

invoice_text = read_pdf("invoice.pdf")


def extract_invoice_with_ai(invoice_text):
    prompt = f"""
    Extract these five fields from the invoice:
    - Invoice Number
    - Invoice Date
    - Seller
    - Buyer
    - Invoice Total

    Return only a valid JSON object with exactly these
    field names. Use an empty string for missing fields.
    Do not invent values.

    Invoice text:
    {invoice_text}
    """

    
    print("Sending invoice text to Gemini...")
    response = model.invoke(prompt)
    print("Gemini response received.")
    content = response.content

    # Convert list-based responses into text.
    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, str):
                text_parts.append(block)
            elif isinstance(block, dict):
                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

        content = "\n".join(text_parts)

    content = content.strip()

    # Remove Markdown code fences, if present.
    if content.startswith("```"):
        content = content.split("\n", 1)[1]
        content = content.rsplit("```", 1)[0].strip()

    return json.loads(content)

invoice_details=extract_invoice_with_ai(invoice_text)
process_invoice(invoice_details)

