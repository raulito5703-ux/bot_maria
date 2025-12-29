import random
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

RESPUESTAS = [
    "Claro que te quiero, sobre todo por cómo te ríes por tonterías 💕",
    "Te quiero porque haces mis días más bonitos 🌸",
    "Te quiero incluso cuando no te das cuenta de lo increíble que eres ❤️",
    "Te quiero más de lo que las palabras pueden explicar 🥰",
    "Te quiero porque eres tú, y eso ya es suficiente 💖"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [InlineKeyboardButton("¿Que si te quiero?", callback_data="te_quiero")]
    ]
    await update.message.reply_text(
        "Hola amor 💌\nPulsa el botón:",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def boton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(random.choice(RESPUESTAS))

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(boton))
    app.run_polling()

