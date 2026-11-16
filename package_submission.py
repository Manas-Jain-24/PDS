import os
import zipfile

def package_submission(group_id="13"):
    zip_name = f"Project_{group_id}.zip"
    notebook_src = os.path.join("PDS", "notebooks", "fraud_detection.ipynb")
    report_src = os.path.join("PDS", "report", "report.pdf")
    
    if not os.path.exists(notebook_src):
        print(f"Error: Notebook not found at {notebook_src}")
        return
        
    if not os.path.exists(report_src):
        print(f"Notice: {report_src} not found yet.")
        print("Please compile PDS/report/report.tex on Overleaf, download report.pdf, and place it at PDS/report/report.pdf.")
        print("Creating placeholder zip with fraud_detection.ipynb for now...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(notebook_src, arcname="fraud_detection.ipynb")
        if os.path.exists(report_src):
            z.write(report_src, arcname="report.pdf")
            print(f"Added {report_src} as report.pdf")
        else:
            print("(report.pdf will need to be added once compiled)")
            
    print(f"\nSubmission archive generated: {os.path.abspath(zip_name)}")
    with zipfile.ZipFile(zip_name, 'r') as z:
        print("Archive contents:")
        for info in z.infolist():
            print(f" - {info.filename} ({info.file_size:,} bytes)")

if __name__ == "__main__":
    package_submission("13")
