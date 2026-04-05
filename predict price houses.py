import pyodbc
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# =========================
# 1. CONNECT DATABASE
# =========================
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=HouseDB;'
    'Trusted_Connection=yes;'
)

# =========================
# 2. LOAD DATA
# =========================
query = "SELECT Area, Bedrooms, Bathrooms, Floors, Price FROM Houses"
df = pd.read_sql(query, conn)

print("📊 Data:")
print(df)

# =========================
# 3. TRAIN MODEL
# =========================
X = df[['Area', 'Bedrooms', 'Bathrooms', 'Floors']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("\n🎯 Accuracy:", accuracy)

# =========================
# 4. PREDICT
# =========================
def predict_price(area, bedrooms, bathrooms, floors):
    new_data = [[area, bedrooms, bathrooms, floors]]
    price = model.predict(new_data)
    return price[0]

# =========================
# 5. TEST
# =========================
print("\n🔮 Predict test:")
price = predict_price(160, 3, 2, 2)
print("👉 Predicted price:", price)

# =========================
# 6. INSERT NEW DATA
# =========================
def insert_house(area, bedrooms, bathrooms, floors, location, price):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Houses (Area, Bedrooms, Bathrooms, Floors, Location, Price)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (area, bedrooms, bathrooms, floors, location, price))
    conn.commit()
    print("✅ Insert success!")

# Example insert
# insert_house(140, 3, 2, 1, 'HCM', 3.0)