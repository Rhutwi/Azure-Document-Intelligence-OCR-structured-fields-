import argparse, os, json
from azure_client import get_client, analyze_custom, analyze_prebuilt
from schemas import DocResult
from parsers import PARSERS

def detect_type(fname:str)->str:
    n=fname.lower()
    if "lic" in n or "dl" in n: return "driver_licence"
    return "unknown"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="folder with images/pdfs")
    ap.add_argument("--out", default="out.json")
    ap.add_argument("--use_custom", type=lambda x:x.lower()=="true", default=False)
    ap.add_argument("--model_id", default=os.getenv("MODEL_ID_CUSTOM",""))
    args=ap.parse_args()

    client=get_client()
    outputs=[]
    for fn in os.listdir(args.input):
        path=os.path.join(args.input, fn)
        if os.path.isdir(path): continue
        doc_type = detect_type(fn)
        res = analyze_custom(client, args.model_id, path) if args.use_custom else analyze_prebuilt(client, path)
        parser = PARSERS.get(doc_type, lambda r: ({}, 0.0))
        fields, conf = parser(res)
        outputs.append(DocResult(doc_type=doc_type, fields=fields, confidence=conf).model_dump())
    with open(args.out,"w") as f: json.dump(outputs,f,indent=2)
    print(f"Saved {len(outputs)} documents to {args.out}")

if __name__=="__main__": main()
