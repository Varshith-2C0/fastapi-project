from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import SessionLocal, engine
import database_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

@app.get("/")
def greet():
    return "welcome to varshith lobby"


products=[
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20)
]

def get_db():
    db = SessionLocal()  # <-- Capital 'S' and 'L'
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db_product = database_models.Product(**product.model_dump())
            db.add(db_product)
        db.commit()

    db.close()

init_db()


@app.get("/products")
def get_all_products(db:SessionLocal= Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()    
    return db_products

@app.get('/product/{id}')
def get_product_by_id(id:int,db:SessionLocal= Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id ==id).first()
    if db_product:
        return db_product
    return "product not found"

@app.post("/products")
def add_product(product: Product,db:SessionLocal= Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product,db:SessionLocal= Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id ==id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated"
    else:
        return "No product found"

@app.delete("/products")
def delete_product(id: int,db:SessionLocal= Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id ==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product delected"
    else:
        return"no product found"