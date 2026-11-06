import pandas as pd

def audit_stakeholder_health(csv_path="data/stakeholder_tracking_sheet.csv"):
    df = pd.read_csv(csv_path)
    print("=== STAKEHOLDER SENTIMENT AUDIT (WEEK 8 CHECKPOINT) ===")
    
    for _, row in df.iterrows():
        group = row["Stakeholder_Group"]
        w8 = int(row["Week_8_Target"])
        base = int(row["Baseline_W0"])
        delta = w8 - base
        
        status = "HEALTHY" if w8 >= 3 else "ACTION REQUIRED"
        print(f"[{status}] {group:<22} | W0: {base} -> W8: {w8} (Δ: {delta:+d})")

if __name__ == "__main__":
    audit_stakeholder_health()
