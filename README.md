# Bot de Telegram - @FormatCvter_bot

 Este bot puede ayudarte a convertir archivos de diferentes formatos de manera rápida y sencilla directamente desde Telegram.

---

## ¿Qué hace?

@FormatCvter_bot permite convertir archivos de los siguientes formatos:

### **De PDF a DOCX**
- Convierte archivos PDF a documentos editables en formato `.docx`.

### **De otros formatos a PDF**
- Convierte documentos de texto, hojas de cálculo y presentaciones a formato PDF. Los formatos soportados incluyen:
  - **Documentos de texto**: `.doc`, `.docx`, `.odt`, `.txt`, `.rtf`, `.html`, `.htm`
  - **Hojas de cálculo**: `.xls`, `.xlsx`, `.ods`, `.csv`
  - **Presentaciones**: `.ppt`, `.pptx`, `.odp`

---

## ¿Cómo usar el bot?

1. **Inicia el bot**:
   - Busca `@FormatCvter_bot` en Telegram y haz clic en "Iniciar".

2. **Para seleccionar una opción de conversión**:
   - Escribe el comando `/convert` y selecciona una de las opciones disponibles:
     - Convertir PDF a DOCX
     - Convertir a PDF

3. **Envía tu archivo**:
   - Después de seleccionar una opción, envía el archivo que deseas convertir. Asegúrate de que el archivo cumpla con las siguientes condiciones:
        - **Formato soportado**: Consulta la lista de formatos compatibles.
     - **Tamaño máximo**: 20 MB.
     

4. **Recibe tu archivo convertido**:
   - El bot procesará tu archivo y te enviará el resultado en el formato solicitado.

---

## Notas importantes

- ⚠️ **Tamaño máximo de archivo**: Telegram solo permite que los bots descarguen archivos de hasta **20 MB**. Si tu archivo es más grande, no podrá ser convertido.
- **Privacidad**: Los archivos enviados al bot se procesan de manera temporal y se eliminan automáticamente después de la conversión.
- **Errores comunes**:
  - Si el archivo no es compatible con el formato solicitado, el bot te notificará.
  - Si el archivo supera los 20 MB, recibirás un mensaje indicando que el archivo es demasiado grande.
  - Enviar el archivo sin seleccionar el formato a convertir
  no dara respuesta alguna

---

## ¿Cómo funciona el bot por dentro?

El bot está desarrollado en Python y utiliza varias librerías para manejar la interacción con Telegram y realizar las conversiones de archivos. A continuación, se describen las principales tecnologías y librerías utilizadas:

### **Librerías principales**
- **[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)**:
  - Se utiliza para interactuar con la API de Telegram y manejar mensajes, comandos y archivos enviados por los usuarios.
- **[python-docx](https://python-docx.readthedocs.io/)**:
  - Permite crear y manipular documentos en formato `.docx`.
- **[pdf2docx](https://github.com/dothinking/pdf2docx)**:
  - Convierte archivos PDF a documentos `.docx` editables.
- **[LibreOffice](https://www.libreoffice.org/)**:
  - Se utiliza en modo headless (sin interfaz gráfica) para convertir documentos de texto, hojas de cálculo y presentaciones a formato PDF.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)**:
  - Carga variables de entorno, como el token del bot, desde un archivo `.env`.

---
### **Flujo de trabajo del bot**
1. **Inicio del bot**:
   - El bot se inicia con el comando `/start`, que muestra un mensaje de bienvenida y un botón para acceder a las opciones de conversión.

2. **Selección de conversión**:
   - El usuario selecciona una opción de conversión (por ejemplo, "Convertir a PDF") a través de botones.

3. **Recepción del archivo**:
   - El bot valida que el archivo enviado sea compatible y que no supere los 20 MB (límite de descarga de Telegram para bots).

4. **Conversión del archivo**:
   - Dependiendo de la opción seleccionada:
     - **PDF a DOCX**: Usa `pdf2docx` para realizar la conversión.
     - **Otros formatos a PDF**: Usa LibreOffice en modo headless para convertir el archivo.

5. **Envío del archivo convertido**:
   - El bot envía el archivo convertido al usuario y elimina los archivos temporales.

---

## ¿Tienes dudas o sugerencias?

Si tienes alguna pregunta de cómo funciona o se te ocurre algo para que el bot sea aún mejor, ¡escríbeme por Telegram a @Phiexdric!

¡Gracias por usar @FormatCvter_bot!
*(Quizás en el futuro le meta más formatos o formas de usarlo, estén atentos! 😉)*