def run():
    from app.models import Author, Publisher
    # Create sample Author
    if not Author.objects.exists():
        Author.objects.create(first_name="J.K.", last_name="Rowling")
        Author.objects.create(first_name="George", last_name="Orwell")
        print("Created sample authors.")

    # Create sample Publisher
    if not Publisher.objects.exists():
        Publisher.objects.create(name="Penguin Books")
        Publisher.objects.create(name="HarperCollins")
        print("Created sample publishers.")

if __name__ == "__main__":
    import django
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
    django.setup()
    run()
