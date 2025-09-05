# 🌍 AWS Glue ETL Project – CSV → JSON  

## 🎯 Objective  
Transform raw **CSV** data into **JSON** using **AWS Glue (Crawler + ETL Job)**.  

- **Input (S3 → `source/`)** → `country_economic.csv`  
- country, continent, year, life_exp, hdi_index, co2_consump, gdp, services

 - **Transformation** → Keep only `country` & `gdp`, rename `gdp → gross_domestic_product`  
- **Output (S3 → `target/`)** → JSON format  

---

## 📂 Project Structure  

```bash
AWS-GLUE-ETL-PROJECT-CSV-JSON/
├── source/
│   └── country_economic.csv   # raw input file
│
├── target/                    # processed output (JSON files generated here)
│
├── scripts/
│   └── country_gdp_json.py    # AWS Glue auto-generated PySpark script
│
└── README.md                  # project documentation
'''


---

## 🏗️ Steps to Build  

### 🪣 Step 1 – Create S3 Bucket  
- Create bucket → **`awsglueproject`**  
- Inside bucket →  
  - `source/` → upload **country_economic.csv**  
  - `target/` → for processed JSON output  

---

### 🔍 Step 2 – Create Glue Crawler  
- **Name:** `country-economic-crawler`  
- **Source:** S3 → `s3://awsglueproject/source/`  
- **Classifier:** Built-in **CSV classifier**  
- **IAM Role:** `AWSGlueServiceRole` (S3 read/write + Glue permissions)  
- **Database:** `countrydb`  
- **Table:** `country_economic`  

✅ Run crawler → Schema available in **Glue Data Catalog**  

---

### ⚙️ Step 3 – Create Glue ETL Job  
- **Name:** `country-gdp-json-job`  
- **Source:** S3 (`source/`)  
- **Transform:**  
  - Select → `country`, `gdp`  
  - Rename → `gdp → gross_domestic_product`  
- **Target:** S3 (`target/`)  
  - Format → JSON  
  - Compression → None  

▶️ Run job → Output saved in `target/`  

---

### 📊 Step 4 – Verify Output  
Example JSON file in `target/`:  
```json
{"country": "India", "gross_domestic_product": 3250}
{"country": "Switzerland", "gross_domestic_product": 37506}
{"country": "Afghanistan", "gross_domestic_product": 974}
