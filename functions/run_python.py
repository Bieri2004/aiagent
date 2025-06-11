import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        # Absolute Pfade berechnen
        abs_working = os.path.abspath(working_directory)
        abs_file = os.path.abspath(os.path.join(working_directory, file_path))

        # Sicherheitsprüfung: Datei liegt im Arbeitsverzeichnis
        if not abs_file.startswith(abs_working):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Existiert die Datei?
        if not os.path.isfile(abs_file):
            return f'Error: File "{file_path}" not found.'

        # Ist es eine Python-Datei?
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        # Subprocess mit Timeout ausführen
        result = subprocess.run(
            ['python3', abs_file],
            cwd=abs_working,
            timeout=30,
            capture_output=True,
            text=True
        )

        # Ausgabe formatieren
        output = []
        if result.stdout.strip():
            output.append(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr.strip():
            output.append(f"STDERR:\n{result.stderr.strip()}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return '\n'.join(output) if output else "No output produced."

    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Execution timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"
