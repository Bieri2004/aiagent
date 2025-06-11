import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    try:
        # Absoluten Pfad berechnen
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Prüfen, ob die Datei im erlaubten Arbeitsverzeichnis liegt
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Prüfen, ob es eine reguläre Datei ist
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Datei lesen
        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS + 1)  # +1, um zu erkennen, ob die Datei länger ist

        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'
        return content

    except Exception as e:
        return f"Error: {str(e)}"
