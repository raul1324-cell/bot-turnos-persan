import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hola Raúl.\n\n"
        "🤖 Bot de turnos Persán\n\n"
        "Comandos disponibles:\n"
        "/hoy - Ver el turno de hoy\n"
        "/mes - Ver el mes\n"
        "/horas - Ver horas trabajadas\n"
        "/dinero - Ver dinero\n"
        "/resumen - Resumen del mes"
    )


async def hoy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Hoy\n\n"
        "Todavía no hay ningún turno guardado."
    )


async def mes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📆 Calendario mensual\n\n"
        "Aquí iremos poniendo tus turnos."
    )


async def horas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏱️ Horas trabajadas\n\n"
        "Todavía no hay horas registradas."
    )


async def dinero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💶 Dinero\n\n"
        "Aquí calcularemos tu salario según tus tarifas."
    )


async def resumen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Resumen mensual\n\n"
        "Todavía no hay datos registrados."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hoy", hoy))
    app.add_handler(CommandHandler("mes", mes))
    app.add_handler(CommandHandler("horas", horas))
    app.add_handler(CommandHandler("dinero", dinero))
    app.add_handler(CommandHandler("resumen", resumen))

    app.run_polling()


if __name__ == "__main__":
    main()
