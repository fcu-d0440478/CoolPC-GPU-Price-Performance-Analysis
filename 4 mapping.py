import sqlite3
import json
import pandas as pd

# Step 1: Load GPU mapping checklist
with open("3 gpu_mapping_checklist.json", "r", encoding="utf-8") as f:
    mapping = json.load(f)

# Step 2: Connect to vga.db and update schema
vga_conn = sqlite3.connect("vga.db")
vga_cursor = vga_conn.cursor()

# 查詢現有欄位
vga_cursor.execute("PRAGMA table_info(vga)")
existing_columns = [col[1] for col in vga_cursor.fetchall()]

# 如果沒有 pure_chipset 欄位就新增
if "pure_chipset" not in existing_columns:
    vga_cursor.execute("ALTER TABLE vga ADD COLUMN pure_chipset TEXT")

# 如果沒有 score 欄位就新增
if "score" not in existing_columns:
    vga_cursor.execute("ALTER TABLE vga ADD COLUMN score INTEGER")

# 如果沒有 CP 欄位就新增
if "CP" not in existing_columns:
    vga_cursor.execute("ALTER TABLE vga ADD COLUMN CP REAL")

# Step 3: Update pure_chipset column based on mapping
vga_cursor.execute("SELECT rowid, chipset FROM vga")
rows = vga_cursor.fetchall()

for rowid, chipset in rows:
    pure_chipset = mapping.get(chipset)
    vga_cursor.execute(
        "UPDATE vga SET pure_chipset = ? WHERE rowid = ?", (pure_chipset, rowid)
    )

vga_conn.commit()

# Step 4: Load GPU score database
gpus_conn = sqlite3.connect("gpus.db")
gpus_df = pd.read_sql_query("SELECT name, score FROM gpus", gpus_conn)

# Step 5: Update score column in vga table
for _, row in gpus_df.iterrows():
    name, score = row["name"], row["score"]
    vga_cursor.execute("UPDATE vga SET score = ? WHERE pure_chipset = ?", (score, name))

vga_conn.commit()

# Compute CP = score / price
vga_cursor.execute(
    """
    UPDATE vga
    SET CP = CASE
        WHEN score IS NOT NULL AND price IS NOT NULL AND price != 0 THEN CAST(score AS REAL) / price
        ELSE NULL
    END
"""
)
vga_conn.commit()

# Step 6: Output updated vga table
vga_updated_df = pd.read_sql_query("SELECT * FROM vga", vga_conn)

# Close connections
vga_conn.close()
gpus_conn.close()
print(vga_updated_df)
