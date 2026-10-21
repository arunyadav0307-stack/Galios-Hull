#!/usr/bin/env python3
"""Clean HTTP download portal serving the Nova Science Publishers chapter .docx and full package."""

import html
import mimetypes
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DOWNLOAD_MAP = {
    "Quantum_Circuits_and_Quantum_Algorithms_Nova_Chapter.docx": os.path.join(
        BASE_DIR, "Quantum_Circuits_and_Quantum_Algorithms_Nova_Chapter.docx"
    ),
    "Nova_Chapter_Submission_Package.zip": os.path.join(
        BASE_DIR, "Nova_Chapter_Submission_Package.zip"
    ),
    "Verified_Reference_List_APA7.docx": os.path.join(
        BASE_DIR,
        "Nova_Chapter_Submission_Package",
        "3_Verified_Reference_List",
        "Verified_Reference_List_APA7.docx",
    ),
    "Submission_Readiness_Checklist.docx": os.path.join(
        BASE_DIR,
        "Nova_Chapter_Submission_Package",
        "4_Submission_Readiness_Checklist",
        "Submission_Readiness_Checklist.docx",
    ),
}

FIG_DIR = os.path.join(BASE_DIR, "Nova_Chapter_Submission_Package", "2_Separate_Figure_Files")
if os.path.isdir(FIG_DIR):
    for fn in sorted(os.listdir(FIG_DIR)):
        DOWNLOAD_MAP[fn] = os.path.join(FIG_DIR, fn)


def fmt_size(path: str) -> str:
    n = os.path.getsize(path)
    return f"{n / (1024 * 1024):.2f} MB" if n >= 1024 * 1024 else f"{n / 1024:.0f} KB"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        req_path = urllib.parse.unquote(parsed.path).lstrip("/")

        if req_path.startswith("download/"):
            fname = req_path[len("download/"):]
        else:
            fname = req_path

        if fname in DOWNLOAD_MAP and os.path.isfile(DOWNLOAD_MAP[fname]):
            fpath = DOWNLOAD_MAP[fname]
            ctype, _ = mimetypes.guess_type(fpath)
            if fname.endswith(".docx"):
                ctype = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            elif fname.endswith(".pptx"):
                ctype = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
            elif not ctype:
                ctype = "application/octet-stream"
            with open(fpath, "rb") as fh:
                data = fh.read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Content-Disposition", f'attachment; filename="{fname}"')
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
            return

        fig_items = "".join(
            f'<li><a href="download/{html.escape(k)}" download="{html.escape(k)}">{html.escape(k)}</a> '
            f'<span>({fmt_size(v)})</span></li>'
            for k, v in DOWNLOAD_MAP.items()
            if k.startswith("Figure_")
        )
        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nova Science Publishers Chapter — Download Portal</title>
<style>
  body {{ font-family: Georgia, "Times New Roman", serif; max-width: 820px; margin: 36px auto; padding: 0 20px; color: #111; line-height: 1.55; background: #fafafa; }}
  .card {{ background: #fff; border: 1px solid #d4d4d4; border-radius: 6px; padding: 28px 32px; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }}
  h1 {{ font-size: 1.35rem; margin-top: 0; }}
  .meta {{ color: #444; font-size: 0.94rem; margin-bottom: 22px; }}
  .btn {{ display: inline-block; padding: 12px 20px; margin: 6px 10px 6px 0; border-radius: 4px; text-decoration: none; font-weight: bold; font-family: system-ui, sans-serif; font-size: 0.94rem; }}
  .btn-primary {{ background: #111; color: #fff; border: 1px solid #111; }}
  .btn-secondary {{ background: #fff; color: #111; border: 1px solid #333; }}
  h2 {{ font-size: 1.08rem; margin-top: 26px; border-bottom: 1px solid #e2e2e2; padding-bottom: 6px; }}
  ul {{ columns: 2; padding-left: 18px; font-size: 0.9rem; }}
  li {{ margin-bottom: 6px; }}
  li span {{ color: #666; font-size: 0.82rem; }}
</style>
</head>
<body>
<div class="card">
  <h1>Quantum Circuits and Quantum Algorithms: Foundations, Design Principles, and Applications in Intelligent Computing</h1>
  <div class="meta">
    <strong>Book:</strong> <em>Quantum Artificial Intelligence and Machine Learning: Principles, Algorithms, and Applications</em><br>
    <strong>Publisher:</strong> Nova Science Publishers &nbsp;|&nbsp; <strong>Format:</strong> US Letter (8.5 × 11 in), Times New Roman 10.5 pt, 19 pages
  </div>
  <a class="btn btn-primary" href="download/Quantum_Circuits_and_Quantum_Algorithms_Nova_Chapter.docx" download="Quantum_Circuits_and_Quantum_Algorithms_Nova_Chapter.docx">
    Download Chapter Manuscript (.docx — {fmt_size(DOWNLOAD_MAP['Quantum_Circuits_and_Quantum_Algorithms_Nova_Chapter.docx'])})
  </a>
  <a class="btn btn-secondary" href="download/Nova_Chapter_Submission_Package.zip" download="Nova_Chapter_Submission_Package.zip">
    Download Full Submission Package (.zip — {fmt_size(DOWNLOAD_MAP['Nova_Chapter_Submission_Package.zip'])})
  </a>
  <h2>Supporting Deliverables</h2>
  <ul>
    <li><a href="download/Verified_Reference_List_APA7.docx" download="Verified_Reference_List_APA7.docx">Verified_Reference_List_APA7.docx</a> <span>({fmt_size(DOWNLOAD_MAP['Verified_Reference_List_APA7.docx'])})</span></li>
    <li><a href="download/Submission_Readiness_Checklist.docx" download="Submission_Readiness_Checklist.docx">Submission_Readiness_Checklist.docx</a> <span>({fmt_size(DOWNLOAD_MAP['Submission_Readiness_Checklist.docx'])})</span></li>
  </ul>
  <h2>Separate Original Figure Source Files (600 DPI PNG/TIFF + Vector PPTX/DOCX/EPS)</h2>
  <ul>{fig_items}</ul>
</div>
</body>
</html>""".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8080), Handler)
    print("Serving Nova Chapter download portal on http://0.0.0.0:8080", flush=True)
    server.serve_forever()
