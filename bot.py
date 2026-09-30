import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📅 Calendario", callback_data="calendario"),
            InlineKeyboardButton("➕ Añadir turno", callback_data="anadir"),
        ],
        [
            InlineKeyboardButton("⏱️ Horas", callback_data="horas"),
            InlineKeyboardButton("💶 Dinero", callback_data="dinero"),
        ],
        [
            InlineKeyboardButton("📊 Resumen", callback_data="resumen"),
            InlineKeyboardButton("⚙️ Configuración", callback_data="config"),
        ],
    ]

    await update.message.reply_text(
        "🤖 TURNOS PERSÁN\n\n"
        "¿Qué quieres hacer?",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "calendario":
        texto = (
            "📅 CALENDARIO\n\n"
            "Todavía no hay turnos guardados."
        )

    elif query.data == "anadir":
        keyboard = [
            [
                InlineKeyboardButton("🟢 Mañana", callback_data="turno_manana"),
                InlineKeyboardButton("🟡 Tarde", callback_data="turno_tarde"),
            ],
            [
                InlineKeyboardButton("⚫ Noche", callback_data="turno_noche"),
                InlineKeyboardButton("⚪ Descanso", callback_data="turno_descanso"),
            ],
            [
                InlineKeyboardButton("🔴 Vacaciones", callback_data="turno_vacaciones"),
                InlineKeyboardButton("🔵 Asuntos propios", callback_data="turno_asuntos"),
            ],
            [
                InlineKeyboardButton("🟠 Baja", callback_data="turno_baja"),
                InlineKeyboardButton("🎉 Festivo", callback_data="turno_festivo"),
            ],
        ]

        texto = "➕ AÑADIR TURNO\n\n¿Qué turno quieres guardar?"

    elif query.data == "horas":
        texto = "⏱️ HORAS\n\nTodavía no hay horas registradas."

    elif query.data == "dinero":
        texto = "💶 DINERO\n\nTodavía no hay datos para calcular."

    elif query.data == "resumen":
        texto = "📊 RESUMEN\n\nTodavía no hay datos registrados."

    elif query.data == "config":
        texto = "⚙️ CONFIGURACIÓN\n\nAquí configuraremos tus tarifas y preferencias."

    elif query.data.startswith("turno_"):
        turnos = {
            "turno_manana": "🟢 Mañana",
            "turno_tarde": "🟡 Tarde",
            "turno_noche": "⚫ Noche",
            "turno_descanso": "⚪ Descanso",
            "turno_vacaciones": "🔴 Vacaciones",
            "turno_asuntos": "🔵 Asuntos propios",
            "turno_baja": "🟠 Baja",
            "turno_festivo": "🎉 Festivo",
        }

        turno = turnos.get(query.data, "Turno desconocido")

        texto = (
            f"Has elegido: {turno}\n\n"
            "📅 Ahora tendremos que elegir el día."
        )

    else:
        texto = "Opción no disponible."

    keyboard = [
        [InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")]
    ]

    if query.data == "anadir":
        keyboard = [
            [
                InlineKeyboardButton("🟢 Mañana", callback_data="turno_manana"),
                InlineKeyboardButton("🟡 Tarde", callback_data="turno_tarde"),
            ],
            [
                InlineKeyboardButton("⚫ Noche", callback_data="turno_noche"),
                InlineKeyboardButton("⚪ Descanso", callback_data="turno_descanso"),
            ],
            [
                InlineKeyboardButton("🔴 Vacaciones", callback_data="turno_vacaciones"),
                InlineKeyboardButton("🔵 Asuntos propios", callback_data="turno_asuntos"),
            ],
            [
                InlineKeyboardButton("🟠 Baja", callback_data="turno_baja"),
                InlineKeyboardButton("🎉 Festivo", callback_data="turno_festivo"),
            ],
            [
                InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
            ],
        ]

    await query.edit_message_text(
        texto,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("📅 Calendario", callback_data="calendario"),
            InlineKeyboardButton("➕ Añadir turno", callback_data="anadir"),
        ],
        [
            InlineKeyboardButton("⏱️ Horas", callback_data="horas"),
            InlineKeyboardButton("💶 Dinero", callback_data="dinero"),
        ],
        [
            InlineKeyboardButton("📊 Resumen", callback_data="resumen"),
            InlineKeyboardButton("⚙️ Configuración", callback_data="config"),
        ],
    ]

    await query.edit_message_text(
        "🤖 TURNOS PERSÁN\n\n¿Qué quieres hacer?",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(botones))
    app.add_handler(CallbackQueryHandler(inicio, pattern="^inicio$"))

    app.run_polling()


if __name__ == "__main__":
    main()
