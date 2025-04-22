import os
import time
import telebot as tb
from mensajes import *
from pdf_converter import convert_to_docx, convert_to_pdf, convertir_ppt_to_pdf_linux
#botenes inline
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
load_dotenv()

bot = tb.TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('/convert')
    markup.add(btn)
    bot.reply_to(message, welcome_message, reply_markup=markup)
    
@bot.message_handler(commands=['convert'])
def options_btns(message):
    try:
        markup = InlineKeyboardMarkup(row_width=1)
        b1 = InlineKeyboardButton("Convertir PDF a DOCX", callback_data="convert_to_docx")
        b2 = InlineKeyboardButton("Convertir a pdf", callback_data="convert_to_pdf")
        markup.add(b1, b2)
        bot.reply_to(message,"Estas son las opciones que tienes para la conversion de formatos", reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.callback_query_handler(func=lambda call: True)
def respuesta_botones_inline(call):
    mid = call.message.id
    try:
        
        #enviar lista de formatos que soportan la conversion a pdf
        if call.data == "convert_to_pdf":
            bot.send_message(call.message.chat.id, format_soported, parse_mode='HTML')
            time.sleep(2)
        bot.send_message(call.message.chat.id, "Envia el archivo que deseas convertir")
            
        bot.register_next_step_handler(call.message, handle_document, call.data)
        
        
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Error: {e}")

@bot.message_handler(content_types=['document'])
def handle_document(message, accion):
    try:
        # Verificar el tamaño del archivo
        max_size = 20 * 1024 * 1024  # 50 MB en bytes
        if message.document.file_size > max_size:
            bot.reply_to(message, size_files)
            return

        #descargar el archivo
        file_info = bot.get_file(message.document.file_id)#obtiene informacion del archivo incluido la ruta en el server
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)#descarga el archivo
        CARPETA = 'archivos'
        os.makedirs(CARPETA, exist_ok=True)#crea la carpeta si no existe
        #guardar el archivo
        # Guardar el archivo en la carpeta especificada
        file_name = message.document.file_name
        full_path = os.path.join(CARPETA, file_name) # Ruta completa del archivo
        with open(full_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, f"Archivo '{file_name}' descargado correctamente. Procesando...")
        convertido = None
        if accion == "convert_to_docx":
            convertido = convert_to_docx(full_path, file_name, CARPETA)
        #elif accion == "convert_to_pdf":
        elif accion == "convert_to_pdf":
            convertido = convert_to_pdf(full_path, CARPETA)
            if convertido == None:
                bot.reply_to(message, "Error al convertir el archivo. No es compatible con el formato pdf.")

        with open(convertido, 'rb') as documento:
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, documento)
        os.remove(full_path)
        os.remove(convertido)
        user_states={}  # Limpiar el estado del usuario después de la conversión
    except Exception as e:
        msg = bot.reply_to(message, f"Error al descargar el archivo: {e}. Por favor, intenta nuevamente y asegurate de que el archivo sea correcto.")
        time.sleep(10)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, msg.message_id)
   
if __name__ == "__main__":
    print("running...")
    bot.infinity_polling()