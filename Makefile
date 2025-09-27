run:
	docker compose up -d

run-rebuild:
	docker compose up --build -d
down:
	docker compose down