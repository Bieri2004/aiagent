import os

def get_files_info(working_directory, directory=None):
    try:
        # Zielverzeichnis bestimmen
        if directory is None:
            directory = "."

        # Absolute Pfade berechnen
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))

        # Prüfen, ob das Zielverzeichnis im erlaubten Arbeitsverzeichnis liegt
        if not abs_target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Prüfen, ob es ein Verzeichnis ist
        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'

        # Verzeichnisinhalt auflisten
        entries = []
        for entry in os.listdir(abs_target_dir):
            entry_path = os.path.join(abs_target_dir, entry)
            is_dir = os.path.isdir(entry_path)
            try:
                file_size = os.path.getsize(entry_path)
            except Exception as e:
                file_size = "unknown"
            entries.append(
                f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {str(e)}"
