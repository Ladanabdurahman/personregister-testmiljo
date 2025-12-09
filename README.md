# Personregister i testmiljö (Examinationsprojekt)

Detta projekt innehåller en enkel Python-applikation som hanterar ett personregister i en testmiljö med Docker.

# Funktioner
- Initiera databas med testanvändare
- Visa användare
- Rensa all testdata
- Anonymisera alla användare
- Persistent lagring med Docker-volym

# Kör projektet i Docker

Bygg och starta containern:

docker-compose up --build

Kör GDPR-funktioner:

# Anonymisera alla användare
docker exec gdpr-user-registry python -c "import app; app.anonymize_data(); app.display_users()"

# Rensa testdata
docker exec gdpr-user-registry python -c "import app; app.clear_test_data(); app.display_users()"

# Återinitiera databasen
docker exec gdpr-user-registry python -c "import app; app.init_database(); app.display_users()"

# Struktur
/app.py
/Dockerfile
/docker-compose.yml
/README.md
/.gitignore
