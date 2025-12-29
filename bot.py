import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

RESPUESTAS = [
    "Claro que te quiero, sobre todo por cómo te ríes por tonterías 💕",
    "Te quiero porque haces mis días más bonitos 🌸",
    "Te quiero incluso cuando no te das cuenta de lo increíble que eres ❤️",
    "Te quiero porque eres tú, y eso ya es suficiente 💖",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [InlineKeyboardButton("¿Que si te quiero?", callback_data="te_quiero")]
    ]
    await update.message.reply_text(
        "Hola amor 💌\nPulsa el botón:",
        reply_markup=InlineKeyboardMarkup(teclado),
    )

async def boton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(random.choice(RESPUESTAS))

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN no está definido")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(boton))
    app.run_polling()

if __name__ == "__main__":
    main()
