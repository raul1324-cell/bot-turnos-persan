import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.environ.get("BOT_TOKEN")


def menu_principal():
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
    return InlineKeyboardMarkup(keyboard)


def menu_turnos():
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
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 TURNOS PERSÁN\n\n¿Qué quieres hacer?",
        reply_markup=menu_principal(),
    )


async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "inicio":
        await query.edit_message_text(
            "🤖 TURNOS PERSÁN\n\n¿Qué quieres hacer?",
            reply_markup=menu_principal(),
        )
        return

    if query.data == "calendario":
        texto = (
            "📅 CALENDARIO\n\n"
            "Todavía no hay turnos guardados."
        )
        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

    elif query.data == "anadir":
        texto = (
            "➕ AÑADIR TURNO\n\n"
            "¿Qué turno quieres guardar?"
        )
        await query.edit_message_text(
            texto,
            reply_markup=menu_turnos(),
        )
        return

    elif query.data == "horas":
        texto = (
            "⏱️ HORAS\n\n"
            "Todavía no hay horas registradas."
        )
        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

    elif query.data == "dinero":
        texto = (
            "💶 DINERO\n\n"
            "Todavía no hay datos para calcular."
        )
        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

    elif query.data == "resumen":
        texto = (
            "📊 RESUMEN\n\n"
            "Todavía no hay datos registrados."
        )
        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

    elif query.data == "config":
        texto = (
            "⚙️ CONFIGURACIÓN\n\n"
            "Aquí configuraremos tus tarifas y preferencias."
        )
        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

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

        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

    else:
        texto = "Opción no disponible."
        teclado = [[
            InlineKeyboardButton("🏠 Menú principal", callback_data="inicio")
        ]]

    await query.edit_message_text(
        texto,
        reply_markup=InlineKeyboardMarkup(teclado),
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(botones))

    app.run_polling()


if __name__ == "__main__":
    main()
