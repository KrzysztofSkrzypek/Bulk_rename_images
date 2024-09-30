import os
def bulk_rename_images(folder_path, prefix="zdj_"):
    if not os.path.isdir(folder_path):
        raise ValueError("Podana ścieżka nie jest folderem lub nie istnieje.")

    valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}  # Dodaj odpowiednie rozszerzenia

    for count, filename in enumerate(os.listdir(folder_path)):
        old_file_path = os.path.join(folder_path, filename)

        if os.path.isfile(old_file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension in valid_extensions:
                new_filename = f"{prefix}{count + 1}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")


folder_path = "dane/"
bulk_rename_images(folder_path)