from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from pathlib import Path
import uvicorn
app = FastAPI()

pieces= {
     "king": {
      
        "image" :'image/king.jpg',
        "fact": "شاه در شطرنج مهم‌ترین مهرهٔ بازی است. اگر مورد حملهٔ حریف قرار گیرد در وضعیت کیش قرار می‌گیرد و اگر نتوان کیش را برطرف نمود، مات یا کیش‌ومات اتفاق افتاده و بازی با پیروزی حریف به پایان رسیده‌است"
    },

     "queen": {
      
        "image" :'image/queen.jpg',
        "fact": "وزیر در شطرنج قوی‌ترین مهرهٔ بازی است که ترکیبی از حرکت رخ و فیل را با هم انجام می‌دهد"
    },
     "rook": {
      
        "image" :'image/rook.jpg',
        "fact": "رُخ یکی از مهره‌های شطرنج است که می‌تواند به‌طور نامحدود در طول و عرض صفحهٔ شطرنج حرکت کند."
    },
     "bishop": {
      
        "image" :'image/bishop.jpg',
        "fact": "فیل یکی از مهره‌های شطرنج است که می‌تواند به‌طور نامحدود به‌طور مورب حرکت کند. هر یک از بازیکنان دو فیل دارد که یکی بین شاه و اسب و دیگری بین وزیر و اسب قرار می‌گیرد."
    },
     "Knight": {
      
        "image" :'image/Knight.jpg',
        "fact": "اسب متفاوت‌ترین روش حرکت را در میان مهره‌های شطرنج دارد و حرکت آن با دو خانه حرکت عمودی و یک خانه حرکت افقی یا دو خانه حرکت افقی و یک خانه حرکت عمودی انجام می‌شود که به حرف ال در الفبای لاتین شباهت دارد."
    },
    "pawn": {
      
        "image" :'image/pawn.jpg',
        "fact": "سرباز یا پیاده پرتعدادترین مهره در بازی شطرنج است. این مهره با نماد پیاده‌نظام در شطرنج شناخته می‌شود. هر بازیکن در ابتدای بازی دارای هشت پیاده است. پیاده‌های سفید در آغاز بازی در ردیف (صف) دوم و پیاده‌های سیاه در ردیف هفتم قرار دارند."
    }

}
@app.get("/")
def read_root():
    return "Hi, welcome to my api In this api there is about chess"

@app.get("/pieces")
def get_pieces():
    return pieces

@app.get("/pieces/{piece_name}/")
def read_piece_info(piece_name: str):
    if piece_name=='king' or piece_name=='bishop' or piece_name=='knight' or piece_name=='pawn' or piece_name=='queen' or piece_name=='rook' :
        return pieces[piece_name]
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="piece name must king or bishop or knight or pawn or queen or rook")
@app.get("/pieces/image")
def read_default_image():
     image_path = Path("image/6pieces.jpg")
     return FileResponse(image_path)

@app.get("/pieces/image/{piece_name}")
def read_piece_image(piece_name: str):
    if piece_name=='king' or piece_name=='bishop' or piece_name=='knight' or piece_name=='pawn' or piece_name=='queen' or piece_name=='rook' :
        images= pieces[piece_name]
        image_path = images["image"]
        return FileResponse(image_path)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="piece name must  king or bishop or knight or pawn or queen or rook")



